#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Author:   Tim Boyarski
# Date:     2017-08-31
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Call: call("python " + snakeDIR + "/modules/tutorialGen/tutorialGen.py " + YAMLFILE + " " + CLUSTERFILE + " " + SNAKEFILE, shell=True)
# Input:                                    .bam

# Output:                                   .mpileup

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
moduleNAME = "tutorialGen"
#-----------------------------------------------------------------------------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# PYTHON SCRIPT #
#----------------
# 0 --- Validate number of user arguments.
if len(argv) != 4:
    print("Please provide arguments as follows:")
    print("python " + moduleNAME + ".py yaml json snake")
    print("\t-yaml = 'path/name' of the yaml file to write the pipeline parameters")
    print("\t-json = 'path/name' of the json file we write the cluster config to")
    print("\t-snake = 'path/name' of snakefile we are building")
    quit()
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 1 --- Log Files
# Check if directories exist for logging, as the DRMAA caller cannot create directories.
if (path.isdir("log")) != True:
    mkdir("log")
    print(moduleNAME + ".py \tCreating: log/")
if (path.isdir("log/" + moduleNAME) != True):
    # Maintain this list of active submodules.
    ruleLIST = ['tPile']
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
    tutorialGen_samtoolsProg = "tutorialGen_samtoolsProg: samtools\n"
    # 2B. Shared variables
    tutorialGenDIR="tutorialGenDIR: tutorialGen\n"
    bitFlag="bitFlag: 512\n"
    countOrphan="countOrphan: -A\n"
    noBaq="noBaq: -B\n"
    maxDepth="maxDepth: -d 10000000\n"
    mapQuality="mapQuality: -q 20\n"
    bedFILE='bedFILE: ""\n'
    # 2C. bam2mpileup
    # 2D. Write to file
    yamlTARGET.write(
        "\n\n"
        "#####################################\n"
        "# " + moduleNAME + " Parameters\n"
        "#####################################\n"
        "#----------------------------------------------------------------- *Software* ------------------------------------------------------------------------\n" +
        tutorialGen_samtoolsProg +
        "#----------------------------------------------------------------- *Shared Variables* ----------------------------------------------------------------\n" +
        tutorialGen + bitFlag + countOrphan + noBaq + maxDepth + mapQuality + bedFILE +
        "#----------------------------------------------------------------- bam2mpileup -----------------------------------------------------------------------\n"
        "#-----------------------------------------------------------------------------------------------------------------------------------------------------\n"
    )
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 3 --- JSON File
# Generate header for '.json' file.
# 3A. Read file to parse and store '.json' object.
with open(argv[2], "r+") as jsonTARGET:
    jsonOBJ = load(jsonTARGET)
    jsonOBJ['tPile'] = {
            "clusterSpec": "-V -S /bin/bash -o log/tutorialGen/tPile -e log/tutorialGen/tPile -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleTP}{wildcards.chrTP}"
    }
# 3B. Recreate JSON file to delete exiting text.
with open(argv[2], "w+") as jsonTARGET:
    dump(jsonOBJ, jsonTARGET, indent=4)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 4 --- Snakefile
# Open and append o file a descriptin and the last rule call.
with open(argv[3], "a+") as pipeTARGET:
    pipeTARGET.write(
        "\n\n#-----------------------------------------------------------------------------------------------------------------------------------------------------\n"
        "#***** " + moduleNAME + " *****\n" +
        "#  Included:\n" +
        "#      tPile:     Fancy generated description.\n" +
        'include: "' + path.dirname(path.realpath(__file__)) + '/' + moduleNAME + '_INCLUDE"\n' +
        "#  Required: NONE\n" +
        "#  Call via: \n" +
        '#    expand("{outputDIR}/{tutorialGenDIR}/{samples}.mpileup", outputDIR=config["outputDIR"], tutorialGenDIR=config["tutorialGenDIR"], samples=config["sample"])\n'
        '#-----------------------------------------------------------------------------------------------------------------------------------------------------\n'
    )
#-----------------------------------------------------------------------------------------------------------------------------------------------------
