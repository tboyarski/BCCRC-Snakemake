# 4-sam2BAM
This pipeline is to exemplify the default operations of this module. 

## Setting up the: Snakefile
Users must set the following submodule "call via" input requirements:

 * sam2BAM

## Setting up the: YAML
Users must set the following "input/config.yaml" variables:

 * None

## Setting up the: output directory

 * Ensure that the '.sam' files you are using have @SQ header lines.
    This can be accomplished with the following shell calls:
        $samtools view -H input1.bam > output1.bam  
        $samtools view input1.bam >> output1.bam  

```
output
    /bam
        Pfeiffer2.sam    ~Must have @SQ header line(s)
        Pfeiffer3.sam    ~Must have @SQ header line(s)
```

## Snakemake dry run output:
```
rule sam2BAM:
    input: output/sam/Pfeiffer2.sam
    output: output/bam/Pfeiffer2.bam
    log: log/bamGen/sam2BAM/sam2BAM_Pfeiffer2.2017-08-30.12-49-29.samtools.stderr
    jobid: 1
    wildcards: sampleS2B=Pfeiffer2


rule sam2BAM:
    input: output/sam/Pfeiffer3.sam
    output: output/bam/Pfeiffer3.bam
    log: log/bamGen/sam2BAM/sam2BAM_Pfeiffer3.2017-08-30.12-49-29.samtools.stderr
    jobid: 2
    wildcards: sampleS2B=Pfeiffer3


localrule all:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer3.bam
    jobid: 0

Job counts:
	count	jobs
	1	all
	2	sam2BAM
	3
```
