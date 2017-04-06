#-------------------------------
#   Author: Tim Boyarski        
#   Email:  tboyarski@bccrc.ca  
#   Date:   2017-03-02          
#-------------------------------

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


#sampleHashLines
#-------------------------------------------------------------------------------
# Function takes in a file name to generate a pythonic dictionary               
#   of the key-value pairs inside the file. File is to have the                 
#   key value pairs each on a separate line. They may be separated              
#   by any delimited accepted by '.split()'.                                    
#-------------------------------------------------------------------------------
def sampleHashLines(fileName):
    # Delcaration of dictionary to hold the values
    sampleHash = {}

    # Open file, read lines, split lines, stored key-value pair.
    with open(fileName, 'r') as f:
        for s in f.readlines():
            temp = s.split()
            sampleHash[temp[0]] = temp[1]
    
    f.close()
    return sampleHash
#-------------------------------------------------------------------------------


#sampleListLines
#-------------------------------------------------------------------------------
# Function takes in a file name to generate a pythonic list of the              
#   names of each sample as stored inside the file. The file is to              
#   have each sample name stored on a separate line                             
#-------------------------------------------------------------------------------
def sampleListLines(fileName):
    # Delcaration of list to hold the values
    sampleList = []

    # Open file, read lines, split lines, stored key-value pair.
    with open(fileName, 'r') as f:
        for s in f.readlines():
            sampleList.append(s.strip())

    f.close()
    return sampleList
#-------------------------------------------------------------------------------


#sampleListCSV
#-------------------------------------------------------------------------------
# Function takes in a file name to generate a pythonic list of the              
#   names of each sample as stored inside the file. The file is to              
#   have each sample name separated by a comma (.CSV)                           
#-------------------------------------------------------------------------------
def sampleListCSV(fileName):
    # Delcaration of list to hold the values
    sampleList = []

    # Open file, read lines, split lines, stored key-value pair.
    with open(fileName, 'r') as f:
        s = f.readline().strip()
        sampleList = s.split(',')

    f.close()
    return sampleList
#-------------------------------------------------------------------------------


#automatedScripting
# Use first argument to determine how to parse data from second argument.
# exit_function
#-------------------------------------------------------------------------------
# Function used to alert useres when they do not provide this script the correct
#   number of arguments.                                                        
#-------------------------------------------------------------------------------
def exit_function():
    print("Please provide arguments as follows:\n")
    print("python fileParse.py type input output")
    print("\t-type= hash, line, or csv")
    print("\t-input= path+name of file with sample names, formatted as per type")
    print("\t-output= path+name of the yaml file we write the samples to")
    quit()
#-------------------------------------------------------------------------------


# fileParse.py
#-------------------------------------------------------------------------------
# Script will check for the correct number of arguments. It will interpret user
#   arguments to make the correct function all to parse the user provided file
#   name. It returns the parsed results.
#-------------------------------------------------------------------------------

# Required library to accept CLI arguments.
import sys

# Check correct number of arguments.
if len(sys.argv) != 5:
    exit_function()
# Interpret user command and pass filename to appropriate function call.
if sys.argv[1] == "hash":
    userSamples = sampleHashLines(sys.argv[2])
elif sys.argv[1]=="line": 
    userSamples = sampleListLines(sys.argv[2])
elif sys.argv[1]=="csv": 
    userSamples = sampleListCSV(sys.argv[2])
else:
    exit_function()

# Write the parsed result to the user's third argument.
with open(sys.argv[3], "w+") as yamlTARGET:
    #Parameter variables.   
    VER="version: [1, 2]\n"
    fileTAG="fileTAG: _realigned_sorted\n"
    refFILE="refFILE: GRCh37-lite.fa\n"
    paramVAR = "\n#Global Parameter Variables: \n" + VER + fileTAG + refFILE

    #Directory variables.
    bamDIR="bamDIR: bam\n"
    fastqDIR="fastqDIR: fastq\n"
    vcfDIR="vcfDIR: vcf\n"
    mpileDIR="mpileDIR: mpileup\n"
    refDIR="refDIR: ref\n"
    dirVAR = "\n#Global Directory Variables: \n" + bamDIR +  fastqDIR + vcfDIR + mpileDIR + refDIR + refFILE

    # Write it to file
    yamlTARGET.write("#---------------------\n# Author: Unknown\n# Date: 2017-01-01\n#---------------------\n\n")
    yamlTARGET.write("# Global Parameters:\n")
    yamlTARGET.write("sample: " + str(userSamples) + "\n")
    yamlTARGET.write(paramVAR + dirVAR)

# Write the config file name in to the Snakefile (forth argument).
with open(sys.argv[4], "w+") as snakeTARGET:
    snakeTARGET.write("#---------------------\n# Author: Unknown\n# Date: 2017-01-01\n#---------------------\n\n")
    snakeTARGET.write('# Call using: snakemake --jobs 10 --cluster-config BuildArea.json --drmaa "{cluster.minSpec}"\n')
    snakeTARGET.write("# Global config:\n")
    snakeTARGET.write('configfile: "' + sys.argv[3] + '"\n')
    snakeTARGET.write('\n# Global rule to pull all output files:\n')
    snakeTARGET.write('rule all:\n    input:\n        **Replace with Provided Calls**\n\n')
#-------------------------------------------------------------------------------
