# 2-fastq2GZ_mergeFASTQ
This pipeline is to exemplify the default operations of this module. 

## Setting up the: Snakefile
Users must set the following submodule "call via" input requirements:

 * mergeFASTQ

## Setting up the: YAML
Users must set the following "input/config.yaml" variables:

 * None

## Setting up the: output directory

 * None

```
input/
    /rawBam
        Part1-Pfeiffer2.bam
        Part2-Pfeiffer2.bam
        Part3-Pfeiffer2.bam
        Part4-Pfeiffer2.bam
        Part1-Pfeiffer3.bam
        Part2-Pfeiffer3.bam
        Part3-Pfeiffer3.bam
```

## Snakemake dry run output:
```
rule bam2fastq_picard:
    input: input/rawBam/Part2-Pfeiffer3.bam
    output: output/fastq/Part2-Pfeiffer3.1.fastq, output/fastq/Part2-Pfeiffer3.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part2-Pfeiffer3.2017-06-30.13-36-04.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part2-Pfeiffer3.2017-06-30.13-36-04.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part2-Pfeiffer3.2017-06-30.13-36-04.vendor_failed_reads.log
    jobid: 20
    wildcards: sampleB2FP=Part2-Pfeiffer3


rule bam2fastq_picard:
    input: input/rawBam/Part4-Pfeiffer2.bam
    output: output/fastq/Part4-Pfeiffer2.1.fastq, output/fastq/Part4-Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part4-Pfeiffer2.2017-06-30.13-36-04.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part4-Pfeiffer2.2017-06-30.13-36-04.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part4-Pfeiffer2.2017-06-30.13-36-04.vendor_failed_reads.log
    jobid: 22
    wildcards: sampleB2FP=Part4-Pfeiffer2


rule bam2fastq_picard:
    input: input/rawBam/Part3-Pfeiffer3.bam
    output: output/fastq/Part3-Pfeiffer3.1.fastq, output/fastq/Part3-Pfeiffer3.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part3-Pfeiffer3.2017-06-30.13-36-04.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part3-Pfeiffer3.2017-06-30.13-36-04.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part3-Pfeiffer3.2017-06-30.13-36-04.vendor_failed_reads.log
    jobid: 21
    wildcards: sampleB2FP=Part3-Pfeiffer3


rule bam2fastq_picard:
    input: input/rawBam/Part2-Pfeiffer2.bam
    output: output/fastq/Part2-Pfeiffer2.1.fastq, output/fastq/Part2-Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part2-Pfeiffer2.2017-06-30.13-36-04.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part2-Pfeiffer2.2017-06-30.13-36-04.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part2-Pfeiffer2.2017-06-30.13-36-04.vendor_failed_reads.log
    jobid: 24
    wildcards: sampleB2FP=Part2-Pfeiffer2


rule bam2fastq_picard:
    input: input/rawBam/Part1-Pfeiffer3.bam
    output: output/fastq/Part1-Pfeiffer3.1.fastq, output/fastq/Part1-Pfeiffer3.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part1-Pfeiffer3.2017-06-30.13-36-04.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part1-Pfeiffer3.2017-06-30.13-36-04.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part1-Pfeiffer3.2017-06-30.13-36-04.vendor_failed_reads.log
    jobid: 19
    wildcards: sampleB2FP=Part1-Pfeiffer3


rule bam2fastq_picard:
    input: input/rawBam/Part3-Pfeiffer2.bam
    output: output/fastq/Part3-Pfeiffer2.1.fastq, output/fastq/Part3-Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part3-Pfeiffer2.2017-06-30.13-36-04.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part3-Pfeiffer2.2017-06-30.13-36-04.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part3-Pfeiffer2.2017-06-30.13-36-04.vendor_failed_reads.log
    jobid: 23
    wildcards: sampleB2FP=Part3-Pfeiffer2


rule bam2fastq_picard:
    input: input/rawBam/Part1-Pfeiffer2.bam
    output: output/fastq/Part1-Pfeiffer2.1.fastq, output/fastq/Part1-Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part1-Pfeiffer2.2017-06-30.13-36-04.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part1-Pfeiffer2.2017-06-30.13-36-04.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part1-Pfeiffer2.2017-06-30.13-36-04.vendor_failed_reads.log
    jobid: 25
    wildcards: sampleB2FP=Part1-Pfeiffer2


rule fastq2GZ:
    input: output/fastq/Part2-Pfeiffer3.2.fastq
    output: output/fastq/Part2-Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part2-Pfeiffer3.2.2017-06-30.13-36-04.stderr
    jobid: 18
    wildcards: sampleFGZ=Part2-Pfeiffer3.2, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Part4-Pfeiffer2.2.fastq
    output: output/fastq/Part4-Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part4-Pfeiffer2.2.2017-06-30.13-36-04.stderr
    jobid: 8
    wildcards: sampleFGZ=Part4-Pfeiffer2.2, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Part1-Pfeiffer2.1.fastq
    output: output/fastq/Part1-Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part1-Pfeiffer2.1.2017-06-30.13-36-04.stderr
    jobid: 13
    wildcards: sampleFGZ=Part1-Pfeiffer2.1, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Part1-Pfeiffer2.2.fastq
    output: output/fastq/Part1-Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part1-Pfeiffer2.2.2017-06-30.13-36-04.stderr
    jobid: 11
    wildcards: sampleFGZ=Part1-Pfeiffer2.2, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Part2-Pfeiffer3.1.fastq
    output: output/fastq/Part2-Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part2-Pfeiffer3.1.2017-06-30.13-36-04.stderr
    jobid: 6
    wildcards: sampleFGZ=Part2-Pfeiffer3.1, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Part3-Pfeiffer2.2.fastq
    output: output/fastq/Part3-Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part3-Pfeiffer2.2.2017-06-30.13-36-04.stderr
    jobid: 9
    wildcards: sampleFGZ=Part3-Pfeiffer2.2, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Part1-Pfeiffer3.1.fastq
    output: output/fastq/Part1-Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part1-Pfeiffer3.1.2017-06-30.13-36-04.stderr
    jobid: 5
    wildcards: sampleFGZ=Part1-Pfeiffer3.1, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Part3-Pfeiffer3.2.fastq
    output: output/fastq/Part3-Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part3-Pfeiffer3.2.2017-06-30.13-36-04.stderr
    jobid: 16
    wildcards: sampleFGZ=Part3-Pfeiffer3.2, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Part4-Pfeiffer2.1.fastq
    output: output/fastq/Part4-Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part4-Pfeiffer2.1.2017-06-30.13-36-04.stderr
    jobid: 12
    wildcards: sampleFGZ=Part4-Pfeiffer2.1, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Part2-Pfeiffer2.1.fastq
    output: output/fastq/Part2-Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part2-Pfeiffer2.1.2017-06-30.13-36-04.stderr
    jobid: 15
    wildcards: sampleFGZ=Part2-Pfeiffer2.1, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Part2-Pfeiffer2.2.fastq
    output: output/fastq/Part2-Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part2-Pfeiffer2.2.2017-06-30.13-36-04.stderr
    jobid: 10
    wildcards: sampleFGZ=Part2-Pfeiffer2.2, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Part3-Pfeiffer2.1.fastq
    output: output/fastq/Part3-Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part3-Pfeiffer2.1.2017-06-30.13-36-04.stderr
    jobid: 14
    wildcards: sampleFGZ=Part3-Pfeiffer2.1, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Part1-Pfeiffer3.2.fastq
    output: output/fastq/Part1-Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part1-Pfeiffer3.2.2017-06-30.13-36-04.stderr
    jobid: 17
    wildcards: sampleFGZ=Part1-Pfeiffer3.2, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Part3-Pfeiffer3.1.fastq
    output: output/fastq/Part3-Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part3-Pfeiffer3.1.2017-06-30.13-36-04.stderr
    jobid: 7
    wildcards: sampleFGZ=Part3-Pfeiffer3.1, pathFGZ=output/fastq


rule mergeFASTQ:
    input: output/fastq/Part1-Pfeiffer2.1.fastq.gz, output/fastq/Part2-Pfeiffer2.1.fastq.gz, output/fastq/Part3-Pfeiffer2.1.fastq.gz, output/fastq/Part4-Pfeiffer2.1.fastq.gz
    output: output/fastq/Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/mergeFASTQ_PairedReadGz/mergeFASTQ_PairedReadGz_Pfeiffer2..1.2017-06-30.13-36-04.stderr
    jobid: 3
    wildcards: sampleFM=Pfeiffer2, readDirection=.1, compressionSuffix=.gz


rule mergeFASTQ:
    input: output/fastq/Part1-Pfeiffer2.2.fastq.gz, output/fastq/Part2-Pfeiffer2.2.fastq.gz, output/fastq/Part3-Pfeiffer2.2.fastq.gz, output/fastq/Part4-Pfeiffer2.2.fastq.gz
    output: output/fastq/Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/mergeFASTQ_PairedReadGz/mergeFASTQ_PairedReadGz_Pfeiffer2..2.2017-06-30.13-36-04.stderr
    jobid: 2
    wildcards: sampleFM=Pfeiffer2, readDirection=.2, compressionSuffix=.gz


rule mergeFASTQ:
    input: output/fastq/Part1-Pfeiffer3.1.fastq.gz, output/fastq/Part2-Pfeiffer3.1.fastq.gz, output/fastq/Part3-Pfeiffer3.1.fastq.gz
    output: output/fastq/Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/mergeFASTQ_PairedReadGz/mergeFASTQ_PairedReadGz_Pfeiffer3..1.2017-06-30.13-36-04.stderr
    jobid: 1
    wildcards: sampleFM=Pfeiffer3, readDirection=.1, compressionSuffix=.gz


rule mergeFASTQ:
    input: output/fastq/Part1-Pfeiffer3.2.fastq.gz, output/fastq/Part2-Pfeiffer3.2.fastq.gz, output/fastq/Part3-Pfeiffer3.2.fastq.gz
    output: output/fastq/Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/mergeFASTQ_PairedReadGz/mergeFASTQ_PairedReadGz_Pfeiffer3..2.2017-06-30.13-36-04.stderr
    jobid: 4
    wildcards: sampleFM=Pfeiffer3, readDirection=.2, compressionSuffix=.gz


localrule all:
    input: output/fastq/Pfeiffer2.1.fastq.gz, output/fastq/Pfeiffer3.1.fastq.gz, output/fastq/Pfeiffer2.2.fastq.gz, output/fastq/Pfeiffer3.2.fastq.gz
    jobid: 0

Job counts:
	count	jobs
	1	all
	7	bam2fastq_picard
	14	fastq2GZ
	4	mergeFASTQ
	26
```

## Snakemake cluster run output:
```
Provided cluster nodes: 100
Job counts:
    count    jobs
    1    all
    7    bam2fastq_picard
    14    fastq2GZ
    4    mergeFASTQ
    26

rule bam2fastq_picard:
    input: input/rawBam/Part3-Pfeiffer3.bam
    output: output/fastq/Part3-Pfeiffer3.1.fastq, output/fastq/Part3-Pfeiffer3.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part3-Pfeiffer3.2017-06-30.13-36-49.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part3-Pfeiffer3.2017-06-30.13-36-49.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part3-Pfeiffer3.2017-06-30.13-36-49.namesort.stderr
    jobid: 25
    wildcards: sampleB2FP=Part3-Pfeiffer3

Submitted DRMAA job (jobid 8622639)

rule bam2fastq_picard:
    input: input/rawBam/Part4-Pfeiffer2.bam
    output: output/fastq/Part4-Pfeiffer2.1.fastq, output/fastq/Part4-Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part4-Pfeiffer2.2017-06-30.13-36-49.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part4-Pfeiffer2.2017-06-30.13-36-49.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part4-Pfeiffer2.2017-06-30.13-36-49.namesort.stderr
    jobid: 21
    wildcards: sampleB2FP=Part4-Pfeiffer2

Submitted DRMAA job (jobid 8622640)

rule bam2fastq_picard:
    input: input/rawBam/Part3-Pfeiffer2.bam
    output: output/fastq/Part3-Pfeiffer2.1.fastq, output/fastq/Part3-Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part3-Pfeiffer2.2017-06-30.13-36-49.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part3-Pfeiffer2.2017-06-30.13-36-49.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part3-Pfeiffer2.2017-06-30.13-36-49.namesort.stderr
    jobid: 19
    wildcards: sampleB2FP=Part3-Pfeiffer2

Submitted DRMAA job (jobid 8622641)

rule bam2fastq_picard:
    input: input/rawBam/Part2-Pfeiffer2.bam
    output: output/fastq/Part2-Pfeiffer2.1.fastq, output/fastq/Part2-Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part2-Pfeiffer2.2017-06-30.13-36-49.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part2-Pfeiffer2.2017-06-30.13-36-49.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part2-Pfeiffer2.2017-06-30.13-36-49.namesort.stderr
    jobid: 20
    wildcards: sampleB2FP=Part2-Pfeiffer2

Submitted DRMAA job (jobid 8622642)

rule bam2fastq_picard:
    input: input/rawBam/Part1-Pfeiffer2.bam
    output: output/fastq/Part1-Pfeiffer2.1.fastq, output/fastq/Part1-Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part1-Pfeiffer2.2017-06-30.13-36-49.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part1-Pfeiffer2.2017-06-30.13-36-49.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part1-Pfeiffer2.2017-06-30.13-36-49.namesort.stderr
    jobid: 22
    wildcards: sampleB2FP=Part1-Pfeiffer2

Submitted DRMAA job (jobid 8622643)

rule bam2fastq_picard:
    input: input/rawBam/Part1-Pfeiffer3.bam
    output: output/fastq/Part1-Pfeiffer3.1.fastq, output/fastq/Part1-Pfeiffer3.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part1-Pfeiffer3.2017-06-30.13-36-49.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part1-Pfeiffer3.2017-06-30.13-36-49.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part1-Pfeiffer3.2017-06-30.13-36-49.namesort.stderr
    jobid: 23
    wildcards: sampleB2FP=Part1-Pfeiffer3

Submitted DRMAA job (jobid 8622644)

rule bam2fastq_picard:
    input: input/rawBam/Part2-Pfeiffer3.bam
    output: output/fastq/Part2-Pfeiffer3.1.fastq, output/fastq/Part2-Pfeiffer3.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part2-Pfeiffer3.2017-06-30.13-36-49.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part2-Pfeiffer3.2017-06-30.13-36-49.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part2-Pfeiffer3.2017-06-30.13-36-49.namesort.stderr
    jobid: 24
    wildcards: sampleB2FP=Part2-Pfeiffer3

Submitted DRMAA job (jobid 8622645)
Finished job 21.
1 of 26 steps (4%) done

rule fastq2GZ:
    input: output/fastq/Part4-Pfeiffer2.2.fastq
    output: output/fastq/Part4-Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part4-Pfeiffer2.2.2017-06-30.13-36-49.stderr
    jobid: 7
    wildcards: pathFGZ=output/fastq, sampleFGZ=Part4-Pfeiffer2.2

Submitted DRMAA job (jobid 8622679)
Finished job 22.
2 of 26 steps (8%) done

rule fastq2GZ:
    input: output/fastq/Part4-Pfeiffer2.1.fastq
    output: output/fastq/Part4-Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part4-Pfeiffer2.1.2017-06-30.13-36-49.stderr
    jobid: 11
    wildcards: pathFGZ=output/fastq, sampleFGZ=Part4-Pfeiffer2.1

Submitted DRMAA job (jobid 8622680)

rule fastq2GZ:
    input: output/fastq/Part1-Pfeiffer2.1.fastq
    output: output/fastq/Part1-Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part1-Pfeiffer2.1.2017-06-30.13-36-49.stderr
    jobid: 9
    wildcards: pathFGZ=output/fastq, sampleFGZ=Part1-Pfeiffer2.1

Submitted DRMAA job (jobid 8622681)

rule fastq2GZ:
    input: output/fastq/Part1-Pfeiffer2.2.fastq
    output: output/fastq/Part1-Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part1-Pfeiffer2.2.2017-06-30.13-36-49.stderr
    jobid: 8
    wildcards: pathFGZ=output/fastq, sampleFGZ=Part1-Pfeiffer2.2

Submitted DRMAA job (jobid 8622682)
Finished job 23.
3 of 26 steps (12%) done

rule fastq2GZ:
    input: output/fastq/Part1-Pfeiffer3.2.fastq
    output: output/fastq/Part1-Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part1-Pfeiffer3.2.2017-06-30.13-36-49.stderr
    jobid: 18
    wildcards: pathFGZ=output/fastq, sampleFGZ=Part1-Pfeiffer3.2

Submitted DRMAA job (jobid 8622683)

rule fastq2GZ:
    input: output/fastq/Part1-Pfeiffer3.1.fastq
    output: output/fastq/Part1-Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part1-Pfeiffer3.1.2017-06-30.13-36-49.stderr
    jobid: 13
    wildcards: pathFGZ=output/fastq, sampleFGZ=Part1-Pfeiffer3.1

Submitted DRMAA job (jobid 8622684)
Finished job 25.
4 of 26 steps (15%) done

rule fastq2GZ:
    input: output/fastq/Part3-Pfeiffer3.1.fastq
    output: output/fastq/Part3-Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part3-Pfeiffer3.1.2017-06-30.13-36-49.stderr
    jobid: 15
    wildcards: pathFGZ=output/fastq, sampleFGZ=Part3-Pfeiffer3.1

Submitted DRMAA job (jobid 8622685)

rule fastq2GZ:
    input: output/fastq/Part3-Pfeiffer3.2.fastq
    output: output/fastq/Part3-Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part3-Pfeiffer3.2.2017-06-30.13-36-49.stderr
    jobid: 16
    wildcards: pathFGZ=output/fastq, sampleFGZ=Part3-Pfeiffer3.2

Submitted DRMAA job (jobid 8622686)
Finished job 19.
5 of 26 steps (19%) done

rule fastq2GZ:
    input: output/fastq/Part3-Pfeiffer2.2.fastq
    output: output/fastq/Part3-Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part3-Pfeiffer2.2.2017-06-30.13-36-49.stderr
    jobid: 5
    wildcards: pathFGZ=output/fastq, sampleFGZ=Part3-Pfeiffer2.2

Submitted DRMAA job (jobid 8622690)

rule fastq2GZ:
    input: output/fastq/Part3-Pfeiffer2.1.fastq
    output: output/fastq/Part3-Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part3-Pfeiffer2.1.2017-06-30.13-36-49.stderr
    jobid: 10
    wildcards: pathFGZ=output/fastq, sampleFGZ=Part3-Pfeiffer2.1

Submitted DRMAA job (jobid 8622691)
Finished job 24.
6 of 26 steps (23%) done

rule fastq2GZ:
    input: output/fastq/Part2-Pfeiffer3.1.fastq
    output: output/fastq/Part2-Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part2-Pfeiffer3.1.2017-06-30.13-36-49.stderr
    jobid: 14
    wildcards: pathFGZ=output/fastq, sampleFGZ=Part2-Pfeiffer3.1

Submitted DRMAA job (jobid 8622692)

rule fastq2GZ:
    input: output/fastq/Part2-Pfeiffer3.2.fastq
    output: output/fastq/Part2-Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part2-Pfeiffer3.2.2017-06-30.13-36-49.stderr
    jobid: 17
    wildcards: pathFGZ=output/fastq, sampleFGZ=Part2-Pfeiffer3.2

Submitted DRMAA job (jobid 8622694)
Finished job 20.
7 of 26 steps (27%) done

rule fastq2GZ:
    input: output/fastq/Part2-Pfeiffer2.2.fastq
    output: output/fastq/Part2-Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part2-Pfeiffer2.2.2017-06-30.13-36-49.stderr
    jobid: 6
    wildcards: pathFGZ=output/fastq, sampleFGZ=Part2-Pfeiffer2.2

Submitted DRMAA job (jobid 8622696)

rule fastq2GZ:
    input: output/fastq/Part2-Pfeiffer2.1.fastq
    output: output/fastq/Part2-Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part2-Pfeiffer2.1.2017-06-30.13-36-49.stderr
    jobid: 12
    wildcards: pathFGZ=output/fastq, sampleFGZ=Part2-Pfeiffer2.1

Submitted DRMAA job (jobid 8622697)
Finished job 8.
8 of 26 steps (31%) done
Finished job 13.
9 of 26 steps (35%) done
Finished job 7.
10 of 26 steps (38%) done
Finished job 18.
11 of 26 steps (42%) done
Finished job 10.
12 of 26 steps (46%) done
Finished job 15.
13 of 26 steps (50%) done
Finished job 17.
14 of 26 steps (54%) done
Finished job 11.
15 of 26 steps (58%) done
Finished job 16.
16 of 26 steps (62%) done

rule mergeFASTQ:
    input: output/fastq/Part1-Pfeiffer3.2.fastq.gz, output/fastq/Part2-Pfeiffer3.2.fastq.gz, output/fastq/Part3-Pfeiffer3.2.fastq.gz
    output: output/fastq/Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/mergeFASTQ_PairedReadGz/mergeFASTQ_PairedReadGz_Pfeiffer3..2.2017-06-30.13-36-49.stderr
    jobid: 4
    wildcards: compressionSuffix=.gz, sampleFM=Pfeiffer3, readDirection=.2

Submitted DRMAA job (jobid 8622704)
Finished job 14.
17 of 26 steps (65%) done

rule mergeFASTQ:
    input: output/fastq/Part1-Pfeiffer3.1.fastq.gz, output/fastq/Part2-Pfeiffer3.1.fastq.gz, output/fastq/Part3-Pfeiffer3.1.fastq.gz
    output: output/fastq/Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/mergeFASTQ_PairedReadGz/mergeFASTQ_PairedReadGz_Pfeiffer3..1.2017-06-30.13-36-49.stderr
    jobid: 3
    wildcards: compressionSuffix=.gz, sampleFM=Pfeiffer3, readDirection=.1

Submitted DRMAA job (jobid 8622705)
Finished job 9.
18 of 26 steps (69%) done
Finished job 5.
19 of 26 steps (73%) done
Finished job 4.
20 of 26 steps (77%) done
Finished job 3.
21 of 26 steps (81%) done
Finished job 6.
22 of 26 steps (85%) done

rule mergeFASTQ:
    input: output/fastq/Part1-Pfeiffer2.2.fastq.gz, output/fastq/Part2-Pfeiffer2.2.fastq.gz, output/fastq/Part3-Pfeiffer2.2.fastq.gz, output/fastq/Part4-Pfeiffer2.2.fastq.gz
    output: output/fastq/Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/mergeFASTQ_PairedReadGz/mergeFASTQ_PairedReadGz_Pfeiffer2..2.2017-06-30.13-36-49.stderr
    jobid: 1
    wildcards: compressionSuffix=.gz, sampleFM=Pfeiffer2, readDirection=.2

Submitted DRMAA job (jobid 8622728)
Finished job 12.
23 of 26 steps (88%) done

rule mergeFASTQ:
    input: output/fastq/Part1-Pfeiffer2.1.fastq.gz, output/fastq/Part2-Pfeiffer2.1.fastq.gz, output/fastq/Part3-Pfeiffer2.1.fastq.gz, output/fastq/Part4-Pfeiffer2.1.fastq.gz
    output: output/fastq/Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/mergeFASTQ_PairedReadGz/mergeFASTQ_PairedReadGz_Pfeiffer2..1.2017-06-30.13-36-49.stderr
    jobid: 2
    wildcards: compressionSuffix=.gz, sampleFM=Pfeiffer2, readDirection=.1

Submitted DRMAA job (jobid 8622736)
Finished job 2.
24 of 26 steps (92%) done
Finished job 1.
25 of 26 steps (96%) done

localrule all:
    input: output/fastq/Pfeiffer2.1.fastq.gz, output/fastq/Pfeiffer3.1.fastq.gz, output/fastq/Pfeiffer2.2.fastq.gz, output/fastq/Pfeiffer3.2.fastq.gz
    jobid: 0

Finished job 0.
26 of 26 steps (100%) done
```
