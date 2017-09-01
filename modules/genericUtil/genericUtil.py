#---------------------------------------------------
# Author:   Tim Boyarski
# Date:     2017-06-21
#-----------------------------------------------------------
# Call: call("python " + snakeDIR + "/modules/utils/utils.py " + YAMLFILE + " " + CLUSTERFILE + " " + SNAKEFILE, shell=True)
#
# Purpose: Automate the population of user's pipeline
#   Snakefile, '.YAML', and '.JSON' files.
#-------------------------------------------------------------------
# PYTHON PACKAGES #
#------------------
# Request sys so be able to use CLI arguments.
from sys import argv

# Request json to be able to load and write to the config.json file.
from json import load, dump

# Request os permissions to be able to create directories for the log files.
from os import path, mkdir

# Global variable used for reporting of the module name.
moduleNAME = "genericUtil"
#-----------------------------------------------------------------------------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# PYTHON SCTIPT #
#----------------
# 0 --- Validate number of user arguments.
if len(argv) != 4:
    print("Please provide arguments as follows:")
    print("python " + moduleNAME + ".py yaml json snake")
    print("\t-yaml = 'path/name' of the yaml file to write the pipeline parameters")
    print("\t-json = 'path/name' of the json file we write the cluster config to")
    print("\t-snake = 'path/name' of snakefile we are building")
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 1 --- Log Files
# Check if directories exist for logging, as the DRMAA caller cannot create directories.
if (path.isdir("log")) != True:
    print(moduleNAME + ".py \tCreating: log/")
    mkdir("log")
if (path.isdir("log/" + moduleNAME) != True):
     # Maintain this list of active submodules.
     ruleLIST = ['tableMERGE']
    # 1A. Create module directory.
     mkdir("log/" + moduleNAME)
     print(moduleNAME + ".py \tCreating: log/" + moduleNAME)
     # 1B. Create rule directories and report to user.
     for rule in ruleLIST:
         mkdir("log/" + moduleNAME + "/" + rule)
         print(moduleNAME + ".py \tCreating: log/" + moduleNAME + "/" + rule + "/")
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 2 --- YAML File
# Open and append to file the following required paramters.
with open(argv[1], "a+") as yamlTARGET:
    # 2A. Software
    # 2B. Shared variables
    genericUtilDIR="genericUtilDIR: genericUtil\n"
    # 2C. tableMERGE
    outputMergeLocation="outputMergeLocation: vcfGenUtil_varScan/tables\n"
    # Write it to file
    yamlTARGET.write(
        "\n\n"
        "#####################################\n"
        "# " + moduleNAME + " Parameters\n"
        "#####################################\n"
        "#----------------------------------------------------------------- *Software* ------------------------------------------------------------------------\n" +
        "#----------------------------------------------------------------- *Shared Variables* ----------------------------------------------------------------\n" +
        genericUtilDIR +
        "#----------------------------------------------------------------- tableMERGE ------------------------------------------------------------------------\n" +
        outputMergeLocation +
        "#-----------------------------------------------------------------------------------------------------------------------------------------------------\n"
    )
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 3 --- JSON File
# Generate header for '.json' file.
# Read file to parse and store '.json'  object.
with open(argv[2], "r+") as jsonTARGET:
    jsonOBJ = load(jsonTARGET)
    jsonOBJ['tableMERGE'] = {
            "clusterSpec": "-V -S /bin/bash -o log/genericUtil/tableMERGE -e log/genericUtil/tableMERGE -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_all.samples_{wildcards.annotationSUFFIX}"
    }
# Recreate JSON file to delete exiting text.
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
        "#      tableMERGE_ADAPTOR:         Merge '.txt' tables, copying over the header line of the first file.\n"
        'include: "' + path.dirname(path.realpath(__file__)) + '/' + moduleNAME + '_INCLUDE"\n'
        "#  Call via: \n"
        '#tableMERGE:   expand("{outputDIR}/{tableMergeDIR}/all.samples.{vcfProgram}.{form[1][varType]}{form[1][annotated]}.txt", outputDIR=config["outputDIR"], tableMergeDIR=config["outputMergeLocation"], samples=config["sample"], vcfProgram=config["vcfProgram"], form=read_table(StringIO(config["sampleFORM"]), " ").iterrows()),\n'
        "#-----------------------------------------------------------------------------------------------------------------------------------------------------\n"
    )
#-----------------------------------------------------------------------------------------------------------------------------------------------------
