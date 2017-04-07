#!/bin/sh
_SNAKEFILE="Snakefile"
_YAMLFILE="NewYaml.yaml"
python fileParse/fileParse.py line SampleSingleLines.txt NewYaml.yaml Snakefile
python ReBam/ReBam.py NewYaml.yaml Snakefile
