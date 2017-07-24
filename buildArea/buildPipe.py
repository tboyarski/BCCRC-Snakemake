#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Author: tboyarski
# Date: 2017-07-10 @ 11-47
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# PYTHON PACKAGES #
#-------------------
# Required library to make shell calls.
from subprocess import call
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# LOCAL VARIABLES #
#-------------------
# Formatting of the sample file.
TYPE="single"

# Creating a relative variable for the sample file.
SAMPLE="input/sampleFILE" + TYPE + ".txt"

# Store the absolute path of the reference genome file.
REFFILE="/genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa"

# Path and name of the YAML Snakemake pipeline configuration file.
YAMLFILE="input/config.yaml"

# Path and name of the JSON Snakemake pipeline cluster configuration file.
CLUSTERFILE="input/config.json"

# Path and name of the Snakefile for respective pipeline project.
SNAKEFILE="Snakefile"

# Absolute directory for the Snakemake code repository.
snakeDIR="/extscratch/clc/projects/tboyarski/gitRepo-LCR-BCCRC/Snakemake"
#-----------------------------------------------------------------------------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# PYTHON SCRIPT #
#--------------------
# Module 0:  Call to generate .YAML and Snakefiles with header information.
call('python ' + snakeDIR + '/modules/py_buildFile/buildFile.py ' + TYPE + ' ' + SAMPLE + ' ' + REFFILE + ' ' +  YAMLFILE + ' ' + CLUSTERFILE + ' ' + SNAKEFILE, shell=True)

# Module 1:
call('python ' + snakeDIR + '/modules/genericUtil/genericUtil.py ' + YAMLFILE + ' ' + CLUSTERFILE + ' ' +  SNAKEFILE, shell=True)

# Module 2:
call('python ' + snakeDIR + '/modules/vcfAnnotate/vcfAnnotate.py ' + YAMLFILE + ' ' + CLUSTERFILE + ' ' +  SNAKEFILE, shell=True)

# Module 3:
call('python ' + snakeDIR + '/modules/vcfUtil/vcfUtil.py ' + YAMLFILE + ' ' + CLUSTERFILE + ' ' +  SNAKEFILE, shell=True)

# Module 4:
call('python ' + snakeDIR + '/modules/vcfGenUtil_varScan/vcfGenUtil_varScan.py ' + YAMLFILE + ' ' + CLUSTERFILE + ' ' +  SNAKEFILE, shell=True)

# Module 5:
call('python ' + snakeDIR + '/modules/mpileupGen/mpileupGen.py ' + YAMLFILE + ' ' + CLUSTERFILE + ' ' +  SNAKEFILE, shell=True)

# Module 6:
call('python ' + snakeDIR + '/modules/bamUtil/bamUtil.py ' + YAMLFILE + ' ' + CLUSTERFILE + ' ' +  SNAKEFILE, shell=True)

# Module 7:
call('python ' + snakeDIR + '/modules/bamGen/bamGen.py ' + YAMLFILE + ' ' + CLUSTERFILE + ' ' +  SNAKEFILE, shell=True)

# Module 8:
call('python ' + snakeDIR + '/modules/fastqUtil/fastqUtil.py ' + YAMLFILE + ' ' + CLUSTERFILE + ' ' +  SNAKEFILE, shell=True)

# Module 9:
call('python ' + snakeDIR + '/modules/fastqGen/fastqGen.py ' + YAMLFILE + ' ' + CLUSTERFILE + ' ' +  SNAKEFILE, shell=True)

# Module 10:
call('python ' + snakeDIR + '/modules/bamMetrics/bamMetrics.py ' + YAMLFILE + ' ' + CLUSTERFILE + ' ' +  SNAKEFILE, shell=True)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
