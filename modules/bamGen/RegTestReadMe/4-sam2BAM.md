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
input
    /rawBam
        Pfeiffer2.sam    ~Must have @SQ header line(s)
        Pfeiffer3.sam    ~Must have @SQ header line(s)
```

## Snakemake dry run output:
```
rule sam2BAM:
    input: input/rawBam/Pfeiffer2.sam
    output: input/rawBam/Pfeiffer2.bam
    log: log/bamGen/sam2BAM/sam2BAM_Pfeiffer2.2017-07-10.10-27-27.samtools.stderr
    jobid: 1
    wildcards: pathS2B=input/rawBam, sampleS2B=Pfeiffer2


rule sam2BAM:
    input: input/rawBam/Pfeiffer3.sam
    output: input/rawBam/Pfeiffer3.bam
    log: log/bamGen/sam2BAM/sam2BAM_Pfeiffer3.2017-07-10.10-27-27.samtools.stderr
    jobid: 2
    wildcards: pathS2B=input/rawBam, sampleS2B=Pfeiffer3


localrule all:
    input: input/rawBam/Pfeiffer2.bam, input/rawBam/Pfeiffer3.bam
    jobid: 0

Job counts:
	count	jobs
	1	all
	2	sam2BAM
	3
```

## Snakemake cluster run output:
```
Provided cluster nodes: 100
Job counts:
    count    jobs
    1    all
    2    sam2BAM
    3

rule sam2BAM:
    input: input/rawBam/Pfeiffer2.sam
    output: input/rawBam/Pfeiffer2.bam
    log: log/bamGen/sam2BAM/sam2BAM_Pfeiffer2.2017-07-10.10-27-31.samtools.stderr
    jobid: 1
    wildcards: sampleS2B=Pfeiffer2, pathS2B=input/rawBam

Submitted DRMAA job (jobid 8877496)

rule sam2BAM:
    input: input/rawBam/Pfeiffer3.sam
    output: input/rawBam/Pfeiffer3.bam
    log: log/bamGen/sam2BAM/sam2BAM_Pfeiffer3.2017-07-10.10-27-31.samtools.stderr
    jobid: 2
    wildcards: sampleS2B=Pfeiffer3, pathS2B=input/rawBam

Submitted DRMAA job (jobid 8877497)
Finished job 2.
1 of 3 steps (33%) done
Finished job 1.
2 of 3 steps (67%) done

localrule all:
    input: input/rawBam/Pfeiffer2.bam, input/rawBam/Pfeiffer3.bam
    jobid: 0

Finished job 0.
3 of 3 steps (100%) done

real    0m36.387s
user    0m0.997s
sys    0m0.200s
```
