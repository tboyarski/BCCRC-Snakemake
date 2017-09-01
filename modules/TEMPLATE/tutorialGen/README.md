# XXXXXXX Module (Snakemake)
This directory contains the XXXXXXX module. It is a single-module system.

## Modules:
See individual files for expanded explanations of their purpose and the manner in which they accomplish it.
* XXXXXXX: Generate ...
* **XXXXXXX_INCLUDE: Master file which includes the modules above.

## Regression Testing:
Most recently on: **June 21st, 2017**

**Directory Prefix = /genesis/extscratch/clc/projects/tboyarski/RegressionTest/1-.../...-**

Please refer the the contained "RegTestREADME" directory for more information about each of the following directories:
    1 = 1-...

Module | Directory Tested Within
:--------: | :--------
moduleName1 | 1
moduleName2 | 1

## Logging:
Will be stored in: "log/XXXXXXX"

## Global Directories:
Module | Argument | Default Value | Description
:--------: | :--------: | :--------: | :--------
 | outputDIR | output | Directory to contain all file generated by the pipeline.
 | inputDIR | input | Directory to contain all files prior to starting pipeline (Reference and input files).
 | bamDIR | bam | Directory to conatin the symlinked and name-normalized '.bam' and '.BAI' files.
 | metricsDIR | metrics | Directory to contain the processed '.metrics' files.

## Global Parameters:
Module | Argument | Default Value | Description
:--------: | :--------: | :--------: | :--------
 | shellCallFile | shellCalls.txt | File to which a copy of all shell calls is printed.
 | offCluster | False | Adds input redirection to end of shell calls as to capture STDERR when not on cluster.
 | intermediateKEEP | False | Remove intermediate files which are not likely to be used after intial processing.
 | fastqKEEP | False | Flag of 'True' or 'False' on retaining '.fastq' files after they are used in the pipeline.
 | refFILE | ../path/to/GRCh37-lite.fa | Absolute path to genomic reference file.
 | chrLIST | ['chr1', ... 'chrY'] OR ['1', ... 'Y'] | List of organism (Human or Mouse) and format (NCBI or UCSC) specific chromosomes

## Module Specific Software
Module | Argument | Default Value | Description
:--------: | :--------: | :--------: | :--------

## Module Specific Paramters:
Module | Argument | Default Value | Description
:--------- | :--------: | :--------: | :--------
xxx | xxx | --p-value 0.05 | xxx
