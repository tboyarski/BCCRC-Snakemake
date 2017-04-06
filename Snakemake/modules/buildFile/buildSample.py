#-------------------------------
#   Author: Tim Boyarski        
#   Date:   2017-03-06          
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
#       -buildSample: Used to call the sample functions and write to file.      
#           return: None                                                        
#-------------------------------------------------------------------------------


#sampleHashLines
#-------------------------------------------------------------------------------
# Function takes in a file name to generate a pythonic dictionary               
#   of the key-value pairs inside the file. File is to have the                 
#   key value pairs each on a separate line. They may be separated              
#   by any delimited accepted by '.split()'.                                    
#-------------------------------------------------------------------------------
def sampleListPair(fileName):
    # Delcaration of dictionary to hold the values
    sampleList = {}

    # Open file, read lines, split lines, stored key-value pair.
    with open(fileName, 'r') as f:
        for s in f.readlines():
            temp = s.split()
            sampleList[temp[0]] = temp[1]
    
    f.close()
    return sampleList
#-------------------------------------------------------------------------------


#sampleListLines
#-------------------------------------------------------------------------------
# Function takes in a file name to generate a pythonic list of the              
#   names of each sample as stored inside the file. The file is to              
#   have each sample name stored on a separate line                             
#-------------------------------------------------------------------------------
def sampleListSingle(fileName):
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


# buildSample.py
#-------------------------------------------------------------------------------
# Fucntion will validate user format, and append the sample names, as provided
#   in the sample file, to the end of the provided yamlFILE. 
#-------------------------------------------------------------------------------
def buildSample(format, sampleFILE, yamlFILE):
    # Interpret user command and pass filename to appropriate function call.
    if format == "pair":
        userSamples = "sample: " + str(sampleListPair(sampleFILE)) + "\n"
    elif format == "single": 
        userSamples = "sample: " + str(sampleListSingle(sampleFILE)) + "\n"
    elif format == "csv": 
        userSamples = "sample: " + str(sampleListCSV(sampleFILE)) + "\n"
    else:
        print("Invalid format: buildSample.py failed.")

    # Write the parsed result to the user's third argument.
    with open(yamlFILE, "r+") as yamlTARGET:
        # Seek to end of file.
        yamlTARGET.seek(0,2)
        # Write it to file
        yamlTARGET.write("#         -- Sample --          #\n" + userSamples)
        yamlTARGET.write("#################################\n")
#-------------------------------------------------------------------------------
