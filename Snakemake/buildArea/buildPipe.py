# Required library to make shell calls.
from subprocess import call

# File names and directories used in build script
SAMPLE="input/sampleFILE.txt"
YAMLFILE="input/config.yaml"
CLUSTERFILE="input/config.json"
SNAKEFILE="Snakefile"
snakeDIR="~/share/projects/tboyarski/gitRepo-LCR-BCCRC/Snakemake"

# Call to generate .YAML and Snakefiles with header information.
call("python " + snakeDIR + "/modules/buildFile/buildFile.py single " + SAMPLE + " " +  YAMLFILE + " " + CLUSTERFILE + " " + SNAKEFILE, shell=True)

# Call to populate the .YAML with paramters and the Snakefile with rules.
call("python " + snakeDIR + "/modules/reBam/reBam.py " + YAMLFILE + " " + CLUSTERFILE + " " + SNAKEFILE, shell=True)

# Call to generate MPileUp files from previously created BAM files.
call("python " + snakeDIR + "/modules/mPile/mPile.py " + YAMLFILE + " " + CLUSTERFILE + " " + SNAKEFILE, shell=True)

# Call to generate varScan.snps.vcf files from previously created mpileu files.
call("python " + snakeDIR + "/modules/varScan/varScan.py " + YAMLFILE + " " + CLUSTERFILE + " " + SNAKEFILE, shell=True)

# Call to generate varScan.snps.vcf files from previously created mpileu files.
call("python " + snakeDIR + "/modules/muTect/muTect.py " + YAMLFILE + " " + CLUSTERFILE + " " + SNAKEFILE, shell=True)
