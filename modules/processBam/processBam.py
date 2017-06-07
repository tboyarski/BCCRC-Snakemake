#-----------------------------------------------------------
# Author:   Tim Boyarski
# Date:     2017-06-01
#-----------------------------------------------------------
# Call: call("python " + snakeDIR + "/modules/processBam/processBam.py " + YAMLFILE + " " + CLUSTERFILE + " " + SNAKEFILE, shell=True)
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

moduleNAME="processBam"

# 0 --- Validate number of user arguments.
if len(sys.argv) != 4:
    print("Please provide arguments as follows:")
    print("python " + moduleNAME + ".py yaml json snake")
    print("\t-yaml = 'path/name' of the yaml file to write the pipeline parameters")
    print("\t-json = 'path/name' of the json file we write the cluster config to")
    print("\t-snake = 'path/name' of snakefile we are building")
    quit()


# 1 --- Log Files
# Check if directories exist for logging, as the DRMAA caller cannot create directories.
if (os.path.isdir("log")) != True:
    os.mkdir("log")
    print(moduleNAME + ".py \tCreating: log/")
if (os.path.isdir("log/" + moduleNAME) != True):
    # Maintain this list of active submodules.
    moduleLIST = ['alignBAM_bwa','bam2fastq','cleanBAM','fastq2GZ','fastqc',
            'filteredBAM','fixmateBAM','indexBAM','markdupBAM','namesortBAM',
            'rmdupBAM','sortBAM_biobambam','sortBAM_samtools']
    # 1A. Create module directories
    os.mkdir("log/" + moduleNAME)
    print(moduleNAME + ".py \tCreating: log/" + moduleNAME)
    # 1B. Report on directories created.
    for module in moduleLIST:
        os.mkdir("log/" + moduleNAME + "/" + module)
        print(moduleNAME + ".py \tCreating: log/" + moduleNAME + "/" + module + "/")


# 2 --- YAML File
# Open and append to file the following required paramters.
with open(sys.argv[1], "a+") as yamlTARGET:
    # 2A. Software
    processBam_samtoolsProg="processBam_samtoolsProg: samtools\n"
    processBam_picardProg="processBam_picardProg: picard\n"
    processBam_bwaProg="processBam_bwaProg: bwa\n"
    processBam_bamsortProg="processBam_bamsortProg: bamsort\n"
    processBam_perlProg="processBam_perlProg: perl\n"
    processBam_bammarkduplicates2Prog="processBam_bammarkduplicates2Prog: bammarkduplicates2\n"
    SoftwareChoiceFLAG_sortBAM="SoftwareChoiceFLAG_sortBAM: biobambam\n"
    SoftwareChoiceFLAG_alignBAM="SoftwareChoiceFLAG_alignBAM: default\n"
    # 2B. Shared variables
    fastqDIR="fastqDIR: fastq\n"
    processBamDIR="processBamDIR: processBam\n"
    picardValStringency="picardValStringency: VALIDATION_STRINGENCY=LENIENT\n"
    picardMaxRec="picardMaxRec: MAX_RECORDS_IN_RAM=5000000\n"
    # 2C. alignBAM_bwa variables
    picardCompatibility="picardCompatibility: -M\n"
    coreNumber="coreNumber: -t 4\n"
    seqPlatform="seqPlatform: ILLUMINA\n"
    trimReadsFLAG="trimReadsFLAG: False\n"
    phred64="phred64: -Q 33\n"
    firstBaseToKeep="firstBaseToKeep: ''\n"
    lastBaseToKeep="lastBaseToKeep: ''\n"
    # 2C. bam2fastq variables
    rawBamDIR="rawBamDIR: rawBam\n"
    samtoolsSortMem="samtoolsSortMem: 4000000000\n"
    # 2C. cleanBAM variables
    # 2C. fastq2GZ variables
    # 2C. fastqc variables
    fastqc="fastqc: ~/share/usr/fastqc-0.10.1/fastqc.pl\n"
    nogroupFLAG="nogroupFLAG: ''\n"
    # 2C. filteredBAM variables
    filterBitFlag="filterBitFlag: 512\n"
    # 2C. fixmateBAM variables
    # 2C. indexBAM variables
    fileTAG="fileTAG: _realigned_sorted_filtered_markdup\n"
    # 2C. markdupBAM variables
    compressLVL="compressLVL: level=-1\n"
    # 2C. namesortBAM variables
    # 2C. rmdupBAM variables
    # 2C. sortBAM_* variables
    # 2D. Write to file
    yamlTARGET.write("\n\n#################################\n# ----- " + moduleNAME \
            + " Parameters ------ #\n#################################\n")
    yamlTARGET.write("#       -- Software --          #\n" \
            + processBam_samtoolsProg + processBam_picardProg  + processBam_bwaProg \
            + processBam_bamsortProg + processBam_perlProg + processBam_bammarkduplicates2Prog \
            + SoftwareChoiceFLAG_sortBAM + SoftwareChoiceFLAG_alignBAM)
    yamlTARGET.write("#    -- Shared Variables --     #\n" + fastqDIR + processBamDIR \
            + picardValStringency + picardMaxRec)
    yamlTARGET.write("#    -- alignBAM Specific --    #\n" + picardCompatibility + coreNumber \
            + seqPlatform + trimReadsFLAG + phred64 + firstBaseToKeep + lastBaseToKeep)
    yamlTARGET.write("#    -- bam2fastq Specific --   #\n" + rawBamDIR + samtoolsSortMem)
    yamlTARGET.write("#    -- cleanBAM Specific --    #\n")
    yamlTARGET.write("#    -- fastq2GZ Specific --    #\n")
    yamlTARGET.write("#     -- fastqc Specific --     #\n" + fastqc + nogroupFLAG)
    yamlTARGET.write("#   -- filteredBAM Specific --  #\n" + filterBitFlag)
    yamlTARGET.write("#   -- fixmateBAM Specific --   #\n")
    yamlTARGET.write("#    -- indexBAM Specific --    #\n" + fileTAG)
    yamlTARGET.write("#   -- markdupBAM Specific --   #\n" + compressLVL)
    yamlTARGET.write("#  -- namesortBAM Specific --   #\n")
    yamlTARGET.write("#    -- rmdupBAM Specific --    #\n")
    yamlTARGET.write("#   -- sortBAM_* Specific --    #\n")
    yamlTARGET.write("#################################\n")


# 3 --- JSON File
# Generate header for '.json' file.
# 3A. Read file to parse and store '.json'  object.
with open(sys.argv[2], "r+") as jsonTARGET:
    jsonOBJ = json.load(jsonTARGET)
    jsonOBJ['alignBAM_bwa'] = {
            "clusterSpec": "-V -S /bin/bash -o log/processBam/alignBAM_bwa -e log/processBam/alignBAM_bwa -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleAB}"
    }
    jsonOBJ['bam2fastq'] = {
            "clusterSpec": "-V -S /bin/bash -o log/processBam/bam2fastq -e log/processBam/bam2fastq -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleB2F}"
    }
    jsonOBJ['cleanBAM'] = {
            "clusterSpec": "-V -S /bin/bash -o log/processBam/cleanBAM -e log/processBam/cleanBAM -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleCB}"
    }
    jsonOBJ['fastq2GZ'] = {
            "clusterSpec": "-V -S /bin/bash -o log/processBam/fastq2GZ -e log/processBam/fastq2GZ -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleFGZ}"
    }
    jsonOBJ['fastqc'] = {
            "clusterSpec": "-V -S /bin/bash -o log/processBam/fastqc -e log/processBam/fastqc -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleFQC}"
    }
    jsonOBJ['filteredBAM'] = {
            "clusterSpec": "-V -S /bin/bash -o log/processBam/filteredBAM -e log/processBam/filteredBAM -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleFB}"
    }
    jsonOBJ['fixmateBAM'] = {
            "clusterSpec": "-V -S /bin/bash -o log/processBam/fixmateBAM -e log/processBam/fixmateBAM -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleFMB}"
    }
    jsonOBJ['indexBAM'] = {
            "clusterSpec": "-V -S /bin/bash -o log/processBam/indexBAM -e log/processBam/indexBAM -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleIB}"
    }
    jsonOBJ['markdupBAM'] = {
            "clusterSpec": "-V -S /bin/bash -o log/processBam/markdupBAM -e log/processBam/markdupBAM -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleMDB}"
    }
    jsonOBJ['namesortBAM'] = {
            "clusterSpec": "-V -S /bin/bash -o log/processBam/namesortBAM -e log/processBam/namesortBAM -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleNSB}"
    }
    jsonOBJ['rmdupBAM'] = {
            "clusterSpec": "-V -S /bin/bash -o log/processBam/rmdupBAM -e log/processBam/rmdupBAM -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleRDB}"
    }
    jsonOBJ['sortBAM_biobambam'] = {
            "clusterSpec": "-V -S /bin/bash -o log/processBam/sortBAM_biobambam -e log/processBam/sortBAM_biobambam -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleSBB}"
    }
    jsonOBJ['sortBAM_samtools'] = {
            "clusterSpec": "-V -S /bin/bash -o log/processBam/sortBAM_samtools -e log/processBam/sortBAM_samtools -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleSBS}"
    }
#3B. Recreate JSON file to delete exiting text.
with open(sys.argv[2], "w+") as jsonTARGET:
    json.dump(jsonOBJ, jsonTARGET, indent=4)


# 4 -- Snakefile
# Open and append o file a descriptin and the last rule call.
with open(sys.argv[3], "a+") as pipeTARGET:
    pipeTARGET.write(
        "\n\n#**** " + moduleNAME + " ****:\n" +
        "#  Included:\n" +
        "#      alignBAM_bwa:       BAM generation from a '.fastq' file.\n" +
        "#      bam2fastq:          Fastq generation from a '.BAM' file.\n" +
        "#      cleanBAM:           Cleans the provided SAM/BAM, soft-clipping beyond-end-of-reference alignments and setting MAPQ to 0 for unmapped reads.\n" +
        "#      fastq2GZ:           Compress a '.fastq' file into a '.fastq.gz' file.\n" +
        "#      fastqc:             Run Fastqc on '.BAM' files.\n" +
        "#      filteredBAM:        Filtering of a '.BAM' file on read quality.\n" +
        "#      fixmateBAM:         Fill in mate coordinates, ISIZE, and mate related flags from a name-sorted alignment.\n" +
        "#      indexBAM:           Indexing of a '.BAM' file.\n" +
        "#      markdupBAM:         Mark diplicates in a '.BAM' file and produce metrics.\n" +
        "#      namesortBAM:        Produce a name sorted '.BAM' file.\n" +
        "#      rmdupBAM:           Remove dupliates in a '.BAM' file.\n" +
        "#      sortBAM_biobambam:  Sorting of the BAM file, via SAMTOOLS, or BIOBAMBAM.\n" +
        "#      sortBAM_samtools:   Sorting of the BAM file, via SAMTOOLS, or BIOBAMBAM.\n" +
        "#  Files:\n" +
        "#      input:      X.BAM\n" +
        "#      output:     X_{fileTAG}.BAM.\n" +
        "#                  X_{fileTAG}.BAM.BAI\n" +
        'include: "' + os.path.dirname(os.path.realpath(__file__)) + '/' + moduleNAME + '_INCLUDE"\n' +
        "#  Required: NONE\n" +
        "#  Call via:\n" +
        '#alignBAM_bwa      ~ expand("{outputDIR}/{processBamDIR}/{samples}_realigned.bam", outputDIR=config["outputDIR"], processBamDIR=config["processBamDIR"], samples=config["sample"])\n'+
        '#bam2fastq         ~ expand("{outputDIR}/{fastqDIR}/{samples}.{readDirection}.fastq.gz", outputDIR=config["outputDIR"], fastqDIR=config["fastqDIR"], samples=config["sample"], readDirection=["1", "2"])\n'+
        '#cleanBAM          ~ expand("{outputDIR}/{processBamDIR}/{samples}_clean.bam", outputDIR=config["outputDIR"], processBamDIR=config["processBamDIR"], samples=config["sample"])\n'+
        '#fastq2GZ          ~ expand("{outputDIR}/{fastqDIR}/{samples}.{readDirection}.fastq.gz", outputDIR=config["outputDIR"], fastqDIR=config["fastqDIR"], samples=config["sample"], readDirection=["1", "2"])\n'+
        '#fastqc            ~ expand("{outputDIR}/{fastqDIR}/{samples}_fastqc.zip", outputDIR=config["outputDIR"], fastqDIR=config["fastqDIR"], samples=config["sample"])\n'+
        '#filteredBAM       ~ expand("{outputDIR}/{processBamDIR}/{samples}_filtered.bam", outputDIR=config["outputDIR"], processBamDIR=config["processBamDIR"], samples=config["sample"])\n'+
        '#fixmateBAM        ~ expand("{outputDIR}/{processBamDIR}/{samples}_fixmate.bam", outputDIR=config["outputDIR"], processBamDIR=config["processBamDIR"], samples=config["sample"])\n'+
        '#indexBAM          ~ expand("{outputDIR}/{processBamDIR}/{samples}{fileTAG}.bam.bai", outputDIR=config["outputDIR"], processBamDIR=config["processBamDIR"], samples=config["sample"], fileTAG=config["fileTAG"])\n'+
        '#markdupBAM        ~ expand("{outputDIR}/{processBamDIR}/{samples}_markdup.bam", outputDIR=config["outputDIR"], processBamDIR=config["processBamDIR"], samples=config["sample"])\n'+
        '#namesortBAM       ~ expand("{outputDIR}/{processBamDIR}/{samples}_namesort.bam", outputDIR=config["outputDIR"], processBamDIR=config["processBamDIR"], samples=config["sample"])\n'+
        '#rmdupBAM          ~ expand("{outputDIR}/{processBamDIR}/{samples}_rmdup.bam", outputDIR=config["outputDIR"], processBamDIR=config["processBamDIR"], samples=config["sample"])\n'+
        '#sortBAM_biobambam ~ expand("{outputDIR}/{processBamDIR}/{samples}_sorted.bam", outputDIR=config["outputDIR"], processBamDIR=config["processBamDIR"], samples=config["sample"])\n'+
        '#sortBAM_samtools  ~ expand("{outputDIR}/{processBamDIR}/{samples}_sorted.bam", outputDIR=config["outputDIR"], processBamDIR=config["processBamDIR"], samples=config["sample"])\n'
    )
