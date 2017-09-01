#---------------------------------------------------
# Author:   Tim Boyarski
# Date:     2017-07-07
#-----------------------------------------------------------
# Call: call("python " + snakeDIR + "/modules/bamMetrics/bamMetrics.py " + YAMLFILE + " " + CLUSTERFILE + " " + SNAKEFILE, shell=True)

# Purpose: Automate the population of user's pipeline
#   Snakefile, '.YAML', and '.JSON' files.
#-------------------------------------------------------------------
# PYTHON PACKAGES #
#------------------
# Request sys so be able to use CLI arguments.
from sys import argv

# Request json to be able to load and write to the config.json file.
from json import load, dump

# Request os permissions to be able to create directories for the log files.
from os import path, mkdir

# Global variable used for reporting of the module name.
moduleNAME = "bamMetrics"
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
    print(moduleNAME + ".py \tCreating: log/")
    mkdir("log")
if (path.isdir("log/" + moduleNAME) != True):
    # Maintain this list of active submodules.
    ruleLIST = ['collectGCBias',
            'collectMultMetrics',
            'collectRNASeq',
            'collectRNASeqMERGE',
            'collectWGS',
            'collectWGSMERGE',
            'collectInsertSizeMerge',
            'collectAlignmentSummaryMERGE',
            'flagStats',
            'readLen']
    # 1A. Create module directory.
    mkdir("log/" + moduleNAME)
    print(moduleNAME + ".py \tCreating: log/" + moduleNAME)
    # 1B. Create submodule directories and report to user.
    for rule in ruleLIST:
        mkdir("log/" + moduleNAME + "/" + rule)
        print(moduleNAME + ".py \tCreating: log/" + moduleNAME + "/" + rule + "/")
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 2 --- YAML File
# Open and append to file the following required paramters.
with open(argv[1], "a+") as yamlTARGET:
    # 2A. Software
    bamMetrics_samtoolsProg="bamMetrics_samtoolsProg: samtools\n"
    bamMetrics_picardProg="bamMetrics_picardProg: java -Xmx4G -jar /extscratch/clc/usr/anaconda/4.3.0/envs/CentOS5-Compatible/share/picard-2.9.0-0/picard.jar\n"
    # 2B. Shared variables
    bamMetricsDIR="bamMetricsDIR: bamMetrics\n"
    bamMetricsPicardValStringency="bamMetricsPicardValStringency: VALIDATION_STRINGENCY=LENIENT\n"
    bamMetricsPicardMexRec="bamMetricsPicardMexRec: MAX_RECORDS_IN_RAM=5000000\n"
    # 2C. collectGCBias variables
    # 2C. collectMERGE_ADAPTOR variables
    # 2C. collectMultMetrics variables
    fileOutputSuffixLIST="fileOutputSuffixLIST: ['alignment_summary_metrics'," \
        " 'base_distribution_by_cycle_metrics', 'base_distribution_by_cycle.pdf'," \
        " 'insert_size_histogram.pdf','insert_size_metrics', 'quality_by_cycle_metrics'," \
        " 'quality_by_cycle.pdf','quality_distribution_metrics', 'quality_distribution.pdf']\n"
    # 2C. colectRNASeq variables
    #RRNAIntervalList="RRNAIntervalList: /extscratch/clc/references/rRNA.ensg72.hg19.interval_list\n"
    RRNAIntervalList="RRNAIntervalList: /extscratch/clc/references/dbsnp/dbsnp_137.b37.interval_list\n"
    RefFlat="RefFlat: /extscratch/clc/references/refseq.hg19.refFlat\n"
    StrandSpecificity="StrandSpecificity: NONE\n"
    # 2C. collectWGS variables
    # 2C. flagStats variables
    # 2C. insertSize variables
    # 2C. pairAlignSummary variables
    # 2C. readLen variables
    # 2. Write to file
    yamlTARGET.write(
        "\n\n"
        "#####################################\n"
        "# " + moduleNAME + " Parameters\n"
        "#####################################\n"
        "#----------------------------------------------------------------- *Software* ------------------------------------------------------------------------\n" +
        bamMetrics_samtoolsProg + bamMetrics_picardProg +
        "#----------------------------------------------------------------- *Shared Variables* ----------------------------------------------------------------\n" +
        bamMetricsDIR + bamMetricsPicardValStringency + bamMetricsPicardMexRec +
        "#----------------------------------------------------------------- collectGCBias ---------------------------------------------------------------------\n" +
        "#----------------------------------------------------------------- collectMERGE_ADAPTOR --------------------------------------------------------------\n" +
        "#----------------------------------------------------------------- collectMultMetrics ----------------------------------------------------------------\n" +
        fileOutputSuffixLIST +
        "#----------------------------------------------------------------- collectRNASeq ---------------------------------------------------------------------\n" +
        RRNAIntervalList + RefFlat + StrandSpecificity +
        "#----------------------------------------------------------------- collectWGS ------------------------------------------------------------------------\n" +
        "#----------------------------------------------------------------- flagStats -------------------------------------------------------------------------\n" +
        "#----------------------------------------------------------------- readLen ---------------------------------------------------------------------------\n" +
        "#-----------------------------------------------------------------------------------------------------------------------------------------------------\n"
    )
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 3 --- JSON File
# Generate header for '.json' file.
# Read file to parse and store '.json'  object.
with open(argv[2], "r+") as jsonTARGET:
    jsonOBJ = load(jsonTARGET)
    jsonOBJ['collectGCBias'] = {
            "clusterSpec": "-V -S /bin/bash -o log/bamMetrics/collectGCBias -e log/bamMetrics/collectGCBias -l h_vmem=15G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleCGCB}"
    }
    jsonOBJ['collectMultMetrics'] = {
            "clusterSpec": "-V -S /bin/bash -o log/bamMetrics/collectMultMetrics -e log/bamMetrics/collectMultMetrics -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleCMM}"
    }
    jsonOBJ['collectRNASeq'] = {
            "clusterSpec": "-V -S /bin/bash -o log/bamMetrics/collectRNASeq -e log/bamMetrics/collectRNASeq -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleCRNAS}"
    }
    jsonOBJ['collectRNASeqMERGE'] = {
            "clusterSpec": "-V -S /bin/bash -o log/bamMetrics/collectRNASeqMERGE -e log/bamMetrics/collectRNASeqMERGE -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_all.samples"
    }
    jsonOBJ['collectWGS'] = {
            "clusterSpec": "-V -S /bin/bash -o log/bamMetrics/collectWGS -e log/bamMetrics/collectWGS -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleCWGS}"
    }
    jsonOBJ['collectWGSMERGE'] = {
            "clusterSpec": "-V -S /bin/bash -o log/bamMetrics/collectWGSMERGE -e log/bamMetrics/collectWGSMERGE -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_all.samples"
    }
    jsonOBJ['collectInsertSizeMERGE'] = {
            "clusterSpec": "-V -S /bin/bash -o log/bamMetrics/collectInsertSizeMERGE -e log/bamMetrics/collectInsertSizeMERGE -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_all.samples"
    }
    jsonOBJ['collectAlignmentSummaryMERGE'] = {
            "clusterSpec": "-V -S /bin/bash -o log/bamMetrics/collectAlignmentSummaryMERGE -e log/bamMetrics/collectAlignmentSummaryMERGE -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_all.samples"
    }
    jsonOBJ['flagStats'] = {
            "clusterSpec": "-V -S /bin/bash -o log/bamMetrics/flagStats -e log/bamMetrics/flagStats -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleFS}"
    }
    jsonOBJ['readLen'] = {
            "clusterSpec": "-V -S /bin/bash -o log/bamMetrics/readLen -e log/bamMetrics/readLen -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleRL}"
    }
# Recreate JSON file to delete exiting text.
with open(argv[2], "w+") as jsonTARGET:
    dump(jsonOBJ, jsonTARGET, indent=4)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 4 --- Snakefile
# Open and append o file a descriptin and the last rule call.
with open(argv[3], "a+") as pipeTARGET:
    pipeTARGET.write(
        "\n\n#-----------------------------------------------------------------------------------------------------------------------------------------------------\n"
        "#***** " + moduleNAME + " *****\n"
        "#  Included:\n"
        "#    " + moduleNAME + ":     Generated mpileup file from BAM file.\n"
        "#  Files:\n"
        "#    Input:      .BAM\n"
        "#    Output:     .metrics\n"
        'include: "' + path.dirname(path.realpath(__file__)) + '/' + moduleNAME + '_INCLUDE"\n'
        "#  Required: NONE\n"
        "#  Call via: \n"
        '#GCBias:           expand("{outputDIR}/{metricsDIR}/{samples}.collectGCBias.txt", outputDIR=config["outputDIR"], metricsDIR=config["metricsDIR"], samples=config["sample"]),\n'
        '#MultM (PDF):      expand("{outputDIR}/{metricsDIR}/{samples}.collectMultMetrics.quality_distribution.pdf", outputDIR=config["outputDIR"], metricsDIR=config["metricsDIR"], samples=config["sample"]),\n'
        '#MultM (IS):       expand("{outputDIR}/{metricsDIR}/{samples}.collectMultMetrics.insert_size_metrics", outputDIR=config["outputDIR"], metricsDIR=config["metricsDIR"], samples=config["sample"]),\n'
        '#mergeInsertSize:  expand("{outputDIR}/{metricsDIR}/all.insert_size_metrics", outputDIR=config["outputDIR"], metricsDIR=config["metricsDIR"]),\n'
        '#MultM:            expand("{outputDIR}/{metricsDIR}/{samples}.collectMultMetrics.alignment_summary_metrics", outputDIR=config["outputDIR"], metricsDIR=config["metricsDIR"], samples=config["sample"]),\n'
        '#mergeAlignSumm:   expand("{outputDIR}/{metricsDIR}/all.alignment_summary_metrics", outputDIR=config["outputDIR"], metricsDIR=config["metricsDIR"]),\n'
        '#RNASeq:           expand("{outputDIR}/{metricsDIR}/{samples}.collectRNASeq.txt", outputDIR=config["outputDIR"], metricsDIR=config["metricsDIR"], samples=config["sample"]),\n'
        '#mergeRNASeq:     expand("{outputDIR}/{metricsDIR}/all.rnaseq_metrics", outputDIR=config["outputDIR"], metricsDIR=config["metricsDIR"], samples=config["sample"]),\n'
        '#WGS:              expand("{outputDIR}/{metricsDIR}/{samples}.collectWGS.txt", outputDIR=config["outputDIR"], metricsDIR=config["metricsDIR"], samples=config["sample"]),\n'
        '#mergeWGS:        expand("{outputDIR}/{metricsDIR}/all.wgs_metrics", outputDIR=config["outputDIR"], metricsDIR=config["metricsDIR"], samples=config["sample"]),\n'
        '#readLen:          expand("{outputDIR}/{metricsDIR}/{samples}.readLen", outputDIR=config["outputDIR"], metricsDIR=config["metricsDIR"], samples=config["sample"]),\n'
        '#flagStats:        expand("{outputDIR}/{metricsDIR}/{samples}.flagStats", outputDIR=config["outputDIR"], metricsDIR=config["metricsDIR"], samples=config["sample"]),\n'
        '#-----------------------------------------------------------------------------------------------------------------------------------------------------\n'
    )
#-----------------------------------------------------------------------------------------------------------------------------------------------------

