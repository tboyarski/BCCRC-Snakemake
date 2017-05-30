#---------------------------------------------------
# Author:   Tim Boyarski
# Date:     2017-03-06
#-----------------------------------------------------------
# Call: call("python " + snakeDIR + "/modules/varTables/varTables.py " + YAMLFILE + " " + CLUSTERFILE + " " + SNAKEFILE, shell=True)
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

moduleNAME = "utils"

# Function to generate the combination of arguents for vcfGenFields(Paired) variable
#   written to '.YAML' file.
def fieldGenerator(flagLIST, sampleLIST):
    finalString = ""
    for flag in flagLIST:
        for sample in sampleLIST:
            finalString += 'GEN[' + sample + "]." + flag + " "
    return finalString

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
     # Maintain this list of active submodules.
     moduleLIST = ['tableMERGE', 'vcfGetTable', 'vcfMERGE', 'vcfSORT']
     # 1A. Create module directory.
     os.mkdir("log/" + moduleNAME)
     print(moduleNAME + ".py \tCreating: log/" + moduleNAME)
     # 1B. Create submodule directories and report to user.
     for module in moduleLIST:
         os.mkdir("log/" + moduleNAME + "/" + module)
         print(moduleNAME + ".py \tCreating: log/" + moduleNAME + "/" + module + "/")

# Open and append to file the following required paramters.
with open(sys.argv[1], "a+") as yamlTARGET:
    # 2A. Software
    utils_picardProg="utils_picardProg: picard\n"
    utils_javaProg="utils_javaProg: java -Xmx2G\n"
    utils_snpSiftProg="utils_snpSiftProg: -jar ~/share/usr/anaconda/4.3.0/envs/CentOS5-APR28-2/share/snpeff-4.1l-0/SnpSift.jar\n"
    utils_vcfEffOnePerLineProg="utils_vcfEffOnePerLineProg: ~/share/usr/anaconda/4.3.0/envs/CentOS5-APR28-2/share/snpeff-4.1l-0/scripts/vcfEffOnePerLine.pl\n"
    # 2B. Shared pre-yaml variables
    vcfSampleSingleVar=['0']
    vcfGenIDsSingleVar=['GT', 'GQ', 'SDP', 'DP', 'RD', 'AD', 'FREQ', 'PVAL', 'RBQ', 'ABQ', 'RDF', 'RDR', 'ADF', 'ADR']
    vcfSamplePairVar=['0', '1']
    vcfGenIDsPairVar=['GT', 'GQ', 'DP', 'RD', 'AD', 'FREQ', 'DP4']
    # 2B. Shared variables
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
    utilsDIR="utilsDIR: utils\n"
    # 2. vcfMERGE variables
    # 2. vcfGetTable variables
    OnePerLineFLAG="OnePerLineFLAG: False\n"
    # 2. vcfSORT variabless
    vcfSORTInputDIR="vcfSORTInputDIR: varScan\n"
    vcfSORTValStringency="vcfSORTValStringency: VALIDATION_STRINGENCY=LENIENT\n"
    vcfSORTMaxRec="vcfSORTMaxRec: MAX_RECORDS_IN_RAM=5000000\n"
    vcfSORTSeqDict="vcfSORTSeqDict: ~/share/references/genomes/gsc/GRCh37-lite.dict\n"
    # Write it to file
    yamlTARGET.write("\n\n#################################\n# ----- " + moduleNAME + " Parameters ------ #\n#################################\n")
    yamlTARGET.write("#       -- Software --          #\n" + utils_picardProg + utils_javaProg + utils_snpSiftProg + utils_vcfEffOnePerLineProg)
    yamlTARGET.write("#    -- Shared Variables --     #\n" + vcfSampleSingle + vcfGenIDsSingle + vcfInfoFieldsDbSnp + vcfGenFieldsSingle \
            + vcfSamplePair + vcfGenIDsPair + vcfInfoFieldsPair + vcfGenFieldsPair + vcfFields + effFields + utilsDIR)
    yamlTARGET.write("#  -- vcfGetTable Specific --   #\n" + OnePerLineFLAG)
    yamlTARGET.write("#     -- sortVCF Specific --    #\n" + vcfSORTInputDIR + vcfSORTValStringency + vcfSORTMaxRec + vcfSORTSeqDict)
    yamlTARGET.write("#################################\n")

# 3 --- JSON File
# Generate header for '.json' file.
# Read file to parse and store '.json'  object.
with open(sys.argv[2], "r+") as jsonTARGET:
    jsonOBJ = json.load(jsonTARGET)
    jsonOBJ['tableMERGE'] = {
            "clusterSpec": "-V -S /bin/bash -o log/utils/tableMERGE -e log/utils/tableMERGE -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_all.samples_{wildcards.annotationSUFFIX}"
    }
    jsonOBJ['vcfGetTable_utilsDIR'] = {
            "clusterSpec": "-V -S /bin/bash -o log/utils/vcfGetTable -e log/utils/vcfGetTable -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleVCFGT}"
    }
    jsonOBJ['vcfGetTable_annotateVcfDIR'] = {
            "clusterSpec": "-V -S /bin/bash -o log/utils/vcfGetTable -e log/utils/vcfGetTable -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleVCFGT}"
    }
    jsonOBJ['vcfMERGE_varScan'] = {
            "clusterSpec": "-V -S /bin/bash -o log/utils/vcfMERGE -e log/utils/vcfMERGE -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleVCFM}_{wildcards.varTypeVCFM}"
    }
    jsonOBJ['vcfMERGE'] = {
            "clusterSpec": "-V -S /bin/bash -o log/utils/vcfMERGE -e log/utils/vcfMERGE -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleVCFM}_{wildcards.varTypeVCFM}"
    }
    jsonOBJ['vcfSORT_varScanDIR'] = {
            "clusterSpec": "-V -S /bin/bash -o log/utils/vcfSORT -e log/utils/vcfSORT -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleVCFS}"
    }
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
        'include: "' + os.path.dirname(os.getcwd()) + '/modules/' + moduleNAME + '/' + moduleNAME + '_INCLUDE"\n' +
        "#  Required: NONE\n" +
        "#  Call via: \n" +
        '#  expand("{outputDIR}/{utilsDIR}/{samples}.varScan.snps.txt", outputDIR=config["outputDIR"], utilsDIR=config["utilsDIR"], samples=config["sample"])\n' +
        '#  expand("{outputDIR}/{varTableDIR}/{index[1][tumor]}_{index[1][normal]}.varScan.{varType}.txt", outputDIR=config["outputDIR"], varTableDIR=config["varTableDIR"], index=pandas.read_table(config["sampleFILE"], " ").iterrows(), varType=config["varType"])\n'
    )
