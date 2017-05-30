#-------------------------------------------------------------------------------------------------------
# Author:   Tim Boyarski
# Date:     2017-05-26
#-------------------------------------------------------------------------------------------------------
# Call: call("python " + snakeDIR + "/modules/annotateVcf/annotateVcf.py " + YAMLFILE + " " + CLUSTERFILE + " " + SNAKEFILE, shell=True)
# Input:                                    .vcf
# Output:                                   .annotate.vcf
# Purpose: Automate the population of user's pipeline
#   Snakefile, '.YAML', and '.JSON' files.
#-------------------------------------------------------------------------------------------------------

# Request sys so be able to use CLI arguments
import sys
import json
import os

moduleNAME = "annotateVcf"

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
    os.mkdir("log")
    print(moduleNAME + ".py \tCreating: log/")
if (os.path.isdir("log/" + moduleNAME) != True):

    # Maintain this list of active submodules.
    moduleLIST = ['canonical', 'cosmic', 'indel', 'dbsnp', 'noncanonical']

    # 1A. Create module directory.
    os.mkdir("log/" + moduleNAME)
    print(moduleNAME + ".py \tCreating: log/" + moduleNAME)

    # 1B. Create submodule directories and report to user.q
    for module in moduleLIST:
        os.mkdir("log/" + moduleNAME + "/" + module)
        print(moduleNAME + ".py \tCreating: log/" + moduleNAME + "/" + module + "/")


# 2 --- YAML File
# Open and append to file the following required paramters.
with open(sys.argv[1], "a+") as yamlTARGET:
    # 2A. Software
    annotateVcf_javaProg="annotateVcf_javaProg: java -Xmx2G\n"
    annotateVcf_snpSiftProg="annotateVcf_snpSiftProg: -jar ~/share/usr/anaconda/4.3.0/envs/CentOS5-APR28-2/share/snpeff-4.1l-0/SnpSift.jar\n"
    annotateVcf_snpEffProg="annotateVcf_snpEffProg: -jar ~/share/usr/anaconda/4.3.0/envs/CentOS5-APR28-2/share/snpeff-4.1l-0/snpEff.jar\n"
    # 2B. Shared variables
    sampleFORM='sampleFORM: "varType annotated\\nsnp .canonical_annotated.dbsnp_annotated.cosmic_annotated\\n' \
        + 'indel .canonical_annotated.indel_annotated\\n"\n'
    annotateVcfDIR="annotateVcfDIR: annotateVcf\n"
    annotateVerbose="annotateVerbose: -v\n"
    annotateID="annotateID: -id\n"
    annotateDbSnp="annotateDbSnp: ~/share/references/dbsnp/dbsnp_137.hg19.vcf\n"
    snpEffGenomeVersion="snpEffGenomeVersion: GRCh37.72\n"
    snpEffConfig="snpEffConfig: -c ~/share/usr/anaconda/4.3.0/envs/CentOS5-APR28-2/share/snpeff-4.1l-0/snpEff.config\n"
    snpEffFormat="snpEffFormat: -i vcf\n"
    snpEffDownstream="snpEffDownstream: -no-downstream\n"
    snpEffIntergenic="snpEffIntergenic: -no-intergenic\n"
    snpEffUpstream="snpEffUpstream: -no-upstream\n"
    snpEffgatk="snpEffgatk: -o gatk\n"
    snpEffTranscript="snpEffTranscript: ''\n"
    snpEffHGVS="snpEffHGVS: -hgvs\n"
    # 2C. canonical variables
    # 2D. cosmic variables
    snpSiftCosmic="snpSiftCosmic: ~/share/references/cosmic/CosmicCodingMuts_v68.hg19.fixed.sort.vcf\n"
    # 2E. dbsnp variables
    # 2F. indel variables
    knownIndel1000G="knownIndel1000G: ~/share/references/1000g/1000G_phase1.indels.hg19.with_id.vcf\n"
    knownIndelMills1000G="knownIndelMills1000G: ~/share/references/1000g/Mills_and_1000G_gold_standard.indels.hg19.with_id.vcf\n"
    # 2G. noncanonical variables
    # 2H. Write to file
    yamlTARGET.write("\n\n#################################\n# ----- " + moduleNAME + " Parameters ------ #\n#################################\n")
    yamlTARGET.write("#       -- Software --          #\n" + annotateVcf_javaProg + annotateVcf_snpSiftProg + annotateVcf_snpEffProg)
    yamlTARGET.write("#    -- Shared Variables --     #\n" + sampleFORM + annotateVcfDIR + annotateVerbose + annotateID + annotateDbSnp \
            + snpEffGenomeVersion + snpEffConfig + snpEffFormat \
            + snpEffDownstream + snpEffIntergenic + snpEffUpstream + snpEffgatk \
            + snpEffgatk + snpEffTranscript + snpEffHGVS)
    yamlTARGET.write("#   -- canonical Specific --    #\n")
    yamlTARGET.write("#     -- cosmic Specific --     #\n" + snpSiftCosmic)
    yamlTARGET.write("#     -- dbsnp Specific --      #\n")
    yamlTARGET.write("#      -- indel Specific --     #\n" + knownIndel1000G + knownIndelMills1000G)
    yamlTARGET.write("# -- noncanonical Specific --   #\n")
    yamlTARGET.write("#################################\n")




# 3 --- JSON File
# Generate header for '.json' file.
# Read file to parse and store '.json'  object.
with open(sys.argv[2], "r+") as jsonTARGET:
    jsonOBJ = json.load(jsonTARGET)
    jsonOBJ['canonical'] = {
           "clusterSpec": "-V -S /bin/bash -o log/annotateVcf/canonical -e log/annotateVcf/canonical -l h_vmem=10G -pe ncpus 1",
           "jobName": "{rule}_{wildcards.sampleCAN}"
    }
    jsonOBJ['cosmic'] = {
           "clusterSpec": "-V -S /bin/bash -o log/annotateVcf/cosmic -e log/annotateVcf/cosmic -l h_vmem=10G -pe ncpus 1",
           "jobName": "{rule}_{wildcards.sampleCOS}"
    }
    jsonOBJ['dbsnp'] = {
           "clusterSpec": "-V -S /bin/bash -o log/annotateVcf/dbsnp -e log/annotateVcf/dbsnp -l h_vmem=10G -pe ncpus 1",
           "jobName": "{rule}_{wildcards.sampleDbSnp}"
    }
    jsonOBJ['indel'] = {
           "clusterSpec": "-V -S /bin/bash -o log/annotateVcf/indel -e log/annotateVcf/indel -l h_vmem=20G -pe ncpus 1",
           "jobName": "{rule}_{wildcards.sampleIndel}"
    }
    jsonOBJ['noncanonical'] = {
           "clusterSpec": "-V -S /bin/bash -o log/annotateVcf/noncanonical -e log/annotateVcf/noncanonical -l h_vmem=10G -pe ncpus 1",
           "jobName": "{rule}_{wildcards.sampleNCAN}"
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
        "#    canonical: Canonical annotation of a '.VCF' file.\n" +
        "#    cosmic: Cosmic annotation of a '.VCF' file.\n" +
        "#    dbsnp: DbSnp annotation of a '.VCF' file.\n" +
        "#    indel: Indel annotation of a '.VCF' file.\n" +
        "#    noncanonical: Noncanonical annotation of a '.VCF' file.\n" +
        "#  Files:\n" +
        "#    Input:      .vcf\n" +
        "#    Output:     .annotate.vcf\n" +
        'include: "' + os.path.dirname(os.getcwd()) + '/modules/' + moduleNAME + '/' + moduleNAME + '_INCLUDE"\n' +
        "#  Required: NONE\n" +
        "#  Call via: \n" +
        '#    expand("{outputDIR}/{annotateVcfDIR}/{samples}.canonical_annotated.vcf", outputDIR=config["outputDIR"], annotateVcfDIR=config["annotateVcfDIR"], samples=config["sample"])\n'+
        '#    expand("{outputDIR}/{annotateVcfDIR}/{samples}.cosmic_annotated.vcf", outputDIR=config["outputDIR"], annotateVcfDIR=config["annotateVcfDIR"], samples=config["sample"])\n'+
        '#    expand("{outputDIR}/{annotateVcfDIR}/{samples}.dbsnp_annotated.vcf", outputDIR=config["outputDIR"], annotateVcfDIR=config["annotateVcfDIR"], samples=config["sample"])\n'+
        '#    expand("{outputDIR}/{annotateVcfDIR}/{samples}.indel_annotated.vcf", outputDIR=config["outputDIR"], annotateVcfDIR=config["annotateVcfDIR"], samples=config["sample"])\n'+
        '#    expand("{outputDIR}/{annotateVcfDIR}/{samples}.noncanonical_annotated.vcf", outputDIR=config["outputDIR"], annotateVcfDIR=config["annotateVcfDIR"], samples=config["sample"])\n'
    )
