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


# 2 --- YAML File
# Open and append to file the following required paramters.
with open(sys.argv[1], "a+") as yamlTARGET:
    # 2A. Software
    mpileup2snp_varScanProg = "mpileup2snp_varScanProg: varScan\n"
    mpileup2indel_varScanProg = "mpileup2indel_varScanProg: varScan\n"
    somatic_varScanProg = "somatic_varScanProg: varScan\n"
    # 2B. Shared variables
    vcfDIR="vcfDIR: vcf\n"
    varScanDIR="varScanDIR: varScan\n"
    varScanChrSplit="varScanChrSplit: True\n"
    minCOV = "minCOV: --min-coverage 20\n"
    minREAD = "minREAD: --min-reads2 10\n"
    minQUAL = "minQUAL: --min-avg-qual 20\n"
    minFREQ = "minFREQ: --min-var-freq 0.01\n"
    pVALUE = "pVALUE: --p-value 0.05\n"
    strandFILT = "strandFILT: --strand-filter 0\n"
    outVCF = "outVCF: --output-vcf 1\n"
    # 2C. mpileup2snp only variables
    # 2D. mpileup2indel only variables
    # 2E. Somatic only variables
    minSTRAND = "minSTRAND: --min-strands2 0\n"
    posVALID = "posVALID: --validation 1\n"
    # 2F. Write to file.
    yamlTARGET.write("\n\n\n#################################\n# ---- " + moduleNAME + " Parameters ----- #\n#################################\n")
    yamlTARGET.write("#       -- Software --          #\n" + mpileup2snp_varScanProg + mpileup2indel_varScanProg + somatic_varScanProg)
    yamlTARGET.write("#    -- Shared Variables --     #\n" + vcfDIR + varScanDIR + varScanChrSplit + minCOV + minREAD + minQUAL + minFREQ + pVALUE + strandFILT + outVCF)
    yamlTARGET.write("#   -- mpileup2snp Specific --  #\n")
    yamlTARGET.write("# -- mpileup2indels Specific -- #\n")
    yamlTARGET.write("#    -- somatic Specific --     #\n" + minSTRAND + posVALID)
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
    jsonOBJ['somatic'] = jsonRULE
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
        "#    somatic:    Coming soon!.\n" + 
        "#  Files:\n" +
        "#    input:      X.mpileup\n" +
        "#    output:     X.varScan.snps.vcf\n" +
        'include: "/home/tboyarski/share/projects/tboyarski/gitRepo-LCR-BCCRC/Snakemake/modules/' + moduleNAME + '/' + moduleNAME + '_INCLUDE"\n' +
        "#  Required:\n" +
        "#    >mPile:      Generate a MPileUp file from a BAM file.\n" +
        '#    @include: "/home/tboyarski/share/projects/tboyarski/gitRepo-LCR-BCCRC/Snakemake/modules/mPile/mPile_INCLUDE"\n' +
        "#  Call via:\n" +
        '# expand("{outputDIR}/{vcfDIR}/{samples}.varScan.snps.vcf", outputDIR=config["outputDIR"], vcfDIR=config["vcfDIR"], samples=config["sample"])\n' +
        '# expand("{outputDIR}/{vcfDIR}/{samples}.varScan.indels.vcf", outputDIR=config["outputDIR"], vcfDIR=config["vcfDIR"], samples=config["sample"])\n'
    )
