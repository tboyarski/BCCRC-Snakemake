#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Author:   Tim Boyarski
# Date:     2017-06-14
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Call: call("python " + snakeDIR + "/modules/bamGen/bamGen.py " + YAMLFILE + " " + CLUSTERFILE + " " + SNAKEFILE, shell=True)
#
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
moduleNAME="bamGen"
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
    ruleLIST = ['bamALIGN_bwa',
        'bamALIGN_star',
        'sam2BAM']
    # 1A. Create module directory
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
    bamGen_bwaProg="bamGen_bwaProg: bwa\n"
    bamGen_fastxProg="bamGen_fastxProg: /genesis/extscratch/clc/usr/fastx_toolkit-0.0.13.2/bin/fastx_trimmer\n"
    bamGen_samtoolsProg="bamGen_samtoolsProg: samtools\n"
    bamGen_starProg="bamGen_starProg: STAR\n"
    SoftwareChoiceFLAG_bamALIGN="SoftwareChoiceFLAG_bamALIGN: bwa\n"
    # 2B. Shared variables
    bamGenDIR="bamGenDIR: bamGen\n"
    # 2C. bamALIGN_bwa variables
    bwa_refFILE="bwa_refFILE: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa\n"
    bwa_supportingRefFILE="bwa_supportingRefFILE: ['/genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict', '/genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb', '/genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann', '/genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt', '/genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai', '/genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac', '/genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa']\n"
    picardCompatibility="picardCompatibility: -M\n"
    coreNumber="coreNumber: -t 4\n"
    seqPlatform="seqPlatform: ILLUMINA\n"
    trimReadsFlag="trimReadsFlag: False\n"
    phred64="phred64: -Q 33\n"
    firstBaseToKeep="firstBaseToKeep: -f 1\n"
    lastBaseToKeep="lastBaseToKeep: -l 1\n"
    # 2C. bamALIGN_star variables
    starRefGenomeDIR="starRefGenomeDIR: /genesis/extscratch/clc/references/star/GRCh37/ref_genome.fa.star.idx\n"
    runThreadN="runThreadN: --runThreadN 4\n"
    readFilesCommand="readFilesCommand: --readFilesCommand zcat\n"
    outSAMtype="outSAMtype: --outSAMtype BAM Unsorted\n"
    outSAMunmapped="outSAMunmapped: --outSAMunmapped Within KeepPairs\n"
    quantMode="quantMode: --quantMode GeneCounts\n"
    #sjdbGTFfile="sjdbGTFfile: /genesis/extscratch/clc/references/star/hg19/gencode.v19.annotation.gtf\n"
    sjdbGTFfile="sjdbGTFfile: /genesis/extscratch/clc/references/star/GRCh37/ref_annot.gtf\n"
    chimSegmentMin="chimSegmentMin: --chimSegmentMin 15\n"
    outSAMstrandField="outSAMstrandField: --outSAMstrandField intronMotif\n"
    outputSuffixLIST_star="outputSuffixLIST_star: ['_Chimeric.out.sam','_Log.final.out','_Log.out','_Log.progress.out','_ReadsPerGene.out.tab','_SJ.out.tab']\n"
    # 2C. sam2BAM variables
    sam2BamARGS="sam2BamARGS: ''\n"
    samINDIR="samDIR: xx/sam\n"
    samOUTDIR="samDIR: xx/sam\n"
    # 2D. Write to file
    yamlTARGET.write(
        "\n\n"
        "#####################################\n"
        "# " + moduleNAME + " Parameters\n"
        "#####################################\n"
        "#----------------------------------------------------------------- *Software* ------------------------------------------------------------------------\n" +
        bamGen_bwaProg + bamGen_fastxProg + bamGen_samtoolsProg + bamGen_starProg + SoftwareChoiceFLAG_bamALIGN +
        "#----------------------------------------------------------------- *Shared Variables* ----------------------------------------------------------------\n" +
        bamGenDIR +
        "#----------------------------------------------------------------- bamALIGN_bwa ----------------------------------------------------------------------\n" +
        bwa_refFILE + bwa_supportingRefFILE + picardCompatibility + coreNumber + seqPlatform + trimReadsFlag + phred64 + firstBaseToKeep + lastBaseToKeep +
        "#----------------------------------------------------------------- bamALIGN_star ---------------------------------------------------------------------\n" +
        starRefGenomeDIR + runThreadN + readFilesCommand + outSAMtype + outSAMunmapped + quantMode +
        sjdbGTFfile + chimSegmentMin + outSAMstrandField + outputSuffixLIST_star +
        "#----------------------------------------------------------------- sam2BAM ---------------------------------------------------------------------------\n" +
        sam2BamARGS + samDIR +
        "#-----------------------------------------------------------------------------------------------------------------------------------------------------\n"
    )
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 3 --- JSON File
# Generate header for '.json' file.
# 3A. Read file to parse and store '.json' object.
with open(argv[2], "r+") as jsonTARGET:
    jsonOBJ = load(jsonTARGET)
    jsonOBJ['bamALIGN_bwa'] = {
            "clusterSpec": "-V -S /bin/bash -o log/bamGen/bamALIGN_bwa -e log/bamGen/bamALIGN_bwa -l h_vmem=8G -pe ncpus 2",
            "jobName": "{rule}_{wildcards.sampleBAB}"
    }
    jsonOBJ['bamALIGN_star'] = {
            "clusterSpec": "-V -S /bin/bash -o log/bamGen/bamALIGN_star -e log/bamGen/bamALIGN_star -l h_vmem=8G -pe ncpus 4",
            "jobName": "{rule}_{wildcards.sampleBAS}"
    }
    jsonOBJ['sam2BAM'] = {
            "clusterSpec": "-V -S /bin/bash -o log/bamGen/sam2BAM -e log/bamGen/sam2BAM -l h_vmem=10G -pe ncpus 1",
            "jobName": "{rule}_{wildcards.sampleS2B}"
    }
#3B. Recreate JSON file to delete exiting text.
with open(argv[2], "w+") as jsonTARGET:
    dump(jsonOBJ, jsonTARGET, indent=4)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 4 -- Snakefile
# Open and append to file a descriptin and the last rule call.
with open(argv[3], "a+") as pipeTARGET:
    pipeTARGET.write(
        "\n\n#-----------------------------------------------------------------------------------------------------------------------------------------------------\n"
        "#**** " + moduleNAME + " ****:\n"
        "#  Included:\n"
        "#      bamALIGN_bwa:           Generate a '.bam' file from paired '.fastq' files, via BWA.\n"
        "#      bamALIGN_star:          Generate a '.bam' file from paired '.fastq' files, via STAR.\n"
        "#      sam2BAM:                Generate a '.bam' file from a '.sam' file, via samtools.\n"
        'include: "' + path.dirname(path.realpath(__file__)) + '/' + moduleNAME + '_INCLUDE"\n'
        "#  Required: NONE\n"
        "#  Call via:\n"
        '#bamALIGN_bwa:             expand("{outputDIR}/{bamDIR}/{samples}_Aligned.out.bam", outputDIR=config["outputDIR"], bamDIR=config["bamDIR"], samples=config["sample"]),\n'
        '#bamALIGN_star:            expand("{outputDIR}/{bamDIR}/{samples}_Aligned.out.bam", outputDIR=config["outputDIR"], bamDIR=config["bamDIR"], samples=config["sample"]),\n'
        '#sam2BAM:                  expand("{outputDIR}/{bamDIR}/{samples}.bam", outputDIR=config["outputDIR"], bamDIR=config["bamDIR"], samples=config["sample"]),\n'
        "#-----------------------------------------------------------------------------------------------------------------------------------------------------\n"
    )
#-----------------------------------------------------------------------------------------------------------------------------------------------------
