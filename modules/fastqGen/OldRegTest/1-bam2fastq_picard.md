# 1-bam2fastq_picard
This pipeline is to exemplify the default operations of this module. Techincally it requires
the fastqUtil module as well, since it contains the rule 'mergeFASTQ', which bam2fastq_picard
competes with. They both create the same output. 

## Setting up the: Snakefile
Users must set the following submodule "call via" input requirements:

 * bam2fastq

## Setting up the: YAML
Users must set the following "input/config.yaml" variables:

 * None

## Setting up the: output directory

 * None

```
input/
    /rawBam
        Pfeiffer2.bam
        Pfeiffer3.bam
```

## Snakemake dry run output:
```
