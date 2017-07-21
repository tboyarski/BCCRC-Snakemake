#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Author:   Tim Boyarski
# Date:     2017-06-19
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Call: call("python " + snakeDIR + "/modules/vcfAnnotate/vcfAnnotate.py " + YAMLFILE + " " + CLUSTERFILE + " " + SNAKEFILE, shell=True)

# Purpose: Automate the population of user's pipeline
#   Snakefile, '.YAML', and '.JSON' files.
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# PYTHON PACKAGES #
#------------------
# Request sys so be able to use CLI arguments.
from sys import argv

# Request json to be able to load and write to the config.json file.
from json import load, dump

# Request os permissions to be able to create directories for the log files.
from os import path, mkdir

# Global variable used for reporting of the module name.
moduleNAME = "vcfAnnotate"
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
    mkdir("log")
    print(moduleNAME + ".py \tCreating: log/")
if (path.isdir("log/" + moduleNAME) != True):
    # Maintain this list of active submodules.
    moduleLIST = ['canonical', 'cosmic', 'indel', 'dbsnp', 'noncanonical']
    # 1A. Create module directory.
    mkdir("log/" + moduleNAME)
    print(moduleNAME + ".py \tCreating: log/" + moduleNAME)
    # 1B. Create submodule directories and report to user.q
    for module in moduleLIST:
        mkdir("log/" + moduleNAME + "/" + module)
        print(moduleNAME + ".py \tCreating: log/" + moduleNAME + "/" + module + "/")
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 2 --- YAML File
# Open and append to file the following required paramters.
with open(argv[1], "a+") as yamlTARGET:
    # 2A. Software
    vcfAnnotate_javaProg="vcfAnnotate_javaProg: java -Xmx4G\n"
    vcfAnnotate_snpSiftProg="vcfAnnotate_snpSiftProg: -jar /genesis/extscratch/clc/usr/anaconda/4.3.0/envs/CentOS5-APR28-2/share/snpeff-4.1l-0/SnpSift.jar\n"
    vcfAnnotate_snpEffProg="vcfAnnotate_snpEffProg: -jar /genesis/extscratch/clc/usr/anaconda/4.3.0/envs/CentOS5-APR28-2/share/snpeff-4.1l-0/snpEff.jar\n"
    # 2B. Shared variables
    sampleFORM='sampleFORM: "varType annotated\\nsnp .canonical_annotated.dbsnp_annotated.cosmic_annotated\\n' \
        + 'indel .canonical_annotated.indel_annotated\\n"\n'
    vcfAnnotateDIR="vcfAnnotateDIR: vcfGenUtil_varScan\n"
    annotateVerbose="annotateVerbose: -v\n"
    annotateID="annotateID: -id\n"
    #annotateDbSnp="annotateDbSnp: /genesis/extscratch/clc/references/dbsnp/dbsnp_137.hg19.vcf\n"
    annotateDbSnp="annotateDbSnp: /genesis/extscratch/clc/references/dbsnp/dbsnp_137.b37.vcf\n"
    snpEffGenomeVersion="snpEffGenomeVersion: GRCh37.72\n"
    snpEffConfig="snpEffConfig: -c /genesis/extscratch/clc/usr/anaconda/4.3.0/envs/CentOS5-APR28-2/share/snpeff-4.1l-0/snpEff.config\n"
    snpEffFormat="snpEffFormat: -i vcf\n"
    snpEffDownstream="snpEffDownstream: -no-downstream\n"
    snpEffIntergenic="snpEffIntergenic: -no-intergenic\n"
    snpEffUpstream="snpEffUpstream: -no-upstream\n"
    snpEffgatk="snpEffgatk: -o gatk\n"
    snpEffTranscript="snpEffTranscript: ''\n"
    snpEffHGVS="snpEffHGVS: -hgvs\n"
    # 2C. canonical variables
    # 2C. cosmic variables
    #snpSiftCosmic="snpSiftCosmic: /genesis/extscratch/clc/references/cosmic/CosmicCodingMuts_v68.hg19.fixed.sort.vcf\n"
    snpSiftCosmic="snpSiftCosmic: /genesis/extscratch/clc/references/cosmic/CosmicCodingMuts_v68.b37.vcf\n"
    # 2C. dbsnp variables
    # 2C. indel variables
    #knownIndel1000G="knownIndel1000G: /genesis/extscratch/clc/references/1000g/1000G_phase1.indels.hg19.with_id.vcf\n"
    #knownIndelMills1000G="knownIndelMills1000G: /genesis/extscratch/clc/references/1000g/Mills_and_1000G_gold_standard.indels.hg19.with_id.vcf\n"
    knownIndel1000G="knownIndel1000G: /genesis/extscratch/clc/references/1000g/1000G_phase1.indels.b37.with_id.vcf\n"
    knownIndelMills1000G="knownIndelMills1000G: /genesis/extscratch/clc/references/1000g/Mills_and_1000G_gold_standard.indels.b37.with_id.vcf\n"
    # 2C. noncanonical variables
    # 2D. Write to file
    yamlTARGET.write(
        "\n\n"+
        "#####################################\n"
        "# " + moduleNAME + " Parameters\n"
        "#####################################\n"
        "#----------------------------------------------------------------- *Software* ------------------------------------------------------------------------\n"+
        vcfAnnotate_javaProg + vcfAnnotate_snpSiftProg + vcfAnnotate_snpEffProg +
        "#----------------------------------------------------------------- *Shared Variables* ----------------------------------------------------------------\n"+
        sampleFORM + vcfAnnotateDIR + annotateVerbose + annotateID + annotateDbSnp + snpEffGenomeVersion + snpEffConfig + snpEffFormat +
        snpEffDownstream + snpEffIntergenic + snpEffUpstream + snpEffgatk + snpEffTranscript + snpEffHGVS +
        "#----------------------------------------------------------------- canonical -------------------------------------------------------------------------\n"
        "#----------------------------------------------------------------- cosmic ----------------------------------------------------------------------------\n" +
        snpSiftCosmic +
        "#----------------------------------------------------------------- dbsnp -----------------------------------------------------------------------------\n"
        "#----------------------------------------------------------------- indel -----------------------------------------------------------------------------\n" +
        knownIndel1000G + knownIndelMills1000G +
        "#----------------------------------------------------------------- noncanonical ----------------------------------------------------------------------\n"
        "#-----------------------------------------------------------------------------------------------------------------------------------------------------\n"
    )
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 3 --- JSON File
# Generate header for '.json' file.
# Read file to parse and store '.json'  object.
with open(argv[2], "r+") as jsonTARGET:
    jsonOBJ = load(jsonTARGET)
    jsonOBJ['canonical'] = {
           "clusterSpec": "-V -S /bin/bash -o log/vcfAnnotate/canonical -e log/vcfAnnotate/canonical -l h_vmem=10G -pe ncpus 1",
           "jobName": "{rule}_{wildcards.sampleCAN}"
    }
    jsonOBJ['cosmic'] = {
           "clusterSpec": "-V -S /bin/bash -o log/vcfAnnotate/cosmic -e log/vcfAnnotate/cosmic -l h_vmem=10G -pe ncpus 1",
           "jobName": "{rule}_{wildcards.sampleCOS}"
    }
    jsonOBJ['dbsnp'] = {
           "clusterSpec": "-V -S /bin/bash -o log/vcfAnnotate/dbsnp -e log/vcfAnnotate/dbsnp -l h_vmem=10G -pe ncpus 1",
           "jobName": "{rule}_{wildcards.sampleDbSnp}"
    }
    jsonOBJ['indel'] = {
           "clusterSpec": "-V -S /bin/bash -o log/vcfAnnotate/indel -e log/vcfAnnotate/indel -l h_vmem=20G -pe ncpus 1",
           "jobName": "{rule}_{wildcards.sampleIndel}"
    }
    jsonOBJ['noncanonical'] = {
           "clusterSpec": "-V -S /bin/bash -o log/vcfAnnotate/noncanonical -e log/vcfAnnotate/noncanonical -l h_vmem=10G -pe ncpus 1",
           "jobName": "{rule}_{wildcards.sampleNCAN}"
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
        "#    canonical:        Canonical annotation of a '.VCF' file.\n"
        "#    cosmic:           Cosmic annotation of a '.VCF' file.\n"
        "#    dbsnp:            DbSnp annotation of a '.VCF' file.\n"
        "#    indel:            Indel annotation of a '.VCF' file.\n"
        "#    noncanonical:     Noncanonical annotation of a '.VCF' file.\n"
        "#  Files:\n"
        "#    Input:      .vcf\n"
        "#    Output:     .annotate.vcf\n"
        'include: "' + path.dirname(path.realpath(__file__)) + '/' + moduleNAME + '_INCLUDE"\n'
        "#  Required:\n" +
        "#    >vcfUtil:       Utility functions, with a focus on manipulating '.vcf' files (E.g merging, sorted, summarizing) \n"
        '#    @include: "' + path.dirname(path.dirname(path.realpath(__file__))) + '/utils/utils_INCLUDE"\n'
        "#  Call via: \n" +
        "# - Pair Runs (#pairTXT and #pairALL require modules/utils) Via:\n"
        '#pairVCF:          expand("{outputDIR}/{vcfAnnotateDIR}/{sample[1][tumor]}_{sample[1][normal]}.{vcfProgram}.{form[1][varType]}{form[1][annotated]}.vcf", outputDIR=config["outputDIR"], vcfAnnotateDIR=config["vcfAnnotateDIR"], sample=read_table(config["sampleFILE"], " ").iterrows(), vcfProgram=config["vcfProgram"], form=read_table(StringIO(config["sampleFORM"]), " ").iterrows())\n'
        '#pairTXT:          expand("{outputDIR}/{vcfAnnotateDIR}/{sample[1][tumor]}_{sample[1][normal]}.{vcfProgram}.{form[1][varType]}{form[1][annotated]}.txt", outputDIR=config["outputDIR"], vcfAnnotateDIR=config["vcfAnnotateDIR"], sample=read_table(config["sampleFILE"], " ").iterrows(), vcfProgram=config["vcfProgram"], form=read_table(StringIO(config["sampleFORM"]), " ").iterrows())\n'
        '#pairALL:          expand("{outputDIR}/{vcfAnnotateDIR}/all.samples.{vcfProgram}.{form[1][varType]}{form[1][annotated]}.txt", outputDIR=config["outputDIR"], vcfAnnotateDIR=config["vcfAnnotateDIR"], vcfProgram=config["vcfProgram"], form=read_table(StringIO(config["sampleFORM"]), " ").iterrows())\n'
        "# - Single Runs (#singleTXT and #singleALL require  modules/utils) Via:\n"
        '#singleVCF:        expand("{outputDIR}/{vcfAnnotateDIR}/{samples}.{vcfProgram}.{form[1][varType]}{form[1][annotated]}.vcf", outputDIR=config["outputDIR"], vcfAnnotateDIR=config["vcfAnnotateDIR"], samples=config["sample"], vcfProgram=config["vcfProgram"], form=read_table(StringIO(config["sampleFORM"]), " ").iterrows())\n'
        '#singleTXT:        expand("{outputDIR}/{vcfAnnotateDIR}/{samples}.{vcfProgram}.{form[1][varType]}{form[1][annotated]}.txt", outputDIR=config["outputDIR"], vcfAnnotateDIR=config["vcfAnnotateDIR"], samples=config["sample"], vcfProgram=config["vcfProgram"], form=read_table(StringIO(config["sampleFORM"]), " ").iterrows())\n'
        '#singleALL:        expand("{outputDIR}/{vcfAnnotateDIR}/all.samples.{vcfProgram}.{form[1][varType]}{form[1][annotated]}.txt", outputDIR=config["outputDIR"], vcfAnnotateDIR=config["vcfAnnotateDIR"], vcfProgram=config["vcfProgram"],  form=read_table(StringIO(config["sampleFORM"]), " ").iterrows())\n'
        '#-----------------------------------------------------------------------------------------------------------------------------------------------------\n'
    )
#-----------------------------------------------------------------------------------------------------------------------------------------------------
