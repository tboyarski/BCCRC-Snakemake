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
 * (Line 158) bamMergeRootDIR = output/bam
 * (Line 159) bamMergeSuffix = _Aligned.out_sorted_filtered

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

rule bam2fastq_picard:
    input: input/rawBam/Part2-Pfeiffer2.bam
    output: output/fastq/Part2-Pfeiffer2.1.fastq, output/fastq/Part2-Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part2-Pfeiffer2.2017-07-07.16-08-40.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part2-Pfeiffer2.2017-07-07.16-08-40.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part2-Pfeiffer2.2017-07-07.16-08-40.namesort.stderr
    jobid: 88
    wildcards: sampleB2FP=Part2-Pfeiffer2


rule bam2fastq_picard:
    input: input/rawBam/Part4-Pfeiffer2.bam
    output: output/fastq/Part4-Pfeiffer2.1.fastq, output/fastq/Part4-Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part4-Pfeiffer2.2017-07-07.16-08-40.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part4-Pfeiffer2.2017-07-07.16-08-40.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part4-Pfeiffer2.2017-07-07.16-08-40.namesort.stderr
    jobid: 89
    wildcards: sampleB2FP=Part4-Pfeiffer2


rule bam2fastq_picard:
    input: input/rawBam/Part1-Pfeiffer2.bam
    output: output/fastq/Part1-Pfeiffer2.1.fastq, output/fastq/Part1-Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part1-Pfeiffer2.2017-07-07.16-08-40.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part1-Pfeiffer2.2017-07-07.16-08-40.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part1-Pfeiffer2.2017-07-07.16-08-40.namesort.stderr
    jobid: 87
    wildcards: sampleB2FP=Part1-Pfeiffer2


rule bam2fastq_picard:
    input: input/rawBam/Part3-Pfeiffer3.bam
    output: output/fastq/Part3-Pfeiffer3.1.fastq, output/fastq/Part3-Pfeiffer3.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part3-Pfeiffer3.2017-07-07.16-08-40.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part3-Pfeiffer3.2017-07-07.16-08-40.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part3-Pfeiffer3.2017-07-07.16-08-40.namesort.stderr
    jobid: 85
    wildcards: sampleB2FP=Part3-Pfeiffer3


rule bam2fastq_picard:
    input: input/rawBam/Part1-Pfeiffer3.bam
    output: output/fastq/Part1-Pfeiffer3.1.fastq, output/fastq/Part1-Pfeiffer3.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part1-Pfeiffer3.2017-07-07.16-08-40.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part1-Pfeiffer3.2017-07-07.16-08-40.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part1-Pfeiffer3.2017-07-07.16-08-40.namesort.stderr
    jobid: 86
    wildcards: sampleB2FP=Part1-Pfeiffer3


rule bam2fastq_picard:
    input: input/rawBam/Part2-Pfeiffer3.bam
    output: output/fastq/Part2-Pfeiffer3.1.fastq, output/fastq/Part2-Pfeiffer3.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part2-Pfeiffer3.2017-07-07.16-08-40.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part2-Pfeiffer3.2017-07-07.16-08-40.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part2-Pfeiffer3.2017-07-07.16-08-40.namesort.stderr
    jobid: 84
    wildcards: sampleB2FP=Part2-Pfeiffer3


rule bam2fastq_picard:
    input: input/rawBam/Part3-Pfeiffer2.bam
    output: output/fastq/Part3-Pfeiffer2.1.fastq, output/fastq/Part3-Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part3-Pfeiffer2.2017-07-07.16-08-40.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part3-Pfeiffer2.2017-07-07.16-08-40.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part3-Pfeiffer2.2017-07-07.16-08-40.namesort.stderr
    jobid: 90
    wildcards: sampleB2FP=Part3-Pfeiffer2


rule fastq2GZ:
    input: output/fastq/Part3-Pfeiffer2.1.fastq
    output: output/fastq/Part3-Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part3-Pfeiffer2.1.2017-07-07.16-08-40.stderr
    jobid: 82
    wildcards: sampleFGZ=Part3-Pfeiffer2.1, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Part3-Pfeiffer3.2.fastq
    output: output/fastq/Part3-Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part3-Pfeiffer3.2.2017-07-07.16-08-40.stderr
    jobid: 73
    wildcards: sampleFGZ=Part3-Pfeiffer3.2, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Part2-Pfeiffer2.2.fastq
    output: output/fastq/Part2-Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part2-Pfeiffer2.2.2017-07-07.16-08-40.stderr
    jobid: 79
    wildcards: sampleFGZ=Part2-Pfeiffer2.2, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Part2-Pfeiffer2.1.fastq
    output: output/fastq/Part2-Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part2-Pfeiffer2.1.2017-07-07.16-08-40.stderr
    jobid: 78
    wildcards: sampleFGZ=Part2-Pfeiffer2.1, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Part3-Pfeiffer3.1.fastq
    output: output/fastq/Part3-Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part3-Pfeiffer3.1.2017-07-07.16-08-40.stderr
    jobid: 72
    wildcards: sampleFGZ=Part3-Pfeiffer3.1, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Part3-Pfeiffer2.2.fastq
    output: output/fastq/Part3-Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part3-Pfeiffer2.2.2017-07-07.16-08-40.stderr
    jobid: 83
    wildcards: sampleFGZ=Part3-Pfeiffer2.2, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Part1-Pfeiffer3.1.fastq
    output: output/fastq/Part1-Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part1-Pfeiffer3.1.2017-07-07.16-08-40.stderr
    jobid: 75
    wildcards: sampleFGZ=Part1-Pfeiffer3.1, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Part4-Pfeiffer2.1.fastq
    output: output/fastq/Part4-Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part4-Pfeiffer2.1.2017-07-07.16-08-40.stderr
    jobid: 80
    wildcards: sampleFGZ=Part4-Pfeiffer2.1, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Part1-Pfeiffer2.2.fastq
    output: output/fastq/Part1-Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part1-Pfeiffer2.2.2017-07-07.16-08-40.stderr
    jobid: 77
    wildcards: sampleFGZ=Part1-Pfeiffer2.2, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Part2-Pfeiffer3.1.fastq
    output: output/fastq/Part2-Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part2-Pfeiffer3.1.2017-07-07.16-08-40.stderr
    jobid: 71
    wildcards: sampleFGZ=Part2-Pfeiffer3.1, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Part2-Pfeiffer3.2.fastq
    output: output/fastq/Part2-Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part2-Pfeiffer3.2.2017-07-07.16-08-40.stderr
    jobid: 70
    wildcards: sampleFGZ=Part2-Pfeiffer3.2, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Part1-Pfeiffer3.2.fastq
    output: output/fastq/Part1-Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part1-Pfeiffer3.2.2017-07-07.16-08-40.stderr
    jobid: 74
    wildcards: sampleFGZ=Part1-Pfeiffer3.2, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Part1-Pfeiffer2.1.fastq
    output: output/fastq/Part1-Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part1-Pfeiffer2.1.2017-07-07.16-08-40.stderr
    jobid: 76
    wildcards: sampleFGZ=Part1-Pfeiffer2.1, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Part4-Pfeiffer2.2.fastq
    output: output/fastq/Part4-Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part4-Pfeiffer2.2.2017-07-07.16-08-40.stderr
    jobid: 81
    wildcards: sampleFGZ=Part4-Pfeiffer2.2, pathFGZ=output/fastq


rule bamALIGN_bwa:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, output/fastq/Part2-Pfeiffer2.1.fastq.gz, output/fastq/Part2-Pfeiffer2.2.fastq.gz
    output: output/bam/Part2-Pfeiffer2_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Part2-Pfeiffer2.2017-07-07.16-08-40.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Part2-Pfeiffer2.2017-07-07.16-08-40.samtools.stderr
    jobid: 67
    wildcards: sampleBAB=Part2-Pfeiffer2


rule bamALIGN_bwa:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, output/fastq/Part3-Pfeiffer3.1.fastq.gz, output/fastq/Part3-Pfeiffer3.2.fastq.gz
    output: output/bam/Part3-Pfeiffer3_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Part3-Pfeiffer3.2017-07-07.16-08-40.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Part3-Pfeiffer3.2017-07-07.16-08-40.samtools.stderr
    jobid: 64
    wildcards: sampleBAB=Part3-Pfeiffer3


rule bamALIGN_bwa:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, output/fastq/Part2-Pfeiffer3.1.fastq.gz, output/fastq/Part2-Pfeiffer3.2.fastq.gz
    output: output/bam/Part2-Pfeiffer3_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Part2-Pfeiffer3.2017-07-07.16-08-40.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Part2-Pfeiffer3.2017-07-07.16-08-40.samtools.stderr
    jobid: 63
    wildcards: sampleBAB=Part2-Pfeiffer3


rule bamALIGN_bwa:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, output/fastq/Part4-Pfeiffer2.1.fastq.gz, output/fastq/Part4-Pfeiffer2.2.fastq.gz
    output: output/bam/Part4-Pfeiffer2_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Part4-Pfeiffer2.2017-07-07.16-08-40.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Part4-Pfeiffer2.2017-07-07.16-08-40.samtools.stderr
    jobid: 68
    wildcards: sampleBAB=Part4-Pfeiffer2


rule bamALIGN_bwa:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, output/fastq/Part1-Pfeiffer3.1.fastq.gz, output/fastq/Part1-Pfeiffer3.2.fastq.gz
    output: output/bam/Part1-Pfeiffer3_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Part1-Pfeiffer3.2017-07-07.16-08-40.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Part1-Pfeiffer3.2017-07-07.16-08-40.samtools.stderr
    jobid: 65
    wildcards: sampleBAB=Part1-Pfeiffer3


rule bamALIGN_bwa:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, output/fastq/Part1-Pfeiffer2.1.fastq.gz, output/fastq/Part1-Pfeiffer2.2.fastq.gz
    output: output/bam/Part1-Pfeiffer2_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Part1-Pfeiffer2.2017-07-07.16-08-40.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Part1-Pfeiffer2.2017-07-07.16-08-40.samtools.stderr
    jobid: 66
    wildcards: sampleBAB=Part1-Pfeiffer2


rule bamALIGN_bwa:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, output/fastq/Part3-Pfeiffer2.1.fastq.gz, output/fastq/Part3-Pfeiffer2.2.fastq.gz
    output: output/bam/Part3-Pfeiffer2_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Part3-Pfeiffer2.2017-07-07.16-08-40.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Part3-Pfeiffer2.2017-07-07.16-08-40.samtools.stderr
    jobid: 69
    wildcards: sampleBAB=Part3-Pfeiffer2


rule sortBAM_biobambam:
    input: output/bam/Part4-Pfeiffer2_Aligned.out.bam
    output: output/bam/Part4-Pfeiffer2_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Part4-Pfeiffer2_Aligned.out.2017-07-07.16-08-40.bamsort.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Part4-Pfeiffer2_Aligned.out.2017-07-07.16-08-40.samtools.stderr
    jobid: 61
    wildcards: pathSBB=output/bam, sampleSBB=Part4-Pfeiffer2_Aligned.out


rule sortBAM_biobambam:
    input: output/bam/Part1-Pfeiffer2_Aligned.out.bam
    output: output/bam/Part1-Pfeiffer2_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Part1-Pfeiffer2_Aligned.out.2017-07-07.16-08-40.bamsort.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Part1-Pfeiffer2_Aligned.out.2017-07-07.16-08-40.samtools.stderr
    jobid: 59
    wildcards: pathSBB=output/bam, sampleSBB=Part1-Pfeiffer2_Aligned.out


rule sortBAM_biobambam:
    input: output/bam/Part3-Pfeiffer2_Aligned.out.bam
    output: output/bam/Part3-Pfeiffer2_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Part3-Pfeiffer2_Aligned.out.2017-07-07.16-08-40.bamsort.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Part3-Pfeiffer2_Aligned.out.2017-07-07.16-08-40.samtools.stderr
    jobid: 62
    wildcards: pathSBB=output/bam, sampleSBB=Part3-Pfeiffer2_Aligned.out


rule sortBAM_biobambam:
    input: output/bam/Part2-Pfeiffer3_Aligned.out.bam
    output: output/bam/Part2-Pfeiffer3_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Part2-Pfeiffer3_Aligned.out.2017-07-07.16-08-40.bamsort.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Part2-Pfeiffer3_Aligned.out.2017-07-07.16-08-40.samtools.stderr
    jobid: 56
    wildcards: pathSBB=output/bam, sampleSBB=Part2-Pfeiffer3_Aligned.out


rule sortBAM_biobambam:
    input: output/bam/Part3-Pfeiffer3_Aligned.out.bam
    output: output/bam/Part3-Pfeiffer3_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Part3-Pfeiffer3_Aligned.out.2017-07-07.16-08-40.bamsort.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Part3-Pfeiffer3_Aligned.out.2017-07-07.16-08-40.samtools.stderr
    jobid: 57
    wildcards: pathSBB=output/bam, sampleSBB=Part3-Pfeiffer3_Aligned.out


rule sortBAM_biobambam:
    input: output/bam/Part2-Pfeiffer2_Aligned.out.bam
    output: output/bam/Part2-Pfeiffer2_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Part2-Pfeiffer2_Aligned.out.2017-07-07.16-08-40.bamsort.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Part2-Pfeiffer2_Aligned.out.2017-07-07.16-08-40.samtools.stderr
    jobid: 60
    wildcards: pathSBB=output/bam, sampleSBB=Part2-Pfeiffer2_Aligned.out


rule sortBAM_biobambam:
    input: output/bam/Part1-Pfeiffer3_Aligned.out.bam
    output: output/bam/Part1-Pfeiffer3_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Part1-Pfeiffer3_Aligned.out.2017-07-07.16-08-40.bamsort.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Part1-Pfeiffer3_Aligned.out.2017-07-07.16-08-40.samtools.stderr
    jobid: 58
    wildcards: pathSBB=output/bam, sampleSBB=Part1-Pfeiffer3_Aligned.out


rule filteredBAM:
    input: output/bam/Part3-Pfeiffer2_Aligned.out_sorted.bam
    output: output/bam/Part3-Pfeiffer2_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Part3-Pfeiffer2_Aligned.out_sorted.2017-07-07.16-08-40.stderr
    jobid: 55
    wildcards: pathFB=output/bam, sampleFB=Part3-Pfeiffer2_Aligned.out_sorted


rule filteredBAM:
    input: output/bam/Part2-Pfeiffer3_Aligned.out_sorted.bam
    output: output/bam/Part2-Pfeiffer3_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Part2-Pfeiffer3_Aligned.out_sorted.2017-07-07.16-08-40.stderr
    jobid: 49
    wildcards: pathFB=output/bam, sampleFB=Part2-Pfeiffer3_Aligned.out_sorted


rule filteredBAM:
    input: output/bam/Part2-Pfeiffer2_Aligned.out_sorted.bam
    output: output/bam/Part2-Pfeiffer2_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Part2-Pfeiffer2_Aligned.out_sorted.2017-07-07.16-08-40.stderr
    jobid: 53
    wildcards: pathFB=output/bam, sampleFB=Part2-Pfeiffer2_Aligned.out_sorted


rule filteredBAM:
    input: output/bam/Part1-Pfeiffer2_Aligned.out_sorted.bam
    output: output/bam/Part1-Pfeiffer2_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Part1-Pfeiffer2_Aligned.out_sorted.2017-07-07.16-08-40.stderr
    jobid: 52
    wildcards: pathFB=output/bam, sampleFB=Part1-Pfeiffer2_Aligned.out_sorted


rule filteredBAM:
    input: output/bam/Part4-Pfeiffer2_Aligned.out_sorted.bam
    output: output/bam/Part4-Pfeiffer2_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Part4-Pfeiffer2_Aligned.out_sorted.2017-07-07.16-08-40.stderr
    jobid: 54
    wildcards: pathFB=output/bam, sampleFB=Part4-Pfeiffer2_Aligned.out_sorted


rule filteredBAM:
    input: output/bam/Part3-Pfeiffer3_Aligned.out_sorted.bam
    output: output/bam/Part3-Pfeiffer3_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Part3-Pfeiffer3_Aligned.out_sorted.2017-07-07.16-08-40.stderr
    jobid: 50
    wildcards: pathFB=output/bam, sampleFB=Part3-Pfeiffer3_Aligned.out_sorted


rule filteredBAM:
    input: output/bam/Part1-Pfeiffer3_Aligned.out_sorted.bam
    output: output/bam/Part1-Pfeiffer3_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Part1-Pfeiffer3_Aligned.out_sorted.2017-07-07.16-08-40.stderr
    jobid: 51
    wildcards: pathFB=output/bam, sampleFB=Part1-Pfeiffer3_Aligned.out_sorted


rule mergeBAM:
    input: output/bam/Part1-Pfeiffer3_Aligned.out_sorted_filtered.bam, output/bam/Part2-Pfeiffer3_Aligned.out_sorted_filtered.bam, output/bam/Part3-Pfeiffer3_Aligned.out_sorted_filtered.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/mergeBAM/mergeBAM.2017-07-07.16-08-40.stderr
    jobid: 47
    wildcards: sampleMB=Pfeiffer3


rule mergeBAM:
    input: output/bam/Part1-Pfeiffer2_Aligned.out_sorted_filtered.bam, output/bam/Part2-Pfeiffer2_Aligned.out_sorted_filtered.bam, output/bam/Part3-Pfeiffer2_Aligned.out_sorted_filtered.bam, output/bam/Part4-Pfeiffer2_Aligned.out_sorted_filtered.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/mergeBAM/mergeBAM.2017-07-07.16-08-40.stderr
    jobid: 48
    wildcards: sampleMB=Pfeiffer2


rule markdupBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    output: output/metrics/Pfeiffer2_Aligned.out_sorted_filtered.dup_metrics, output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer2_Aligned.out_sorted_filtered.2017-07-07.16-08-40.biobammarkdup.stderr
    jobid: 46
    wildcards: outputDIR=output, sampleMDB=Pfeiffer2_Aligned.out_sorted_filtered


rule markdupBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    output: output/metrics/Pfeiffer3_Aligned.out_sorted_filtered.dup_metrics, output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer3_Aligned.out_sorted_filtered.2017-07-07.16-08-40.biobammarkdup.stderr
    jobid: 45
    wildcards: outputDIR=output, sampleMDB=Pfeiffer3_Aligned.out_sorted_filtered


rule indexBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam.bai, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer2.2017-07-07.16-08-40.stderr
    jobid: 44
    wildcards: outputDIR=output, sampleIB=Pfeiffer2


rule indexBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam.bai, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer3.2017-07-07.16-08-40.stderr
    jobid: 43
    wildcards: outputDIR=output, sampleIB=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_2.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-08-40.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-08-40.view.stderr
    jobid: 32
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_2.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-08-40.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-08-40.view.stderr
    jobid: 36
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-08-40.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-08-40.view.stderr
    jobid: 38
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_3.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-08-40.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-08-40.view.stderr
    jobid: 33
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-08-40.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-08-40.view.stderr
    jobid: 31
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_4.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-08-40.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-08-40.view.stderr
    jobid: 34
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_4


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_4.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-08-40.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-08-40.view.stderr
    jobid: 37
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_4


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_3.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-08-40.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-08-40.view.stderr
    jobid: 35
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_4.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_4.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_4.snp.2017-07-07.16-08-40.stderr
    jobid: 27
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_4, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_4.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_4.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_4.snp.2017-07-07.16-08-40.stderr
    jobid: 42
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_4, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_2.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_2.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_2.snp.2017-07-07.16-08-40.stderr
    jobid: 30
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_2, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_1.snp.2017-07-07.16-08-40.stderr
    jobid: 39
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_3.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_3.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_3.snp.2017-07-07.16-08-40.stderr
    jobid: 40
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_3, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_3.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_3.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_3.snp.2017-07-07.16-08-40.stderr
    jobid: 29
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_3, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_2.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_2.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_2.snp.2017-07-07.16-08-40.stderr
    jobid: 41
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_2, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_1.snp.2017-07-07.16-08-40.stderr
    jobid: 28
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_4.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_4.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_4.indel.2017-07-07.16-08-40.stderr
    jobid: 24
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_4, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_2.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_2.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_2.indel.2017-07-07.16-08-40.stderr
    jobid: 19
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_2, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_4.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_4.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_4.indel.2017-07-07.16-08-40.stderr
    jobid: 21
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_4, varTypeMPU2VCFS=indel


rule mergeVCF:
    input: output/vcfGenUtil_varScan/Pfeiffer3_1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_2.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_3.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_4.varScan.snp.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.vcf
    log: log/vcfUtil/mergeVCF/mergeVCF_Pfeiffer3.varScan.snp.2017-07-07.16-08-40.stderr
    jobid: 26
    wildcards: varTypeMVCF=snp, vcfProgramMVCF=varScan, sampleMVCF=Pfeiffer3, pathMV=output/vcfGenUtil_varScan


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_3.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_3.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_3.indel.2017-07-07.16-08-40.stderr
    jobid: 22
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_3, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_3.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_3.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_3.indel.2017-07-07.16-08-40.stderr
    jobid: 20
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_3, varTypeMPU2VCFS=indel


rule mergeVCF:
    input: output/vcfGenUtil_varScan/Pfeiffer2_1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_2.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_3.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_4.varScan.snp.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.vcf
    log: log/vcfUtil/mergeVCF/mergeVCF_Pfeiffer2.varScan.snp.2017-07-07.16-08-40.stderr
    jobid: 17
    wildcards: varTypeMVCF=snp, vcfProgramMVCF=varScan, sampleMVCF=Pfeiffer2, pathMV=output/vcfGenUtil_varScan


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_1.indel.2017-07-07.16-08-40.stderr
    jobid: 18
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_2.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_2.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_2.indel.2017-07-07.16-08-40.stderr
    jobid: 23
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_2, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_1.indel.2017-07-07.16-08-40.stderr
    jobid: 25
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_1, varTypeMPU2VCFS=indel


rule canonical:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical.summary.genes.txt, output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical.summary.html
    log: log/vcfGenUtil_varScan/canonical/canonical_Pfeiffer2.varScan.snp.2017-07-07.16-08-40.stderr
    jobid: 13
    wildcards: sampleCAN=Pfeiffer2.varScan.snp, pathCAN=vcfGenUtil_varScan


rule mergeVCF:
    input: output/vcfGenUtil_varScan/Pfeiffer2_1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_2.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_3.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_4.varScan.indel.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.vcf
    log: log/vcfUtil/mergeVCF/mergeVCF_Pfeiffer2.varScan.indel.2017-07-07.16-08-40.stderr
    jobid: 15
    wildcards: varTypeMVCF=indel, vcfProgramMVCF=varScan, sampleMVCF=Pfeiffer2, pathMV=output/vcfGenUtil_varScan


rule canonical:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical.summary.genes.txt, output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical.summary.html
    log: log/vcfGenUtil_varScan/canonical/canonical_Pfeiffer3.varScan.snp.2017-07-07.16-08-40.stderr
    jobid: 16
    wildcards: sampleCAN=Pfeiffer3.varScan.snp, pathCAN=vcfGenUtil_varScan


rule mergeVCF:
    input: output/vcfGenUtil_varScan/Pfeiffer3_1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_2.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_3.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_4.varScan.indel.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.vcf
    log: log/vcfUtil/mergeVCF/mergeVCF_Pfeiffer3.varScan.indel.2017-07-07.16-08-40.stderr
    jobid: 14
    wildcards: varTypeMVCF=indel, vcfProgramMVCF=varScan, sampleMVCF=Pfeiffer3, pathMV=output/vcfGenUtil_varScan


rule dbsnp:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated.vcf
    log: log/vcfGenUtil_varScan/dbsnp/dbsnp_Pfeiffer3.varScan.snp.canonical_annotated.2017-07-07.16-08-40.stderr
    jobid: 12
    wildcards: pathDbSnp=output/vcfGenUtil_varScan, sampleDbSnp=Pfeiffer3.varScan.snp.canonical_annotated


rule canonical:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.canonical.summary.genes.txt, output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.canonical_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.canonical.summary.html
    log: log/vcfGenUtil_varScan/canonical/canonical_Pfeiffer2.varScan.indel.2017-07-07.16-08-40.stderr
    jobid: 11
    wildcards: sampleCAN=Pfeiffer2.varScan.indel, pathCAN=vcfGenUtil_varScan


rule canonical:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.canonical.summary.genes.txt, output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.canonical_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.canonical.summary.html
    log: log/vcfGenUtil_varScan/canonical/canonical_Pfeiffer3.varScan.indel.2017-07-07.16-08-40.stderr
    jobid: 10
    wildcards: sampleCAN=Pfeiffer3.varScan.indel, pathCAN=vcfGenUtil_varScan


rule dbsnp:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated.vcf
    log: log/vcfGenUtil_varScan/dbsnp/dbsnp_Pfeiffer2.varScan.snp.canonical_annotated.2017-07-07.16-08-40.stderr
    jobid: 9
    wildcards: pathDbSnp=output/vcfGenUtil_varScan, sampleDbSnp=Pfeiffer2.varScan.snp.canonical_annotated


rule cosmic:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated.cosmic_annotated.vcf
    log: log/vcfGenUtil_varScan/cosmic/cosmic_Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated.2017-07-07.16-08-40.stderr
    jobid: 5
    wildcards: pathCOS=output/vcfGenUtil_varScan, sampleCOS=Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated


rule indel:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.canonical_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.canonical_annotated.indel_annotated.vcf
    log: log/vcfGenUtil_varScan/indel/indel_Pfeiffer3.varScan.indel.canonical_annotated.2017-07-07.16-08-40dbsnp.stderr, log/vcfGenUtil_varScan/indel/indel_Pfeiffer3.varScan.indel.canonical_annotated.2017-07-07.16-08-40.mills_100g.log, log/vcfGenUtil_varScan/indel/indel_Pfeiffer3.varScan.indel.canonical_annotated.2017-07-07.16-08-40.1000g.log
    jobid: 6
    wildcards: pathIndel=output/vcfGenUtil_varScan, sampleIndel=Pfeiffer3.varScan.indel.canonical_annotated


rule cosmic:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated.cosmic_annotated.vcf
    log: log/vcfGenUtil_varScan/cosmic/cosmic_Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated.2017-07-07.16-08-40.stderr
    jobid: 8
    wildcards: pathCOS=output/vcfGenUtil_varScan, sampleCOS=Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated


rule indel:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.canonical_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.canonical_annotated.indel_annotated.vcf
    log: log/vcfGenUtil_varScan/indel/indel_Pfeiffer2.varScan.indel.canonical_annotated.2017-07-07.16-08-40dbsnp.stderr, log/vcfGenUtil_varScan/indel/indel_Pfeiffer2.varScan.indel.canonical_annotated.2017-07-07.16-08-40.mills_100g.log, log/vcfGenUtil_varScan/indel/indel_Pfeiffer2.varScan.indel.canonical_annotated.2017-07-07.16-08-40.1000g.log
    jobid: 7
    wildcards: pathIndel=output/vcfGenUtil_varScan, sampleIndel=Pfeiffer2.varScan.indel.canonical_annotated


rule getVcfTable:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.canonical_annotated.indel_annotated.vcf
    output: output/vcfGenUtil_varScan/tables/Pfeiffer2.varScan.indel.canonical_annotated.indel_annotated.txt
    log: log/vcfUtil/vcfGetTable_annotateVcfDIR/vcfGetTable_annotateVcfDIR_{wildcards.sampleVCFGT}.2017-07-07.16-08-40.stderr, log/vcfUtil/vcfGetTable_annotateVcfDIR/vcfGetTable_annotateVcfDIR_{wildcards.sampleVCFGT}.2017-07-07.16-08-40.OnePerLine.stderr
    jobid: 3
    wildcards: sampleGVCFT=Pfeiffer2.varScan.indel.canonical_annotated.indel_annotated, pathGVCFT=output/vcfGenUtil_varScan


rule getVcfTable:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.canonical_annotated.indel_annotated.vcf
    output: output/vcfGenUtil_varScan/tables/Pfeiffer3.varScan.indel.canonical_annotated.indel_annotated.txt
    log: log/vcfUtil/vcfGetTable_annotateVcfDIR/vcfGetTable_annotateVcfDIR_{wildcards.sampleVCFGT}.2017-07-07.16-08-40.stderr, log/vcfUtil/vcfGetTable_annotateVcfDIR/vcfGetTable_annotateVcfDIR_{wildcards.sampleVCFGT}.2017-07-07.16-08-40.OnePerLine.stderr
    jobid: 2
    wildcards: sampleGVCFT=Pfeiffer3.varScan.indel.canonical_annotated.indel_annotated, pathGVCFT=output/vcfGenUtil_varScan


rule getVcfTable:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated.cosmic_annotated.vcf
    output: output/vcfGenUtil_varScan/tables/Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated.cosmic_annotated.txt
    log: log/vcfUtil/vcfGetTable_annotateVcfDIR/vcfGetTable_annotateVcfDIR_{wildcards.sampleVCFGT}.2017-07-07.16-08-40.stderr, log/vcfUtil/vcfGetTable_annotateVcfDIR/vcfGetTable_annotateVcfDIR_{wildcards.sampleVCFGT}.2017-07-07.16-08-40.OnePerLine.stderr
    jobid: 1
    wildcards: sampleGVCFT=Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated.cosmic_annotated, pathGVCFT=output/vcfGenUtil_varScan


rule getVcfTable:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated.cosmic_annotated.vcf
    output: output/vcfGenUtil_varScan/tables/Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated.cosmic_annotated.txt
    log: log/vcfUtil/vcfGetTable_annotateVcfDIR/vcfGetTable_annotateVcfDIR_{wildcards.sampleVCFGT}.2017-07-07.16-08-40.stderr, log/vcfUtil/vcfGetTable_annotateVcfDIR/vcfGetTable_annotateVcfDIR_{wildcards.sampleVCFGT}.2017-07-07.16-08-40.OnePerLine.stderr
    jobid: 4
    wildcards: sampleGVCFT=Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated.cosmic_annotated, pathGVCFT=output/vcfGenUtil_varScan


localrule all:
    input: output/vcfGenUtil_varScan/tables/Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated.cosmic_annotated.txt, output/vcfGenUtil_varScan/tables/Pfeiffer2.varScan.indel.canonical_annotated.indel_annotated.txt, output/vcfGenUtil_varScan/tables/Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated.cosmic_annotated.txt, output/vcfGenUtil_varScan/tables/Pfeiffer3.varScan.indel.canonical_annotated.indel_annotated.txt
    jobid: 0

Job counts:
	count	jobs
	1	all
	7	bam2fastq_picard
	8	bam2mpileup
	7	bamALIGN_bwa
	4	canonical
	2	cosmic
	2	dbsnp
	14	fastq2GZ
	7	filteredBAM
	4	getVcfTable
	2	indel
	2	indexBAM
	2	markdupBAM
	2	mergeBAM
	4	mergeVCF
	16	mpileup2vcf_single
	7	sortBAM_biobambam
	91
