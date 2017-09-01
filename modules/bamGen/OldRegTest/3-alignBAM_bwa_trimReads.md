# 3-bamALIGN_bwa_trimReads
This pipeline is to exemplify the default operations of this module. 

## Setting up the: Snakefile
Users must set the following submodule "call via" input requirements:

 * alignBMA_bwa

## Setting up the: YAML
Users must set the following "input/config.yaml" variables:

 * (Line 82) trimReadsFlag: True

## Setting up the: output directory

 * None

```
input
    /rawBam
        Pfeiffer2.bam
        Pfeiffer3.bam
```

## Snakemake dry run output:
```
rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer3.bam
    output: output/fastq/Pfeiffer3.1.fastq, output/fastq/Pfeiffer3.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-08-30.12-33-07.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-08-30.12-33-07.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-08-30.12-33-07.stderr
    jobid: 8
    wildcards: sampleB2FP=Pfeiffer3


rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer2.bam
    output: output/fastq/Pfeiffer2.1.fastq, output/fastq/Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-08-30.12-33-07.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-08-30.12-33-07.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-08-30.12-33-07.stderr
    jobid: 7
    wildcards: sampleB2FP=Pfeiffer2


rule fastq2GZ:
    input: output/fastq/Pfeiffer2.2.fastq
    output: output/fastq/Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.2.2017-08-30.12-33-08.stderr
    jobid: 3
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer2.2


rule fastq2GZ:
    input: output/fastq/Pfeiffer2.1.fastq
    output: output/fastq/Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.1.2017-08-30.12-33-08.stderr
    jobid: 4
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer2.1


rule bamALIGN_bwa:
    input: output/fastq/Pfeiffer2.1.fastq.gz, output/fastq/Pfeiffer2.2.fastq.gz, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa
    output: output/bam/Pfeiffer2_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-08-30.12-33-08.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-08-30.12-33-08.samtools.stderr
    jobid: 1
    wildcards: sampleBAB=Pfeiffer2


rule fastq2GZ:
    input: output/fastq/Pfeiffer3.1.fastq
    output: output/fastq/Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.1.2017-08-30.12-33-08.stderr
    jobid: 6
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer3.1


rule fastq2GZ:
    input: output/fastq/Pfeiffer3.2.fastq
    output: output/fastq/Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.2.2017-08-30.12-33-08.stderr
    jobid: 5
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer3.2


rule bamALIGN_bwa:
    input: output/fastq/Pfeiffer3.1.fastq.gz, output/fastq/Pfeiffer3.2.fastq.gz, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa
    output: output/bam/Pfeiffer3_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-08-30.12-33-08.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-08-30.12-33-08.samtools.stderr
    jobid: 2
    wildcards: sampleBAB=Pfeiffer3


localrule all:
    input: output/bam/Pfeiffer2_Aligned.out.bam, output/bam/Pfeiffer3_Aligned.out.bam
    jobid: 0

Job counts:
	count	jobs
	1	all
	2	bam2fastq_picard
	2	bamALIGN_bwa
	4	fastq2GZ
	9
```
