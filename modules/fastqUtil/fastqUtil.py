#---------------------------------------------------
# Author:   Tim Boyarski
# Date:     2017-06-28
#-----------------------------------------------------------
# Call: call("python " + snakeDIR + "/modules/fastqUtil/fastqUtil.py " + YAMLFILE + " " + CLUSTERFILE + " " + SNAKEFILE, shell=True)
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
moduleNAME = "fastqUtil"
#-----------------------------------------------------------------------------------------------------------------------------------------------------



##################################################
# fieldGenerator
##################################################
# Function to generate the combination of arguments for vcfGenFields(Paired) variable written to '.YAML' file.
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def fieldGenerator(flagLIST, sampleLIST):
    finalString = ""
    for flag in flagLIST:
        for sample in sampleLIST:
            finalString += 'GEN[' + sample + "]." + flag + " "
    return finalString
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
    print(moduleNAME + ".py \tCreating: log/")
    mkdir("log")
if (path.isdir("log/" + moduleNAME) != True):
     # Maintain this list of active submodules.
     ruleLIST = ['fastq2GZ',
             'fastqc',
             'mergeFASTQ']
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
    fastqUtil_perlProg="fastqUtil_perlProg: perl\n"
    # 2B. Shared variables
    fastqUtilDIR="fastqUtilDIR: fastqUtil\n"
    # 2C. fast2GZ variables
    # 2C. fastqc variables
    fastqc="fastqc: /genesis/extscratch/clc/usr/fastqc-0.10.1/fastqc.pl\n"
    fastqcDIR="fastqcDIR: fastqc\n"
    nogroupFlag="nogroupFlag: ''\n"
    # 2C. mergeFASTQ_ADAPTOR variables
    mergeFastqRootDIR="mergeFastqRootDIR: ''\n"
    # Write it to file
    yamlTARGET.write(
        "\n\n"
        "#####################################\n"
        "# " + moduleNAME + " Parameters\n"
        "#####################################\n"
        "#----------------------------------------------------------------- *Software* ------------------------------------------------------------------------\n" +
        fastqUtil_perlProg +
        "#----------------------------------------------------------------- *Shared Variables* ----------------------------------------------------------------\n" +
        fastqUtilDIR +
        "#----------------------------------------------------------------- fastq2GZ --------------------------------------------------------------------------\n" +
        "#----------------------------------------------------------------- fastqc ----------------------------------------------------------------------------\n" +
        fastqc + fastqcDIR + nogroupFlag +
        "#----------------------------------------------------------------- mergeFASTQ ------------------------------------------------------------------------\n" +
        mergeFastqRootDIR +
        "#-----------------------------------------------------------------------------------------------------------------------------------------------------\n"
    )
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 3 --- JSON File
# Read file to parse and store '.json'  object.
with open(argv[2], "r+") as jsonTARGET:
    jsonOBJ = load(jsonTARGET)
    jsonOBJ['fastq2GZ'] = {
            "clusterSpec": "-V -S /bin/bash -o log/fastqUtil/fastq2GZ -e log/fastqUtil/fastq2GZ -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleFGZ}"
    }
    jsonOBJ['fastqc'] = {
            "clusterSpec": "-V -S /bin/bash -o log/fastqUtil/fastqc -e log/fastqUtil/fastqc -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleFQC}"
    }
    jsonOBJ['mergeFASTQ'] = {
            "clusterSpec": "-V -S /bin/bash -o log/fastqUtil/mergeFASTQ -e log/fastqUtil/mergeFASTQ -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleFM}_{wildcards.readDirection}_{wildcards.compressionSuffix}"
    }
# Recreate JSON file to delete exiting text.
with open(argv[2], "w+") as jsonTARGET:
    dump(jsonOBJ, jsonTARGET, indent=4)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 4 --- Snakefile
# Open and append o file a descriptin and the last rule call.
with open(argv[3], "a+") as pipeTARGET:
    pipeTARGET.write(
        "\n\n#***** " + moduleNAME + " *****\n"
        "#  Included:\n"
        "#      fastq2GZ:                   Run perl QC script and convert a '.bam' file into a '.fastq.zip'\n"
        "#      fastqc:                     Compress a '.fastq' file into a '.fastq.gz' file\n"
        "#      mergeFASTQ_ADAPTOR:         Produce a single '.fastq' file from a list of '.fastq' files.\n"
        'include: "' + path.dirname(path.realpath(__file__)) + '/' + moduleNAME + '_INCLUDE"\n'
        "#  Call via: \n"
        '#fastq2GZ:             expand("{outputDIR}/{fastqDIR}/{samples}.{readDirection}.fastq.gz", outputDIR=config["outputDIR"], fastqDIR=config["fastqDIR"], samples=config["sample"], readDirection=["1", "2"])\n'
        '#fastqc:               expand("{outputDIR}/{fastqcDIR}/{samples}_fastqc.zip", outputDIR=config["outputDIR"], fastqcDIR=config["fastqcDIR"], samples=config["sample"])\n'
        '#mergeFASTQ:           expand("{outputDIR}/{fastqDIR}/{samples}.{readDirection}.fastq{compressionSuffix}", outputDIR=config["outputDIR"], fastqDIR=config["fastqDIR"], samples=config["sample"], readDirection=["1","2"], compressionSuffix=[".gz"])\n'
    )
#-----------------------------------------------------------------------------------------------------------------------------------------------------
