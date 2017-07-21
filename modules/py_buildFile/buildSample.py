#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Author:   Tim Boyarski
# Date:     2017-06-28
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Purpose: This code takes in arguments to help generate the "sample" line of
#   the .YAML file. There are two functions designed to do this. The functions
#   differ in that they accept files of different formats, and output collection
#   type based off of relative input format.
#-----------------------------------------------------------------------------------------------------------------------------------------------------



##################################################
# sampleListPair
##################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Function takes in a file name to generate a pythonic dictionary
#   of the key-value pairs inside the file. File is to have the
#   key value pairs each on a separate line. They may be separated
#   by any delimited accepted by '.split()'.
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def sampleListPair(fileName):
    # Delcaration of dictionary to hold the values
    sampleList = {}

    # Open file, read lines, split lines, stored key-value pair.
    with open(fileName, 'r') as f:
        for s in f.readlines():
            temp = s.split()
            sampleList[temp[0]] = temp[1]

    # Return python dictionary of tumor-normal sample pairs.
    return sampleList
#-----------------------------------------------------------------------------------------------------------------------------------------------------



##################################################
# sampleListSingle
##################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Function takes in a file name to generate a pythonic list of the
#   names of each sample as stored inside the file. The file is to
#   have each sample name stored on a separate line
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def sampleListSingle(fileName):
    # Delcaration of list to hold the values
    sampleList = []

    # Open file, read lines, split lines, stored key-value pair.
    with open(fileName, 'r') as f:
        for s in f.readlines():
            sampleList.append(s.strip())

    # Return python list of sample names.
    return sampleList
#-----------------------------------------------------------------------------------------------------------------------------------------------------



##################################################
# buildSample
##################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Fucntion will validate user format, and append the sample names, as provided
#   in the sample file, to the end of the provided YAML file..
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def buildSample(fileFormat, sampleFILE, yamlFILE):
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # 0 --- Input Validation
    # No input validation performed. Function is being called by a script.
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # 1 --- Variable Declaration & Instantiation
    # Setup function variables.
    if fileFormat == "pair":
        userSamples = "sample: " + str(sampleListPair(sampleFILE)) + "\n"
    else:
        userSamples = "sample: " + str(sampleListSingle(sampleFILE)) + "\n"
    sampleLOC="sampleFILE: " + sampleFILE + "\n"
    sampleFORMAT="sampleFORMAT: " + fileFormat + "\n"
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # 2 --- Write to File.
    # Append to the YAML file the pipeline specific sample data.
    with open(yamlFILE, "r+") as yamlTARGET:
        # 2A. Seek to end of file.
        yamlTARGET.seek(0,2)
        # 2B. Write it to file
        yamlTARGET.write(
            "#----------------------------------------------------------------- Sample Info -----------------------------------------------------------------------\n" +
            userSamples + sampleLOC + sampleFORMAT +
            "#-----------------------------------------------------------------------------------------------------------------------------------------------------\n"
        )
#-----------------------------------------------------------------------------------------------------------------------------------------------------
