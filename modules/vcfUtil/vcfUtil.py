#---------------------------------------------------
# Author:   Tim Boyarski
# Date:     2017-06-21
#-----------------------------------------------------------
# Call: call("python " + snakeDIR + "/modules/vcfUtil/vcfUtil.py " + YAMLFILE + " " + CLUSTERFILE + " " + SNAKEFILE, shell=True)
#
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
moduleNAME = "vcfUtil"
#-----------------------------------------------------------------------------------------------------------------------------------------------------



##################################################
# fieldGenerator
##################################################
# Function to generate the combination of arguents for vcfGenFields(Paired) variable
#   written to '.YAML' file.
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def fieldGenerator(flagLIST, sampleLIST):
    finalString = ""
    for flag in flagLIST:
        for sample in sampleLIST:
            finalString += 'GEN[' + sample + "]." + flag + " "
    return finalString
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
     ruleLIST = ['getVcfTable',
             'mergeVCF',
             'sortVCF']
    # 1A. Create module directory.
     mkdir("log/" + moduleNAME)
     print(moduleNAME + ".py \tCreating: log/" + moduleNAME)
     # 1B. Create rule directories and report to user.
     for rule in ruleLIST:
         mkdir("log/" + moduleNAME + "/" + rule)
         print(moduleNAME + ".py \tCreating: log/" + moduleNAME + "/" + rule + "/")
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 2 --- YAML File
# Open and append to file the following required paramters.
with open(argv[1], "a+") as yamlTARGET:
    # 2A. Software
    vcfUtil_samtoolsProg="vcfUtil_samtoolsProg: samtools\n"
    vcfUtil_picardProg="vcfUtil_picardProg: picard\n"
    vcfUtil_javaProg="vcfUtil_javaProg: java -Xmx2G\n"
    vcfUtil_snpSiftProg="vcfUtil_snpSiftProg: -jar ~/share/usr/anaconda/4.3.0/envs/CentOS5-APR28-2/share/snpeff-4.1l-0/SnpSift.jar\n"
    vcfUtil_vcfEffOnePerLineProg="vcfUtil_vcfEffOnePerLineProg: ~/share/usr/anaconda/4.3.0/envs/CentOS5-APR28-2/share/snpeff-4.1l-0/scripts/vcfEffOnePerLine.pl\n"
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
    vcfUtilDIR="vcfUtilDIR: vcfUtil\n"
    # 2C. getVcfTable variables
    OnePerLineFLAG="OnePerLineFLAG: False\n"
    # 2C. mergeVCF variables
    # 2C. sortVCF variables
    vcfSORTValStringency="vcfSORTValStringency: VALIDATION_STRINGENCY=LENIENT\n"
    vcfSORTMaxRec="vcfSORTMaxRec: MAX_RECORDS_IN_RAM=5000000\n"
    vcfSORTSeqDict="vcfSORTSeqDict: ~/share/references/genomes/gsc/GRCh37-lite.dict\n"
    # Write it to file
    yamlTARGET.write(
        "\n\n"
        "#####################################\n"
        "# " + moduleNAME + " Parameters\n"
        "#####################################\n"
        "#----------------------------------------------------------------- *Software* ------------------------------------------------------------------------\n" +
        vcfUtil_samtoolsProg + vcfUtil_picardProg + vcfUtil_javaProg + vcfUtil_snpSiftProg +
        vcfUtil_vcfEffOnePerLineProg +
        "#----------------------------------------------------------------- *Shared Variables* ----------------------------------------------------------------\n" +
        vcfSampleSingle + vcfGenIDsSingle + vcfInfoFieldsDbSnp + vcfGenFieldsSingle + vcfSamplePair +
        vcfGenIDsPair + vcfInfoFieldsPair + vcfGenFieldsPair + vcfFields + effFields + vcfUtilDIR +
        "#----------------------------------------------------------------- getVcfTable -----------------------------------------------------------------------\n" +
        OnePerLineFLAG +
        "#----------------------------------------------------------------- mergeVCF --------------------------------------------------------------------------\n" +
        "#----------------------------------------------------------------- sortVCF ---------------------------------------------------------------------------\n" +
        vcfSORTValStringency + vcfSORTMaxRec + vcfSORTSeqDict +
        "#-----------------------------------------------------------------------------------------------------------------------------------------------------\n"
    )
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 3 --- JSON File
# Generate header for '.json' file.
# Read file to parse and store '.json'  object.
with open(argv[2], "r+") as jsonTARGET:
    jsonOBJ = load(jsonTARGET)
    jsonOBJ['getVcfTable'] = {
            "clusterSpec": "-V -S /bin/bash -o log/vcfUtil/getVcfTable -e log/vcfUtil/getVcfTable -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleGVCFT}"
    }
    jsonOBJ['mergeVCF'] = {
            "clusterSpec": "-V -S /bin/bash -o log/vcfUtil/mergeVCF -e log/vcfUtil/mergeVCF -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleMVCF}.{wildcards.vcfProgramMVCF}.{wildcards.varTypeMVCF}"
    }
    jsonOBJ['sortVCF'] = {
            "clusterSpec": "-V -S /bin/bash -o log/vcfUtil/sortVCF -e log/vcfUtil/sortVCF -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleSVCF}"
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
        "#      getVcfTable:        Produce a variant table from a '.VCF' file.\n"
        "#      mergeVCF:           Merge chromosomal '.VCF' files into a single genomic '.VCF' file.\n"
        "#      sortVCF:            Sort a '.VCF' file based on sequence provided.\n"
        "#  Files:\n"
        "#    Input:      **Various**f\n"
        "#    Output:     **Various**\n"
        'include: "' + path.dirname(path.realpath(__file__)) + '/' + moduleNAME + '_INCLUDE"\n'
        "#  Required:   vcfProgram to be set in YAML to the name of the program used to create the '.vcf's'\n"
        "#              vcfUtilDIR to be set in YAML to directory which produced the '.vcf's'\n"
        "#  Call via: \n"
        '#getVcfTable:      expand("{outputDIR}/{pathGVCFT}/tables/{samples}.{vcfProgram}.{form[1][varType]}{form[1][annotated]}.txt", outputDIR=config["outputDIR"], pathGVCFT=config["vcfGenUtil_varScanDIR"], samples=config["sample"], vcfProgram=config["vcfProgram"], form=read_table(StringIO(config["sampleFORM"]), " ").iterrows())\n'
        '#mergeVCF:         expand("{outputDIR}/{pathMVCF}/{samples}.{vcfProgram}.{varType}.vcf", outputDIR=config["outputDIR"], pathMVCF=config["vcfGenUtil_varScanDIR"], samples=config["sample"], vcfProgram=config["vcfProgram"], varType=config["varType"])\n'
        '#sortVCF:          expand("{outputDIR}/{pathSVCF}/{samples}_sorted.{vcfProgram}.{varType}.vcf", outputDIR=config["outputDIR"], pathSVCF=config["vcfGenUtil_varScanDIR"], samples=config["sample"], vcfProgram=config["vcfProgram"], varType=config["varType"])\n'
        "#-----------------------------------------------------------------------------------------------------------------------------------------------------\n"
    )
#-----------------------------------------------------------------------------------------------------------------------------------------------------
