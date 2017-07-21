#-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Author: Tim Boyarski
#   Date:   2017-06-28
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Call: python startHERE.py /path/to/project/location projectDirectoryName module1 module2 module3
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Purpose: This code builds the starting project environment directory. It
#   provides some of the basic files required for a project. The files are
#   provided to help users understand what files are required by the program.
#   It's either this or your read the README and the Pipeline Vignette and
#   you then figure it out yourself. This is just a convenience script.
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Request os permissions to be able to access and create directories.
from os import listdir, path, mkdir, getcwd

# Access packages to interact with shell
from subprocess import call, sys

# Request sys to abe able to use CLI arguments.
from sys import argv

# Gathers user name for tagging when creating files.
from getpass import getuser

# Used for timestamping the log files.
from time import localtime, strftime
#-----------------------------------------------------------------------------------------------------------------------------------------------------



##################################################
# getModuleList
##################################################
# Function provides the list of current available modules.
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def getModuleList():
    # Get a list of all the available modules.
    moduleList=listdir((path.dirname(getcwd())))

    # Remove all the things I don't want to the user seeing. List won't likely change.
    for omittedFileName in ['README.md', 'SnakeTricks.md', 'TEMPLATE', 'startHERE', 'buildFile']:
        if omittedFileName in moduleList:
            moduleList.remove(omittedFileName)
    return moduleList
#-----------------------------------------------------------------------------------------------------------------------------------------------------



##################################################
# printModuleList
##################################################
# Function prints the list of current available modules.
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def printModuleList(moduleList):
    wordCounter = 0
    print("\t", end='')
    for x in moduleList:
        print("\t\t" + x, end='')
        wordCounter += 1
        if wordCounter % 5 == 0:
            print("\n\t", end='')
    print("\n")
#-----------------------------------------------------------------------------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# PYTHON SCRIPT #
# 0 --- Accept and assign if minimal number of arguements provided.
if len(argv) < 3:
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
    buildLocation = argv[1]
    directoryName = argv[2]

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 1 --- Validate existence of user provided destination.
if path.isdir(buildLocation) == False:
    print("Invalid directory location")
    exit()
else:
    print("Creating workspace directory " + directoryName + " at location:\n")
    print("\t" + buildLocation + '\n')

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 2 --- Primary Setup for buildPipe.py file.
# Variable to hold location of buildPipe.py file.
buildDirectory = buildLocation + '/' + directoryName
buildPipeFILE = buildDirectory + "/buildPipe.py"

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 3 --- Begin creation and population of directory.
mkdir(buildDirectory)

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 4 --- Creating buildPipe.py
with open(buildPipeFILE, "a+") as outputTARGET:
    # 4A. Write header for file, getting user name and date
    outputTARGET.write(
        "#-----------------------------------------------------------------------------------------------------------------------------------------------------\n"
        "# Author: " + getuser() + "\n"
        "# Date: " + strftime("%Y-%m-%d @ %H-%M ", localtime()) + "\n"
        "#-----------------------------------------------------------------------------------------------------------------------------------------------------\n"
    )

    # 4B. Copy in template buildPipe.py from resources/buildPipeCore.txt
    with open("resource/buildPipeCore.txt", "r") as inputTARGET:
        for lines in inputTARGET:
            outputTARGET.write(lines)

    # 4C. Add the absoulute working directory of the Snakemake Folder System, it's 2 above current directory.
    snakeDIR = path.dirname(path.dirname(getcwd()))
    outputTARGET.write(
        '\n# Absolute directory for the Snakemake code repository.\n'
        'snakeDIR="' + snakeDIR + '"\n'
        "#-----------------------------------------------------------------------------------------------------------------------------------------------------\n"
    )


    # 4D. Add the call for the pythonic buildFile module.
    outputTARGET.write(
        '\n\n\n'
        "#-----------------------------------------------------------------------------------------------------------------------------------------------------\n"
        '# PYTHON SCRIPT #\n'
        '#--------------------\n'
        "# Module 0:  Call to generate .YAML and Snakefiles with header information.\n"
        "call('python ' + snakeDIR + '/modules/py_buildFile/buildFile.py '"
        " + TYPE + ' ' + SAMPLE + ' ' + REFFILE + ' ' +  YAMLFILE + ' ' + CLUSTERFILE"
        " + ' ' + SNAKEFILE, shell=True)"
    )

    # 4E. Adding optionally requested Snakemake modules to buildPipe.py
    argCounter=3
    moduleList = getModuleList()
    while(argCounter < len(argv)):
        if argv[argCounter] in moduleList:
            print("Module found: " + argv[argCounter])
        else:
            print("**Warning** Module not found: " + argv[argCounter] +
                  "\n**Warning** Still added string, please check buildPipe.py to validate path"
                  " to module: " + argv[argCounter]
                  )
        outputTARGET.write(
            "\n\n# Module " + str(argCounter - 2) + ":\n"
            "call('python ' + snakeDIR + '/modules/" + argv[argCounter] + "/"
            + argv[argCounter] + ".py ' "
            "+ YAMLFILE + ' ' + CLUSTERFILE + ' ' +  SNAKEFILE, shell=True)"
        )
        argCounter += 1

    # 4F. Write one last line to imply the end of the listed modules.
    outputTARGET.write(
        "\n#-----------------------------------------------------------------------------------------------------------------------------------------------------\n"
    )

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 5 --- Copying over template and convenience files.
call("cp resource/clean.sh " + buildDirectory, shell=True)
call("cp resource/README.md " + buildDirectory, shell=True)

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 6 --- Copy over this input directory to the user new build location.
call(" cp -rf input " + buildDirectory, shell=True)

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 7 --- Final reporting to send you to the directory you just created!
print("Build complete!\n")
#-----------------------------------------------------------------------------------------------------------------------------------------------------
