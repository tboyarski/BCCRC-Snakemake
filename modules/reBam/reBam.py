#-----------------------------------------------------------
# Author:   Tim Boyarski                                    
# Date:     2017-02-28                                      
#-----------------------------------------------------------
# Call: call("python " + snakeDIR + "/modules/reBam/reBam.py " + YAMLFILE + " " + CLUSTERFILE + " " + SNAKEFILE, shell=True)
# Rule specific configurations set in:      ReBamPlus.json          
# Rule specific parameters set in:          ReBamPlus.yaml          
# Input:                                    .BAM                    
# Output:                                   1.fastq                 
#                                           2.fastq                 
#                                           realigned.BAM           
#                                           realigned_sorted.BAM,   
#                                           realigned_sorted.BAM.BAI
# Purpose: This is a python script to provide the code structure for
#   the required Snakefile and Parameter calls. The script will     
#   append the information to the two file names provided.          
#-------------------------------------------------------------------

# Request sys so be able to use CLI arguments.
import sys
import json
import os

moduleNAME="reBam"

# 0 --- Validate number of user arguments.
if len(sys.argv) != 4:
    print("Please provide arguments as follows:")
    print("python " + moduleNAME + ".py yaml snake")
    print("\t-yaml = 'path/name' of the yaml file to write the pipeline parameters")
    print("\t-snake = 'path/name' of snakefile we are building")
    print("\t-json = 'path/name' of the json file we write the cluster config to")
    quit() 


# 1 --- Log Files
# Check if directories exist for logging, as the DRMAA caller cannot create directories.
if (os.path.isdir("log")) != True:
    print(moduleNAME + ".py \tCreating: log/")
    os.mkdir("log")
if (os.path.isdir("log/" + moduleNAME) != True):
    os.mkdir("log/" + moduleNAME)
    print(moduleNAME + ".py \tCreating: log/" + moduleNAME)


# 2 --- YAML File
# Open and append to file the following required paramters.
with open(sys.argv[1], "a+") as yamlTARGET:
    # 2A. Software
    undoBAM_picardProg="undoBAM_picardProg: picard\n"
    alignBAM_bwaProg="alignBAM_bwaProg: bwa\n"
    alignBAM_samtoolsProg="alignBAM_samtoolsProg: samtools\n"
    sortBAM_samtoolsProg="sortBAM_samtoolsProg: samtools\n"
    sortBAM_bamsortProg="sortBAM_bamsortProg: bamsort\n"
    indexBAM_samtoolsProg="indexBAM_samtoolsProg: samtools\n"
    filteredBAM_samtoolsProg="filteredBAM_samtoolsProg: samtools\n"
    rmdupBAM_samtoolsProg="rmdupBAM_samtoolsProg: samtools\n"
    markdupBAM_samtoolsProg="markdupBAM_samtoolsProg: samtools\n"
    markdupBAM_bammarkduplicatesProg="markdupBAM_bammarkduplicatesProg: bammarkduplicates2\n"
    # 2B. Shared variables
    fastqDIR="fastqDIR: fastq\n"
    reBamDIR="reBamDIR: reBam\n"
    # 2. undoBAM only variables
    rawBamDIR="rawBamDIR: rawBam\n"
    # 2. alignBAM only variables
    # 2. sortBAM only variables
    sortProg="sortProg: samtools\n"
    # 2. indexBAM only variables
    fileTAG="fileTAG: _realigned_filtered_markdup_sorted\n"
    # 2. filteredBAM only variables
    # 2. rmdupBAM only variables
    # 2. Write to file
    yamlTARGET.write("\n\n#################################\n# ----- " + moduleNAME + " Parameters ------ #\n#################################\n")
    yamlTARGET.write("#       -- Software --          #\n" + undoBAM_picardProg + alignBAM_bwaProg + alignBAM_samtoolsProg \
            + sortBAM_samtoolsProg + sortBAM_bamsortProg + indexBAM_samtoolsProg + filteredBAM_samtoolsProg + rmdupBAM_samtoolsProg \
            + markdupBAM_samtoolsProg + markdupBAM_bammarkduplicatesProg) 
    yamlTARGET.write("#    -- Shared Variables --     #\n" + fastqDIR + reBamDIR)
    yamlTARGET.write("#     -- undoBAM Specific --    #\n" + rawBamDIR)
    yamlTARGET.write("#    -- alignBAM Specific --    #\n")
    yamlTARGET.write("#    -- sortBAM Specific --     #\n" + sortProg)
    yamlTARGET.write("#    -- indexBAM Specific --    #\n" + fileTAG)
    yamlTARGET.write("#   -- filteredBAM Specific --  #\n")
    yamlTARGET.write("#    -- rmdupBAM Specific --    #\n")
    yamlTARGET.write("#################################\n")


# 3 --- JSON File
# Generate header for '.json' file.
jsonOBJ = {}
# Read file to parse and store '.json'  object.
with open(sys.argv[2], "r+") as jsonTARGET:
    jsonRULE = {}
    jsonOBJ = json.load(jsonTARGET)
    jsonRULE['clusterSpec'] = '-V -S /bin/bash -o log/' + moduleNAME + ' -e log/' + moduleNAME + ' -l h_vmem=10G -pe ncpus 1'
    jsonOBJ['undoBAM'] = jsonRULE
    jsonOBJ['alignBAM'] = jsonRULE
    jsonOBJ['sortBAM'] = jsonRULE
    jsonOBJ['indexBAM'] = jsonRULE
    jsonOBJ['rmdupBAM'] = jsonRULE
    jsonOBJ['filteredBAM'] = jsonRULE
# Recreate JSON file to delete exiting text.
with open(sys.argv[2], "w+") as jsonTARGET:
    json.dump(jsonOBJ, jsonTARGET, indent=4)


# 4 -- Snakefile
# Open and append o file a descriptin and the last rule call.
with open(sys.argv[3], "a+") as pipeTARGET:
    pipeTARGET.write(
        "\n\n#**** " + moduleNAME + " ****:\n" +
        "#  Included:\n" +
        "#    undoBAM:    Fastq generation from a BAM file\n" +
        "#    alignBAM:   BAM generation from a Fastq file\n" +
        "#    sortBAM:    Sorting of the BAM file\n" +
        "#    indexBAM:   Indexing of a BAM file\n" +
        "#    filteredBAM:Filtering of a BAM file on read quality\n" +
        "#    rmdupBAM:   Remove dupliates in a BAM file\n" +
        "#  Files:\n" +
        "#    input:      X.BAM\n" +
        "#    output:     X_realigned_sorted.BAM.\n" +
        "#                X_realigned_sorted.BAM.BAI\n" +
        'include: "/home/tboyarski/share/projects/tboyarski/gitRepo-LCR-BCCRC/Snakemake/modules/' + moduleNAME + '/' + moduleNAME + '_INCLUDE"\n' +
        "#  Required: NONE\n" +
        "#  Call via:\n" +
        '#  expand("{outputDIR}/{fastqDIR}/{samples}.{version}.fastq", outputDIR=config["outputDIR"], fastqDIR=config["fastqDIR"], samples=config["sample"], version=["1", "2"])                 #undoBAM\n'+
        '#  expand("{outputDIR}/{reBamDIR}/{samples}_realigned.bam", outputDIR=config["outputDIR"], reBamDIR=config["reBamDIR"], samples=config["sample"])                                       #alignBAM\n'+
        '#  expand("{outputDIR}/{reBamDIR}/{samples}_sorted.bam", outputDIR=config["outputDIR"], reBamDIR=config["reBamDIR"], samples=config["sample"])                                          #sortBAM\n'+
        '#  expand("{outputDIR}/{reBamDIR}/{samples}.bam.bai", outputDIR=config["outputDIR"], reBamDIR=config["reBamDIR"], samples=config["sample"])                                             #indexBAM\n'+
        '#  expand("{outputDIR}/{reBamDIR}/{samples}{fileTAG}.bam.bai", outputDIR=config["outputDIR"], reBamDIR=config["reBamDIR"], samples=config["sample"], fileTAG=config["fileTAG"])         #indexBAM\n'+
        '#  expand("{outputDIR}/{reBamDIR}/{samples}_realigned_sorted.bam.bai", outputDIR=config["outputDIR"], reBamDIR=config["reBamDIR"], samples=config["sample"], fileTAG=config["fileTAG"]) #indexBAM\n'+
        '#  expand("{outputDIR}/{reBamDIR}/{samples}_filtered.bam", outputDIR=config["outputDIR"], reBamDIR=config["reBamDIR"], samples=config["sample"])                                        #filteredBAM\n'+
        '#  expand("{outputDIR}/{reBamDIR}/{samples}_rmdup.bam", outputDIR=config["outputDIR"], reBamDIR=config["reBamDIR"], samples=config["sample"])                                           #rmdupBAM\n'
    )
