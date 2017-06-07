# Required library to make shell calls.
from subprocess import call

# File names and directories used in build script
TYPE="single"
SAMPLE="input/sampleFILE" + TYPE + ".txt"
CHRTYPE="hncbi"
YAMLFILE="input/config.yaml"
CLUSTERFILE="input/config.json"
SNAKEFILE="Snakefile"
