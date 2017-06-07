#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Author:   Tim Boyarski
# Date:     2017-05-24
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Call: call("python " + snakeDIR + "/modules/mpileup/mpileup.py " + YAMLFILE + " " + CLUSTERFILE + " " + SNAKEFILE, shell=True)
# Purpose: Automate the population of user's Snakefile, '.YAML', and '.JSON' files.
#-----------------------------------------------------------------------------------------------------------------------------------------------------

import sys
import json
import os

moduleNAME = "mpileup"

# 0 --- Validate number of user arguments.
if len(sys.argv) != 4:
    print("Please provide arguments as follows:")
    print("python " + moduleNAME + ".py yaml json snake")
    print("\t-yaml = 'path/name' of the yaml file to write the pipeline parameters")
    print("\t-snake = 'path/name' of snakefile we are building")
    print("\t-json = 'path/name' of the json file we write the cluster config to")
    quit()


# 1 --- Log Files
# Check if directories exist for logging, as the DRMAA caller cannot create directories.
if (os.path.isdir("log")) != True:
    os.mkdir("log")
    print(moduleNAME + ".py \tCreating: log/")
if (os.path.isdir("log/" + moduleNAME) != True):
    # Maintain this list of active submodules.
    moduleLIST = ['mpileupSPLIT','mpileupUNSPLIT']
    # 1A. Create module directories
    os.mkdir("log/" + moduleNAME)
    print(moduleNAME + ".py \tCreating: log/" + moduleNAME)
    # 1B. Report on directories created.
    for module in moduleLIST:
        os.mkdir("log/" + moduleNAME + "/" + module)
        print(moduleNAME + ".py \tCreating: log/" + moduleNAME + "/" + module + "/")


# 2 --- YAML File
# Open and append to file the following required paramters.
with open(sys.argv[1], "a+") as yamlTARGET:
    # 2A. Software
    mpileup_samtoolsProg = "mpileup_samtoolsProg: samtools\n"
    # 2B. Shared variables
    mpileupDIR="mpileupDIR: mpileup\n"
    bitFLAG="bitFLAG: 512\n"
    countORPHAN="countORPHAN: -A\n"
    noBAQ="noBAQ: -B\n"
    maxDEP="maxDEP: -d 10000000\n"
    mapQUAL="mapQUAL: -q 20\n"
    bedFILE='bedFILE: ""\n'
    # 2C. mpileupUNSPLIT only variables
    # 2D. mpileupSPLIT only variables
    # 2E. Write to file
    yamlTARGET.write("\n\n\n#################################\n# ----- " + moduleNAME + " Parameters ------ #\n#################################\n")
    yamlTARGET.write("#            Software           #\n" + mpileup_samtoolsProg)
    yamlTARGET.write("#        Shared Variables       #\n" + mpileupDIR + bitFLAG + countORPHAN + noBAQ + maxDEP + mapQUAL + bedFILE)
    yamlTARGET.write("#         mpileupUNSPLIT        #\n")
    yamlTARGET.write("#          mpileupSPLIT         #\n")
    yamlTARGET.write("#################################\n")

# 3 --- JSON File
# Build the JSON file.
# 3A. Read file to parse and store '.json'  object.
with open(sys.argv[2], "r+") as jsonTARGET:
    jsonOBJ = json.load(jsonTARGET)
    jsonOBJ['mpileupUNSPLIT'] = {
            "clusterSpec": "-V -S /bin/bash -o log/mpileup/mpileupUNSPLIT -e log/mpileup/mpileupUNSPLIT -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleMPUU}"
    }
    jsonOBJ['mpileupSPLIT'] = {
            "clusterSpec": "-V -S /bin/bash -o log/mpileup/mpileupSPLIT -e log/mpileup/mpileupSPLIT -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleMPUS}_chr{wildcards.chrMPUS}"
    }
# 3B. Recreate JSON file to delete exiting text.
with open(sys.argv[2], "w+") as jsonTARGET:
    json.dump(jsonOBJ, jsonTARGET, indent=4)


# 4 --- Snakefile
# Open and append o file a descriptin and the last rule call.
with open(sys.argv[3], "a+") as pipeTARGET:
    pipeTARGET.write(
        "\n\n#***** " + moduleNAME + " *****\n" +
        "#  Included:\n" +
        "#    mpileupUNSPLIT:     Generated mpileup file from BAM file.\n" +
        "#    mpileupSPLIT:     Generated mpileup file from BAM file.\n" +
        "#  Files:\n" +
        "#    Input:      .BAM\n" +
        "#    Output:     .mpileup\n" +
        'include: "' + os.path.dirname(os.path.realpath(__file__)) + '/' + moduleNAME + '_INCLUDE"\n' +
        "#  Required: NONE\n" +
        "#  Call via: \n" +
        '#UNSPLIT  expand("{outputDIR}/{mpileupDIR}/{samples}.mpileup", outputDIR=config["outputDIR"], mpileupDIR=config["mpileupDIR"], samples=config["sample"])\n'
        '#SPLIT    expand("{outputDIR}/{mpileupDIR}/{samples}_{chrLIST}.mpileup", outputDIR=config["outputDIR"], mpileupDIR=config["mpileupDIR"], samples=config["sample"], chrLIST=config["chrLIST"])\n'
    )
#-----------------------------------------------------------------------------------------------------------------------------------------------------
