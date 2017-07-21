# 1-fastqc
This pipeline is to exemplify the default operations of this module. 

## Setting up the: Snakefile
Users must set the following submodule "call via" input requirements:

 * fastqc

## Setting up the: YAML
Users must set the following "input/config.yaml" variables:

 * None

## Setting up the: output directory

 * Copy the directory "outputBACKUP" and name it "output". Structure should be as seen below:

```
output
    /bam
        Pfeiffer2.bam
        Pfeiffer3.bam
```

## Snakemake dry run output:
```
rule fastqc:
    input: output/bam/Pfeiffer3.bam
    output: output/fastqc/Pfeiffer3_fastqc.zip
    log: log/fastqUtil/fastqc/fastqc_Pfeiffer3.2017-06-30.13-17-39.stderr
    jobid: 1
    wildcards: sampleFQC=Pfeiffer3, outputDIR=output


rule fastqc:
    input: output/bam/Pfeiffer2.bam
    output: output/fastqc/Pfeiffer2_fastqc.zip
    log: log/fastqUtil/fastqc/fastqc_Pfeiffer2.2017-06-30.13-17-39.stderr
    jobid: 2
    wildcards: sampleFQC=Pfeiffer2, outputDIR=output


localrule all:
    input: output/fastqc/Pfeiffer2_fastqc.zip, output/fastqc/Pfeiffer3_fastqc.zip
    jobid: 0

Job counts:
	count	jobs
	1	all
	2	fastqc
	3
```

## Snakemake cluster run output:
```
Job counts:
    count    jobs
    1    all
    2    fastqc
    3

rule fastqc:
    input: output/bam/Pfeiffer2.bam
    output: output/fastqc/Pfeiffer2_fastqc.zip
    log: log/fastqUtil/fastqc/fastqc_Pfeiffer2.2017-06-30.13-17-58.stderr
    jobid: 1
    wildcards: outputDIR=output, sampleFQC=Pfeiffer2

Submitted DRMAA job (jobid 8621996)

rule fastqc:
    input: output/bam/Pfeiffer3.bam
    output: output/fastqc/Pfeiffer3_fastqc.zip
    log: log/fastqUtil/fastqc/fastqc_Pfeiffer3.2017-06-30.13-17-58.stderr
    jobid: 2
    wildcards: outputDIR=output, sampleFQC=Pfeiffer3

Submitted DRMAA job (jobid 8621997)
Finished job 1.
1 of 3 steps (33%) done
Finished job 2.
2 of 3 steps (67%) done

localrule all:
    input: output/fastqc/Pfeiffer2_fastqc.zip, output/fastqc/Pfeiffer3_fastqc.zip
    jobid: 0

Finished job 0.
3 of 3 steps (100%) done
```
