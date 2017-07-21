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
rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer3.bam
    output: output/fastq/Pfeiffer3.1.fastq, output/fastq/Pfeiffer3.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-06-30.09-04-26.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-06-30.09-04-26.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-06-30.09-04-26.vendor_failed_reads.log
    jobid: 1
    wildcards: sampleB2FP=Pfeiffer3


rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer2.bam
    output: output/fastq/Pfeiffer2.1.fastq, output/fastq/Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-06-30.09-04-26.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-06-30.09-04-26.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-06-30.09-04-26.vendor_failed_reads.log
    jobid: 2
    wildcards: sampleB2FP=Pfeiffer2


localrule all:
    input: output/fastq/Pfeiffer2.1.fastq, output/fastq/Pfeiffer2.2.fastq, output/fastq/Pfeiffer3.1.fastq, output/fastq/Pfeiffer3.2.fastq
    jobid: 0

Job counts:
    count    jobs
    1    all
    2    bam2fastq_picard
    3

real    0m1.603s
user    0m0.810s
sys    0m0.184s
```

## Snakemake cluster run output:
```
Provided cluster nodes: 100
Job counts:
    count    jobs
    1    all
    2    bam2fastq_picard
    3

rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer3.bam
    output: output/fastq/Pfeiffer3.1.fastq, output/fastq/Pfeiffer3.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-06-30.09-05-19.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-06-30.09-05-19.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-06-30.09-05-19.namesort.stderr
    jobid: 1
    wildcards: sampleB2FP=Pfeiffer3

Submitted DRMAA job (jobid 8615277)

rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer2.bam
    output: output/fastq/Pfeiffer2.1.fastq, output/fastq/Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-06-30.09-05-19.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-06-30.09-05-19.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-06-30.09-05-19.namesort.stderr
    jobid: 2
    wildcards: sampleB2FP=Pfeiffer2

Submitted DRMAA job (jobid 8615278)
Finished job 1.
1 of 3 steps (33%) done
Finished job 2.
2 of 3 steps (67%) done

localrule all:
    input: output/fastq/Pfeiffer2.1.fastq, output/fastq/Pfeiffer2.2.fastq, output/fastq/Pfeiffer3.1.fastq, output/fastq/Pfeiffer3.2.fastq
    jobid: 0

Finished job 0.
3 of 3 steps (100%) done
```
