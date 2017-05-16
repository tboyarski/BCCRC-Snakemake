#---------------------------------------------------
# Author:   Tim Boyarski                                    
# Date:     2017-03-06                                      
#-----------------------------------------------------------
# Call: call("python " + snakeDIR + "/modules/annotate/annotate.py " + YAMLFILE + " " + CLUSTERFILE + " " + SNAKEFILE, shell=True)
# Input:                                    .vcf            
# Output:                                   .annotate.vcf  
# Purpose: Automate the population of user's pipeline 
#   Snakefile, '.YAML', and '.JSON' files.
#-------------------------------------------------------------------

# Request sys so be able to use CLI arguments
import sys
import json
import os

moduleNAME = "annotate"

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
# Open and append to file the following required paramters.
with open(sys.argv[1], "a+") as yamlTARGET:
    # 2A. Software
    annotate_javaProg="annotate_javaProg: java -Xmx2G\n"
    annotate_snpSiftProg="annotate_snpSiftProg: -jar ~/share/usr/anaconda/4.3.0/envs/CentOS5-APR28-2/share/snpeff-4.1l-0/SnpSift.jar\n"
    annotate_snpEffProg="annotate_snpEffProg: -jar ~/share/usr/anaconda/4.3.0/envs/CentOS5-APR28-2/share/snpeff-4.1l-0/snpEff.jar\n"
    # 2B. Shared variables
    annotateDIR="annotateDIR: annotate\n"
    annotateVerbose="annotateVerbose: -v\n"
    annotateID="annotateID: -id\n"
    annotateDbSnp="annotateDbSnp: ~/share/references/dbsnp/dbsnp_137.hg19.vcf\n"
    # 2C. canonical only variables
    snpEffGenomeVersion="snpEffGenomeVersion: GRCh37.72\n"
    snpEffConfig="snpEffConfig: -c ~/share/usr/anaconda/4.3.0/envs/CentOS5-APR28-2/share/snpeff-4.1l-0/snpEff.config\n"
    snpEffFormat="snpEffFormat: -i vcf\n"
    snpEffHGVS="snpEffHGVS: -hgvs\n"
    snpEffDownstream="snpEffDownstream: -no-downstream\n"
    snpEffIntergenic="snpEffIntergenic: -no-intergenic\n"
    snpEffUpstream="snpEffUpstream: -no-upstream\n"
    snpEffgatk="snpEffgatk: -o gatk\n"
    # 2E. cosmic only variables
    snpSiftCosmic="snpSiftCosmic: ~/share/references/cosmic/CosmicCodingMuts_v68.hg19.fixed.sort.vcf\n"
    # 2F. indel only variables
    knownIndel1000G="knownIndel1000G: ~/share/references/1000g/1000G_phase1.indels.hg19.with_id.vcf\n"
    knownIndelMills1000G="knownIndelMills1000G: ~/share/references/1000g/Mills_and_1000G_gold_standard.indels.hg19.with_id.vcf\n"
    # 2G. snp only variables
    # 2H. Write to file
    yamlTARGET.write("\n\n#################################\n# ----- " + moduleNAME + " Parameters ------ #\n#################################\n")
    yamlTARGET.write("#       -- Software --          #\n" + annotate_javaProg + annotate_snpSiftProg + annotate_snpEffProg)
    yamlTARGET.write("#    -- Shared Variables --     #\n" + annotateDIR + annotateVerbose + annotateID + annotateDbSnp)
    yamlTARGET.write("#   -- canonical Specific --    #\n" + snpEffGenomeVersion + snpEffConfig + snpEffFormat + snpEffHGVS \
            + snpEffDownstream + snpEffIntergenic + snpEffUpstream + snpEffgatk)
    yamlTARGET.write("#     -- cosmic Specific --     #\n" + snpSiftCosmic)
    yamlTARGET.write("#      -- indel Specific --     #\n" + knownIndel1000G + knownIndelMills1000G)
    yamlTARGET.write("#       -- snp Specific --      #\n")
    yamlTARGET.write("#################################\n")

# 3 --- JSON File
# Generate header for '.json' file.
jsonOBJ = {}
# Read file to parse and store '.json'  object.
with open(sys.argv[2], "r+") as jsonTARGET:
    jsonRULE = {}
    jsonOBJ = json.load(jsonTARGET)
    jsonRULE['clusterSpec'] = '-V -S /bin/bash -o log/' + moduleNAME + ' -e log/' + moduleNAME + ' -l h_vmem=10G -pe ncpus 1'
    jsonOBJ["canonical"] = jsonRULE
    jsonOBJ["cosmic"] = jsonRULE
    jsonOBJ["indel"] = jsonRULE
    jsonOBJ["snp"] = jsonRULE
# Recreate JSON file to delete exiting text.
with open(sys.argv[2], "w+") as jsonTARGET:
    json.dump(jsonOBJ, jsonTARGET, indent=4)

# 4 --- Snakefile
# Open and append o file a descriptin and the last rule call.
with open(sys.argv[3], "a+") as pipeTARGET:
    pipeTARGET.write(
        "\n\n#***** " + moduleNAME + " *****\n" +
        "#  Included:\n" +
        "#    " + moduleNAME + ":     Annotation of a '.VCF' file.\n" +
        "#  Files:\n" +
        "#    Input:      .vcf\n" +
        "#    Output:     .annotate.vcf\n" +
        'include: "/home/tboyarski/share/projects/tboyarski/gitRepo-LCR-BCCRC/Snakemake/modules/' + moduleNAME + '/' + moduleNAME + '_INCLUDE"\n' +
        "#  Required: NONE\n" +
        "#  Call via: \n" +
        '#    expand("{outputDIR}/{annotateDIR}/{samples}.BAMjsonYAML", outputDIR=config["outputDIR"], annotateDIR=config["annotateDIR"], samples=config["sample"])\n'
    )
