#-------------------------------------------------------
# Author:   Tim Boyarski                                
# Date:     2017-03-28                                  
#-------------------------------------------------------
# Call: call("python " + snakeDIR + "/modules/tPile/tPile.py " + YAMLFILE + " " + CLUSTERFILE + " " + SNAKEFILE, shell=True)
# Input:                                    .BAM        
# Output:                                   .mpileup    
# Purpose: Automate the population of user's pipeline   
#   Snakefile, '.YAML', and '.JSON' files.              
#-------------------------------------------------------

#Highlight needed fields with: XXXXXXXX

# Request sys so be able to use CLI arguments
import sys
import json
import os

moduleNAME = "tPile"

# 0 --- Validate number of user arguments.
if len(sys.argv) != 4:
    print("Please provide arguments as follows:")
    print("python " + moduleNAME + ".py yaml snake")
    print("\t-yaml = 'path/name' of the yaml file to write the pipeline parameters")
    print("\t-snake = 'path/name' of snakefile we are building")
    print("\t-json = 'path/name' of the json file we write the cluster config to")
    quit() 


# 1 --- Log Files
# Check if directories exist for logging, as the DRMAA caller cannot create directories.
if (os.path.isdir("log")) != True:
    print(moduleNAME + ".py \tCreating: log/")
    os.mkdir("log")
if (os.path.isdir("log/" + moduleNAME) != True):
    os.mkdir("log/" + moduleNAME)
    print(moduleNAME + ".py \tCreating: log/" + moduleNAME)


# 2 --- YAML File
# Open and append to file the following required paramters.
with open(sys.argv[1], "a+") as yamlTARGET:
    # 2A. Software
    tPile_samtoolsProg = "tPile_samtoolsProg: samtools\n"
    # 2B. Shared variables
    tpileDIR="tpileDIR: tPile\n"
    bitFLAG="bitFLAG: 512\n"
    countORPHAN="countORPHAN: -A\n"
    noBAQ="noBAQ: -B\n"
    maxDEP="maxDEP: -d 10000000\n"
    mapQUAL="mapQUAL: -q 20\n"
    # 2C. tPile only variables
    # 2D. Write to file
    yamlTARGET.write("\n\n\n#################################\n# ----- " + moduleNAME + " Parameters ------ #\n#################################\n")
    yamlTARGET.write("#       -- Software --          #\n" + tPile_samtoolsProg)
    yamlTARGET.write("#    -- Shared Variables --     #\n" + tpileDIR + bitFLAG + countORPHAN + noBAQ + maxDEP + mapQUAL)
    yamlTARGET.write("#     -- tPile Specific --      #\n")
    yamlTARGET.write("#################################\n")


# 3 --- JSON File
# Generate header for '.json' file.
jsonOBJ = {}
# Read file to parse and store '.json'  object.
with open(sys.argv[2], "r+") as jsonTARGET:
    jsonRULE = {}
    jsonOBJ = json.load(jsonTARGET)
    jsonRULE['clusterSpec'] = '-V -S /bin/bash -o log/' + moduleNAME + ' -e log/' + moduleNAME + ' -l h_vmem=10G -pe ncpus 1'
    jsonOBJ['mPileUNSPLIT'] = jsonRULE
    jsonOBJ['mPileSPLIT'] = jsonRULE
# Recreate JSON file to delete exiting text.
with open(sys.argv[2], "w+") as jsonTARGET:
    json.dump(jsonOBJ, jsonTARGET, indent=4)


# 4 --- Snakefile
# Open and append o file a descriptin and the last rule call.
with open(sys.argv[3], "a+") as pipeTARGET:
    pipeTARGET.write(
        "\n\n#***** " + moduleNAME + " *****\n" +
        "#  Included:\n" +
        "#    tPile:     Generated mpileup file from BAM file.\n" +
        "#  Files:\n" +
        "#    Input:      .BAM\n" +
        "#    Output:     .mpileup\n" +
        'include: "/home/tboyarski/share/projects/tboyarski/gitRepo-LCR-BCCRC/Snakemake/modules/' + moduleNAME + '/' + moduleNAME + '_INCLUDE"\n' +
        "#  Required: NONE\n" +
        "#  Call via: \n" +
        '#    expand("{outputDIR}/{tpileDIR}/{samples}.mpileup", outputDIR=config["outputDIR"], tpileDIR=config["tpileDIR"], samples=config["sample"])\n'
    )

