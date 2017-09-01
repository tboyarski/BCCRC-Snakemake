#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Author:   Tim Boyarski
# Date:     2017-06-16
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Call: call("python " + snakeDIR + "/modules/varScan/varScan.py " + YAMLFILE + " " + CLUSTERFILE + " " + SNAKEFILE, shell=True)
#
# Purpose: Generate '.vcf' output from a 'mpileup' file. Module is also
#   able to generate CopyNumber, CopyCall, and Consensus Sequence data.
#-----------------------------------------------------------------------------------------------------------------------------------------------------

# Request sys so be able to use CLI arguments.
from sys import argv

# Request json to be able to load and write to the config.json file.
from json import load, dump

# Request os permissions to be able to create directories for the log files.
from os import path, mkdir

# Global variable used for reporting of the module name.
moduleNAME = "vcfGenUtil_varScan"

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 0 --- Validate number of user arguments.
if len(argv) !=4:
    print("Please provide arguments as follows:")
    print("python " + moduleNAME + ".py yaml json snake")
    print("\t-yaml = 'path/name' of the yaml file to write the pipeline parameters")
    print("\t-snake = 'path/name' of snakefile we are building")
    print("\t-json = 'path/name' of the json file we write the cluster config to")
    quit()

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 1 --- Log Files
# Check if directories exist for logging, as the DRMAA caller cannot create directories.
if (path.isdir("log")) != True:
    mkdir("log")
    print(moduleNAME + ".py \tCreating: log/")
if (path.isdir("log/" + moduleNAME) != True):
    # Maintain this list of active submodules.
    ruleLIST = ['conSeq',
            'copycall',
            'copynum',
            'mpileup2vcf_pair',
            'mpileup2vcf_single']
    # 1A. Create module directories
    mkdir("log/" + moduleNAME)
    print(moduleNAME + ".py \tCreating: log/" + moduleNAME)
    # 1B. Report on directories created.
    for rule in ruleLIST:
        mkdir("log/" + moduleNAME + "/" + rule)
        print(moduleNAME + ".py \tCreating: log/" + moduleNAME + "/" + rule + "/")

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 2 --- YAML File
# Open and append to file the following required paramters.
with open(argv[1], "a+") as yamlTARGET:
    # 2A. Software
    vcfGenUtil_varScan_varScanProg = "vcfGenUtil_varScan_varScanProg: varscan\n"
    vcfGenUtil_varScan_samtoolsProg="vcfGenUtil_varScan_samtoolsProg: samtools\n"
    # 2B. Shared variables
    vcfProgram="vcfProgram: varScan\n"
    varType="varType: ['snp', 'indel']\n"
    vcfGenUtil_varScanDIR="vcfGenUtil_varScanDIR: vcfGenUtil_varScan\n"
    minCoverage = "minCoverage: --min-coverage 20\n"
    minRead = "minRead: --min-reads2 10\n"
    minQuality = "minQuality: --min-avg-qual 20\n"
    minFrequency = "minFrequency: --min-var-freq 0.01\n"
    pValue = "pValue: --p-value 0.05\n"
    strandFilter = "strandFilter: --strand-filter 0\n"
    outVCF = "outVCF: --output-vcf 1\n"
    minStrand = "minStrand: --min-strands2 0\n"
    posValid = "posValid: --validation 0\n"
    # 2C. conSeq variables
    # 2C. copycall variables
    # 2C. copynum variables
    mapQSkip="mapQSkip: -q 1\n"
    # 2C. mpileup2vcf_pair variables
    # 2C. mpileup2vcf_single variables
    # 2D. Write to file.
    yamlTARGET.write(
        "\n\n"+
        "#####################################\n"
        "# " + moduleNAME + " Parameters\n"
        "#####################################\n"
        "#----------------------------------------------------------------- *Software* ------------------------------------------------------------------------\n"+
        vcfGenUtil_varScan_varScanProg + vcfGenUtil_varScan_samtoolsProg +
        "#----------------------------------------------------------------- *Shared Variables* ----------------------------------------------------------------\n"+
        vcfProgram + varType + vcfGenUtil_varScanDIR + minCoverage + minRead + minQuality + minFrequency + pValue + strandFilter + outVCF + minStrand + posValid +
        "#----------------------------------------------------------------- conSeq ----------------------------------------------------------------------------\n"
        "#----------------------------------------------------------------- copycall --------------------------------------------------------------------------\n"
        "#----------------------------------------------------------------- copynum ---------------------------------------------------------------------------\n"+
        mapQSkip +
        "#----------------------------------------------------------------- mpileup2vcf_pair ------------------------------------------------------------------\n"
        "#----------------------------------------------------------------- mpileup2vcf_single ----------------------------------------------------------------\n"
        "#-----------------------------------------------------------------------------------------------------------------------------------------------------\n"
    )

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 3 --- JSON File
# Build the JSON file.
# 3A. Read file to parse and store '.json'  object.
with open(argv[2], "r+") as jsonTARGET:
    jsonOBJ = load(jsonTARGET)
    jsonOBJ['conSeq'] = {
            "clusterSpec": "-V -S /bin/bash -o log/vcfGenUtil_varScan/conSeq -e log/vcfGenUtil_varScan/conSeq -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleCS}"
    }
    jsonOBJ['copycall'] = {
            "clusterSpec": "-V -S /bin/bash -o log/vcfGenUtil_varScan/copycall -e log/vcfGenUtil_varScan/copycal -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampletCC}_{wildcards.samplenCC}"
    }
    jsonOBJ['copynum'] = {
            "clusterSpec": "-V -S /bin/bash -o log/vcfGenUtil_varScan/copynum -e log/vcfGenUtil_varScan/copynum -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampletCN}_{wildcards.samplenCN}"
    }
    jsonOBJ['mpileup2vcf_pair'] = {
            "clusterSpec": "-V -S /bin/bash -o log/vcfGenUtil_varScan/mpileup2vcf_pair -e log/vcfGenUtil_varScan/mpileup2vcf_pair -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampletMPU2VCFP}_{wildcards.samplenMPU2VCFP}_chr{wildcards.chrMPU2VCFP}.SNPandINDEL"
    }
    jsonOBJ['mpileup2vcf_single'] = {
            "clusterSpec": "-V -S /bin/bash -o log/vcfGenUtil_varScan/mpileup2vcf_single -e log/vcfGenUtil_varScan/mpileup2vcf_single -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleMPU2VCFS}_chr{wildcards.chrMPU2VCFS}.SNPandINDEL"
    }
# 3B. Recreate JSON file to delete exiting text.
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
        "#    conSeq:                       Generate concensus calls from a '.mpileup' file.\n"
        "#    copycall:                     Infer somatic copy number changes using data from matched tumor-normal pairs.\n"
        "#    copynumb                      Call variants and identify their somatic status.\n"
        "#    mpileup2vcf_pair:             Generate '.VCF' output of SNPs from a chromosomal tumor-normal '.mpileup' file.\n"
        "#    mpileup2vcf_single:           Generate '.VCF' output of SNPs from a chromosomeal sample '.mpileup' file.\n"
        "#  Files:\n"
        "#    input:      X.mpileup\n"
        "#    output:     X.varScan.snps.vcf\n"
        "#                X.varScan.indels.vcf\n"
        'include: "' + path.dirname(path.realpath(__file__)) + '/' + moduleNAME + '_INCLUDE"\n'
        "#  Required:\n"
        "#    >mpileupGen:      Generate a '.mpileup' file from a '.BAM' file. (Required to set 'mpileupDIR' variable in 'config.yaml' file.\n"
        "#    >vcfUtil:         Utility functions, required to merge the '.vcf' files if run on a per chromosome basis, and to parse the '.vcf' files for '.txt' representation.\n"
        "#    >genericUtil:     Utility functions, required for the merging of '.txt' files.\n"
        '#    @include: "' + path.dirname(path.dirname(path.realpath(__file__))) + '/utils/utils_INCLUDE"\n'
        "# --- Call Pair (Tumor-Normal) Runs Via: --------------------------------------------------\n"
        '#pairSPLIT:     expand("{outputDIR}/{vcfGenUtil_varScanDIR}/{sample[1][tumor]}_{sample[1][normal]}_{chrLIST}.{vcfProgram}.{varType}.vcf", outputDIR=config["outputDIR"], vcfGenUtil_varScanDIR=config["vcfGenUtil_varScanDIR"], sample=read_table(config["sampleFILE"], " ").iterrows(), chrLIST=config["chrLIST"], vcfProgram=config["vcfProgram"], varType=config["varType"]),\n'
        '#pairUNSPLIT:   expand("{outputDIR}/{vcfGenUtil_varScanDIR}/{sample[1][tumor]}_{sample[1][normal]}.{vcfProgram}.{varType}.vcf", outputDIR=config["outputDIR"], vcfGenUtil_varScanDIR=config["vcfGenUtil_varScanDIR"], sample=read_table(config["sampleFILE"], " ").iterrows(), vcfProgram=config["vcfProgram"], varType=config["varType"]),\n'
        "# - Annotated Paired Runs (Requiring modules: genericUtil, vcfUtil, vcfAnnotate):\n"
        '#pairVCF:          expand("{outputDIR}/{vcfAnnotateDIR}/{sample[1][tumor]}_{sample[1][normal]}.{vcfProgram}.{form[1][varType]}{form[1][annotated]}.vcf", outputDIR=config["outputDIR"], vcfAnnotateDIR=config["vcfAnnotateDIR"], sample=read_table(config["sampleFILE"], " ").iterrows(), vcfProgram=config["vcfProgram"], form=read_table(StringIO(config["sampleFORM"]), " ").iterrows()),\n'
        '#pairTXT:          expand("{outputDIR}/{vcfUtilDIR}/{sample[1][tumor]}_{sample[1][normal]}.{vcfProgram}.{form[1][varType]}{form[1][annotated]}.txt", outputDIR=config["outputDIR"], vcfUtilDIR=config["vcfUtilDIR"], sample=read_table(config["sampleFILE"], " ").iterrows(), vcfProgram=config["vcfProgram"], form=read_table(StringIO(config["sampleFORM"]), " ").iterrows()),\n'
        '#pairALL:          expand("{outputDIR}/{vcfUtilDIR}/all.samples.{vcfProgram}.{form[1][varType]}{form[1][annotated]}.txt", outputDIR=config["outputDIR"], vcfUtilDIR=config["vcfUtilDIR"], vcfProgram=config["vcfProgram"], form=read_table(StringIO(config["sampleFORM"]), " ").iterrows()),\n'
        "# --- Call Single Runs Via: ---------------------------------------------------------------\n"
        '#singleSPLIT:     expand("{outputDIR}/{vcfGenUtil_varScanDIR}/{samples}_{chrLIST}.{vcfProgram}.{varType}.vcf", outputDIR=config["outputDIR"], vcfGenUtil_varScanDIR=config["vcfGenUtil_varScanDIR"], samples=config["sample"], chrLIST=config["chrLIST"], vcfProgram=config["vcfProgram"], varType=config["varType"]),\n'
        '#singleUNSPLIT:   expand("{outputDIR}/{vcfGenUtil_varScanDIR}/{samples}.{vcfProgram}.{varType}.vcf", outputDIR=config["outputDIR"], vcfGenUtil_varScanDIR=config["vcfGenUtil_varScanDIR"], samples=config["sample"], vcfProgram=config["vcfProgram"], varType=config["varType"]),\n'
        "# - Annotated Single Runs (Requiring modules: genericUtil, vcfUtil, vcfAnnotate):\n"
        '#singleVCF:          expand("{outputDIR}/{vcfAnnotateDIR}/{samples}.{vcfProgram}.{form[1][varType]}{form[1][annotated]}.vcf", outputDIR=config["outputDIR"], vcfAnnotateDIR=config["vcfAnnotateDIR"], samples=config["sample"], vcfProgram=config["vcfProgram"], form=read_table(StringIO(config["sampleFORM"]), " ").iterrows()),\n'
        '#singleTXT:          expand("{outputDIR}/{vcfUtilDIR}/{samples}.{vcfProgram}.{form[1][varType]}{form[1][annotated]}.txt", outputDIR=config["outputDIR"], vcfUtilDIR=config["vcfUtilDIR"], samples=config["sample"], vcfProgram=config["vcfProgram"], form=read_table(StringIO(config["sampleFORM"]), " ").iterrows()),\n'
        '#singleALL:          expand("{outputDIR}/{vcfUtilDIR}/all.samples.{vcfProgram}.{form[1][varType]}{form[1][annotated]}.txt", outputDIR=config["outputDIR"], vcfUtilDIR=config["vcfUtilDIR"], samples=config["sample"], vcfProgram=config["vcfProgram"], form=read_table(StringIO(config["sampleFORM"]), " ").iterrows()),\n'
        "# --- Call Other Via: ---------------------------------------------------------------\n"
        '#conSeq1:      expand("{outputDIR}/{vcfGenUtil_varScanDIR}/{sample[1][tumor]}.{vcfProgram}.mpileup2cns", outputDIR=config["outputDIR"], vcfGenUtil_varScanDIR=config["vcfGenUtil_varScanDIR"], sample=read_table(config["sampleFILE"], " ").iterrows(), vcfProgram=config["vcfProgram"],),\n'
        '#conSeq2:      expand("{outputDIR}/{vcfGenUtil_varScanDIR}/{sample[1][normal]}.{vcfProgram}.mpileup2cns", outputDIR=config["outputDIR"], vcfGenUtil_varScanDIR=config["vcfGenUtil_varScanDIR"], sample=read_table(config["sampleFILE"], " ").iterrows(),  vcfProgram=config["vcfProgram"]),\n'
        '#copycall:     expand("{outputDIR}/{vcfGenUtil_varScanDIR}/{sample[1][tumor]}_{sample[1][normal]}.{vcfProgram}.copycall", outputDIR=config["outputDIR"], vcfGenUtil_varScanDIR=config["vcfGenUtil_varScanDIR"], sample=read_table(config["sampleFILE"], " ").iterrows(),  vcfProgram=config["vcfProgram"]),\n'
        '#copynum:      expand("{outputDIR}/{vcfGenUtil_varScanDIR}/{sample[1][tumor]}_{sample[1][normal]}.{vcfProgram}.copynumber", outputDIR=config["outputDIR"], vcfGenUtil_varScanDIR=config["vcfGenUtil_varScanDIR"], sample=read_table(config["sampleFILE"], " ").iterrows(),  vcfProgram=config["vcfProgram"]),\n'
        '#-----------------------------------------------------------------------------------------------------------------------------------------------------\n'
    )
#-----------------------------------------------------------------------------------------------------------------------------------------------------
