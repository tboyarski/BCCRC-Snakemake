#-------------------------------
#   Author: Tim Boyarski
#   Date:   2017-05-12
#-------------------------------

# startHERE.py
#-------------------------------------------------------------------------------
# Purpose: This code builds the starting project environment directory. It
#   provides some of the basic files required for a project. The files are 
#   provided to help users understand what files are required by the program.
#   It's either this or your read the README and the Pipeline Vignette and 
#   you then figure it out yourself. This is just a convenience script.
#-------------------------------------------------------------------------------

# WARNING!
# Alterting the location of this file from modules/startHERE will break this file
#   becuase I cheaply parse the absolute path of this directory twice.
#   If you need to change this, search for these command or remove them
#   and improve my code. 
#           os.getcwd()[:-18]
#           os.getcwd()[:-9]

import os
import sys
import getpass
from time import localtime, strftime
from subprocess import call

# Function to provide a list of the available modules.
def getModuleList():
    # Get a list of all the available modules.
    moduleList=os.listdir((os.path.dirname(os.getcwd())))

    # Remove all the things I don't want to the user seeing. List won't likely change.
    for x in ['README.md', 'SnakeTricks.md', 'Template', 'startHERE', 'buildFile']:
        moduleList.remove(x)
    return moduleList

def printModuleList(moduleList):
    wordCounter = 0
    print("\t", end='')
    for x in moduleList:
        print("\t\t" + x, end='')
        wordCounter += 1
        if wordCounter % 5 == 0:
            print("\n\t", end='')
    print("\n")


# Accept mnd assign if minimal number of arguements provided.
if len(sys.argv) < 3:
    print("**ERROR** Invalid number of arguments.\n"
          "\tPlease provide absolute path for desintation of the directory, and also the new directory's name.\n"
          "\t\tE.g. python startHERE.py /home/tboyarski/share/projects/tboyarski NewAwesomeProject\n"
          "\n\n"
          "\tIf you're feeling really confident, you can also just add the module names to the end of the call.\n"
          "\t\tE.g. python startHERE.py /home/tboyarski/share/projects/tboyarski PMBCL1 processBam mpileup varScan annotateVcf utils bamMetrics\n"
          "\n\n"
          "\tHere are the modules currently listed. They may not all work, this just queries the directory and edits a bit.\n"
          )
    printModuleList(getModuleList())
    exit()
else:
    buildLocation = sys.argv[1]
    directoryName = sys.argv[2]

# --- Destination validation.
if os.path.isdir(buildLocation) == False:
    print("Invalid directory location")
    exit()
else:
    print("Creating workspace directory " + directoryName + " at location:\n")
    print("\t" + buildLocation)


# --- Primary Setup
# Variable to hold location of buildPipe.py file.
buildLocation = buildLocation + '/' + directoryName
buildPipeFILE = buildLocation + "/buildPipe.py"


# Begin creation and population of directory.
os.mkdir(buildLocation)

# --- Creating buildPipe.py
# Write heading to file, getting user name and date
with open(buildPipeFILE, "a+") as outputTARGET:
    headerString = (
        "#---------------------\n"
        "# Author: " + getpass.getuser() + "\n"
        "# Date: " + strftime("%Y-%m-%d @ %H-%M ", localtime()) + "\n"
        "#---------------------\n\n"
        )
    outputTARGET.write(headerString)

    # Copy in template buildPipe.py portion
    with open("resource/buildPipeCore.py", "r") as inputTARGET:
        for lines in inputTARGET:
            outputTARGET.write(lines)


    # Add the absoulute working directory of the Snakemake Folder System, it's 2 above current directory.
    snakeDIR = os.path.dirname(os.path.dirname(os.getcwd()))
    outputTARGET.write('snakeDIR="' + snakeDIR + '"\n')
    buildFileString = (
        "\n\n# Call to generate .YAML and Snakefiles with header information.\n"
        "call('python ' + snakeDIR + '/modules/buildFile/buildFile.py '"
        " + TYPE + ' ' + SAMPLE + ' ' + CHRTYPE + ' ' +  YAMLFILE + ' ' + CLUSTERFILE"
        " + ' ' + SNAKEFILE, shell=True)\n\n"
        )
    outputTARGET.write(buildFileString)
    
    # Adding modules to buildPipe.py
    argCounter=3
    moduleList = getModuleList()
    while(argCounter < len(sys.argv)):
        if sys.argv[argCounter] in moduleList:
            print("Module found: " + sys.argv[argCounter])
        else:
            print("**Warning** Module not found: " + sys.argv[argCounter] +
                  "\n**Warning** Still added string, please check buildPipe.py to validate path"
                  " to module: " + sys.argv[argCounter]
                  )
        moduleCallString = (
            "# Module " + str(argCounter - 2) + ":\n"
            "call('python ' + snakeDIR + '/modules/" + sys.argv[argCounter] + "/"
            + sys.argv[argCounter] + ".py ' "
            "+ YAMLFILE + ' ' + CLUSTERFILE + ' ' +  SNAKEFILE, shell=True)\n\n"
            )
        outputTARGET.write(moduleCallString)
        argCounter += 1


# --- Copying over template and convenience files.
# Copy over a convenience based clean-up script
call("cp resource/clean.sh " + buildLocation, shell=True)
call("cp resource/README.md " + buildLocation, shell=True)

# Copy over this input directory to the user new build location. 
call(" cp -rf input " + buildLocation, shell=True)

# Sending you to the directory you just created!
print("Build complete!\n")
print("\t... generating quick-link to send you to the directory just created\n")
print("\tcd " + buildLocation)
