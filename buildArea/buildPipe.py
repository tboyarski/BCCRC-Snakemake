#---------------------
# Author: tboyarski
# Date: 2017-06-07 @ 10-26 
#---------------------

# Required library to make shell calls.
from subprocess import call

# File names and directories used in build script
TYPE="single"
SAMPLE="input/sampleFILE" + TYPE + ".txt"
CHRTYPE="hncbi"
YAMLFILE="input/config.yaml"
CLUSTERFILE="input/config.json"
SNAKEFILE="Snakefile"
snakeDIR="/Users/tboyarski/Desktop/Tim/BCCRC-Snakemake"


# Call to generate .YAML and Snakefiles with header information.
call('python ' + snakeDIR + '/modules/buildFile/buildFile.py ' + TYPE + ' ' + SAMPLE + ' ' + CHRTYPE + ' ' +  YAMLFILE + ' ' + CLUSTERFILE + ' ' + SNAKEFILE, shell=True)

# Module 1:
call('python ' + snakeDIR + '/modules/utils/utils.py ' + YAMLFILE + ' ' + CLUSTERFILE + ' ' +  SNAKEFILE, shell=True)

# Module 2:
call('python ' + snakeDIR + '/modules/annotateVcf/annotateVcf.py ' + YAMLFILE + ' ' + CLUSTERFILE + ' ' +  SNAKEFILE, shell=True)

# Module 3:
call('python ' + snakeDIR + '/modules/varScan/varScan.py ' + YAMLFILE + ' ' + CLUSTERFILE + ' ' +  SNAKEFILE, shell=True)

# Module 4:
call('python ' + snakeDIR + '/modules/mpileup/mpileup.py ' + YAMLFILE + ' ' + CLUSTERFILE + ' ' +  SNAKEFILE, shell=True)

# Module 5:
call('python ' + snakeDIR + '/modules/processBam/processBam.py ' + YAMLFILE + ' ' + CLUSTERFILE + ' ' +  SNAKEFILE, shell=True)

