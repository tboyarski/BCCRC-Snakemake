#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Author:   Tim Boyarski
# Date:     2017-05-24
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Call: call("python " + snakeDIR + "/modules/varScan/varScan.py " + YAMLFILE + " " + CLUSTERFILE + " " + SNAKEFILE, shell=True)
# Purpose: Generate VCF output from a MPileup file.
#-----------------------------------------------------------------------------------------------------------------------------------------------------

import sys
import json
import os

moduleNAME = "varScan"

# 0 --- Validate number of user arguments.
if len(sys.argv) !=4:
    print("Please provide arguments as follows:")
    print("python " + moduleNAME + ".py yaml json snake")
    print("\t-yaml = 'path/name' of the yaml file to write the pipeline parameters")
    print("\t-snake = 'path/name' of snakefile we are building")
    print("\t-json = 'path/name' of the json file we write the cluster config to")
    quit()


# 1 --- Log Files
# Check if directories exist for logging, as the DRMAA caller cannot create directories.
if (os.path.isdir("log")) != True:
    os.mkdir("log")
    print(moduleNAME + ".py \tCreating: log/")
if (os.path.isdir("log/" + moduleNAME) != True):
    # Maintain this list of active submodules.
    moduleLIST1 = ['mpileup2cns_SingleUNSPLIT','mpileup2copycall_PairUNSPLIT','mpileup2copynum_PairUNSPLIT',
            'mpileup2vcf_PairUNSPLIT','mpileup2vcf_SingleUNSPLIT']
    moduleLIST2 = ['Split/mpileup2vcf_PairSPLIT','Split/mpileup2vcf_SingleSPLIT']
    # 1A. Create module directories
    os.mkdir("log/" + moduleNAME)
    print(moduleNAME + ".py \tCreating: log/" + moduleNAME)
    os.mkdir("log/" + moduleNAME + 'Split')
    print(moduleNAME + ".py \tCreating: log/" + moduleNAME + 'Split')
    # 1B. Report on directories created.
    for module in moduleLIST1:
        os.mkdir("log/" + moduleNAME + "/" + module)
        print(moduleNAME + ".py \tCreating: log/" + moduleNAME + "/" + module + "/")
    for module in moduleLIST2:
        os.mkdir("log/" + moduleNAME + module)
        print(moduleNAME + ".py \tCreating: log/" + moduleNAME + module + "/")


# 2 --- YAML File
# Open and append to file the following required paramters.
with open(sys.argv[1], "a+") as yamlTARGET:
    # 2A. Software
    varScan_varScanProg = "varScan_varScanProg: varscan\n"
    varScan_samtoolsProg="varScan_samtoolsProg: samtools\n"
    # 2B. Shared variables
    vcfProgram="vcfProgram: varScan\n"
    varType="varType: ['snp', 'indel']\n"
    varScanSplitDIR="varScanSplitDIR: varScanSplit\n"
    varScanDIR="varScanDIR: varScan\n"
    varScanChrSplit="varScanChrSplit: True\n"
    minCOV = "minCOV: --min-coverage 20\n"
    minREAD = "minREAD: --min-reads2 10\n"
    minQUAL = "minQUAL: --min-avg-qual 20\n"
    minFREQ = "minFREQ: --min-var-freq 0.01\n"
    pVALUE = "pVALUE: --p-value 0.05\n"
    strandFILT = "strandFILT: --strand-filter 0\n"
    outVCF = "outVCF: --output-vcf 1\n"
    minSTRAND = "minSTRAND: --min-strands2 0\n"
    posVALID = "posVALID: --validation 1\n"
    # 2C. mpileup2cns_SingleUNSPLIT variables
    # 2C. mpileup2copycall_PairUNSPLIT variables
    # 2C. mpileup2copynum_PairUNSPLIT variables
    mapQSkip="mapQSkip: -q 1\n"
    # 2C. mpileup2vcf_PairUNSPLIT variables
    # 2C. mpileup2vcf_SingleUNSPLIT variables
    # 2C. mpileup2vcf_PairSPLIT variables
    # 2C. mpileup2vcf_SingleSPLIT variables
    # 2D. Write to file.
    yamlTARGET.write("\n\n\n#################################\n# ---- " + moduleNAME + " Parameters ----- #\n#################################\n")
    yamlTARGET.write("#       -- Software --          #\n" + varScan_varScanProg + varScan_samtoolsProg)
    yamlTARGET.write("#    -- Shared Variables --     #\n" + vcfProgram + varType + varScanSplitDIR + varScanDIR + varScanChrSplit \
            + minCOV + minREAD + minQUAL + minFREQ + pVALUE + strandFILT + outVCF + minSTRAND + posVALID)
    yamlTARGET.write("#   mpileup2cns_SingleUNSPLIT   #\n")
    yamlTARGET.write("# mpileup2copycall_PairUNSPLIT  #\n")
    yamlTARGET.write("#  mpileup2copynum_PairUNSPLIT  #\n" + mapQSkip)
    yamlTARGET.write("#    mpileup2vcf_PairUNSPLIT    #\n")
    yamlTARGET.write("#   mpileup2vcf_SingleUNSPLIT   #\n")
    yamlTARGET.write("#     mpileup2vcf_PairSPLIT     #\n")
    yamlTARGET.write("#    mpileup2vcf_SingleSPLIT    #\n")
    yamlTARGET.write("#################################\n")


# 3 --- JSON File
# Build the JSON file.
# 3A. Read file to parse and store '.json'  object.
with open(sys.argv[2], "r+") as jsonTARGET:
    jsonOBJ = json.load(jsonTARGET)
    jsonOBJ['mpileup2cns_SingleUNSPLIT'] = {
            "clusterSpec": "-V -S /bin/bash -o log/varScan/mpileup2cns_SingleUNSPLIT -e log/varScan/mpileup2cns_SingleUNSPLIT -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleMPU2CNS}"
    }
    jsonOBJ['mpileup2copycall_PairUNSPLIT'] = {
            "clusterSpec": "-V -S /bin/bash -o log/varScan/mpileup2copycall_PairUNSPLIT -e log/varScan/mpileup2copycall_PairUNSPLIT -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampletMPU2CC}_{wildcards.samplenMPU2CC}"
    }
    jsonOBJ['mpileup2copynum_PairUNSPLIT'] = {
            "clusterSpec": "-V -S /bin/bash -o log/varScan/mpileup2copynum_PairUNSPLIT -e log/varScan/mpileup2copynum_PairUNSPLIT -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampletMPU2CN}_{wildcards.samplenMPU2CN}"
    }
    jsonOBJ['mpileup2vcf_PairSPLIT'] = {
            "clusterSpec": "-V -S /bin/bash -o log/varScan/mpileup2vcf_PairSPLIT -e log/varScan/mpileup2vcf_PairSPLIT -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampletMPU2VCFPS}_{wildcards.samplenMPU2VCFPS}_chr{wildcards.chrMPU2}.SNPandINDEL"
    }
    jsonOBJ['mpileup2vcf_PairUNSPLIT'] = {
            "clusterSpec": "-V -S /bin/bash -o log/varScan/mpileup2vcf_PairUNSPLIT -e log/varScan/mpileup2vcf_PairUNSPLIT -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampletMPU2VCFPU}_{wildcards.samplenMPU2VCFPU}.SNPandINDEL"
    }
    jsonOBJ['mpileup2vcf_SingleSPLIT'] = {
            "clusterSpec": "-V -S /bin/bash -o log/varScan/mpileup2vcf_SingleSPLIT -e log/varScan/mpileup2vcf_SingleSPLIT -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleMPU2VCFSS}_chr{wildcards.chrMPU2VCFSS}_{wildcards.varTypeMPU2VCFSS}"
    }
    jsonOBJ['mpileup2vcf_SingleUNSPLIT'] = {
            "clusterSpec": "-V -S /bin/bash -o log/varScan/mpileup2vcf_SingleUNSPLIT -e log/varScan/mpileup2vcf_SingleUNSPLIT -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleMPU2VCFSU}_{wildcards.varTypeMPU2VCFSU}"
    }
# 3B. Recreate JSON file to delete exiting text.
with open(sys.argv[2], "w+") as jsonTARGET:
    json.dump(jsonOBJ, jsonTARGET, indent=4)


# 4 --- Snakefile
# Open and append o file a descriptin and the last rule call.
with open(sys.argv[3], "a+") as pipeTARGET:
    pipeTARGET.write(
        "\n\n#***** " + moduleNAME + " *****\n" +
        "#  Included:\n" +
        "#    mpileup2cns_SingleUNSPLIT:    Generate concensus calls from a '.mpileup' file.\n" +
        "#    mpileup2copycall_PairUNSPLIT: Infer somatic copy number changes using data from matched tumor-normal pairs.\n" +
        "#    mpileup2copynum_PairUNSPLIT:  Call variants and identify their somatic status.\n" +
        "#    mpileup2vcf_PairSPLIT:        Generate '.VCF' output of SNPs from a chromosomal tumor-normal '.mpileup' file.\n" +
        "#    mpileup2vcf_PairUNSPLIT:      Generate '.VCF' output of SNPs from a genomic tumor-normal '.mpileup' file.\n" +
        "#    mpileup2vcf_SingleSPLIT:      Generate '.VCF' output of SNPs from a chromosomeal sample '.mpileup' file.\n" +
        "#    mpileup2vcf_SingleUNSPLIT:    Generate '.VCF' output of SNPs from a genomic sample '.mpileup' file.\n" +
        "#  Files:\n" +
        "#    input:      X.mpileup\n" +
        "#    output:     X.varScan.snps.vcf\n" +
        "#                X.varScan.indels.vcf\n" +
        'include: "' + os.path.dirname(os.path.realpath(__file__)) + '/' + moduleNAME + '_INCLUDE"\n' +
        "#  Required:\n" +
        "#    >mpileup:      Generate a '.mpileup' file from a '.BAM' file.\n" +
        '#    @include: "' + os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + '/mileup/mileup_INCLUDE"\n' +
        "#  Call Pair (Tumor-Normal) Runs Via:\n" +
        '#VcfSplit   ~ expand("{outputDIR}/{varScanSplitDIR}/{sample[1][tumor]}_{sample[1][normal]}_{chrLIST}.varScan.{varType}.vcf", outputDIR=config["outputDIR"], varScanSplitDIR=config["varScanSplitDIR"], sample=pandas.read_table(config["sampleFILE"], " ").iterrows(), chrLIST=config["chrLIST"], varType=config["varType"])\n' +
        '#VcfUnsplit ~ expand("{outputDIR}/{varScanDIR}/{sample[1][tumor]}_{sample[1][normal]}.varScan.{varType}.vcf", outputDIR=config["outputDIR"], varScanDIR=config["varScanDIR"], sample=pandas.read_table(config["sampleFILE"], " ").iterrows(), varType=config["varType"])\n' +
        "#  Annotated Pair Runs (Requiring modules/utils) Via:\n" +
        '#VCFs ~ expand("{outputDIR}/{varScanDIR}/{sample[1][tumor]}_{sample[1][normal]}.varScan.{form[1][varType]}{form[1][annotated]}.vcf", outputDIR=config["outputDIR"],varScanDIR=config["varScanDIR"], sample=pandas.read_table(config["sampleFILE"], " ").iterrows(), form=pandas.read_table(io.StringIO(config["sampleFORM"]), " ").iterrows())\n' +
        '#TXTs ~ expand("{outputDIR}/{varTablesDIR}/{sample[1][tumor]}_{sample[1][normal]}.varScan.{form[1][varType]}{form[1][annotated]}.txt", outputDIR=config["outputDIR"], varTablesDIR=config["varTablesDIR"], sample=pandas.read_table(config["sampleFILE"], " ").iterrows(), form=pandas.read_table(io.StringIO(config["sampleFORM"]), " ").iterrows())\n'
        '#ALLs ~ expand("{outputDIR}/{varTablesDIR}/all.samples.varScan.{form[1][varType]}{form[1][annotated]}.txt", outputDIR=config["outputDIR"], varTablesDIR=config["varTablesDIR"], form=pandas.read_table(io.StringIO(config["sampleFORM"]), " ").iterrows())\n'
        "#  Call Single Runs Via:\n" +
        '#VcfSplit ~ expand("{outputDIR}/{varScanSplitDIR}/{samples}_{chrLIST}.varScan.{varType}.vcf", outputDIR=config["outputDIR"], varScanSplitDIR=config["varScanSplitDIR"], samples=config["sample"], chrLIST=config["chrLIST"], varType=config["varType"])\n' +
        '#VcfUnsplit   ~ expand("{outputDIR}/{varScanDIR}/{samples}.varScan.{varType}.vcf", outputDIR=config["outputDIR"], varScanDIR=config["varScanDIR"], samples=config["sample"], varType=config["varType"])\n' +
        "#  Annotated Single Runs (Requiring modules/utils) Via:\n" +
        '#VCFs ~ expand("{outputDIR}/{varScanDIR}/{samples}.varScan.{form[1][varType]}{form[1][annotated]}.vcf", outputDIR=config["outputDIR"], varScanDIR=config["varScanDIR"], samples=config["sample"], form=pandas.read_table(io.StringIO(config["sampleFORM"]), " ").iterrows())\n'
        '#TXTs ~ expand("{outputDIR}/{varTablesDIR}/{samples}.varScan.{form[1][varType]}{form[1][annotated]}.txt", outputDIR=config["outputDIR"], varTablesDIR=config["varTablesDIR"], samples=config["sample"], form=pandas.read_table(io.StringIO(config["sampleFORM"]), " ").iterrows())\n'
        '#ALLs ~ expand("{outputDIR}/{varTablesDIR}/all.samples.varScan.{form[1][varType]}{form[1][annotated]}.txt", outputDIR=config["outputDIR"], varTablesDIR=config["varTablesDIR"], samples=config["sample"], form=pandas.read_table(io.StringIO(config["sampleFORM"]), " ").iterrows())\n'
        )
#-----------------------------------------------------------------------------------------------------------------------------------------------------
