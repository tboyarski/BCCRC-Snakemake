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
    print("python " + moduleNAME + ".py yaml json snake")
    print("\t-yaml = 'path/name' of the yaml file to write the pipeline parameters")
    print("\t-json = 'path/name' of the json file we write the cluster config to")
    print("\t-snake = 'path/name' of snakefile we are building")
    quit()


# 1 --- Log Files
# Check if directories exist for logging, as the DRMAA caller cannot create directories.
if (os.path.isdir("log")) != True:
    print(moduleNAME + ".py \tCreating: log/")
    os.mkdir("log")
if (os.path.isdir("log/" + moduleNAME) != True):
     # Maintain this list of active submodules.
     moduleLIST = ['sam2BAM', 'tableMERGE', 'vcfGetTable', 'vcfMERGE', 'vcfSORT']
     # 1A. Create module directory.
     os.mkdir("log/" + moduleNAME)
     print(moduleNAME + ".py \tCreating: log/" + moduleNAME)
     # 1B. Create submodule directories and report to user.
     for module in moduleLIST:
         os.mkdir("log/" + moduleNAME + "/" + module)
         print(moduleNAME + ".py \tCreating: log/" + moduleNAME + "/" + module + "/")

# 2 --- YAML File
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
    # 2C. sam2BAM variables
    Sam2BamARGS="Sam2BamARGS: -bS\n"
    samDIR="samDIR: sam\n"
    # 2C. tableMERGE_ADAPTOR
    # 2C. vcfGetTable_ADAPTOR variables
    OnePerLineFLAG="OnePerLineFLAG: False\n"
    # 2C. vcfMERG_ADAPTOR variables
    # 2C. vcfSORT_ADAPTOR variabless
    vcfSORTInputDIR="vcfSORTInputDIR: varScan\n"
    vcfSORTValStringency="vcfSORTValStringency: VALIDATION_STRINGENCY=LENIENT\n"
    vcfSORTMaxRec="vcfSORTMaxRec: MAX_RECORDS_IN_RAM=5000000\n"
    vcfSORTSeqDict="vcfSORTSeqDict: ~/share/references/genomes/gsc/GRCh37-lite.dict\n"
    # Write it to file
    yamlTARGET.write("\n\n#################################\n# ----- " + moduleNAME + " Parameters ------ #\n#################################\n")
    yamlTARGET.write("#       -- Software --          #\n" + utils_picardProg + utils_javaProg + utils_snpSiftProg + utils_vcfEffOnePerLineProg)
    yamlTARGET.write("#    -- Shared Variables --     #\n" + vcfSampleSingle + vcfGenIDsSingle + vcfInfoFieldsDbSnp + vcfGenFieldsSingle \
            + vcfSamplePair + vcfGenIDsPair + vcfInfoFieldsPair + vcfGenFieldsPair + vcfFields + effFields + utilsDIR)
    yamlTARGET.write("#    -- sam2BAM Specific --     #\n" + Sam2BamARGS + samDIR)
    yamlTARGET.write("#  tableMERGE_ADAPTOR Specific  #\n")
    yamlTARGET.write("#  vcfGetTable_ADAPTOR Specific #\n" + OnePerLineFLAG)
    yamlTARGET.write("#    vcfMERGE_ADAPTOR Specific  #\n")
    yamlTARGET.write("#    vcfSORT_ADAPTOR Specific   #\n" + vcfSORTInputDIR + vcfSORTValStringency + vcfSORTMaxRec + vcfSORTSeqDict)
    yamlTARGET.write("#################################\n")


# 3 --- JSON File
# Generate header for '.json' file.
# Read file to parse and store '.json'  object.
with open(sys.argv[2], "r+") as jsonTARGET:
    jsonOBJ = json.load(jsonTARGET)
    jsonOBJ['sam2BAM'] = {
            "clusterSpec": "-V -S /bin/bash -o log/utils/sam2BAM -e log/utils/sam2BAM -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleS2B}"
    }
    jsonOBJ['tableMERGE_ADAPTOR'] = {
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
    jsonOBJ['vcfMERGE_varScanDIR'] = {
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
        "#      sam2BAM:                    SAM generation from a '.BAM' file.\n" +
        "#      tableMERGE_ADAPTOR:         Merge variant tables.\n" +
        "#      vcfGetTable_ADAPTOR:        Produce a variant table from a '.VCF' file.\n" +
        "#      vcfMERGE_ADAPTOR:           Merge chromosomal '.VCF' files into a single genomic '.VCF' file.\n" +
        "#      vcfSORT_ADAPTOR:            Sort a '.VCF' file based on sequence provided.\n" +
        "#  Files:\n" +
        "#    Input:      **Various**f\n" +
        "#    Output:     **Various**\n" +
        'include: "' + os.path.dirname(os.path.realpath(__file__)) + '/' + moduleNAME + '_INCLUDE"\n' +
        "#  Required: vcfProgram to be set in YAML by program producing '.vcf'\n" +
        "#  Call via: \n" +
        '#sam2BAM               ~ expand("{outputDIR}/{samDIR}/{samples}.bam", outputDIR=config["outputDIR"], samDIR=config["samDIR"], samples=config["sample"])\n'+
        '#tableMERGE_ADAPTOR    ~ expand("{outputDIR}/{utilsDIR}/all.samples.{vcfProgram}.{form[1][varType]}{form[1][annotated]}.txt", outputDIR=config["outputDIR"], utilsDIR=config["utilsDIR"], samples=config["sample"], vcfProgram=config["vcfProgram"], form=pandas.read_table(io.StringIO(config["sampleFORM"]), " ").iterrows())\n'+
        '#vcfGetTable_ADAPTOR   ~ expand("{outputDIR}/{utilsDIR}/{samples}.{vcfProgram}.{form[1][varType]}{form[1][annotated]}.txt", outputDIR=config["outputDIR"], utilsDIR=config["utilsDIR"], samples=config["sample"], vcfProgram=config["vcfProgram"], form=pandas.read_table(io.StringIO(config["sampleFORM"]), " ").iterrows())\n'+
        '#vcfMERGE_ADAPTOR      ~ expand("{outputDIR}/{varScanDIR}/{samples}.{vcfProgram}.{varType}.vcf", outputDIR=config["outputDIR"], varScanDIR=config["varScanDIR"], samples=config["sample"], vcfProgram=config["vcfProgram"], varType=config["varType"])\n'+
        '#vcfSORT_ADAPTOR       ~ expand("{outputDIR}/{varScanDIR}/{samples}.sorted.{vcfProgram}.{varType}.vcf", outputDIR=config["outputDIR"], varScanDIR=config["varScanDIR"], samples=config["sample"], vcfProgram=config["vcfProgram"], varType=config["varType"])\n'
    )
