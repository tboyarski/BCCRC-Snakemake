#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Author:   Tim Boyarski
# Date:     2017-06-14
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Call: call("python " + snakeDIR + "/modules/starFusion/starFusion.py " + YAMLFILE + " " + CLUSTERFILE + " " + SNAKEFILE, shell=True)
# Input:                                    ./{processBamDIR}/junctions/{sample}_junctions.txt

# Output:                                   ./{starFusionDIR}/fusions/{sample}_fusions.txt

# Purpose: Automate the population of user's pipeline
#   Snakefile, '.YAML', and '.JSON' files.
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# PYTHON PACKAGES #
#------------------
# Request sys so be able to use CLI arguments.
from sys import argv

# Request json to be able to load and write to the config.json file.
from json import load, dump

# Request os permissions to be able to create directories for the log files.
from os import path, mkdir

# Global variable used for reporting of the module name.
moduleNAME = "starFusion"
#-----------------------------------------------------------------------------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# PYTHON SCRIPT #
#----------------
# 0 --- Validate number of user arguments.
if len(argv) != 4:
    print("Please provide arguments as follows:")
    print("python " + moduleNAME + ".py yaml json snake")
    print("\t-yaml = 'path/name' of the yaml file to write the pipeline parameters")
    print("\t-snake = 'path/name' of snakefile we are building")
    print("\t-json = 'path/name' of the json file we write the cluster config to")
    quit()
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 1 --- Log Files
# Check if directories exist for logging, as the DRMAA caller cannot create directories.
if (path.isdir("log")) != True:
    mkdir("log")
    print(moduleNAME + ".py \tCreating: log/")
if (path.isdir("log/" + moduleNAME) != True):
    # Maintain this list of active submodules.
    ruleLIST = ['fusion']
    # 1A. Create module directories
    mkdir("log/" + moduleNAME)
    print(moduleNAME + ".py \tCreating: log/" + moduleNAME)
    # 1B. Report on directories created.
    for rule in ruleLIST:
        mkdir("log/" + moduleNAME + "/" + rule)
        print(moduleNAME + ".py \tCreating: log/" + moduleNAME + "/" + rule + "/")
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 2 --- YAML File
# Open and append to file the following required paramters.
with open(argv[1], "a+") as yamlTARGET:
    # 2A. Software
    starFusion_starFusionProg="starFusion_starFusionProg: /extscratch/clc/usr/star-fusion/0.7.0/STAR-Fusion\n"
    # 2B. Shared variables
    starFusionDIR="starFusionDIR: starFusion\n"
    fusionRefGenomeDIR="fusionRefGenomeDIR: /extscratch/clc/references/star/GRCh37\n"
    # 2D. Write to file
    yamlTARGET.write(
        "\n\n"+
        "#####################################\n"+
        "# " + moduleNAME + " Parameters\n"+
        "#####################################\n"+
        "#----------------------------------------------------------------- *Software* ------------------------------------------------------------------------\n" +
        starFusion_starFusionProg +
        "#----------------------------------------------------------------- *Shared Variables* ----------------------------------------------------------------\n" +
        starFusionDIR + fusionRefGenomeDIR +
        "#-----------------------------------------------------------------------------------------------------------------------------------------------------\n"
    )
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 3 --- JSON File
# Generate header for '.json' file.
# 3A. Read file to parse and store '.json'  object.
with open(argv[2], "r+") as jsonTARGET:
    jsonOBJ = load(jsonTARGET)
    jsonOBJ['fusion'] = {
            "clusterSpec": "-V -S /bin/bash -o log/starFusion/fusion -e log/starFusion/fusion -l h_vmem=35G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleSAF}"
    }
#3B. Recreate JSON file to delete exiting text.
with open(argv[2], "w+") as jsonTARGET:
    dump(jsonOBJ, jsonTARGET, indent=4)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 4 --- Snakefile
# Open and append o file a descriptin and the last rule call.
with open(argv[3], "a+") as pipeTARGET:
    pipeTARGET.write(
        "\n\n#-----------------------------------------------------------------------------------------------------------------------------------------------------"
        "\n\n#***** " + moduleNAME + " *****\n"
        "#  Included:\n"
        "#      fusion:     Run starFusion on '.BAM' files.\n"
        "#  Files:\n"
        "#    Input:      ./{processBamDIR}/junctions/{sample}_junctions.txt\n"
        "#    Output:     ./{starFusionDIR}/fusions/{sample}_fusions.txt\n"
        'include: "' + path.dirname(path.realpath(__file__)) + '/' + moduleNAME + '_INCLUDE"\n'
        "#  Required: \n"
        '#    @include: "' + path.dirname(path.dirname(path.realpath(__file__))) + '/bamGen/bamGen_INCLUDE"\n'
        '#    @include: "' + path.dirname(path.dirname(path.realpath(__file__))) + '/bamUtil/bamUtil_INCLUDE"\n'
        "#  Call via: \n"
        '# fusion:    expand("{outputDIR}/{starFusionDIR}/fusions/{samples}_fusions.txt", outputDIR=config["outputDIR"], starFusionDIR=config["starFusionDIR"], samples=config["sample"]),\n'
    )
#-----------------------------------------------------------------------------------------------------------------------------------------------------
