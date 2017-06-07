#-------------------------------
#   Author: Tim Boyarski        
#   Date:   2017-03-06          
#-------------------------------
# Call: call("python " + snakeDIR + "/modules/buildFile/buildFile.py single " + SAMPLE + " " +  YAMLFILE + " " + CLUSTERFILE + " " + SNAKEFILE, shell=True)
#-------------------------------------------------------------------------------
# Purpose: This code takes in arguments to help generate the "sample" line of   
#   the .YAML file. There are three functions designed to do this. The functions
#   differ in that they accept files of different formats, and output collection
#   type based off of relative input format.                                    
#       -sampleHashLines: Used for parsing key-value pairs                      
#           return: Pythonic Dictionary                                         
#       -sampleListLines: Used for parsing samples on separate lines            
#           return: Pythonic List                                               
#       -sampleListCSV: Used for parsing CSV delimited samples                  
#           return: Pythonic List                                               
#-------------------------------------------------------------------------------

from buildHeader import buildHeader
from buildSample import buildSample
from subprocess import sys
from os import path

# exit_function
#-------------------------------------------------------------------------------
# Function used to alert useres when they do not provide this script the correct
#   number of arguments.                                                        
#-------------------------------------------------------------------------------
def exit_function():
    print("Incorrect nuber of arguments. ")
    print("Please provide arguments as follows:")
    print("  **python buildFile.py type samplefilename.txt yours.yaml Snakefile**")
    print("\t -type~1 = 'pair', 'single', or 'csv'")
    print("\t -input~2 = 'path/name' of file with sample names, formatted as per type")
    print("\t -chrtype~3 = chromosome formatting type; Human: 'hncbi', 'hucs'; Mouse: 'mncbi', 'mucs'")
    print("\t -yaml~4 = 'path/name' of the yaml file we write the samples to")
    print("\t -json~5 = 'path/name' of the json file we write the cluster config to")
    print("\t -Snakefile~6 = 'path/name' of the Snakefile to write rules to")
    quit()
#-------------------------------------------------------------------------------

# 0 --- Validate argument count.
if len(sys.argv) != 7:
    exit_function()

# 1 --- Validate user's format command
if (sys.argv[1]=="single"):
    print("buildFile.py \tUsing: single column format.")        
elif (sys.argv[1]=="pair"):
    print("buildFile.py \tUsing: paired column format.")        
elif (sys.argv[1]=="csv"):
    print("buildFile.py \tUsing: csv format.")        
else:
    print("You have not provided a proper sample file format argument.\n")

# 2 --- Validate user's chromosomal type command
if (sys.argv[3]=="hncbi"):
    typeREPORT="Human: NCBI ~ " + sys.argv[3]
elif (sys.argv[3]=="hucs"):
    typeREPORT="Human: UCS ~ " + sys.argv[3]
elif (sys.argv[3]=="mncbi"):
    typeREPORT="Mouse: NCBI ~ " + sys.argv[3]
elif (sys.argv[3]=="mucs"):
    typeREPORT="Mouse: UCS ~ " + sys.argv[3]
else:
    print("You have not provided a proper chromosomal format argument.\n")

# 3 --- Reporting for user and calls to file building methods.
if path.isfile(sys.argv[2]):
    print("buildFile.py \tSampling: " + sys.argv[2] + " of type: " + typeREPORT) 
    print("buildFile.py \tCreating: " + sys.argv[4] + "\n\t\tCreating: " + sys.argv[5] + "\n\t\tCreating: " + sys.argv[6]) 
    # Creatae and populate files and generic parameters.
    buildHeader(sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    # Parse user sample file and add sample names to YAML file.
    buildSample(sys.argv[1], sys.argv[2], sys.argv[4])
else:
    print("buildFile.py \tFile not found:" + sys.argv[2])
