#---------------------------------------------------
# Author:   Tim Boyarski                                    
# Date:     2017-03-06                                      
#-----------------------------------------------------------
# Call: call("python " + snakeDIR + "/modules/getVarTable/getVarTable.py " + YAMLFILE + " " + CLUSTERFILE + " " + SNAKEFILE, shell=True)
# Input:                                    .XXXXXXXX       
# Output:                                   .XXXXXXXX       
# Purpose: Automate the population of user's pipeline 
#   Snakefile, '.YAML', and '.JSON' files.
#-------------------------------------------------------------------

#Highlight needed fields with: XXXXXXXX

# Request sys so be able to use CLI arguments
import sys
import json
import os

moduleNAME = "getVarTable"

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

# Function to generate the combination of arguents for vcfGenFields(Paired)
def fieldGenerator(flagLIST, sampleLIST):
    finalString = ""
    for flag in flagLIST:
        for sample in sampleLIST:
            finalString += 'GEN[' + sample + "]." + flag + " "
    return finalString        



# Open and append to file the following required paramters.
with open(sys.argv[1], "a+") as yamlTARGET:
    # 2A. Software
    getVarTable_javaProg="getVarTable_javaProg: java -Xmx2G\n"
    getVarTable_snpSiftProg="getVarTable_snpSiftProg: -jar ~/share/usr/anaconda/4.3.0/envs/CentOS5-APR28-2/share/snpeff-4.1l-0/SnpSift.jar\n"
    getVarTable_vcfEffOnePerLineProg="getVarTable_vcfEffOnePerLineProg: ~/share/usr/anaconda/4.3.0/envs/CentOS5-APR28-2/share/snpeff-4.1l-0/scripts/vcfEffOnePerLine.pl\n"
    
    # 2B.1 Shared non-yaml variables
    vcfSampleSingleVar=['0']
    vcfGenIDsSingleVar=['GT', 'GQ', 'SDP', 'DP', 'RD', 'AD', 'FREQ', 'PVAL', 'RBQ', 'ABQ', 'RDF', 'RDR', 'ADF', 'ADR']
    vcfSamplePairVar=['0', '1']
    vcfGenIDsPairVar=['GT', 'GQ', 'DP', 'RD', 'AD', 'FREQ', 'DP4']
    # 2B.2 Shared variables
    vcfSampleSingle="vcfSampleSingle: " + " ".join(vcfSampleSingleVar) + " \n"
    vcfGenIDsSingle="vcfGenIDsSingle: " + " ".join(vcfGenIDsSingleVar) + " \n"
    vcfInfoFieldsDbSnp="vcfInfoFieldsDbSnp: CDA KGValidated OM PM GMAF\n"
    vcfGenFieldsSingle="vcfGenFieldsSingle: " + fieldGenerator(vcfGenIDsSingleVar, vcfSampleSingleVar) + " \n"
    vcfSamplePair="vcfSamplePair: " + " ".join(vcfSamplePairVar) + " \n"
    vcfGenIDsPair="vcfGenIDsPair: " + " ".join(vcfGenIDsPairVar) + " \n"
    vcfInfoFieldsPair="vcfInfoFieldsPair: DP SS SSC GPV SPV CDA KGValidated OM PM GMAF\n"
    vcfGenFieldsPair="vcfGenFieldsPair: " + fieldGenerator(vcfGenIDsPairVar, vcfSamplePairVar)  + " \n"
    vcfFields="vcfFields: CHROM POS ID REF ALT QUAL FILTER\n"
    effFields="effFields: ['\"EFF[*].EFFECT\"', '\"EFF[*].IMPACT\"', '\"EFF[*].FUNCLASS\"', '\"EFF[*].CODON\"', '\"EFF[*].AA\"', '\"EFF[*].GENE\"', '\"EFF[*].BIOTYPE\"', '\"EFF[*].CODING\"', '\"EFF[*].TRID\"', '\"EFF[*].RANK\"']\n"
    getVarTableDIR="getVarTableDIR: getVarTable\n"
    getVarTableFlag="getVarTableFlag: False\n"
    # Write it to file
    yamlTARGET.write("\n\n#################################\n# ----- " + moduleNAME + " Parameters ------ #\n#################################\n")
    yamlTARGET.write("#       -- Software --          #\n" + getVarTable_javaProg + getVarTable_snpSiftProg + getVarTable_vcfEffOnePerLineProg)
    yamlTARGET.write("#    -- Shared Variables --     #\n" + vcfSampleSingle + vcfGenIDsSingle + vcfInfoFieldsDbSnp + vcfGenFieldsSingle \
            + vcfSamplePair + vcfGenIDsPair + vcfInfoFieldsPair + vcfGenFieldsPair \
            + vcfFields + effFields)
    yamlTARGET.write("#  -- getVarTable Specific --   #\n" + getVarTableDIR + getVarTableFlag)
    yamlTARGET.write("#################################\n")

# 3 --- JSON File
# Generate header for '.json' file.
jsonOBJ = {}
# Read file to parse and store '.json'  object.
with open(sys.argv[2], "r+") as jsonTARGET:
    jsonRULE = {}
    jsonOBJ = json.load(jsonTARGET)
    jsonRULE['clusterSpec'] = '-V -S /bin/bash -o log/' + moduleNAME + ' -e log/' + moduleNAME + ' -l h_vmem=10G -pe ncpus 1'
    jsonOBJ[moduleNAME] = jsonRULE
# Recreate JSON file to delete exiting text.
with open(sys.argv[2], "w+") as jsonTARGET:
    json.dump(jsonOBJ, jsonTARGET, indent=4)

# 4 --- Snakefile
# Open and append o file a descriptin and the last rule call.
with open(sys.argv[3], "a+") as pipeTARGET:
    pipeTARGET.write(
        "\n\n#***** " + moduleNAME + " *****\n" +
        "#  Included:\n" +
        "#    " + moduleNAME + ":     Generates a '.TXT' file from a '.VCF' file.\n" +
        "#  Files:\n" +
        "#    Input:      .vcf\n" +
        "#    Output:     .txt\n" +
        'include: "/home/tboyarski/share/projects/tboyarski/gitRepo-LCR-BCCRC/Snakemake/modules/' + moduleNAME + '/' + moduleNAME + '_INCLUDE"\n' +
        "#  Required: NONE\n" +
        "#  Call via: \n" +
        '#  expand("{outputDIR}/{getVarTableDIR}/{samples}.varScan.snps.txt", outputDIR=config["outputDIR"], getVarTableDIR=config["getVarTableDIR"], samples=config["sample"])\n' +
        '#  expand("{outputDIR}/{getVarTableDIR}/{index[1][tumor]}_{index[1][normal]}.varScan.{varType}.txt", outputDIR=config["outputDIR"], getVarTableDIR=config["getVarTableDIR"], index=pandas.read_table(config["sampleFILE"], " ").iterrows(), varType=config["varType"])\n'
    )
