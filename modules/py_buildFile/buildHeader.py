#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Author: Tim Boyarski
# Date:   2017-06-28
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Purpose: This function builds the headers for the YAML, JSON, and Snakemake files.
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# PYTHON PACKAGES #
#------------------
# Assess validity of a directory and to make a directory.
from os import path, mkdir

# To create and manipulate JSON objects written to file for JSON file.
from json import load, dump

# To identify user and to write their name to the generated file.
from getpass import getuser

# Used for timestamping the log files.
from time import localtime, strftime
#-----------------------------------------------------------------------------------------------------------------------------------------------------



##################################################
# genSupportingFileList
##################################################
# Function used to assemble the supporting file names and to
#   return all these names in a list objet.
#
#   **Pre-Condition** Validated to be a file ending in '.fa'
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def genSupportingFileList(refFile):
    print("\t...Calling genSupportingFileList")
    # Object to store the list of chromosomes.
    supFileList = []

    # List of all the required file suffixes
    supportingRefFileSuffixList=['.dict',
        '.fa.amb',
        '.fa.ann',
        '.fa.bwt',
        '.fa.fai',
        '.fa.pac',
        '.fa.sa']

    # Generate list of files using reference file name as a base.
    for suffix in supportingRefFileSuffixList:
        supFileList.append(refFile[:-3] + suffix)

    # Return generated list
    return supFileList
#-----------------------------------------------------------------------------------------------------------------------------------------------------



##################################################
# genChrList
##################################################
# Function used to parse the reference 'fa.fai' file in order to generate a
#   list of the chromosomes applicable to the dataset.
#
#   **Pre-Condition** Validated to be a file ending in '.fa'
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def genChrList(refFile):
    print("\t...Calling genChrList")
    # Object to store the list of chromosomes.
    refChrList = []

    # Setup the desired file ending as '.fa.fai'
    faiRefFile = refFile + '.fai'

    # Store the values from the first column of every line in a list.
    with open(faiRefFile, 'r') as inputFILE:
        for line in inputFILE:
            refChrList.append(line.split()[0])

    # Return generated list
    return refChrList
#-----------------------------------------------------------------------------------------------------------------------------------------------------



##################################################
# buildHeader
##################################################
# Function used to write the generic headaer information required at the top of,
#   and unique to, each file (YAML, JSON, Snakemake). These files form the basis
#   configuration documents which the Snakemake pipeline refers to when linking
#   or assessing variables.
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def buildHeader(userRefFILE, yamlNAME, jsonNAME, snakeNAME):
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # 0 --- Input Validation
    # No input validation performed. Function is being called by a script.
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # 1 --- Log Files
    # Check if directories exist for logging, as the DRMAA caller cannot create directories.
    if (path.isdir("log")) != True:
        print("buildHeader.py \tCreating: log/")
        mkdir("log")
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # 2 --- YAML File
    # Generate and append to file the following required paramters.
    with open(yamlNAME, "w+") as yamlTARGET:
        # 2A. Global Parameters
        shellCallFile="shellCallFile: shellCalls.txt\n"
        offCluster="offCluster: False\n"
        fastqKEEP="fastqKEEP: True\n"
        inputPartList='inputPartList: input/inputPartList.txt\n'
        refFILE="refFILE: " + userRefFILE + "\n"
        supportingRefFILE="supportingRefFILE: " + str(genSupportingFileList(userRefFILE)) + '\n'
        chrLIST="chrLIST: " + str(genChrList(userRefFILE)) + '\n'
        # 2A. Wildcard Contraint Regex
        sampleREGEX="sampleREGEX: '[^_|-|\/][0-9a-zA-Z]*'\n"
        chrREGEX="chrREGEX: '(_[0-9a-zA-Z\.]*(\.\d)?)?'\n"
        vcfProgramREGEX="vcfProgramREGEX: '[0-9a-zA-Z]*'\n"
        varTypeREGEX="varTypeREGEX: '[0-9a-zA-Z]*'\n"
        fastqReadDirectionREGEX="fastqReadDirectionREGEX: '(\.\d)?'\n"
        fastqCompressionSuffixREGEX="fastqCompressionSuffixREGEX: '(\.gz)?'\n"
        # 2B. Global Directories
        inputDIR="inputDIR: input\n"
        outputDIR="outputDIR: output\n"
        bamDIR="bamDIR: bam\n"
        fastqDIR="fastqDIR: fastq\n"
        metricsDIR="metricsDIR: metrics\n"
        mpileupDIR="mpileupDIR: mpileup\n"
        # 2C. Write to file
        yamlTARGET.write(
            "#-----------------------------------------------------------------------------------------------------------------------------------------------------\n"+
            "# Author: " + getuser() + "\n"+
            "# Date: " + strftime("%Y-%m-%d.%H-%M-%S", localtime()) + "\n"+
            "#-----------------------------------------------------------------------------------------------------------------------------------------------------\n"+
            "\n\n"+
            "#####################################\n"+
            "# Global Parameters\n"+
            "#####################################\n"+
            "#----------------------------------------------------------------- Parameters ------------------------------------------------------------------------\n" +
            shellCallFile + offCluster + fastqKEEP + inputPartList + refFILE + supportingRefFILE + chrLIST +
            "#----------------------------------------------------------------- Wildcard Constraint Regex ---------------------------------------------------------\n" +
            sampleREGEX + chrREGEX + vcfProgramREGEX + varTypeREGEX + fastqReadDirectionREGEX + fastqCompressionSuffixREGEX +
            "#----------------------------------------------------------------- Directory -------------------------------------------------------------------------\n" +
            inputDIR + outputDIR + bamDIR + fastqDIR + metricsDIR + mpileupDIR
        )
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # 3 --- JSON File
    # Generate header for '.json' file.
    with open(jsonNAME, "w+") as jsonTARGET:
        jsonOBJ = {}
        jsonOBJ['__default__'] = {
                "clusterSpec": "-V -S /bin/bash -o log -e log -l h_vmem=10G -pe ncpus 1",
                "jobName": "{rule}__defaultSpec__"
        }
        dump(jsonOBJ, jsonTARGET, indent=4)
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # 4 -- Snakefile
    # Generate and append to file a header for the Snakemake file.
    with open(snakeNAME, "w+") as snakeTARGET:
        snakeTARGET.write(
            "#-----------------------------------------------------------------------------------------------------------------------------------------------------\n"+
            "# Author: " + getuser() + "\n"+
            "# Date: " + strftime("%Y-%m-%d.%H-%M-%S", localtime()) + "\n"+
            '# Call using: snakemake --jobs 10 --cluster-config input/config.json --jobname "{cluster.jobName}{jobid}" --drmaa "{cluster.clusterSpec}"\n'+
            "#-----------------------------------------------------------------------------------------------------------------------------------------------------\n"+
            '\n# Used by some modules which require paired tumor-normal samples\nfrom pandas import read_table\n'+
            '\n# Used by some modules which require paired tumor-normal samples\nfrom io import StringIO\n'+
            '\n# Global config:\n'+
            'configfile: "' + yamlNAME + '"\n\n'+
            "#-----------------------------------------------------------------------------------------------------------------------------------------------------\n"+
            '\n# Global rule to pull all output files:\n'+
            'rule all:\n    input:\n'+
            '        # Single: Normal Runs\n'+
            '        expand(...)\n'
    )
#-----------------------------------------------------------------------------------------------------------------------------------------------------
