#-------------------------------
#   Author: Tim Boyarski
#   Date:   2017-03-06
#-------------------------------

# buildHeader.py
#-------------------------------------------------------------------------------
# Purpose: This code builds the headers for the Snakemake, '.yaml' and '.json'
#   files.
#-------------------------------------------------------------------------------

import os
import json
import getpass
from time import gmtime, strftime

def buildHeader(yamlNAME, jsonNAME, snakeNAME):
    # 1 --- Generate header for '.yaml' file.
    with open(yamlNAME, "w+") as yamlTARGET:
        # 1A. Global Parameters
        fastqKEEP="fastqKEEP: False\n"
        refFILE="refFILE: GRCh37-lite.fa\n"
        chrLIST="chrLIST: ['chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8', 'chr9', 'chr10', 'chr11', 'chr12', 'chr13', 'chr14', 'chr15', 'chr16', 'chr17', 'chr18', 'chr19', 'chr20', 'chr21', 'chr22', 'chrM', 'chrX', 'chrY']\n"
        # 1B. Global Directories
        inputDIR="inputDIR: input\n"
        refDIR="refDIR: ref\n"
        outputDIR="outputDIR: output\n"
        bamDIR="bamDIR: bam\n"
        metricsDIR="metricsDIR: metrics\n"
        # 1C. Write to file
        yamlTARGET.write("#---------------------\n# Author: " + getpass.getuser() + "\n# Date: " + strftime("%Y-%m-%d.%H-%M-%S", gmtime()) + "\n#---------------------\n")
        yamlTARGET.write("\n\n#################################\n# ----- Global Variables ------ #\n#################################\n")
        yamlTARGET.write("#       -- Parameters --        #\n" + fastqKEEP + refFILE + chrLIST)
        yamlTARGET.write("#       -- Directory --         #\n" + inputDIR + refDIR + outputDIR + bamDIR + metricsDIR)

    # 2 --- Check if directories exist for logging, as the DRMAA caller cannot create directories.
    if (os.path.isdir("log")) != True:
        print("buildHeader.py \tCreating: log/")
        os.mkdir("log")

    # 3 --- Generate header for '.json' file.
    with open(jsonNAME, "w+") as jsonTARGET:
        jsonOBJ = {}
        jsonRULE = {}
        jsonRULE['clusterSpec'] = '-V -S /bin/bash -o log -e log -l h_vmem=10G -pe ncpus 1'
        jsonOBJ['__default__'] = jsonRULE
        json.dump(jsonOBJ, jsonTARGET, indent=4)

    # 4 --- Generate header for the Snakemake file.
    with open(snakeNAME, "w+") as snakeTARGET:
        snakeTARGET.write("#---------------------\n# Author: " + getpass.getuser() + "\n# Date: " + strftime("%Y-%m-%d.%H-%M-%S", gmtime()) + "\n#---------------------\n")
        snakeTARGET.write('# Call using: snakemake --jobs 10 --cluster-config input/config.json --drmaa "{cluster.clusterSpec}"\n')
        snakeTARGET.write("# Global config:\n")
        snakeTARGET.write('configfile: "' + yamlNAME + '"\n')
        snakeTARGET.write('\n# Global rule to pull all output files:\n')
        snakeTARGET.write('rule all:\n    input:\n        expand("{outputDIR}/{vcfDIR}/{samples}.varScan.snps.vcf", outputDIR=config["outputDIR"], vcfDIR=config["vcfDIR"], samples=config["sample"])\n\n')
#-------------------------------------------------------------------------------
