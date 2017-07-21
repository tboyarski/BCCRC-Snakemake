#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Author:   Tim Boyarski
# Date:     2017-06-28
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Call: call("python " + snakeDIR + "/modules/mpileup/mpileup.py " + YAMLFILE + " " + CLUSTERFILE + " " + SNAKEFILE, shell=True)

# Purpose: Automate the population of user's Snakefile, '.YAML', and '.JSON' files.
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
moduleNAME = "mpileupGen"
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
    ruleLIST = ['bam2mpileup']
    # 1A. Create module directories
    mkdir("log/" + moduleNAME)
    print(moduleNAME + ".py \tCreating: log/" + moduleNAME)
    # 1B. Report on rule directories created.
    for rule in ruleLIST:
        mkdir("log/" + moduleNAME + "/" + rule)
        print(moduleNAME + ".py \tCreating: log/" + moduleNAME + "/" + rule + "/")
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 2 --- YAML File
# Open and append to file the following required paramters.
with open(argv[1], "a+") as yamlTARGET:
    # 2A. Software
    mpileup_samtoolsProg = "mpileup_samtoolsProg: samtools\n"
    # 2B. Shared variables
    mpileupGenDIR="mpileupGenDIR: mpileupGen\n"
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
        mpileup_samtoolsProg +
        "#----------------------------------------------------------------- *Shared Variables* ----------------------------------------------------------------\n" +
        mpileupGenDIR + bitFlag + countOrphan + noBaq + maxDepth + mapQuality + bedFILE +
        "#----------------------------------------------------------------- bam2mpileup -----------------------------------------------------------------------\n"
        "#-----------------------------------------------------------------------------------------------------------------------------------------------------\n"
    )
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 3 --- JSON File
# Generate header for '.json' file.
# 3A. Read file to parse and store '.json' object.
with open(argv[2], "r+") as jsonTARGET:
    jsonOBJ = load(jsonTARGET)
    jsonOBJ['bam2mpileup'] = {
            "clusterSpec": "-V -S /bin/bash -o log/mpileupGen/bam2mpileup -e log/mpileupGen/bam2mpileup -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleB2M}{wildcards.chrB2M}"
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
        "#***** " + moduleNAME + " *****\n"
        "#  Included:\n"
        "#      mpileupUNSPLIT:     Generated '.mpileup' file from'.bam' file.\n"
        "#      mpileupSPLIT:       Generated '.mpileup' file from'.bam' file.\n"
        'include: "' + path.dirname(path.realpath(__file__)) + '/' + moduleNAME + '_INCLUDE"\n'
        "#  Required: NONE\n"
        "#  Call via: \n"
        '#bam2mpileup:      expand("{outputDIR}/{mpileupDIR}/{samples}.mpileup", outputDIR=config["outputDIR"], mpileupDIR=config["mpileupDIR"], samples=config["sample"])\n'
        '#bam2mpileupCHR:   expand("{outputDIR}/{mpileupDIR}/{samples}_{chrLIST}.mpileup", outputDIR=config["outputDIR"], mpileupDIR=config["mpileupDIR"], samples=config["sample"], chrLIST=config["chrLIST"])\n'
        '#-----------------------------------------------------------------------------------------------------------------------------------------------------\n'
    )
#-----------------------------------------------------------------------------------------------------------------------------------------------------
