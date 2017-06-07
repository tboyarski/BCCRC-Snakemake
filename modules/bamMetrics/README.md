#   Module (Snakemake)
This directory contains the templates for building modules or following the Tutorial Vignette (tPile).

## Modules:
See individual files for expanded explanations of their purpose and the manner in which they accomplish it.
* XXXXXXA: Description
* XXXXXXB: Description
* **XXXXXX_INCLUDE: Description

## Logging:
Will be stored in: "log/XXXXXX"

## Global Directories:
* inputDIR = Directory to contain all files prior to starting pipeline.
* refDIR = Directory to contain the reference genome file.
* outputDIR = Directory to contain all file generated by the pipeline
* bamDIR = Directory to contain the '.BAM' files.
* XXXXXXDIR = Directory to contain the '.XXXXXX' file.

## Global Paramters:
Module | Argument | Default Value | Description
:--------: | :--------: | :--------: | :--------
All | refFILE | GRCh37-lite.fa | Name of the reference genome file in the refDIR directory.

## Module Specific Paramters:
Module | Argument | Default Value | Description
:--------- | :--------: | :--------: | :--------
xxx | xxx | --p-value 0.05 | xxx