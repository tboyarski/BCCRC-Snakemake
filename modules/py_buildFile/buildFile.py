#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Author: Tim Boyarski
# Date:   2017-06-28
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Call: call("python " + snakeDIR + "/modules/buildFile/buildFile.py single " + SAMPLE + " " +  YAMLFILE + " " + CLUSTERFILE + " " + SNAKEFILE, shell=True)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Purpose: Validate arguments and call functions to generate the files required by
#   a Snakemake pipeline. Two scripts were written to assist in the generation and
#   population of the required pipeline files.
#
#   **NOTE** Calls the following scripts:
#       buildHeader.py
#       buildSample.py
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# PYTHON PACKAGES #
#------------------
# Creates the required generic files (YAML, JSON, Snakemake)  and writes the headers of each.
from buildHeader import buildHeader

# Appends to the YAML file the sample specific information.
from buildSample import buildSample

# Access of CLI arguements.
from subprocess import sys

# Request sys to abe able to use CLI arguments.
from sys import argv

# Assess validity of a file.
from os import path
#-----------------------------------------------------------------------------------------------------------------------------------------------------



##################################################
# exit_function
##################################################
# Function used to alert users when they do not provide this script the correct
#   number of arguments.
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def exit_function():
    print("Error during processing within buildFile.py")
    print("Please provide arguments as follows:")
    print("  **python buildFile.py type input refFile yaml json Snakefile**")
    print("\t -type~1 = type of sample coupling, E.g 'pair' or 'single'")
    print("\t -input~2 = 'name' of file with sample names, formatted as per type, E.g sampleFILEsingle.txt")
    print("\t -refFile~3 = '/path/to/name' of file to be used a genomic reference, directiory must also contain supporting genomic files")
    print("\t -yaml~4 = 'name' of the yaml file we write the samples to, E.g. config.yaml")
    print("\t -json~5 = 'name' of the json file we write the cluster config to, E.g. config.json")
    print("\t -Snakefile~6 = 'name' of the Snakefile to write rules to. E.g Snakefile")
    quit()
#-----------------------------------------------------------------------------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# PYTHON SCRIPT #
#----------------
# 0 --- Argument Count Validation
# Validation the user provided the correct number of arguments.
if len(argv) != 7:
    print("Incorrect nuber of arguments. ")
    exit_function()
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 1 --- Format Validation
# Validate the user correctly advised of their choice of sample file format.
if argv[1]=="single":
    print("buildFile.py \tUsing: single column format.")
elif argv[1]=="pair":
    print("buildFile.py \tUsing: paired column format.")
else:
    print("You have not provided a proper sample file format argument.\n")
    exit_function()
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 2 --- Referience file validation
# Confirm file exists.
if path.isfile(argv[3]):
    # 2A. Check that the file ends with '.fa'
    if argv[3][-3:] != '.fa':
        print("Incorrect reference file provided. Must end in '.fa'")
        exit_function()
else:
    print("Unable to find reference file")
    exit_function()
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 3 --- Report and call.
# Provide user import and explain the actions being performed.
print("buildFile.py \tSampling: " + argv[2])
print("buildFile.py \tCreating: " + argv[4] + "\n\t\tCreating: " + argv[5] + "\n\t\tCreating: " + argv[6])

# 3A. Create and populate files with generic parameters.
buildHeader(argv[3], argv[4], argv[5], argv[6])

# 3B. Parse user sample file and add sample names to YAML file.
buildSample(argv[1], argv[2], argv[4])
#-----------------------------------------------------------------------------------------------------------------------------------------------------
