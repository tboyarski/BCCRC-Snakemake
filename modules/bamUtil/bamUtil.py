#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Author:   Tim Boyarski
# Date:     2017-06-14
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Call: call("python " + snakeDIR + "/modules/bamUtil/bamUtil.py " + YAMLFILE + " " + CLUSTERFILE + " " + SNAKEFILE, shell=True)
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
moduleNAME="bamUtil"
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
    ruleLIST = ['mergeBAM',
        'cleanBAM',
        'filteredBAM',
        'fixmateBAM',
        'indexBAM',
        'markdupBAM',
        'namesortBAM_biobambam',
        'namesortBAM_samtools',
        'rmdupBAM',
        'sortBAM_biobambam',
        'sortBAM_samtools']
    # 1A. Create module directory
    mkdir("log/" + moduleNAME)
    print(moduleNAME + ".py \tCreating: log/" + moduleNAME)
    # 1B. Report on rules created.
    for rule in ruleLIST:
        mkdir("log/" + moduleNAME + "/" + rule)
        print(moduleNAME + ".py \tCreating: log/" + moduleNAME + "/" + rule + "/")
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 2 --- YAML File
# Open and append to file the following required paramters.
with open(argv[1], "a+") as yamlTARGET:
    # 2A. Software
    bamUtil_samtoolsProg="bamUtil_samtoolsProg: samtools\n"
    bamUtil_picardProg="bamUtil_picardProg: picard\n"
    bamUtil_bamsortProg="bamUtil_bamsortProg: bamsort\n"
    bamUtil_bammarkduplicates2Prog="bamUtil_bammarkduplicates2Prog: bammarkduplicates2\n"
    SoftwareChoiceFLAG_namesortBAM="SoftwareChoiceFLAG_namesortBAM: biobambam\n"
    SoftwareChoiceFLAG_sortBAM="SoftwareChoiceFLAG_sortBAM: biobambam\n"
    # 2B. Shared variables
    bamUtilDIR="bamUtilDIR: bamUtil\n"
    bamUtil_picardValStringency="bamUtil_picardValStringency: VALIDATION_STRINGENCY=LENIENT\n"
    bamUtil_picardMaxRec="bamUtil_picardMaxRec: MAX_RECORDS_IN_RAM=5000000\n"
    # 2C. mergeBAM variables
    bamMergeRootDIR='bamMergeRootDIR: input/rawBam\n'
    bamMergeSuffix='bamMergeSuffix: _Aligned.out_sorted_filtered\n'
    # 2C. cleanBAM variables
    # 2C. filteredBAM variables
    filterBitFlag="filterBitFlag: 512\n"
    # 2C. fixmateBAM variables
    # 2C. indexBAM variables
    fileTag="fileTag: _Aligned.out_sorted_filtered_markdup\n"
    # 2C. markdupBAM variables
    compressLevel="compressLevel: level=-1\n"
    # 2C. namesortBAM_biobambmam variables
    # 2C. namesortBAM_samtools variables
    bamUtil_samtoolsSortMem="bamUtil_samtoolsSortMem: 4000000000\n"
    # 2C. rmdupBAM variables
    # 2C. sortBAM_biobambam variables
    # 2C. sortBAM_samtools variables
    # 2D. Write to file
    yamlTARGET.write(
        "\n\n"
        "#####################################\n"
        "# " + moduleNAME + " Parameters\n"
        "#####################################\n"
        "#----------------------------------------------------------------- *Software* ------------------------------------------------------------------------\n" +
        bamUtil_samtoolsProg + bamUtil_picardProg  + bamUtil_bamsortProg + bamUtil_bammarkduplicates2Prog +
        SoftwareChoiceFLAG_namesortBAM + SoftwareChoiceFLAG_sortBAM +
        "#----------------------------------------------------------------- *Shared Variables* ----------------------------------------------------------------\n" +
        bamUtilDIR + bamUtil_picardValStringency + bamUtil_picardMaxRec +
        "#----------------------------------------------------------------- mergeBAM --------------------------------------------------------------------------\n" +
        bamMergeRootDIR + bamMergeSuffix +
        "#----------------------------------------------------------------- cleanBAM --------------------------------------------------------------------------\n" +
        "#----------------------------------------------------------------- filteredBAM -----------------------------------------------------------------------\n" +
        filterBitFlag +
        "#----------------------------------------------------------------- fixmateBAM ------------------------------------------------------------------------\n" +
        "#----------------------------------------------------------------- indexBAM --------------------------------------------------------------------------\n" +
        fileTag +
        "#----------------------------------------------------------------- markdupBAM ------------------------------------------------------------------------\n" +
        compressLevel +
        "#----------------------------------------------------------------- namesortBAM_biobambam -------------------------------------------------------------\n" +
        "#----------------------------------------------------------------- namesortBAM_samtools --------------------------------------------------------------\n" +
        bamUtil_samtoolsSortMem +
        "#----------------------------------------------------------------- rmdupBAM --------------------------------------------------------------------------\n" +
        "#----------------------------------------------------------------- sortBAM_biobambam -----------------------------------------------------------------\n" +
        "#----------------------------------------------------------------- sortBAM_samtools ------------------------------------------------------------------\n" +
        "#-----------------------------------------------------------------------------------------------------------------------------------------------------\n"
    )
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 3 --- JSON File
# Generate header for '.json' file.
# 3A. Read file to parse and store '.json' object.
with open(argv[2], "r+") as jsonTARGET:
    jsonOBJ = load(jsonTARGET)
    jsonOBJ['mergeBAM'] = {
            "clusterSpec": "-V -S /bin/bash -o log/bamUtil/mergeBAM -e log/bamUtil/mergeBAM -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleMB}"
    }
    jsonOBJ['cleanBAM'] = {
            "clusterSpec": "-V -S /bin/bash -o log/bamUtil/cleanBAM -e log/bamUtil/cleanBAM -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleCB}"
    }
    jsonOBJ['filteredBAM'] = {
            "clusterSpec": "-V -S /bin/bash -o log/bamUtil/filteredBAM -e log/bamUtil/filteredBAM -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleFB}"
    }
    jsonOBJ['fixmateBAM'] = {
            "clusterSpec": "-V -S /bin/bash -o log/bamUtil/fixmateBAM -e log/bamUtil/fixmateBAM -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleFMB}"
    }
    jsonOBJ['indexBAM'] = {
            "clusterSpec": "-V -S /bin/bash -o log/bamUtil/indexBAM -e log/bamUtil/indexBAM -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleIB}"
    }
    jsonOBJ['markdupBAM'] = {
            "clusterSpec": "-V -S /bin/bash -o log/bamUtil/markdupBAM -e log/bamUtil/markdupBAM -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleMDB}"
    }
    jsonOBJ['namesortBAM_biobambam'] = {
            "clusterSpec": "-V -S /bin/bash -o log/bamUtil/namesortBAM_biobambam -e log/bamUtil/namesortBAM_biobambam -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleNSBB}"
    }
    jsonOBJ['namesortBAM_samtools'] = {
            "clusterSpec": "-V -S /bin/bash -o log/bamUtil/namesortBAM_samtools -e log/bamUtil/namesortBAM_samtools -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleNSBS}"
    }
    jsonOBJ['rmdupBAM'] = {
            "clusterSpec": "-V -S /bin/bash -o log/bamUtil/rmdupBAM -e log/bamUtil/rmdupBAM -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleRDB}"
    }
    jsonOBJ['sortBAM_biobambam'] = {
            "clusterSpec": "-V -S /bin/bash -o log/bamUtil/sortBAM_biobambam -e log/bamUtil/sortBAM_biobambam -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleSBB}"
    }
    jsonOBJ['sortBAM_samtools'] = {
            "clusterSpec": "-V -S /bin/bash -o log/bamUtil/sortBAM_samtools -e log/bamUtil/sortBAM_samtools -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleSBS}"
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
        "#      mergeBAM:               Produce a single '.bam' file from a list of '.bam' files.\n"
        "#      cleanBAM:               Cleans the provided SAM/BAM, soft-clipping beyond-end-of-reference alignments and setting MAPQ to 0 for unmapped reads.\n"
        "#      filteredBAM:            Filtering of a '.bam' file on read quality.\n"
        "#      fixmateBAM:             Fill in mate coordinates, ISIZE, and mate related flags from a name-sorted alignment.\n"
        "#      indexBAM:               Indexing of a '.bam' file.\n"
        "#      markdupBAM:             Mark diplicates in a '.bam' file and produce metrics.\n"
        "#      namesortBAM:            Produce a name sorted '.bam' file.\n"
        "#      rmdupBAM:               Remove dupliates in a '.bam' file.\n"
        "#      sortBAM_biobambam:      Sorting of the '.bam' file, via BIOBAMBAM.\n"
        "#      sortBAM_samtools:       Sorting of the '.bam'  file, via SAMTOOLS.\n"
        'include: "' + path.dirname(path.realpath(__file__)) + '/' + moduleNAME + '_INCLUDE"\n'
        "#  Required: NONE\n"
        "#  Call via:\n"
        '#mergeBAM:                 expand("{bamMergeRootDIR}/{samples}.bam", bamMergeRootDIR=config["bamMergeRootDIR"], samples=config["sample"]),\n'
        '#cleanBAM:                 expand("{outputDIR}/{bamDIR}/{samples}_clean.bam", outputDIR=config["outputDIR"], bamDIR=config["bamDIR"], samples=config["sample"]),\n'
        '#filteredBAM:              expand("{outputDIR}/{bamDIR}/{samples}_filtered.bam", outputDIR=config["outputDIR"], bamDIR=config["bamDIR"], samples=config["sample"]),\n'
        '#fixmateBAM:               expand("{outputDIR}/{bamDIR}/{samples}_fixmate.bam", outputDIR=config["outputDIR"], bamDIR=config["bamDIR"], samples=config["sample"]),\n'
        '#indexBAM:                 expand("{outputDIR}/{bamDIR}/{samples}{fileTag}.bam.bai", outputDIR=config["outputDIR"], bamDIR=config["bamDIR"], samples=config["sample"], fileTag=config["fileTag"]),\n'
        '#markdupBAM:               expand("{outputDIR}/{bamDIR}/{samples}_markdup.bam", outputDIR=config["outputDIR"], bamDIR=config["bamDIR"], samples=config["sample"]),\n'
        '#namesortBAM_*:            expand("{outputDIR}/{bamDIR}/{samples}_namesort.bam", outputDIR=config["outputDIR"], bamDIR=config["bamDIR"], samples=config["sample"]),\n'
        '#rmdupBAM:                 expand("{outputDIR}/{bamDIR}/{samples}_rmdup.bam", outputDIR=config["outputDIR"], bamDIR=config["bamDIR"], samples=config["sample"]),\n'
        '#sortBAM_*:                expand("{outputDIR}/{bamDIR}/{samples}_sorted.bam", outputDIR=config["outputDIR"], bamDIR=config["bamDIR"], samples=config["sample"]),\n'
        "#-----------------------------------------------------------------------------------------------------------------------------------------------------\n"
    )
#-----------------------------------------------------------------------------------------------------------------------------------------------------
