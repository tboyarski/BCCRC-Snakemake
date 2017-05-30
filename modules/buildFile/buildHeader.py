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
from time import localtime, strftime

def buildHeader(chrTYPE, yamlNAME, jsonNAME, snakeNAME):
    # 1 --- Generate header for '.yaml' file.
    with open(yamlNAME, "w+") as yamlTARGET:
        # 1A. Global Parameters
        shellCallFile="shellCallFile: shellCalls.txt\n"
        offCluster="offCluster: False\n"
        fastqKEEP="fastqKEEP: True\n"
        intermediateKEEP="intermediateKEEP: False\n"
        refFILE="refFILE: GRCh37-lite.fa\n"
        if chrTYPE == 'hucs':
            chrLIST="chrLIST: ['chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8', 'chr9', 'chr10', 'chr11', 'chr12', 'chr13', 'chr14', 'chr15', 'chr16', 'chr17', 'chr18', 'chr19', 'chr20', 'chr21', 'chr22', 'chrM', 'chrX', 'chrY']\n"
        elif chrTYPE == 'hncbi':
            #chrLIST="chrLIST: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', 'MT', 'X', 'Y']\n"
            chrLIST="chrLIST: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', 'X', 'Y', 'MT', 'GL000207.1', 'GL000226.1', 'GL000229.1', 'GL000231.1', 'GL000210.1', 'GL000239.1', 'GL000235.1', 'GL000201.1', 'GL000247.1', 'GL000245.1', 'GL000197.1', 'GL000203.1', 'GL000246.1', 'GL000249.1', 'GL000196.1', 'GL000248.1', 'GL000244.1', 'GL000238.1', 'GL000202.1', 'GL000234.1', 'GL000232.1', 'GL000206.1', 'GL000240.1', 'GL000236.1', 'GL000241.1', 'GL000243.1', 'GL000242.1', 'GL000230.1', 'GL000237.1', 'GL000233.1', 'GL000204.1', 'GL000198.1', 'GL000208.1', 'GL000191.1', 'GL000227.1', 'GL000228.1', 'GL000214.1', 'GL000221.1', 'GL000209.1', 'GL000218.1', 'GL000220.1', 'GL000213.1', 'GL000211.1', 'GL000199.1', 'GL00217.1', 'GL000216.1', 'GL000215.1', 'GL000205.1', 'GL000219.1', 'GL000224.1', 'GL000223.1', 'GL000195.1', 'GL000212.1', 'GL000222.1', 'GL000200.1', 'GL000193.1', 'GL000194.1', 'GL000225.1', 'GL000192.1']\n"
        elif chrTYPE == 'mucs':
            chrLIST="chrLIST: ['chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8', 'chr9', 'chr10', 'chr11', 'chr12', 'chr13', 'chr14', 'chr15', 'chr16', 'chr17', 'chr18', 'chr19', 'chrM', 'chrX', 'chrY']\n"
        elif chrTYPE == 'mncbi':
            chrLIST="chrLIST: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', 'MT', 'X', 'Y']\n"
        # 1B. Global Directories
        inputDIR="inputDIR: input\n"
        refDIR="refDIR: ref\n"
        outputDIR="outputDIR: output\n"
        bamDIR="bamDIR: bam\n"
        metricsDIR="metricsDIR: metrics\n"
        # 1C. Write to file
        yamlTARGET.write("#---------------------\n# Author: " + getpass.getuser() + "\n# Date: " + strftime("%Y-%m-%d.%H-%M-%S", localtime()) + "\n#---------------------\n")
        yamlTARGET.write("\n\n#################################\n# ----- Global Variables ------ #\n#################################\n")
        yamlTARGET.write("#       -- Parameters --        #\n" + shellCallFile + offCluster + fastqKEEP + intermediateKEEP + refFILE + chrLIST)
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
        snakeTARGET.write("#---------------------\n# Author: " + getpass.getuser() + "\n# Date: " + strftime("%Y-%m-%d.%H-%M-%S", localtime()) + "\n#---------------------\n")
        snakeTARGET.write('# Call using: snakemake --jobs 10 --cluster-config input/config.json --drmaa "{cluster.clusterSpec}"\n')
        snakeTARGET.write('\n\nimport io\nimport pandas\n\n')
        snakeTARGET.write("# Global config:\n")
        snakeTARGET.write('configfile: "' + yamlNAME + '"\n')
        snakeTARGET.write('\n# Global rule to pull all output files:\n')
        snakeTARGET.write('rule all:\n    input:\n')
        snakeTARGET.write('        # Pair: Tumor-Normal Runs\n')
        snakeTARGET.write('        #expand("{outputDIR}/{annotateVcfDIR}/{sample[1][tumor]}_{sample[1][normal]}.varScan.{form[1][varType]}{form[1][annotated]}.vcf", outputDIR=config["outputDIR"], annotateVcfDIR=config["annotateVcfDIR"], sample=pandas.read_table(config["sampleFILE"], " ").iterrows(), form=pandas.read_table(io.StringIO(config["sampleFORM"]), " ").iterrows())\n')
        snakeTARGET.write('        #expand("{outputDIR}/{utilsDIR}/{sample[1][tumor]}_{sample[1][normal]}.varScan.{form[1][varType]}{form[1][annotated]}.txt", outputDIR=config["outputDIR"], utilsDIR=config["utilsDIR"], sample=pandas.read_table(config["sampleFILE"], " ").iterrows(), form=pandas.read_table(io.StringIO(config["sampleFORM"]), " ").iterrows())\n')
        snakeTARGET.write('        #expand("{outputDIR}/{utilsDIR}/all.samples.varScan.{form[1][varType]}{form[1][annotated]}.txt", outputDIR=config["outputDIR"], utilsDIR=config["utilsDIR"], form=pandas.read_table(io.StringIO(config["sampleFORM"]), " ").iterrows())\n')
        snakeTARGET.write('        # Single: Normal Runs\n')
        snakeTARGET.write('        #expand("{outputDIR}/{annotateVcfDIR}/{samples}.varScan.{form[1][varType]}{form[1][annotated]}.vcf", outputDIR=config["outputDIR"], annotateVcfDIR=config["annotateVcfDIR"], samples=config["sample"], form=pandas.read_table(io.StringIO(config["sampleFORM"]), " ").iterrows())\n')
        snakeTARGET.write('        expand("{outputDIR}/{utilsDIR}/{samples}.varScan.{form[1][varType]}{form[1][annotated]}.txt", outputDIR=config["outputDIR"], utilsDIR=config["utilsDIR"], samples=config["sample"], form=pandas.read_table(io.StringIO(config["sampleFORM"]), " ").iterrows())\n')
        snakeTARGET.write('        #expand("{outputDIR}/{utilsDIR}/all.samples.varScan.{form[1][varType]}{form[1][annotated]}.txt", outputDIR=config["outputDIR"], utilsDIR=config["utilsDIR"], samples=config["sample"], form=pandas.read_table(io.StringIO(config["sampleFORM"]), " ").iterrows())\n')
#-------------------------------------------------------------------------------
