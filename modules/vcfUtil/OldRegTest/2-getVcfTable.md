# 2-getVcfTable
This pipeline is to exemplify the default operations of this module.

## Setting up the: buildPipe.py
Users must set the following variable:

 * (Line 13) TYPE = "single"

## Setting up the: Snakefile
Users must set the following submodule "call via" input requirements:

 * getVcfTable

## Setting up the: YAML
Users must set the following "input/config.yaml" variables:

 * (Line 15) intermediateKEEP = True

## Setting up the: output directory

 * None

```
input
    /rawBam
        Pfeiffer2.bam
        Pfeiffer3.bam
```
```

## Snakemake cluster run output:
```

## Snakemake dry run output:
```
