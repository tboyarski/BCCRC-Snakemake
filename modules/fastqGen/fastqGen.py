#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Author:   Tim Boyarski
# Date:     2017-06-14
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Call: call("python " + snakeDIR + "/modules/fastqGen/fastqGen.py " + YAMLFILE + " " + CLUSTERFILE + " " + SNAKEFILE, shell=True)
#
# Purpose: Automate the population of user's pipeline
#   Snakefile, '.YAML', and '.JSON' files.
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# PYTHON PACKAGES #
#------------------
# Request sys so be able to use CLI arguments.
from sys import argv

# Request json to be able to load and write to the config.json file.
from json import load, dump

# Request os permissions to be able to create directories for the log files.
from os import path, mkdir

# Global variable used for reporting of the module name.
moduleNAME="fastqGen"
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
    mkdir("log")
    print(moduleNAME + ".py \tCreating: log/")
if (path.isdir("log/" + moduleNAME) != True):
    # Maintain this list of active submodules.
    ruleLIST = ['bam2fastq_picard']
    # 1A. Create module directories
    mkdir("log/" + moduleNAME)
    print(moduleNAME + ".py \tCreating: log/" + moduleNAME)
    # 1B. Report on directories created.
    for rule in ruleLIST:
        mkdir("log/" + moduleNAME + "/" + rule)
        print(moduleNAME + ".py \tCreating: log/" + moduleNAME + "/" + rule + "/")
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 2 --- YAML File
# Open and append to file the following required paramters.
with open(argv[1], "a+") as yamlTARGET:
    # 2A. Software
    fastqGen_samtoolsProg="fastqGen_samtoolsProg: samtools\n"
    fastqGen_picardProg="fastqGen_picardProg: picard\n"
    # 2B. Shared variables
    fastqGenDIR="fastqGenDIR: fastqGen\n"
    # 2C. bam2fastq variables
    rawBamDIR="rawBamDIR: rawBam\n"
    samtoolsSortMem="samtoolsSortMem: 4000000000\n"
    picardValStringency="picardValStringency: VALIDATION_STRINGENCY=LENIENT\n"
    picardMaxRec="picardMaxRec: MAX_RECORDS_IN_RAM=5000000\n"
    # 2D. Write to file
    yamlTARGET.write(
        "\n\n"
        "#####################################\n"
        "# " + moduleNAME + " Parameters\n"
        "#####################################\n"
        "#----------------------------------------------------------------- *Software* ------------------------------------------------------------------------\n" +
        fastqGen_samtoolsProg + fastqGen_picardProg +
        "#----------------------------------------------------------------- *Shared Variables* ----------------------------------------------------------------\n" +
        fastqGenDIR +
        "#----------------------------------------------------------------- bam2fastq_picard ------------------------------------------------------------------\n" +
        rawBamDIR + samtoolsSortMem + picardValStringency + picardMaxRec +
        "#-----------------------------------------------------------------------------------------------------------------------------------------------------\n"
    )
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 3 --- JSON File
# Generate header for '.json' file.
# 3A. Read file to parse and store '.json' object.
with open(argv[2], "r+") as jsonTARGET:
    jsonOBJ = load(jsonTARGET)
    jsonOBJ['bam2fastq_picard'] = {
            "clusterSpec": "-V -S /bin/bash -o log/fastqGen/bam2fastq_picard -e log/fastqGen/bam2fastq_picard -l h_vmem=8G -pe ncpus 2",
            "jobName": "{rule}_{wildcards.sampleB2FP}"
    }
#3B. Recreate JSON file to delete exiting text.
with open(argv[2], "w+") as jsonTARGET:
    dump(jsonOBJ, jsonTARGET, indent=4)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 4 -- Snakefile
# Open and append to file a descriptin and the last rule call.
with open(argv[3], "a+") as pipeTARGET:
    pipeTARGET.write(
        "\n\n#-----------------------------------------------------------------------------------------------------------------------------------------------------\n"
        "#**** " + moduleNAME + " ****:\n"
        "#  Included:\n"
        "#      bam2fastq:              Fastq generation from a '.bam' file.\n"
        "#  Files:\n"
        "#      input:      X.bam\n"
        "#      output:     X.1.fastq\n"
        "#                  X.2.fastq\n"
        'include: "' + path.dirname(path.realpath(__file__)) + '/' + moduleNAME + '_INCLUDE"\n'
        "#  Required: NONE\n"
        "#  Call via:\n"
        '#bam2fastq_picard:     expand("{outputDIR}/{fastqDIR}/{samples}.{readDirection}.fastq", outputDIR=config["outputDIR"], fastqDIR=config["fastqDIR"], samples=config["sample"], readDirection=["1", "2"])\n'
        "#-----------------------------------------------------------------------------------------------------------------------------------------------------\n"
    )
#-----------------------------------------------------------------------------------------------------------------------------------------------------
