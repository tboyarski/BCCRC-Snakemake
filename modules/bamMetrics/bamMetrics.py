#---------------------------------------------------
# Author:   Tim Boyarski
# Date:     2017-03-06
#-----------------------------------------------------------
# Call: call("python " + snakeDIR + "/modules/bamMetrics/bamMetrics.py " + YAMLFILE + " " + CLUSTERFILE + " " + SNAKEFILE, shell=True)
# Input:                                    .BAM
# Output:                                   .metrics
# Purpose: Automate the population of user's pipeline
#   Snakefile, '.YAML', and '.JSON' files.
#-------------------------------------------------------------------

# Request sys so be able to use CLI arguments
import sys
import json
import os

moduleNAME = "bamMetrics"

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
    bamMetrics_samtoolsProg="bamMetrics_samtoolsProg: samtools\n"
    bamMetrics_picardProg="bamMetrics_picardProg: picard\n"
    bamMetrics_RScriptProg="bamMetrics_RScriptProg: ~/share/usr/R/3.1.2/bin/Rscript\n"
    # 2B. Shared variables
    bamMetricsDIR="bamMetricsDIR: bamMetrics\n"
    bamMetricsPicardValStringency="bamMetricsPicardValStringency: VALIDATION_STRINGENCY=LENIENT\n"
    bamMetricsPicardMexRec="bamMetricsPicardMexRec: MAX_RECORDS_IN_RAM=5000000\n"
    # 2.C.01 biasGC variables
    # 2.C.02 colectRNASeq variables
    RRNAIntervalList="RRNAIntervalList: ~/share/references/rRNA.ensg72.hg19.interval_list\n"
    RefFlat="RefFlat: ~/share/references/refseq.hg19.refFlat\n"
    StrandSpecificity="StrandSpecificity: NONE\n"
    # 2.C.03 collectWGS variables
    # 2.C.04 flagStats variables
    # 2.C.05 insertSize variables
    # 2.C.06 metricsALL variables
    # 2.C.07 metricsMERGE variables
    # 2.C.08 pairAlignSummary variables
    # 2.C.09 readLen variables
    # 2.C.10 timeStamp variables
    # 2. Write to file
    yamlTARGET.write("\n\n#################################\n# ----- " + moduleNAME \
            + " Parameters ------ #\n#################################\n")
    yamlTARGET.write("#       -- Software --          #\n" + bamMetrics_samtoolsProg \
            + bamMetrics_picardProg + bamMetrics_RScriptProg)
    yamlTARGET.write("#    -- Shared Variables --     #\n" + bamMetricsDIR \
            + bamMetricsPicardValStringency + bamMetricsPicardMexRec)
    yamlTARGET.write("#     -- biasGC Specific --    #\n")
    yamlTARGET.write("#     -- collectRNASeq Specific --    #\n" + RRNAIntervalList \
            + RefFlat + StrandSpecificity)
    yamlTARGET.write("#     -- collectWGS Specific --    #\n")
    yamlTARGET.write("#     -- flagStats Specific --    #\n")
    yamlTARGET.write("#     -- insertSize Specific --    #\n")
    yamlTARGET.write("#     -- metricsALL Specific --    #\n")
    yamlTARGET.write("#     -- metricsMERGE Specific --    #\n")
    yamlTARGET.write("#     -- pairAlignSummary Specific --    #\n")
    yamlTARGET.write("#     -- readLen Specific --    #\n")
    yamlTARGET.write("#     -- timeStamp Specific --    #\n")
    yamlTARGET.write("#################################\n")

# 3 --- JSON File
# Generate header for '.json' file.
jsonOBJ = {}
# Read file to parse and store '.json'  object.
with open(sys.argv[2], "r+") as jsonTARGET:
    jsonRULE = {}
    jsonOBJ = json.load(jsonTARGET)
    jsonRULE['clusterSpec'] = '-V -S /bin/bash -o log/' + moduleNAME + ' -e log/' + moduleNAME + ' -l h_vmem=10G -pe ncpus 1'
    jsonOBJ['collectGCBias'] = jsonRULE
    jsonOBJ['collectMultMetrics'] = jsonRULE
    jsonOBJ['collectRNASeq'] = jsonRULE
    jsonOBJ['collectWGS'] = jsonRULE
    jsonOBJ['flagStats'] = jsonRULE
    jsonOBJ['insertSize'] = jsonRULE
    jsonOBJ['pairAlignSummary'] = jsonRULE
    jsonOBJ['readLen'] = jsonRULE
# Recreate JSON file to delete exiting text.
with open(sys.argv[2], "w+") as jsonTARGET:
    json.dump(jsonOBJ, jsonTARGET, indent=4)

# 4 --- Snakefile
# Open and append o file a descriptin and the last rule call.
with open(sys.argv[3], "a+") as pipeTARGET:
    pipeTARGET.write(
        "\n\n#***** " + moduleNAME + " *****\n" +
        "#  Included:\n" +
        "#    " + moduleNAME + ":     Generated mpileup file from BAM file.\n" +
        "#  Files:\n" +
        "#    Input:      .BAM\n" +
        "#    Output:     .metrics\n" +
        'include: "' + os.path.dirname(os.getcwd()) + '/modules/' + moduleNAME + '/' + moduleNAME + '_INCLUDE"\n' +
        "#  Required: NONE\n" +
        "#  Call via: \n" +
        '#    expand("{outputDIR}/{metricsDIR}/{samples}.collectGCBiasi.txt", outputDIR=config["outputDIR"], metricsDIR=config["metricsDIR"], samples=config["sample"])\n'+
        '#    expand("{outputDIR}/{metricsDIR}/{samples}.collectMultMetrics.quality_distribution.pdf", outputDIR=config["outputDIR"], metricsDIR=config["metricsDIR"], samples=config["sample"])\n'+
        '#    expand("{outputDIR}/{metricsDIR}/{samples}.collectRNASeq.txt", outputDIR=config["outputDIR"], metricsDIR=config["metricsDIR"], samples=config["sample"])\n'+
        '#    expand("{outputDIR}/{metricsDIR}/{samples}.collectWGS.txt", outputDIR=config["outputDIR"], metricsDIR=config["metricsDIR"], samples=config["sample"])\n'+
        '#    expand("{outputDIR}/{metricsDIR}/{samples}.flatStats.txt", outputDIR=config["outputDIR"], metricsDIR=config["metricsDIR"], samples=config["sample"])\n'+
        '#    expand("{outputDIR}/{metricsDIR}/{samples}.insertSize.txt", outputDIR=config["outputDIR"], metricsDIR=config["metricsDIR"], samples=config["sample"])\n'+
        '#    expand("{outputDIR}/{metricsDIR}/{samples}.pairAlignSummary.txt", outputDIR=config["outputDIR"], metricsDIR=config["metricsDIR"], samples=config["sample"])\n'+
        '#    expand("{outputDIR}/{metricsDIR}/{samples}.readLen.txt", outputDIR=config["outputDIR"], metricsDIR=config["metricsDIR"], samples=config["sample"])\n'
    )
