#-------------------------------------------------------------------
# Author:   Tim Boyarski                                            
# Date:     2017-03-06                                              
#-------------------------------------------------------------------
# Call: call("python " + snakeDIR + "/modules/varScan/varScan.py " + YAMLFILE + " " + CLUSTERFILE + " " + SNAKEFILE, shell=True)
# Input:                                    .mpileup                
# Output:                                   .varScan.snps.vcf       
# Purpose: Generate VCF output from a MPileup file.                 
#-------------------------------------------------------------------

# Request sys so be able to use CLI arguments
import sys
import json
import os

moduleNAME = "varScan"

# 0 --- Validate number of user arguments.
if len(sys.argv) !=4:
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
    os.mkdir("log/" + moduleNAME + 'Split')
    print(moduleNAME + ".py \tCreating: log/" + moduleNAME + 'Split')


# 2 --- YAML File
# Open and append to file the following required paramters.
with open(sys.argv[1], "a+") as yamlTARGET:
    # 2A. Software
    mpileup2_varScanProg = "mpileup2_varScanProg: varscan\n"
    somTumorNormal_varScanProg = "somTumorNormal_varScanProg: varscan\n"
    # 2B. Shared variables
    varScanSplitDIR="varScanSplitDIR: varScanSplit\n"
    varScanDIR="varScanDIR: varScan\n"
    varScanChrSplit="varScanChrSplit: True\n"
    varType="varType: ['snp', 'indel']\n"
    minCOV = "minCOV: --min-coverage 20\n"
    minREAD = "minREAD: --min-reads2 10\n"
    minQUAL = "minQUAL: --min-avg-qual 20\n"
    minFREQ = "minFREQ: --min-var-freq 0.01\n"
    pVALUE = "pVALUE: --p-value 0.05\n"
    strandFILT = "strandFILT: --strand-filter 0\n"
    outVCF = "outVCF: --output-vcf 1\n"
    minSTRAND = "minSTRAND: --min-strands2 0\n"
    posVALID = "posVALID: --validation 1\n"
    # 2C. mpileup2SPLIT only variables
    # 2D. mpileup2UNSPLIT only variables
    # 2E. mpileup2MERGE only variables
    # 2F. somTumorNormalUNSPLIT
    # 2G. somTumorNormalSPLIT
    # 2H. somTumorNormalMERGE
    # 2I. Write to file.
    yamlTARGET.write("\n\n\n#################################\n# ---- " + moduleNAME + " Parameters ----- #\n#################################\n")
    yamlTARGET.write("#       -- Software --          #\n" + mpileup2_varScanProg + somTumorNormal_varScanProg)
    yamlTARGET.write("#    -- Shared Variables --     #\n" + varScanSplitDIR + varScanDIR + varScanChrSplit + varType + minCOV + minREAD + minQUAL + minFREQ + pVALUE + strandFILT + outVCF + minSTRAND + posVALID)
    yamlTARGET.write("#   - mpileup2SPLIT Specific -  #\n")
    yamlTARGET.write("#  - mpileup2UNSPLIT Specific - #\n")
    yamlTARGET.write("#   - mpileup2MERGE Specific -  #\n")
    yamlTARGET.write("#   somTumorNormalSPLIT Spec.   #\n")
    yamlTARGET.write("#  somTumorNormalUNSPLIT Spec.  #\n")
    yamlTARGET.write("#   somTumorNormalMERGE Spec.   #\n")
    yamlTARGET.write("#################################\n")


# 3 --- JSON File
# Generate header for '.json' file.
jsonOBJ = {}
# Read file to parse and store '.json'  object.
with open(sys.argv[2], "r+") as jsonTARGET:
    jsonRULE = {}
    jsonOBJ = json.load(jsonTARGET)
    jsonRULE['clusterSpec'] = '-V -S /bin/bash -o log/' + moduleNAME + ' -e log/' + moduleNAME + ' -l h_vmem=10G -pe ncpus 1'
    jsonOBJ['mpileup2snp'] = jsonRULE
    jsonOBJ['mpileup2indel'] = jsonRULE
    jsonOBJ['somTumorNormalUNSPLIT'] = jsonRULE
    jsonOBJ['somTumorNormalSPLIT'] = jsonRULE
    jsonOBJ['somTumorNormalMERGE'] = jsonRULE
# Recreate JSON file to delete exiting text.
with open(sys.argv[2], "w+") as jsonTARGET:
    json.dump(jsonOBJ, jsonTARGET, indent=4)

# 4 --- Snakefile
# Open and append o file a descriptin and the last rule call.
with open(sys.argv[3], "a+") as pipeTARGET:
    pipeTARGET.write(
        "\n\n#***** " + moduleNAME + " *****\n" +
        "#  Included:\n" +
        "#    mpileup2snp:    Generate VCF output of SNPs from a mPileUp file.\n" + 
        "#    mpileup2indel:    Generate VCF output of INDELs from a mPileUp file.\n" + 
        "#    somTumorNormalUNSPLIT:    Generate VCF output for tumor-normal pairs.\n" + 
        "#    somTumorNormalSPLIT:    Genereate VCF output for tumor-normal pairs, process chromosomes in parallel.\n" + 
        "#    somTumorNormalMERGE:    Combine single chromosome VCF tumor-normal pairs output into single file.\n" + 
        "#  Files:\n" +
        "#    input:      X.mpileup\n" +
        "#    output:     X.varScan.snps.vcf\n" +
        "#                X.varScan.indels.vcf\n" +
        'include: "/home/tboyarski/share/projects/tboyarski/gitRepo-LCR-BCCRC/Snakemake/modules/' + moduleNAME + '/' + moduleNAME + '_INCLUDE"\n' +
        "#  Required:\n" +
        "#    >mPile:      Generate a MPileUp file from a BAM file.\n" +
        '#    @include: "/home/tboyarski/share/projects/tboyarski/gitRepo-LCR-BCCRC/Snakemake/modules/mPile/mPile_INCLUDE"\n' +
        "#  Call via:\n" +
        '# expand("{outputDIR}/{vcfDIR}/{samples}.varScan.{varType}.vcf", outputDIR=config["outputDIR"], vcfDIR=config["vcfDIR"], samples=config["sample"], varType=config["varType"])      #mpileup2\n' +
        '# expand("{outputDIR}/{vcfDIR}/{index[1][tumor]}_{index[1][normal]}.varScan.{varType}.txt", outputDIR=config["outputDIR"], vcfDIR=config["vcfDIR"], index=pandas.read_table(config["sampleFILE"], " ").iterrows(), varType=config["varType"])  #somTumorNormal\n'
        )
