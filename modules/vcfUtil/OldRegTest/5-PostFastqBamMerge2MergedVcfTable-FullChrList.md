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
Cancelling snakemake on user request.

rule bam2fastq_picard:
    input: input/rawBam/Part4-Pfeiffer2.bam
    output: output/fastq/Part4-Pfeiffer2.1.fastq, output/fastq/Part4-Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part4-Pfeiffer2.2017-07-07.16-13-08.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part4-Pfeiffer2.2017-07-07.16-13-08.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part4-Pfeiffer2.2017-07-07.16-13-08.vendor_failed_reads.log
    jobid: 567
    wildcards: sampleB2FP=Part4-Pfeiffer2


rule bam2fastq_picard:
    input: input/rawBam/Part2-Pfeiffer3.bam
    output: output/fastq/Part2-Pfeiffer3.1.fastq, output/fastq/Part2-Pfeiffer3.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part2-Pfeiffer3.2017-07-07.16-13-08.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part2-Pfeiffer3.2017-07-07.16-13-08.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part2-Pfeiffer3.2017-07-07.16-13-08.vendor_failed_reads.log
    jobid: 566
    wildcards: sampleB2FP=Part2-Pfeiffer3


rule bam2fastq_picard:
    input: input/rawBam/Part1-Pfeiffer2.bam
    output: output/fastq/Part1-Pfeiffer2.1.fastq, output/fastq/Part1-Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part1-Pfeiffer2.2017-07-07.16-13-08.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part1-Pfeiffer2.2017-07-07.16-13-08.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part1-Pfeiffer2.2017-07-07.16-13-08.vendor_failed_reads.log
    jobid: 568
    wildcards: sampleB2FP=Part1-Pfeiffer2


rule bam2fastq_picard:
    input: input/rawBam/Part2-Pfeiffer2.bam
    output: output/fastq/Part2-Pfeiffer2.1.fastq, output/fastq/Part2-Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part2-Pfeiffer2.2017-07-07.16-13-08.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part2-Pfeiffer2.2017-07-07.16-13-08.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part2-Pfeiffer2.2017-07-07.16-13-08.vendor_failed_reads.log
    jobid: 570
    wildcards: sampleB2FP=Part2-Pfeiffer2


rule bam2fastq_picard:
    input: input/rawBam/Part3-Pfeiffer2.bam
    output: output/fastq/Part3-Pfeiffer2.1.fastq, output/fastq/Part3-Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part3-Pfeiffer2.2017-07-07.16-13-08.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part3-Pfeiffer2.2017-07-07.16-13-08.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part3-Pfeiffer2.2017-07-07.16-13-08.vendor_failed_reads.log
    jobid: 569
    wildcards: sampleB2FP=Part3-Pfeiffer2


rule bam2fastq_picard:
    input: input/rawBam/Part3-Pfeiffer3.bam
    output: output/fastq/Part3-Pfeiffer3.1.fastq, output/fastq/Part3-Pfeiffer3.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part3-Pfeiffer3.2017-07-07.16-13-08.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part3-Pfeiffer3.2017-07-07.16-13-08.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part3-Pfeiffer3.2017-07-07.16-13-08.vendor_failed_reads.log
    jobid: 564
    wildcards: sampleB2FP=Part3-Pfeiffer3


rule bam2fastq_picard:
    input: input/rawBam/Part1-Pfeiffer3.bam
    output: output/fastq/Part1-Pfeiffer3.1.fastq, output/fastq/Part1-Pfeiffer3.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part1-Pfeiffer3.2017-07-07.16-13-08.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part1-Pfeiffer3.2017-07-07.16-13-08.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part1-Pfeiffer3.2017-07-07.16-13-08.vendor_failed_reads.log
    jobid: 565
    wildcards: sampleB2FP=Part1-Pfeiffer3


rule fastq2GZ:
    input: output/fastq/Part2-Pfeiffer2.1.fastq
    output: output/fastq/Part2-Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part2-Pfeiffer2.1.2017-07-07.16-13-08.stderr
    jobid: 562
    wildcards: pathFGZ=output/fastq, sampleFGZ=Part2-Pfeiffer2.1


rule fastq2GZ:
    input: output/fastq/Part4-Pfeiffer2.2.fastq
    output: output/fastq/Part4-Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part4-Pfeiffer2.2.2017-07-07.16-13-08.stderr
    jobid: 557
    wildcards: pathFGZ=output/fastq, sampleFGZ=Part4-Pfeiffer2.2


rule fastq2GZ:
    input: output/fastq/Part2-Pfeiffer3.2.fastq
    output: output/fastq/Part2-Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part2-Pfeiffer3.2.2017-07-07.16-13-08.stderr
    jobid: 555
    wildcards: pathFGZ=output/fastq, sampleFGZ=Part2-Pfeiffer3.2


rule fastq2GZ:
    input: output/fastq/Part3-Pfeiffer2.1.fastq
    output: output/fastq/Part3-Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part3-Pfeiffer2.1.2017-07-07.16-13-08.stderr
    jobid: 560
    wildcards: pathFGZ=output/fastq, sampleFGZ=Part3-Pfeiffer2.1


rule fastq2GZ:
    input: output/fastq/Part4-Pfeiffer2.1.fastq
    output: output/fastq/Part4-Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part4-Pfeiffer2.1.2017-07-07.16-13-08.stderr
    jobid: 556
    wildcards: pathFGZ=output/fastq, sampleFGZ=Part4-Pfeiffer2.1


rule fastq2GZ:
    input: output/fastq/Part2-Pfeiffer2.2.fastq
    output: output/fastq/Part2-Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part2-Pfeiffer2.2.2017-07-07.16-13-08.stderr
    jobid: 563
    wildcards: pathFGZ=output/fastq, sampleFGZ=Part2-Pfeiffer2.2


rule fastq2GZ:
    input: output/fastq/Part3-Pfeiffer3.1.fastq
    output: output/fastq/Part3-Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part3-Pfeiffer3.1.2017-07-07.16-13-08.stderr
    jobid: 551
    wildcards: pathFGZ=output/fastq, sampleFGZ=Part3-Pfeiffer3.1


rule fastq2GZ:
    input: output/fastq/Part2-Pfeiffer3.1.fastq
    output: output/fastq/Part2-Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part2-Pfeiffer3.1.2017-07-07.16-13-08.stderr
    jobid: 554
    wildcards: pathFGZ=output/fastq, sampleFGZ=Part2-Pfeiffer3.1


rule fastq2GZ:
    input: output/fastq/Part1-Pfeiffer3.2.fastq
    output: output/fastq/Part1-Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part1-Pfeiffer3.2.2017-07-07.16-13-08.stderr
    jobid: 552
    wildcards: pathFGZ=output/fastq, sampleFGZ=Part1-Pfeiffer3.2


rule fastq2GZ:
    input: output/fastq/Part1-Pfeiffer2.2.fastq
    output: output/fastq/Part1-Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part1-Pfeiffer2.2.2017-07-07.16-13-08.stderr
    jobid: 558
    wildcards: pathFGZ=output/fastq, sampleFGZ=Part1-Pfeiffer2.2


rule fastq2GZ:
    input: output/fastq/Part3-Pfeiffer2.2.fastq
    output: output/fastq/Part3-Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part3-Pfeiffer2.2.2017-07-07.16-13-08.stderr
    jobid: 561
    wildcards: pathFGZ=output/fastq, sampleFGZ=Part3-Pfeiffer2.2


rule fastq2GZ:
    input: output/fastq/Part1-Pfeiffer2.1.fastq
    output: output/fastq/Part1-Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part1-Pfeiffer2.1.2017-07-07.16-13-08.stderr
    jobid: 559
    wildcards: pathFGZ=output/fastq, sampleFGZ=Part1-Pfeiffer2.1


rule fastq2GZ:
    input: output/fastq/Part3-Pfeiffer3.2.fastq
    output: output/fastq/Part3-Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part3-Pfeiffer3.2.2017-07-07.16-13-08.stderr
    jobid: 550
    wildcards: pathFGZ=output/fastq, sampleFGZ=Part3-Pfeiffer3.2


rule fastq2GZ:
    input: output/fastq/Part1-Pfeiffer3.1.fastq
    output: output/fastq/Part1-Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part1-Pfeiffer3.1.2017-07-07.16-13-08.stderr
    jobid: 553
    wildcards: pathFGZ=output/fastq, sampleFGZ=Part1-Pfeiffer3.1


rule bamALIGN_bwa:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, output/fastq/Part1-Pfeiffer3.1.fastq.gz, output/fastq/Part1-Pfeiffer3.2.fastq.gz
    output: output/bam/Part1-Pfeiffer3_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Part1-Pfeiffer3.2017-07-07.16-13-08.samtools.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Part1-Pfeiffer3.2017-07-07.16-13-08.bwa.stderr
    jobid: 544
    wildcards: sampleBAB=Part1-Pfeiffer3


rule bamALIGN_bwa:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, output/fastq/Part4-Pfeiffer2.1.fastq.gz, output/fastq/Part4-Pfeiffer2.2.fastq.gz
    output: output/bam/Part4-Pfeiffer2_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Part4-Pfeiffer2.2017-07-07.16-13-08.samtools.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Part4-Pfeiffer2.2017-07-07.16-13-08.bwa.stderr
    jobid: 546
    wildcards: sampleBAB=Part4-Pfeiffer2


rule bamALIGN_bwa:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, output/fastq/Part3-Pfeiffer3.1.fastq.gz, output/fastq/Part3-Pfeiffer3.2.fastq.gz
    output: output/bam/Part3-Pfeiffer3_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Part3-Pfeiffer3.2017-07-07.16-13-08.samtools.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Part3-Pfeiffer3.2017-07-07.16-13-08.bwa.stderr
    jobid: 543
    wildcards: sampleBAB=Part3-Pfeiffer3


rule bamALIGN_bwa:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, output/fastq/Part1-Pfeiffer2.1.fastq.gz, output/fastq/Part1-Pfeiffer2.2.fastq.gz
    output: output/bam/Part1-Pfeiffer2_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Part1-Pfeiffer2.2017-07-07.16-13-08.samtools.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Part1-Pfeiffer2.2017-07-07.16-13-08.bwa.stderr
    jobid: 547
    wildcards: sampleBAB=Part1-Pfeiffer2


rule bamALIGN_bwa:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, output/fastq/Part3-Pfeiffer2.1.fastq.gz, output/fastq/Part3-Pfeiffer2.2.fastq.gz
    output: output/bam/Part3-Pfeiffer2_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Part3-Pfeiffer2.2017-07-07.16-13-08.samtools.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Part3-Pfeiffer2.2017-07-07.16-13-08.bwa.stderr
    jobid: 548
    wildcards: sampleBAB=Part3-Pfeiffer2


rule bamALIGN_bwa:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, output/fastq/Part2-Pfeiffer2.1.fastq.gz, output/fastq/Part2-Pfeiffer2.2.fastq.gz
    output: output/bam/Part2-Pfeiffer2_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Part2-Pfeiffer2.2017-07-07.16-13-08.samtools.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Part2-Pfeiffer2.2017-07-07.16-13-08.bwa.stderr
    jobid: 549
    wildcards: sampleBAB=Part2-Pfeiffer2


rule bamALIGN_bwa:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, output/fastq/Part2-Pfeiffer3.1.fastq.gz, output/fastq/Part2-Pfeiffer3.2.fastq.gz
    output: output/bam/Part2-Pfeiffer3_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Part2-Pfeiffer3.2017-07-07.16-13-08.samtools.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Part2-Pfeiffer3.2017-07-07.16-13-08.bwa.stderr
    jobid: 545
    wildcards: sampleBAB=Part2-Pfeiffer3


rule sortBAM_biobambam:
    input: output/bam/Part2-Pfeiffer2_Aligned.out.bam
    output: output/bam/Part2-Pfeiffer2_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Part2-Pfeiffer2_Aligned.out.2017-07-07.16-13-08.samtools.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Part2-Pfeiffer2_Aligned.out.2017-07-07.16-13-08.bamsort.stderr
    jobid: 542
    wildcards: sampleSBB=Part2-Pfeiffer2_Aligned.out, pathSBB=output/bam


rule sortBAM_biobambam:
    input: output/bam/Part4-Pfeiffer2_Aligned.out.bam
    output: output/bam/Part4-Pfeiffer2_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Part4-Pfeiffer2_Aligned.out.2017-07-07.16-13-08.samtools.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Part4-Pfeiffer2_Aligned.out.2017-07-07.16-13-08.bamsort.stderr
    jobid: 539
    wildcards: sampleSBB=Part4-Pfeiffer2_Aligned.out, pathSBB=output/bam


rule sortBAM_biobambam:
    input: output/bam/Part1-Pfeiffer2_Aligned.out.bam
    output: output/bam/Part1-Pfeiffer2_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Part1-Pfeiffer2_Aligned.out.2017-07-07.16-13-08.samtools.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Part1-Pfeiffer2_Aligned.out.2017-07-07.16-13-08.bamsort.stderr
    jobid: 540
    wildcards: sampleSBB=Part1-Pfeiffer2_Aligned.out, pathSBB=output/bam


rule sortBAM_biobambam:
    input: output/bam/Part3-Pfeiffer2_Aligned.out.bam
    output: output/bam/Part3-Pfeiffer2_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Part3-Pfeiffer2_Aligned.out.2017-07-07.16-13-08.samtools.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Part3-Pfeiffer2_Aligned.out.2017-07-07.16-13-08.bamsort.stderr
    jobid: 541
    wildcards: sampleSBB=Part3-Pfeiffer2_Aligned.out, pathSBB=output/bam


rule sortBAM_biobambam:
    input: output/bam/Part1-Pfeiffer3_Aligned.out.bam
    output: output/bam/Part1-Pfeiffer3_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Part1-Pfeiffer3_Aligned.out.2017-07-07.16-13-08.samtools.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Part1-Pfeiffer3_Aligned.out.2017-07-07.16-13-08.bamsort.stderr
    jobid: 537
    wildcards: sampleSBB=Part1-Pfeiffer3_Aligned.out, pathSBB=output/bam


rule sortBAM_biobambam:
    input: output/bam/Part3-Pfeiffer3_Aligned.out.bam
    output: output/bam/Part3-Pfeiffer3_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Part3-Pfeiffer3_Aligned.out.2017-07-07.16-13-08.samtools.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Part3-Pfeiffer3_Aligned.out.2017-07-07.16-13-08.bamsort.stderr
    jobid: 536
    wildcards: sampleSBB=Part3-Pfeiffer3_Aligned.out, pathSBB=output/bam


rule sortBAM_biobambam:
    input: output/bam/Part2-Pfeiffer3_Aligned.out.bam
    output: output/bam/Part2-Pfeiffer3_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Part2-Pfeiffer3_Aligned.out.2017-07-07.16-13-08.samtools.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Part2-Pfeiffer3_Aligned.out.2017-07-07.16-13-08.bamsort.stderr
    jobid: 538
    wildcards: sampleSBB=Part2-Pfeiffer3_Aligned.out, pathSBB=output/bam


rule filteredBAM:
    input: output/bam/Part2-Pfeiffer3_Aligned.out_sorted.bam
    output: output/bam/Part2-Pfeiffer3_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Part2-Pfeiffer3_Aligned.out_sorted.2017-07-07.16-13-08.stderr
    jobid: 531
    wildcards: sampleFB=Part2-Pfeiffer3_Aligned.out_sorted, pathFB=output/bam


rule filteredBAM:
    input: output/bam/Part1-Pfeiffer2_Aligned.out_sorted.bam
    output: output/bam/Part1-Pfeiffer2_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Part1-Pfeiffer2_Aligned.out_sorted.2017-07-07.16-13-08.stderr
    jobid: 533
    wildcards: sampleFB=Part1-Pfeiffer2_Aligned.out_sorted, pathFB=output/bam


rule filteredBAM:
    input: output/bam/Part1-Pfeiffer3_Aligned.out_sorted.bam
    output: output/bam/Part1-Pfeiffer3_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Part1-Pfeiffer3_Aligned.out_sorted.2017-07-07.16-13-08.stderr
    jobid: 530
    wildcards: sampleFB=Part1-Pfeiffer3_Aligned.out_sorted, pathFB=output/bam


rule filteredBAM:
    input: output/bam/Part4-Pfeiffer2_Aligned.out_sorted.bam
    output: output/bam/Part4-Pfeiffer2_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Part4-Pfeiffer2_Aligned.out_sorted.2017-07-07.16-13-08.stderr
    jobid: 532
    wildcards: sampleFB=Part4-Pfeiffer2_Aligned.out_sorted, pathFB=output/bam


rule filteredBAM:
    input: output/bam/Part3-Pfeiffer3_Aligned.out_sorted.bam
    output: output/bam/Part3-Pfeiffer3_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Part3-Pfeiffer3_Aligned.out_sorted.2017-07-07.16-13-08.stderr
    jobid: 529
    wildcards: sampleFB=Part3-Pfeiffer3_Aligned.out_sorted, pathFB=output/bam


rule filteredBAM:
    input: output/bam/Part2-Pfeiffer2_Aligned.out_sorted.bam
    output: output/bam/Part2-Pfeiffer2_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Part2-Pfeiffer2_Aligned.out_sorted.2017-07-07.16-13-08.stderr
    jobid: 535
    wildcards: sampleFB=Part2-Pfeiffer2_Aligned.out_sorted, pathFB=output/bam


rule filteredBAM:
    input: output/bam/Part3-Pfeiffer2_Aligned.out_sorted.bam
    output: output/bam/Part3-Pfeiffer2_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Part3-Pfeiffer2_Aligned.out_sorted.2017-07-07.16-13-08.stderr
    jobid: 534
    wildcards: sampleFB=Part3-Pfeiffer2_Aligned.out_sorted, pathFB=output/bam


rule mergeBAM:
    input: output/bam/Part1-Pfeiffer3_Aligned.out_sorted_filtered.bam, output/bam/Part2-Pfeiffer3_Aligned.out_sorted_filtered.bam, output/bam/Part3-Pfeiffer3_Aligned.out_sorted_filtered.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/mergeBAM/mergeBAM.2017-07-07.16-13-08.stderr
    jobid: 527
    wildcards: sampleMB=Pfeiffer3


rule mergeBAM:
    input: output/bam/Part1-Pfeiffer2_Aligned.out_sorted_filtered.bam, output/bam/Part2-Pfeiffer2_Aligned.out_sorted_filtered.bam, output/bam/Part3-Pfeiffer2_Aligned.out_sorted_filtered.bam, output/bam/Part4-Pfeiffer2_Aligned.out_sorted_filtered.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/mergeBAM/mergeBAM.2017-07-07.16-13-08.stderr
    jobid: 528
    wildcards: sampleMB=Pfeiffer2


rule markdupBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam, output/metrics/Pfeiffer2_Aligned.out_sorted_filtered.dup_metrics
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer2_Aligned.out_sorted_filtered.2017-07-07.16-13-08.biobammarkdup.stderr
    jobid: 526
    wildcards: sampleMDB=Pfeiffer2_Aligned.out_sorted_filtered, outputDIR=output


rule markdupBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam, output/metrics/Pfeiffer3_Aligned.out_sorted_filtered.dup_metrics
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer3_Aligned.out_sorted_filtered.2017-07-07.16-13-08.biobammarkdup.stderr
    jobid: 525
    wildcards: sampleMDB=Pfeiffer3_Aligned.out_sorted_filtered, outputDIR=output


rule indexBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam.bai, output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer2.2017-07-07.16-13-08.stderr
    jobid: 524
    wildcards: sampleIB=Pfeiffer2, outputDIR=output


rule indexBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam.bai, output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer3.2017-07-07.16-13-08.stderr
    jobid: 523
    wildcards: sampleIB=Pfeiffer3, outputDIR=output


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_15.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 375
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_15


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000192.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 299
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000192.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000212.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 432
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000212.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000238.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 422
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000238.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000224.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 302
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000224.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000200.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 392
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000200.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_16.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 332
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_16


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000243.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 275
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000243.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000230.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 285
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000230.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000231.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 410
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000231.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000216.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 301
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000216.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000201.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 354
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000201.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000230.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 435
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000230.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_12.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 409
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_12


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000194.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 290
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000194.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000225.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 382
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000225.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_22.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 363
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_22


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000227.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 399
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000227.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_6.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 437
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_6


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000218.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 274
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000218.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000243.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 364
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000243.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000247.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 371
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000247.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_13.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 355
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_13


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000209.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 295
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000209.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000226.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 427
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000226.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000197.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 415
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000197.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000239.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 294
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000239.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_20.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 425
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_20


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_7.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 348
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_7


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_14.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 316
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_14


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000205.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 402
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000205.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000214.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 357
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000214.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_3.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 398
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_3


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000248.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 430
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000248.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000198.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 386
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000198.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000232.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 436
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000232.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000194.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 434
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000194.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000246.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 337
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000246.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000231.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 313
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000231.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_12.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 317
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_12


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_13.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 309
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_13


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000249.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 429
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000249.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_X.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 358
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_X


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000227.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 271
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000227.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000220.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 362
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000220.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_10.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 338
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_10


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000245.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 308
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000245.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000203.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 278
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000203.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_3.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 324
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_3


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_21.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 414
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_21


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000208.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 351
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000208.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000215.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 352
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000215.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000191.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 431
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000191.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000229.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 360
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000229.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000242.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 376
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000242.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000205.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 322
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000205.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000202.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 292
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000202.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000213.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 377
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000213.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000219.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 385
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000219.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_9.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 282
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_9


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000203.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 404
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000203.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000199.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 339
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000199.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_2.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 319
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_2


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_11.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 372
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_11


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_15.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 305
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_15


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000210.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 412
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000210.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_10.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 403
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_10


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000204.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 334
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000204.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000218.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 421
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000218.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000237.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 350
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000237.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_18.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 310
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_18


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000235.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 323
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000235.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_8.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 286
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_8


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000222.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 418
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000222.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000208.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 356
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000208.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000222.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 330
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000222.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000217.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 342
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000217.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_4.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 287
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_4


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_4.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 406
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_4


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000245.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 417
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000245.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000228.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 318
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000228.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000213.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 293
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000213.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_19.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 405
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_19


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_Y.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 390
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_Y


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000241.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 361
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000241.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000195.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 389
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000195.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000224.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 393
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000224.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000214.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 289
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000214.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000233.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 321
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000233.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000234.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 367
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000234.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_5.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 407
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_5


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000236.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 397
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000236.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000237.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 428
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000237.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000240.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 391
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000240.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000244.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 365
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000244.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000192.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 366
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000192.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_17.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 374
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_17


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 279
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000201.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 388
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000201.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000240.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 307
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000240.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_20.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 349
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_20


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000220.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 341
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000220.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_6.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 343
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_6


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000233.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 408
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000233.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000221.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 413
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000221.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_9.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 373
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_9


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000223.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 370
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000223.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000199.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 400
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000199.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000191.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 325
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000191.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000244.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 347
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000244.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000209.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 379
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000209.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000232.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 336
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000232.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_MT.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 297
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_MT


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000225.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 273
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000225.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000234.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 280
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000234.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000226.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 277
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000226.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_7.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 381
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_7


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000215.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 359
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000215.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000221.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 312
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000221.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000238.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 333
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000238.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_11.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 314
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_11


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000242.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 291
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000242.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_14.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 401
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_14


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000223.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 311
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000223.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_16.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 368
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_16


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000229.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 276
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000229.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000197.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 288
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000197.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000193.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 328
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000193.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_8.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 433
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_8


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000200.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 284
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000200.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000207.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 384
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000207.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000206.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 344
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000206.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_19.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 331
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_19


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000206.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 424
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000206.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000210.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 272
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000210.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000235.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 419
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000235.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_18.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 416
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_18


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_2.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 438
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_2


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_X.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 335
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_X


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000248.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 303
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000248.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000239.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 387
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000239.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000202.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 423
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000202.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000236.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 327
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000236.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000217.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 378
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000217.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000211.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 394
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000211.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000216.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 383
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000216.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000241.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 296
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000241.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000247.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 340
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000247.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000193.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 420
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000193.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000219.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 304
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000219.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000196.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 411
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000196.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000204.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 395
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000204.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_5.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 298
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_5


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000195.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 283
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000195.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 426
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_MT.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 380
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_MT


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000196.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 345
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000196.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_17.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 320
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_17


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000228.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 396
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000228.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_22.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 315
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_22


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000211.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 306
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000211.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000198.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 281
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000198.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000207.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 329
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000207.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2_GL000246.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-13-08.mpileup.stderr
    jobid: 369
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000246.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000212.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 353
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000212.1


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_21.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 326
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_21


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_Y.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 346
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_Y


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3_GL000249.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-13-08.mpileup.stderr
    jobid: 300
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000249.1


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000194.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000194.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000194.1.snp.2017-07-07.16-13-08.stderr
    jobid: 446
    wildcards: chrMPU2VCFS=_GL000194.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000243.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000243.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000243.1.snp.2017-07-07.16-13-08.stderr
    jobid: 198
    wildcards: chrMPU2VCFS=_GL000243.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000211.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000211.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000211.1.snp.2017-07-07.16-13-08.stderr
    jobid: 514
    wildcards: chrMPU2VCFS=_GL000211.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000218.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000218.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000218.1.snp.2017-07-07.16-13-08.stderr
    jobid: 501
    wildcards: chrMPU2VCFS=_GL000218.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000237.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000237.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000237.1.snp.2017-07-07.16-13-08.stderr
    jobid: 217
    wildcards: chrMPU2VCFS=_GL000237.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_6.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_6.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_6.snp.2017-07-07.16-13-08.stderr
    jobid: 226
    wildcards: chrMPU2VCFS=_6, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000236.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000236.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000236.1.snp.2017-07-07.16-13-08.stderr
    jobid: 482
    wildcards: chrMPU2VCFS=_GL000236.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000249.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000249.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000249.1.snp.2017-07-07.16-13-08.stderr
    jobid: 452
    wildcards: chrMPU2VCFS=_GL000249.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_7.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_7.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_7.snp.2017-07-07.16-13-08.stderr
    jobid: 496
    wildcards: chrMPU2VCFS=_7, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000246.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000246.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000246.1.snp.2017-07-07.16-13-08.stderr
    jobid: 252
    wildcards: chrMPU2VCFS=_GL000246.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000201.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000201.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000201.1.snp.2017-07-07.16-13-08.stderr
    jobid: 507
    wildcards: chrMPU2VCFS=_GL000201.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000215.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000215.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000215.1.snp.2017-07-07.16-13-08.stderr
    jobid: 258
    wildcards: chrMPU2VCFS=_GL000215.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000195.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000195.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000195.1.snp.2017-07-07.16-13-08.stderr
    jobid: 512
    wildcards: chrMPU2VCFS=_GL000195.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000222.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000222.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000222.1.snp.2017-07-07.16-13-08.stderr
    jobid: 269
    wildcards: chrMPU2VCFS=_GL000222.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_MT.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_MT.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_MT.snp.2017-07-07.16-13-08.stderr
    jobid: 506
    wildcards: chrMPU2VCFS=_MT, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000210.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000210.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000210.1.snp.2017-07-07.16-13-08.stderr
    jobid: 443
    wildcards: chrMPU2VCFS=_GL000210.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000206.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000206.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000206.1.snp.2017-07-07.16-13-08.stderr
    jobid: 474
    wildcards: chrMPU2VCFS=_GL000206.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000231.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000231.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000231.1.snp.2017-07-07.16-13-08.stderr
    jobid: 188
    wildcards: chrMPU2VCFS=_GL000231.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_10.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_10.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_10.snp.2017-07-07.16-13-08.stderr
    jobid: 445
    wildcards: chrMPU2VCFS=_10, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000203.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000203.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000203.1.snp.2017-07-07.16-13-08.stderr
    jobid: 202
    wildcards: chrMPU2VCFS=_GL000203.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000229.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000229.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000229.1.snp.2017-07-07.16-13-08.stderr
    jobid: 448
    wildcards: chrMPU2VCFS=_GL000229.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_4.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_4.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_4.snp.2017-07-07.16-13-08.stderr
    jobid: 199
    wildcards: chrMPU2VCFS=_4, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000248.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000248.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000248.1.snp.2017-07-07.16-13-08.stderr
    jobid: 270
    wildcards: chrMPU2VCFS=_GL000248.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_1.snp.2017-07-07.16-13-08.stderr
    jobid: 458
    wildcards: chrMPU2VCFS=_1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000216.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000216.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000216.1.snp.2017-07-07.16-13-08.stderr
    jobid: 205
    wildcards: chrMPU2VCFS=_GL000216.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000235.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000235.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000235.1.snp.2017-07-07.16-13-08.stderr
    jobid: 461
    wildcards: chrMPU2VCFS=_GL000235.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000208.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000208.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000208.1.snp.2017-07-07.16-13-08.stderr
    jobid: 209
    wildcards: chrMPU2VCFS=_GL000208.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000222.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000222.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000222.1.snp.2017-07-07.16-13-08.stderr
    jobid: 466
    wildcards: chrMPU2VCFS=_GL000222.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000228.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000228.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000228.1.snp.2017-07-07.16-13-08.stderr
    jobid: 467
    wildcards: chrMPU2VCFS=_GL000228.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_21.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_21.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_21.snp.2017-07-07.16-13-08.stderr
    jobid: 509
    wildcards: chrMPU2VCFS=_21, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000195.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000195.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000195.1.snp.2017-07-07.16-13-08.stderr
    jobid: 215
    wildcards: chrMPU2VCFS=_GL000195.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_8.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_8.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_8.snp.2017-07-07.16-13-08.stderr
    jobid: 450
    wildcards: chrMPU2VCFS=_8, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_19.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_19.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_19.snp.2017-07-07.16-13-08.stderr
    jobid: 476
    wildcards: chrMPU2VCFS=_19, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000248.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000248.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000248.1.snp.2017-07-07.16-13-08.stderr
    jobid: 447
    wildcards: chrMPU2VCFS=_GL000248.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_Y.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_Y.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_Y.snp.2017-07-07.16-13-08.stderr
    jobid: 477
    wildcards: chrMPU2VCFS=_Y, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000233.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000233.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000233.1.snp.2017-07-07.16-13-08.stderr
    jobid: 231
    wildcards: chrMPU2VCFS=_GL000233.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000214.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000214.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000214.1.snp.2017-07-07.16-13-08.stderr
    jobid: 232
    wildcards: chrMPU2VCFS=_GL000214.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_MT.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_MT.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_MT.snp.2017-07-07.16-13-08.stderr
    jobid: 240
    wildcards: chrMPU2VCFS=_MT, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000200.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000200.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000200.1.snp.2017-07-07.16-13-08.stderr
    jobid: 491
    wildcards: chrMPU2VCFS=_GL000200.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000224.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000224.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000224.1.snp.2017-07-07.16-13-08.stderr
    jobid: 493
    wildcards: chrMPU2VCFS=_GL000224.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_20.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_20.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_20.snp.2017-07-07.16-13-08.stderr
    jobid: 463
    wildcards: chrMPU2VCFS=_20, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_10.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_10.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_10.snp.2017-07-07.16-13-08.stderr
    jobid: 242
    wildcards: chrMPU2VCFS=_10, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000225.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000225.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000225.1.snp.2017-07-07.16-13-08.stderr
    jobid: 504
    wildcards: chrMPU2VCFS=_GL000225.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_17.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_17.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_17.snp.2017-07-07.16-13-08.stderr
    jobid: 254
    wildcards: chrMPU2VCFS=_17, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000196.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000196.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000196.1.snp.2017-07-07.16-13-08.stderr
    jobid: 255
    wildcards: chrMPU2VCFS=_GL000196.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_18.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_18.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_18.snp.2017-07-07.16-13-08.stderr
    jobid: 265
    wildcards: chrMPU2VCFS=_18, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000230.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000230.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000230.1.snp.2017-07-07.16-13-08.stderr
    jobid: 266
    wildcards: chrMPU2VCFS=_GL000230.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000231.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000231.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000231.1.snp.2017-07-07.16-13-08.stderr
    jobid: 440
    wildcards: chrMPU2VCFS=_GL000231.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000202.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000202.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000202.1.snp.2017-07-07.16-13-08.stderr
    jobid: 206
    wildcards: chrMPU2VCFS=_GL000202.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000219.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000219.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000219.1.snp.2017-07-07.16-13-08.stderr
    jobid: 192
    wildcards: chrMPU2VCFS=_GL000219.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000217.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000217.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000217.1.snp.2017-07-07.16-13-08.stderr
    jobid: 253
    wildcards: chrMPU2VCFS=_GL000217.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000196.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000196.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000196.1.snp.2017-07-07.16-13-08.stderr
    jobid: 454
    wildcards: chrMPU2VCFS=_GL000196.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000229.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000229.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000229.1.snp.2017-07-07.16-13-08.stderr
    jobid: 201
    wildcards: chrMPU2VCFS=_GL000229.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_7.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_7.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_7.snp.2017-07-07.16-13-08.stderr
    jobid: 204
    wildcards: chrMPU2VCFS=_7, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000227.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000227.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000227.1.snp.2017-07-07.16-13-08.stderr
    jobid: 208
    wildcards: chrMPU2VCFS=_GL000227.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_14.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_14.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_14.snp.2017-07-07.16-13-08.stderr
    jobid: 468
    wildcards: chrMPU2VCFS=_14, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000203.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000203.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000203.1.snp.2017-07-07.16-13-08.stderr
    jobid: 483
    wildcards: chrMPU2VCFS=_GL000203.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000205.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000205.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000205.1.snp.2017-07-07.16-13-08.stderr
    jobid: 218
    wildcards: chrMPU2VCFS=_GL000205.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000202.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000202.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000202.1.snp.2017-07-07.16-13-08.stderr
    jobid: 473
    wildcards: chrMPU2VCFS=_GL000202.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000245.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000245.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000245.1.snp.2017-07-07.16-13-08.stderr
    jobid: 207
    wildcards: chrMPU2VCFS=_GL000245.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000210.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000210.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000210.1.snp.2017-07-07.16-13-08.stderr
    jobid: 225
    wildcards: chrMPU2VCFS=_GL000210.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000244.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000244.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000244.1.snp.2017-07-07.16-13-08.stderr
    jobid: 460
    wildcards: chrMPU2VCFS=_GL000244.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_15.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_15.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_15.snp.2017-07-07.16-13-08.stderr
    jobid: 498
    wildcards: chrMPU2VCFS=_15, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_22.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_22.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_22.snp.2017-07-07.16-13-08.stderr
    jobid: 503
    wildcards: chrMPU2VCFS=_22, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_15.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_15.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_15.snp.2017-07-07.16-13-08.stderr
    jobid: 191
    wildcards: chrMPU2VCFS=_15, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000242.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000242.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000242.1.snp.2017-07-07.16-13-08.stderr
    jobid: 239
    wildcards: chrMPU2VCFS=_GL000242.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000192.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000192.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000192.1.snp.2017-07-07.16-13-08.stderr
    jobid: 492
    wildcards: chrMPU2VCFS=_GL000192.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000236.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000236.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000236.1.snp.2017-07-07.16-13-08.stderr
    jobid: 235
    wildcards: chrMPU2VCFS=_GL000236.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_1.snp.2017-07-07.16-13-08.stderr
    jobid: 249
    wildcards: chrMPU2VCFS=_1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000200.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000200.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000200.1.snp.2017-07-07.16-13-08.stderr
    jobid: 212
    wildcards: chrMPU2VCFS=_GL000200.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000213.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000213.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000213.1.snp.2017-07-07.16-13-08.stderr
    jobid: 261
    wildcards: chrMPU2VCFS=_GL000213.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000206.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000206.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000206.1.snp.2017-07-07.16-13-08.stderr
    jobid: 241
    wildcards: chrMPU2VCFS=_GL000206.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000247.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000247.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000247.1.snp.2017-07-07.16-13-08.stderr
    jobid: 518
    wildcards: chrMPU2VCFS=_GL000247.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000239.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000239.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000239.1.snp.2017-07-07.16-13-08.stderr
    jobid: 268
    wildcards: chrMPU2VCFS=_GL000239.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000197.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000197.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000197.1.snp.2017-07-07.16-13-08.stderr
    jobid: 189
    wildcards: chrMPU2VCFS=_GL000197.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000243.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000243.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000243.1.snp.2017-07-07.16-13-08.stderr
    jobid: 444
    wildcards: chrMPU2VCFS=_GL000243.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000193.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000193.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000193.1.snp.2017-07-07.16-13-08.stderr
    jobid: 194
    wildcards: chrMPU2VCFS=_GL000193.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000198.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000198.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000198.1.snp.2017-07-07.16-13-08.stderr
    jobid: 520
    wildcards: chrMPU2VCFS=_GL000198.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000234.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000234.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000234.1.snp.2017-07-07.16-13-08.stderr
    jobid: 442
    wildcards: chrMPU2VCFS=_GL000234.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_12.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_12.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_12.snp.2017-07-07.16-13-08.stderr
    jobid: 213
    wildcards: chrMPU2VCFS=_12, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_18.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_18.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_18.snp.2017-07-07.16-13-08.stderr
    jobid: 441
    wildcards: chrMPU2VCFS=_18, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000191.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000191.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000191.1.snp.2017-07-07.16-13-08.stderr
    jobid: 216
    wildcards: chrMPU2VCFS=_GL000191.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000221.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000221.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000221.1.snp.2017-07-07.16-13-08.stderr
    jobid: 228
    wildcards: chrMPU2VCFS=_GL000221.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000227.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000227.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000227.1.snp.2017-07-07.16-13-08.stderr
    jobid: 481
    wildcards: chrMPU2VCFS=_GL000227.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000220.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000220.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000220.1.snp.2017-07-07.16-13-08.stderr
    jobid: 237
    wildcards: chrMPU2VCFS=_GL000220.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000194.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000194.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000194.1.snp.2017-07-07.16-13-08.stderr
    jobid: 244
    wildcards: chrMPU2VCFS=_GL000194.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_16.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_16.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_16.snp.2017-07-07.16-13-08.stderr
    jobid: 497
    wildcards: chrMPU2VCFS=_16, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_14.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_14.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_14.snp.2017-07-07.16-13-08.stderr
    jobid: 195
    wildcards: chrMPU2VCFS=_14, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000192.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000192.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000192.1.snp.2017-07-07.16-13-08.stderr
    jobid: 259
    wildcards: chrMPU2VCFS=_GL000192.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000230.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000230.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000230.1.snp.2017-07-07.16-13-08.stderr
    jobid: 517
    wildcards: chrMPU2VCFS=_GL000230.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000244.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000244.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000244.1.snp.2017-07-07.16-13-08.stderr
    jobid: 190
    wildcards: chrMPU2VCFS=_GL000244.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000232.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000232.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000232.1.snp.2017-07-07.16-13-08.stderr
    jobid: 464
    wildcards: chrMPU2VCFS=_GL000232.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_2.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_2.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_2.snp.2017-07-07.16-13-08.stderr
    jobid: 196
    wildcards: chrMPU2VCFS=_2, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000221.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000221.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000221.1.snp.2017-07-07.16-13-08.stderr
    jobid: 456
    wildcards: chrMPU2VCFS=_GL000221.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000211.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000211.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000211.1.snp.2017-07-07.16-13-08.stderr
    jobid: 210
    wildcards: chrMPU2VCFS=_GL000211.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_19.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_19.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_19.snp.2017-07-07.16-13-08.stderr
    jobid: 211
    wildcards: chrMPU2VCFS=_19, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000212.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000212.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000212.1.snp.2017-07-07.16-13-08.stderr
    jobid: 470
    wildcards: chrMPU2VCFS=_GL000212.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000213.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000213.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000213.1.snp.2017-07-07.16-13-08.stderr
    jobid: 475
    wildcards: chrMPU2VCFS=_GL000213.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000207.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000207.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000207.1.snp.2017-07-07.16-13-08.stderr
    jobid: 203
    wildcards: chrMPU2VCFS=_GL000207.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_X.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_X.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_X.snp.2017-07-07.16-13-08.stderr
    jobid: 484
    wildcards: chrMPU2VCFS=_X, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_11.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_11.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_11.snp.2017-07-07.16-13-08.stderr
    jobid: 238
    wildcards: chrMPU2VCFS=_11, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000207.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000207.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000207.1.snp.2017-07-07.16-13-08.stderr
    jobid: 478
    wildcards: chrMPU2VCFS=_GL000207.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000220.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000220.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000220.1.snp.2017-07-07.16-13-08.stderr
    jobid: 490
    wildcards: chrMPU2VCFS=_GL000220.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000246.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000246.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000246.1.snp.2017-07-07.16-13-08.stderr
    jobid: 515
    wildcards: chrMPU2VCFS=_GL000246.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000219.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000219.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000219.1.snp.2017-07-07.16-13-08.stderr
    jobid: 519
    wildcards: chrMPU2VCFS=_GL000219.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_13.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_13.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_13.snp.2017-07-07.16-13-08.stderr
    jobid: 245
    wildcards: chrMPU2VCFS=_13, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000224.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000224.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000224.1.snp.2017-07-07.16-13-08.stderr
    jobid: 246
    wildcards: chrMPU2VCFS=_GL000224.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000233.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000233.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000233.1.snp.2017-07-07.16-13-08.stderr
    jobid: 495
    wildcards: chrMPU2VCFS=_GL000233.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000232.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000232.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000232.1.snp.2017-07-07.16-13-08.stderr
    jobid: 251
    wildcards: chrMPU2VCFS=_GL000232.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_5.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_5.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_5.snp.2017-07-07.16-13-08.stderr
    jobid: 256
    wildcards: chrMPU2VCFS=_5, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_12.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_12.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_12.snp.2017-07-07.16-13-08.stderr
    jobid: 516
    wildcards: chrMPU2VCFS=_12, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000238.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000238.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000238.1.snp.2017-07-07.16-13-08.stderr
    jobid: 263
    wildcards: chrMPU2VCFS=_GL000238.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_9.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_9.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_9.snp.2017-07-07.16-13-08.stderr
    jobid: 248
    wildcards: chrMPU2VCFS=_9, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000215.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000215.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000215.1.snp.2017-07-07.16-13-08.stderr
    jobid: 449
    wildcards: chrMPU2VCFS=_GL000215.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000242.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000242.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000242.1.snp.2017-07-07.16-13-08.stderr
    jobid: 451
    wildcards: chrMPU2VCFS=_GL000242.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_22.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_22.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_22.snp.2017-07-07.16-13-08.stderr
    jobid: 197
    wildcards: chrMPU2VCFS=_22, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_17.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_17.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_17.snp.2017-07-07.16-13-08.stderr
    jobid: 459
    wildcards: chrMPU2VCFS=_17, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_13.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_13.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_13.snp.2017-07-07.16-13-08.stderr
    jobid: 472
    wildcards: chrMPU2VCFS=_13, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_4.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_4.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_4.snp.2017-07-07.16-13-08.stderr
    jobid: 505
    wildcards: chrMPU2VCFS=_4, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000247.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000247.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000247.1.snp.2017-07-07.16-13-08.stderr
    jobid: 222
    wildcards: chrMPU2VCFS=_GL000247.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000235.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000235.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000235.1.snp.2017-07-07.16-13-08.stderr
    jobid: 223
    wildcards: chrMPU2VCFS=_GL000235.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000218.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000218.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000218.1.snp.2017-07-07.16-13-08.stderr
    jobid: 227
    wildcards: chrMPU2VCFS=_GL000218.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000201.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000201.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000201.1.snp.2017-07-07.16-13-08.stderr
    jobid: 233
    wildcards: chrMPU2VCFS=_GL000201.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000204.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000204.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000204.1.snp.2017-07-07.16-13-08.stderr
    jobid: 234
    wildcards: chrMPU2VCFS=_GL000204.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000240.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000240.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000240.1.snp.2017-07-07.16-13-08.stderr
    jobid: 224
    wildcards: chrMPU2VCFS=_GL000240.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000191.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000191.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000191.1.snp.2017-07-07.16-13-08.stderr
    jobid: 488
    wildcards: chrMPU2VCFS=_GL000191.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000208.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000208.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000208.1.snp.2017-07-07.16-13-08.stderr
    jobid: 455
    wildcards: chrMPU2VCFS=_GL000208.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000234.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000234.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000234.1.snp.2017-07-07.16-13-08.stderr
    jobid: 243
    wildcards: chrMPU2VCFS=_GL000234.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000241.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000241.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000241.1.snp.2017-07-07.16-13-08.stderr
    jobid: 479
    wildcards: chrMPU2VCFS=_GL000241.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000241.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000241.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000241.1.snp.2017-07-07.16-13-08.stderr
    jobid: 250
    wildcards: chrMPU2VCFS=_GL000241.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000225.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000225.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000225.1.snp.2017-07-07.16-13-08.stderr
    jobid: 257
    wildcards: chrMPU2VCFS=_GL000225.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000214.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000214.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000214.1.snp.2017-07-07.16-13-08.stderr
    jobid: 510
    wildcards: chrMPU2VCFS=_GL000214.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000197.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000197.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000197.1.snp.2017-07-07.16-13-08.stderr
    jobid: 513
    wildcards: chrMPU2VCFS=_GL000197.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000249.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000249.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000249.1.snp.2017-07-07.16-13-08.stderr
    jobid: 260
    wildcards: chrMPU2VCFS=_GL000249.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_11.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_11.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_11.snp.2017-07-07.16-13-08.stderr
    jobid: 521
    wildcards: chrMPU2VCFS=_11, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000204.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000204.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000204.1.snp.2017-07-07.16-13-08.stderr
    jobid: 439
    wildcards: chrMPU2VCFS=_GL000204.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_3.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_3.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_3.snp.2017-07-07.16-13-08.stderr
    jobid: 457
    wildcards: chrMPU2VCFS=_3, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000209.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000209.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000209.1.snp.2017-07-07.16-13-08.stderr
    jobid: 193
    wildcards: chrMPU2VCFS=_GL000209.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_8.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_8.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_8.snp.2017-07-07.16-13-08.stderr
    jobid: 187
    wildcards: chrMPU2VCFS=_8, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000209.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000209.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000209.1.snp.2017-07-07.16-13-08.stderr
    jobid: 453
    wildcards: chrMPU2VCFS=_GL000209.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_X.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_X.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_X.snp.2017-07-07.16-13-08.stderr
    jobid: 200
    wildcards: chrMPU2VCFS=_X, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000240.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000240.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000240.1.snp.2017-07-07.16-13-08.stderr
    jobid: 522
    wildcards: chrMPU2VCFS=_GL000240.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000228.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000228.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000228.1.snp.2017-07-07.16-13-08.stderr
    jobid: 214
    wildcards: chrMPU2VCFS=_GL000228.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000199.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000199.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000199.1.snp.2017-07-07.16-13-08.stderr
    jobid: 480
    wildcards: chrMPU2VCFS=_GL000199.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_16.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_16.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_16.snp.2017-07-07.16-13-08.stderr
    jobid: 230
    wildcards: chrMPU2VCFS=_16, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000223.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000223.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000223.1.snp.2017-07-07.16-13-08.stderr
    jobid: 485
    wildcards: chrMPU2VCFS=_GL000223.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_3.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_3.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_3.snp.2017-07-07.16-13-08.stderr
    jobid: 236
    wildcards: chrMPU2VCFS=_3, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000217.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000217.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000217.1.snp.2017-07-07.16-13-08.stderr
    jobid: 494
    wildcards: chrMPU2VCFS=_GL000217.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000245.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000245.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000245.1.snp.2017-07-07.16-13-08.stderr
    jobid: 508
    wildcards: chrMPU2VCFS=_GL000245.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000237.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000237.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000237.1.snp.2017-07-07.16-13-08.stderr
    jobid: 499
    wildcards: chrMPU2VCFS=_GL000237.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_9.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_9.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_9.snp.2017-07-07.16-13-08.stderr
    jobid: 500
    wildcards: chrMPU2VCFS=_9, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000212.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000212.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000212.1.snp.2017-07-07.16-13-08.stderr
    jobid: 264
    wildcards: chrMPU2VCFS=_GL000212.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_20.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_20.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_20.snp.2017-07-07.16-13-08.stderr
    jobid: 267
    wildcards: chrMPU2VCFS=_20, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000239.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000239.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000239.1.snp.2017-07-07.16-13-08.stderr
    jobid: 511
    wildcards: chrMPU2VCFS=_GL000239.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_5.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_5.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_5.snp.2017-07-07.16-13-08.stderr
    jobid: 462
    wildcards: chrMPU2VCFS=_5, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000238.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000238.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000238.1.snp.2017-07-07.16-13-08.stderr
    jobid: 469
    wildcards: chrMPU2VCFS=_GL000238.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000205.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000205.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000205.1.snp.2017-07-07.16-13-08.stderr
    jobid: 471
    wildcards: chrMPU2VCFS=_GL000205.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000223.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000223.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000223.1.snp.2017-07-07.16-13-08.stderr
    jobid: 219
    wildcards: chrMPU2VCFS=_GL000223.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000226.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000226.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000226.1.snp.2017-07-07.16-13-08.stderr
    jobid: 486
    wildcards: chrMPU2VCFS=_GL000226.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000198.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000198.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000198.1.snp.2017-07-07.16-13-08.stderr
    jobid: 229
    wildcards: chrMPU2VCFS=_GL000198.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000193.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000193.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000193.1.snp.2017-07-07.16-13-08.stderr
    jobid: 487
    wildcards: chrMPU2VCFS=_GL000193.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_21.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_21.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_21.snp.2017-07-07.16-13-08.stderr
    jobid: 220
    wildcards: chrMPU2VCFS=_21, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000216.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000216.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000216.1.snp.2017-07-07.16-13-08.stderr
    jobid: 465
    wildcards: chrMPU2VCFS=_GL000216.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_6.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_6.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_6.snp.2017-07-07.16-13-08.stderr
    jobid: 489
    wildcards: chrMPU2VCFS=_6, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000226.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000226.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000226.1.snp.2017-07-07.16-13-08.stderr
    jobid: 247
    wildcards: chrMPU2VCFS=_GL000226.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_2.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_2.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_2.snp.2017-07-07.16-13-08.stderr
    jobid: 502
    wildcards: chrMPU2VCFS=_2, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000199.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000199.1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000199.1.snp.2017-07-07.16-13-08.stderr
    jobid: 221
    wildcards: chrMPU2VCFS=_GL000199.1, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_Y.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_Y.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_Y.snp.2017-07-07.16-13-08.stderr
    jobid: 262
    wildcards: chrMPU2VCFS=_Y, varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000241.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000241.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000241.1.indel.2017-07-07.16-13-08.stderr
    jobid: 108
    wildcards: chrMPU2VCFS=_GL000241.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_18.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_18.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_18.indel.2017-07-07.16-13-08.stderr
    jobid: 57
    wildcards: chrMPU2VCFS=_18, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_22.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_22.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_22.indel.2017-07-07.16-13-08.stderr
    jobid: 62
    wildcards: chrMPU2VCFS=_22, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_17.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_17.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_17.indel.2017-07-07.16-13-08.stderr
    jobid: 121
    wildcards: chrMPU2VCFS=_17, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000213.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000213.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000213.1.indel.2017-07-07.16-13-08.stderr
    jobid: 40
    wildcards: chrMPU2VCFS=_GL000213.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000241.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000241.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000241.1.indel.2017-07-07.16-13-08.stderr
    jobid: 43
    wildcards: chrMPU2VCFS=_GL000241.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_MT.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_MT.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_MT.indel.2017-07-07.16-13-08.stderr
    jobid: 44
    wildcards: chrMPU2VCFS=_MT, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000224.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000224.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000224.1.indel.2017-07-07.16-13-08.stderr
    jobid: 49
    wildcards: chrMPU2VCFS=_GL000224.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_15.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_15.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_15.indel.2017-07-07.16-13-08.stderr
    jobid: 52
    wildcards: chrMPU2VCFS=_15, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000235.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000235.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000235.1.indel.2017-07-07.16-13-08.stderr
    jobid: 70
    wildcards: chrMPU2VCFS=_GL000235.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000204.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000204.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000204.1.indel.2017-07-07.16-13-08.stderr
    jobid: 81
    wildcards: chrMPU2VCFS=_GL000204.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000199.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000199.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000199.1.indel.2017-07-07.16-13-08.stderr
    jobid: 86
    wildcards: chrMPU2VCFS=_GL000199.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_X.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_X.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_X.indel.2017-07-07.16-13-08.stderr
    jobid: 105
    wildcards: chrMPU2VCFS=_X, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000218.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000218.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000218.1.indel.2017-07-07.16-13-08.stderr
    jobid: 21
    wildcards: chrMPU2VCFS=_GL000218.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000226.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000226.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000226.1.indel.2017-07-07.16-13-08.stderr
    jobid: 174
    wildcards: chrMPU2VCFS=_GL000226.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000230.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000230.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000230.1.indel.2017-07-07.16-13-08.stderr
    jobid: 182
    wildcards: chrMPU2VCFS=_GL000230.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000232.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000232.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000232.1.indel.2017-07-07.16-13-08.stderr
    jobid: 183
    wildcards: chrMPU2VCFS=_GL000232.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_13.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_13.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_13.indel.2017-07-07.16-13-08.stderr
    jobid: 102
    wildcards: chrMPU2VCFS=_13, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000214.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000214.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000214.1.indel.2017-07-07.16-13-08.stderr
    jobid: 104
    wildcards: chrMPU2VCFS=_GL000214.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000244.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000244.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000244.1.indel.2017-07-07.16-13-08.stderr
    jobid: 112
    wildcards: chrMPU2VCFS=_GL000244.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000217.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000217.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000217.1.indel.2017-07-07.16-13-08.stderr
    jobid: 89
    wildcards: chrMPU2VCFS=_GL000217.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000198.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000198.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000198.1.indel.2017-07-07.16-13-08.stderr
    jobid: 28
    wildcards: chrMPU2VCFS=_GL000198.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000234.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000234.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000234.1.indel.2017-07-07.16-13-08.stderr
    jobid: 114
    wildcards: chrMPU2VCFS=_GL000234.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_19.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_19.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_19.indel.2017-07-07.16-13-08.stderr
    jobid: 78
    wildcards: chrMPU2VCFS=_19, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_15.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_15.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_15.indel.2017-07-07.16-13-08.stderr
    jobid: 122
    wildcards: chrMPU2VCFS=_15, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000219.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000219.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000219.1.indel.2017-07-07.16-13-08.stderr
    jobid: 51
    wildcards: chrMPU2VCFS=_GL000219.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mergeVCF:
    input: output/vcfGenUtil_varScan/Pfeiffer2_1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_2.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_3.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_4.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_5.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_6.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_7.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_8.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_9.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_10.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_11.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_12.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_13.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_14.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_15.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_16.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_17.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_18.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_19.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_20.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_21.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_22.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_X.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_Y.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_MT.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000207.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000226.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000229.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000231.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000210.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000239.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000235.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000201.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000247.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000245.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000197.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000203.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000246.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000249.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000196.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000248.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000244.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000238.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000202.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000234.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000232.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000206.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000240.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000236.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000241.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000243.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000242.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000230.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000237.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000233.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000204.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000198.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000208.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000191.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000227.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000228.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000214.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000221.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000209.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000218.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000220.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000213.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000211.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000199.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000217.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000216.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000215.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000205.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000219.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000224.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000223.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000195.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000212.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000222.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000200.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000193.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000194.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000225.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000192.1.varScan.snp.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.vcf
    log: log/vcfUtil/mergeVCF/mergeVCF_Pfeiffer2.varScan.snp.2017-07-07.16-13-07.stderr
    jobid: 17
    wildcards: varTypeMVCF=snp, sampleMVCF=Pfeiffer2, vcfProgramMVCF=varScan, pathMV=output/vcfGenUtil_varScan


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_16.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_16.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_16.indel.2017-07-07.16-13-08.stderr
    jobid: 115
    wildcards: chrMPU2VCFS=_16, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000245.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000245.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000245.1.indel.2017-07-07.16-13-08.stderr
    jobid: 55
    wildcards: chrMPU2VCFS=_GL000245.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000240.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000240.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000240.1.indel.2017-07-07.16-13-08.stderr
    jobid: 138
    wildcards: chrMPU2VCFS=_GL000240.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000240.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000240.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000240.1.indel.2017-07-07.16-13-08.stderr
    jobid: 54
    wildcards: chrMPU2VCFS=_GL000240.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000247.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000247.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000247.1.indel.2017-07-07.16-13-08.stderr
    jobid: 118
    wildcards: chrMPU2VCFS=_GL000247.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_4.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_4.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_4.indel.2017-07-07.16-13-08.stderr
    jobid: 153
    wildcards: chrMPU2VCFS=_4, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000234.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000234.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000234.1.indel.2017-07-07.16-13-08.stderr
    jobid: 27
    wildcards: chrMPU2VCFS=_GL000234.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000200.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000200.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000200.1.indel.2017-07-07.16-13-08.stderr
    jobid: 139
    wildcards: chrMPU2VCFS=_GL000200.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000231.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000231.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000231.1.indel.2017-07-07.16-13-08.stderr
    jobid: 157
    wildcards: chrMPU2VCFS=_GL000231.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000236.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000236.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000236.1.indel.2017-07-07.16-13-08.stderr
    jobid: 74
    wildcards: chrMPU2VCFS=_GL000236.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000210.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000210.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000210.1.indel.2017-07-07.16-13-08.stderr
    jobid: 159
    wildcards: chrMPU2VCFS=_GL000210.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_5.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_5.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_5.indel.2017-07-07.16-13-08.stderr
    jobid: 154
    wildcards: chrMPU2VCFS=_5, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000221.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000221.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000221.1.indel.2017-07-07.16-13-08.stderr
    jobid: 160
    wildcards: chrMPU2VCFS=_GL000221.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000246.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000246.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000246.1.indel.2017-07-07.16-13-08.stderr
    jobid: 84
    wildcards: chrMPU2VCFS=_GL000246.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000245.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000245.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000245.1.indel.2017-07-07.16-13-08.stderr
    jobid: 164
    wildcards: chrMPU2VCFS=_GL000245.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000202.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000202.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000202.1.indel.2017-07-07.16-13-08.stderr
    jobid: 170
    wildcards: chrMPU2VCFS=_GL000202.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_20.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_20.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_20.indel.2017-07-07.16-13-08.stderr
    jobid: 172
    wildcards: chrMPU2VCFS=_20, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000194.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000194.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000194.1.indel.2017-07-07.16-13-08.stderr
    jobid: 37
    wildcards: chrMPU2VCFS=_GL000194.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_7.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_7.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_7.indel.2017-07-07.16-13-08.stderr
    jobid: 95
    wildcards: chrMPU2VCFS=_7, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000205.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000205.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000205.1.indel.2017-07-07.16-13-08.stderr
    jobid: 149
    wildcards: chrMPU2VCFS=_GL000205.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000248.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000248.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000248.1.indel.2017-07-07.16-13-08.stderr
    jobid: 177
    wildcards: chrMPU2VCFS=_GL000248.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000237.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000237.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000237.1.indel.2017-07-07.16-13-08.stderr
    jobid: 97
    wildcards: chrMPU2VCFS=_GL000237.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000212.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000212.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000212.1.indel.2017-07-07.16-13-08.stderr
    jobid: 100
    wildcards: chrMPU2VCFS=_GL000212.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000208.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000208.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000208.1.indel.2017-07-07.16-13-08.stderr
    jobid: 103
    wildcards: chrMPU2VCFS=_GL000208.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_7.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_7.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_7.indel.2017-07-07.16-13-08.stderr
    jobid: 128
    wildcards: chrMPU2VCFS=_7, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000217.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000217.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000217.1.indel.2017-07-07.16-13-08.stderr
    jobid: 125
    wildcards: chrMPU2VCFS=_GL000217.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_5.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_5.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_5.indel.2017-07-07.16-13-08.stderr
    jobid: 45
    wildcards: chrMPU2VCFS=_5, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000248.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000248.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000248.1.indel.2017-07-07.16-13-08.stderr
    jobid: 50
    wildcards: chrMPU2VCFS=_GL000248.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000236.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000236.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000236.1.indel.2017-07-07.16-13-08.stderr
    jobid: 144
    wildcards: chrMPU2VCFS=_GL000236.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000192.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000192.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000192.1.indel.2017-07-07.16-13-08.stderr
    jobid: 46
    wildcards: chrMPU2VCFS=_GL000192.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_3.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_3.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_3.indel.2017-07-07.16-13-08.stderr
    jobid: 71
    wildcards: chrMPU2VCFS=_3, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000210.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000210.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000210.1.indel.2017-07-07.16-13-08.stderr
    jobid: 19
    wildcards: chrMPU2VCFS=_GL000210.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000193.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000193.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000193.1.indel.2017-07-07.16-13-08.stderr
    jobid: 75
    wildcards: chrMPU2VCFS=_GL000193.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000238.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000238.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000238.1.indel.2017-07-07.16-13-08.stderr
    jobid: 80
    wildcards: chrMPU2VCFS=_GL000238.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_MT.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_MT.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_MT.indel.2017-07-07.16-13-08.stderr
    jobid: 127
    wildcards: chrMPU2VCFS=_MT, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000206.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000206.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000206.1.indel.2017-07-07.16-13-08.stderr
    jobid: 91
    wildcards: chrMPU2VCFS=_GL000206.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000195.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000195.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000195.1.indel.2017-07-07.16-13-08.stderr
    jobid: 136
    wildcards: chrMPU2VCFS=_GL000195.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000249.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000249.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000249.1.indel.2017-07-07.16-13-08.stderr
    jobid: 176
    wildcards: chrMPU2VCFS=_GL000249.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000199.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000199.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000199.1.indel.2017-07-07.16-13-08.stderr
    jobid: 147
    wildcards: chrMPU2VCFS=_GL000199.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000194.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000194.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000194.1.indel.2017-07-07.16-13-08.stderr
    jobid: 181
    wildcards: chrMPU2VCFS=_GL000194.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000229.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000229.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000229.1.indel.2017-07-07.16-13-08.stderr
    jobid: 23
    wildcards: chrMPU2VCFS=_GL000229.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000203.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000203.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000203.1.indel.2017-07-07.16-13-08.stderr
    jobid: 25
    wildcards: chrMPU2VCFS=_GL000203.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000246.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000246.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000246.1.indel.2017-07-07.16-13-08.stderr
    jobid: 116
    wildcards: chrMPU2VCFS=_GL000246.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_4.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_4.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_4.indel.2017-07-07.16-13-08.stderr
    jobid: 34
    wildcards: chrMPU2VCFS=_4, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000207.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000207.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000207.1.indel.2017-07-07.16-13-08.stderr
    jobid: 131
    wildcards: chrMPU2VCFS=_GL000207.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000201.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000201.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000201.1.indel.2017-07-07.16-13-08.stderr
    jobid: 135
    wildcards: chrMPU2VCFS=_GL000201.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_3.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_3.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_3.indel.2017-07-07.16-13-08.stderr
    jobid: 145
    wildcards: chrMPU2VCFS=_3, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000224.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000224.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000224.1.indel.2017-07-07.16-13-08.stderr
    jobid: 140
    wildcards: chrMPU2VCFS=_GL000224.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000221.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000221.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000221.1.indel.2017-07-07.16-13-08.stderr
    jobid: 59
    wildcards: chrMPU2VCFS=_GL000221.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_14.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_14.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_14.indel.2017-07-07.16-13-08.stderr
    jobid: 63
    wildcards: chrMPU2VCFS=_14, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000204.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000204.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000204.1.indel.2017-07-07.16-13-08.stderr
    jobid: 142
    wildcards: chrMPU2VCFS=_GL000204.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000233.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000233.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000233.1.indel.2017-07-07.16-13-08.stderr
    jobid: 155
    wildcards: chrMPU2VCFS=_GL000233.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000191.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000191.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000191.1.indel.2017-07-07.16-13-08.stderr
    jobid: 72
    wildcards: chrMPU2VCFS=_GL000191.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000207.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000207.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000207.1.indel.2017-07-07.16-13-08.stderr
    jobid: 76
    wildcards: chrMPU2VCFS=_GL000207.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mergeVCF:
    input: output/vcfGenUtil_varScan/Pfeiffer3_1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_2.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_3.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_4.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_5.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_6.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_7.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_8.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_9.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_10.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_11.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_12.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_13.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_14.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_15.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_16.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_17.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_18.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_19.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_20.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_21.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_22.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_X.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_Y.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_MT.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000207.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000226.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000229.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000231.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000210.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000239.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000235.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000201.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000247.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000245.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000197.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000203.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000246.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000249.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000196.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000248.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000244.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000238.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000202.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000234.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000232.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000206.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000240.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000236.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000241.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000243.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000242.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000230.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000237.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000233.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000204.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000198.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000208.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000191.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000227.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000228.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000214.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000221.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000209.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000218.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000220.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000213.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000211.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000199.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000217.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000216.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000215.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000205.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000219.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000224.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000223.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000195.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000212.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000222.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000200.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000193.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000194.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000225.1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000192.1.varScan.snp.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.vcf
    log: log/vcfUtil/mergeVCF/mergeVCF_Pfeiffer3.varScan.snp.2017-07-07.16-13-07.stderr
    jobid: 186
    wildcards: varTypeMVCF=snp, sampleMVCF=Pfeiffer3, vcfProgramMVCF=varScan, pathMV=output/vcfGenUtil_varScan


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_18.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_18.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_18.indel.2017-07-07.16-13-08.stderr
    jobid: 163
    wildcards: chrMPU2VCFS=_18, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_X.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_X.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_X.indel.2017-07-07.16-13-08.stderr
    jobid: 82
    wildcards: chrMPU2VCFS=_X, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000222.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000222.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000222.1.indel.2017-07-07.16-13-08.stderr
    jobid: 165
    wildcards: chrMPU2VCFS=_GL000222.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000193.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000193.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000193.1.indel.2017-07-07.16-13-08.stderr
    jobid: 167
    wildcards: chrMPU2VCFS=_GL000193.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000247.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000247.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000247.1.indel.2017-07-07.16-13-08.stderr
    jobid: 87
    wildcards: chrMPU2VCFS=_GL000247.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000238.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000238.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000238.1.indel.2017-07-07.16-13-08.stderr
    jobid: 169
    wildcards: chrMPU2VCFS=_GL000238.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_1.indel.2017-07-07.16-13-08.stderr
    jobid: 173
    wildcards: chrMPU2VCFS=_1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000228.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000228.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000228.1.indel.2017-07-07.16-13-08.stderr
    jobid: 143
    wildcards: chrMPU2VCFS=_GL000228.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000227.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000227.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000227.1.indel.2017-07-07.16-13-08.stderr
    jobid: 18
    wildcards: chrMPU2VCFS=_GL000227.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000225.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000225.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000225.1.indel.2017-07-07.16-13-08.stderr
    jobid: 20
    wildcards: chrMPU2VCFS=_GL000225.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000223.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000223.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000223.1.indel.2017-07-07.16-13-08.stderr
    jobid: 117
    wildcards: chrMPU2VCFS=_GL000223.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000214.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000214.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000214.1.indel.2017-07-07.16-13-08.stderr
    jobid: 36
    wildcards: chrMPU2VCFS=_GL000214.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000213.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000213.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000213.1.indel.2017-07-07.16-13-08.stderr
    jobid: 124
    wildcards: chrMPU2VCFS=_GL000213.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000209.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000209.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000209.1.indel.2017-07-07.16-13-08.stderr
    jobid: 126
    wildcards: chrMPU2VCFS=_GL000209.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000211.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000211.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000211.1.indel.2017-07-07.16-13-08.stderr
    jobid: 53
    wildcards: chrMPU2VCFS=_GL000211.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_13.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_13.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_13.indel.2017-07-07.16-13-08.stderr
    jobid: 56
    wildcards: chrMPU2VCFS=_13, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000230.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000230.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000230.1.indel.2017-07-07.16-13-08.stderr
    jobid: 32
    wildcards: chrMPU2VCFS=_GL000230.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_12.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_12.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_12.indel.2017-07-07.16-13-08.stderr
    jobid: 64
    wildcards: chrMPU2VCFS=_12, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000233.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000233.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000233.1.indel.2017-07-07.16-13-08.stderr
    jobid: 68
    wildcards: chrMPU2VCFS=_GL000233.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_17.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_17.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_17.indel.2017-07-07.16-13-08.stderr
    jobid: 67
    wildcards: chrMPU2VCFS=_17, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000243.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000243.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000243.1.indel.2017-07-07.16-13-08.stderr
    jobid: 22
    wildcards: chrMPU2VCFS=_GL000243.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_21.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_21.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_21.indel.2017-07-07.16-13-08.stderr
    jobid: 73
    wildcards: chrMPU2VCFS=_21, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000218.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000218.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000218.1.indel.2017-07-07.16-13-08.stderr
    jobid: 168
    wildcards: chrMPU2VCFS=_GL000218.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000215.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000215.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000215.1.indel.2017-07-07.16-13-08.stderr
    jobid: 106
    wildcards: chrMPU2VCFS=_GL000215.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000215.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000215.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000215.1.indel.2017-07-07.16-13-08.stderr
    jobid: 99
    wildcards: chrMPU2VCFS=_GL000215.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000239.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000239.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000239.1.indel.2017-07-07.16-13-08.stderr
    jobid: 41
    wildcards: chrMPU2VCFS=_GL000239.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000197.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000197.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000197.1.indel.2017-07-07.16-13-08.stderr
    jobid: 35
    wildcards: chrMPU2VCFS=_GL000197.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_11.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_11.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_11.indel.2017-07-07.16-13-08.stderr
    jobid: 119
    wildcards: chrMPU2VCFS=_11, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000242.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000242.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000242.1.indel.2017-07-07.16-13-08.stderr
    jobid: 38
    wildcards: chrMPU2VCFS=_GL000242.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000205.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000205.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000205.1.indel.2017-07-07.16-13-08.stderr
    jobid: 69
    wildcards: chrMPU2VCFS=_GL000205.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_6.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_6.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_6.indel.2017-07-07.16-13-08.stderr
    jobid: 184
    wildcards: chrMPU2VCFS=_6, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000232.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000232.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000232.1.indel.2017-07-07.16-13-08.stderr
    jobid: 83
    wildcards: chrMPU2VCFS=_GL000232.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_16.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_16.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_16.indel.2017-07-07.16-13-08.stderr
    jobid: 79
    wildcards: chrMPU2VCFS=_16, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_14.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_14.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_14.indel.2017-07-07.16-13-08.stderr
    jobid: 148
    wildcards: chrMPU2VCFS=_14, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000223.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000223.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000223.1.indel.2017-07-07.16-13-08.stderr
    jobid: 58
    wildcards: chrMPU2VCFS=_GL000223.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000228.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000228.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000228.1.indel.2017-07-07.16-13-08.stderr
    jobid: 65
    wildcards: chrMPU2VCFS=_GL000228.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_12.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_12.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_12.indel.2017-07-07.16-13-08.stderr
    jobid: 156
    wildcards: chrMPU2VCFS=_12, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000200.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000200.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000200.1.indel.2017-07-07.16-13-08.stderr
    jobid: 31
    wildcards: chrMPU2VCFS=_GL000200.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000222.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000222.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000222.1.indel.2017-07-07.16-13-08.stderr
    jobid: 77
    wildcards: chrMPU2VCFS=_GL000222.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000197.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000197.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000197.1.indel.2017-07-07.16-13-08.stderr
    jobid: 162
    wildcards: chrMPU2VCFS=_GL000197.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000235.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000235.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000235.1.indel.2017-07-07.16-13-08.stderr
    jobid: 166
    wildcards: chrMPU2VCFS=_GL000235.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000206.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000206.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000206.1.indel.2017-07-07.16-13-08.stderr
    jobid: 171
    wildcards: chrMPU2VCFS=_GL000206.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000220.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000220.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000220.1.indel.2017-07-07.16-13-08.stderr
    jobid: 88
    wildcards: chrMPU2VCFS=_GL000220.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000216.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000216.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000216.1.indel.2017-07-07.16-13-08.stderr
    jobid: 130
    wildcards: chrMPU2VCFS=_GL000216.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000196.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000196.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000196.1.indel.2017-07-07.16-13-08.stderr
    jobid: 158
    wildcards: chrMPU2VCFS=_GL000196.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000208.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000208.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000208.1.indel.2017-07-07.16-13-08.stderr
    jobid: 98
    wildcards: chrMPU2VCFS=_GL000208.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000220.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000220.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000220.1.indel.2017-07-07.16-13-08.stderr
    jobid: 109
    wildcards: chrMPU2VCFS=_GL000220.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000192.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000192.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000192.1.indel.2017-07-07.16-13-08.stderr
    jobid: 113
    wildcards: chrMPU2VCFS=_GL000192.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_1.indel.2017-07-07.16-13-08.stderr
    jobid: 26
    wildcards: chrMPU2VCFS=_1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000195.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000195.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000195.1.indel.2017-07-07.16-13-08.stderr
    jobid: 30
    wildcards: chrMPU2VCFS=_GL000195.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_8.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_8.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_8.indel.2017-07-07.16-13-08.stderr
    jobid: 33
    wildcards: chrMPU2VCFS=_8, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000227.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000227.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000227.1.indel.2017-07-07.16-13-08.stderr
    jobid: 146
    wildcards: chrMPU2VCFS=_GL000227.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000242.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000242.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000242.1.indel.2017-07-07.16-13-08.stderr
    jobid: 123
    wildcards: chrMPU2VCFS=_GL000242.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000202.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000202.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000202.1.indel.2017-07-07.16-13-08.stderr
    jobid: 39
    wildcards: chrMPU2VCFS=_GL000202.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000209.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000209.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000209.1.indel.2017-07-07.16-13-08.stderr
    jobid: 42
    wildcards: chrMPU2VCFS=_GL000209.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000196.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000196.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000196.1.indel.2017-07-07.16-13-08.stderr
    jobid: 92
    wildcards: chrMPU2VCFS=_GL000196.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000211.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000211.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000211.1.indel.2017-07-07.16-13-08.stderr
    jobid: 141
    wildcards: chrMPU2VCFS=_GL000211.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_11.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_11.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_11.indel.2017-07-07.16-13-08.stderr
    jobid: 61
    wildcards: chrMPU2VCFS=_11, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_10.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_10.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_10.indel.2017-07-07.16-13-08.stderr
    jobid: 150
    wildcards: chrMPU2VCFS=_10, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000219.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000219.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000219.1.indel.2017-07-07.16-13-08.stderr
    jobid: 132
    wildcards: chrMPU2VCFS=_GL000219.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_21.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_21.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_21.indel.2017-07-07.16-13-08.stderr
    jobid: 161
    wildcards: chrMPU2VCFS=_21, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000231.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000231.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000231.1.indel.2017-07-07.16-13-08.stderr
    jobid: 60
    wildcards: chrMPU2VCFS=_GL000231.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000239.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000239.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000239.1.indel.2017-07-07.16-13-08.stderr
    jobid: 134
    wildcards: chrMPU2VCFS=_GL000239.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_19.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_19.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_19.indel.2017-07-07.16-13-08.stderr
    jobid: 152
    wildcards: chrMPU2VCFS=_19, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_8.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_8.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_8.indel.2017-07-07.16-13-08.stderr
    jobid: 180
    wildcards: chrMPU2VCFS=_8, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000201.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000201.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000201.1.indel.2017-07-07.16-13-08.stderr
    jobid: 101
    wildcards: chrMPU2VCFS=_GL000201.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000229.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000229.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000229.1.indel.2017-07-07.16-13-08.stderr
    jobid: 107
    wildcards: chrMPU2VCFS=_GL000229.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_22.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_22.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_22.indel.2017-07-07.16-13-08.stderr
    jobid: 110
    wildcards: chrMPU2VCFS=_22, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_9.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_9.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_9.indel.2017-07-07.16-13-08.stderr
    jobid: 120
    wildcards: chrMPU2VCFS=_9, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000225.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000225.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000225.1.indel.2017-07-07.16-13-08.stderr
    jobid: 129
    wildcards: chrMPU2VCFS=_GL000225.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000198.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000198.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000198.1.indel.2017-07-07.16-13-08.stderr
    jobid: 133
    wildcards: chrMPU2VCFS=_GL000198.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000249.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000249.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000249.1.indel.2017-07-07.16-13-08.stderr
    jobid: 47
    wildcards: chrMPU2VCFS=_GL000249.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000216.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000216.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000216.1.indel.2017-07-07.16-13-08.stderr
    jobid: 48
    wildcards: chrMPU2VCFS=_GL000216.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_Y.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_Y.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_Y.indel.2017-07-07.16-13-08.stderr
    jobid: 137
    wildcards: chrMPU2VCFS=_Y, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000226.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000226.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000226.1.indel.2017-07-07.16-13-08.stderr
    jobid: 24
    wildcards: chrMPU2VCFS=_GL000226.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_2.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_2.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_2.indel.2017-07-07.16-13-08.stderr
    jobid: 66
    wildcards: chrMPU2VCFS=_2, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000243.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000243.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000243.1.indel.2017-07-07.16-13-08.stderr
    jobid: 111
    wildcards: chrMPU2VCFS=_GL000243.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000203.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000203.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000203.1.indel.2017-07-07.16-13-08.stderr
    jobid: 151
    wildcards: chrMPU2VCFS=_GL000203.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_10.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_10.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_10.indel.2017-07-07.16-13-08.stderr
    jobid: 85
    wildcards: chrMPU2VCFS=_10, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000191.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000191.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000191.1.indel.2017-07-07.16-13-08.stderr
    jobid: 178
    wildcards: chrMPU2VCFS=_GL000191.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_9.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_9.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_9.indel.2017-07-07.16-13-08.stderr
    jobid: 29
    wildcards: chrMPU2VCFS=_9, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_6.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_6.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_6.indel.2017-07-07.16-13-08.stderr
    jobid: 90
    wildcards: chrMPU2VCFS=_6, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000237.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000237.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000237.1.indel.2017-07-07.16-13-08.stderr
    jobid: 175
    wildcards: chrMPU2VCFS=_GL000237.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_Y.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_Y.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_Y.indel.2017-07-07.16-13-08.stderr
    jobid: 93
    wildcards: chrMPU2VCFS=_Y, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_20.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_20.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_20.indel.2017-07-07.16-13-08.stderr
    jobid: 96
    wildcards: chrMPU2VCFS=_20, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000212.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_GL000212.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000212.1.indel.2017-07-07.16-13-08.stderr
    jobid: 179
    wildcards: chrMPU2VCFS=_GL000212.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000244.1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_GL000244.1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000244.1.indel.2017-07-07.16-13-08.stderr
    jobid: 94
    wildcards: chrMPU2VCFS=_GL000244.1, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_2.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_2.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_2.indel.2017-07-07.16-13-08.stderr
    jobid: 185
    wildcards: chrMPU2VCFS=_2, varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2


rule mergeVCF:
    input: output/vcfGenUtil_varScan/Pfeiffer3_1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_2.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_3.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_4.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_5.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_6.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_7.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_8.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_9.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_10.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_11.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_12.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_13.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_14.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_15.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_16.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_17.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_18.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_19.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_20.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_21.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_22.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_X.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_Y.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_MT.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000207.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000226.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000229.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000231.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000210.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000239.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000235.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000201.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000247.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000245.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000197.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000203.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000246.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000249.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000196.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000248.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000244.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000238.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000202.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000234.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000232.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000206.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000240.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000236.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000241.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000243.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000242.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000230.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000237.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000233.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000204.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000198.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000208.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000191.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000227.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000228.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000214.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000221.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000209.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000218.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000220.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000213.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000211.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000199.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000217.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000216.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000215.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000205.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000219.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000224.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000223.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000195.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000212.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000222.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000200.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000193.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000194.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000225.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_GL000192.1.varScan.indel.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.vcf
    log: log/vcfUtil/mergeVCF/mergeVCF_Pfeiffer3.varScan.indel.2017-07-07.16-13-07.stderr
    jobid: 14
    wildcards: varTypeMVCF=indel, sampleMVCF=Pfeiffer3, vcfProgramMVCF=varScan, pathMV=output/vcfGenUtil_varScan


rule canonical:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical.summary.html, output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical.summary.genes.txt
    log: log/vcfGenUtil_varScan/canonical/canonical_Pfeiffer2.varScan.snp.2017-07-07.16-13-07.stderr
    jobid: 13
    wildcards: sampleCAN=Pfeiffer2.varScan.snp, pathCAN=vcfGenUtil_varScan


rule mergeVCF:
    input: output/vcfGenUtil_varScan/Pfeiffer2_1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_2.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_3.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_4.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_5.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_6.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_7.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_8.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_9.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_10.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_11.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_12.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_13.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_14.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_15.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_16.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_17.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_18.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_19.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_20.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_21.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_22.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_X.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_Y.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_MT.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000207.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000226.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000229.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000231.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000210.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000239.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000235.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000201.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000247.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000245.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000197.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000203.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000246.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000249.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000196.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000248.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000244.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000238.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000202.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000234.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000232.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000206.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000240.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000236.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000241.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000243.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000242.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000230.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000237.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000233.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000204.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000198.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000208.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000191.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000227.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000228.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000214.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000221.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000209.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000218.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000220.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000213.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000211.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000199.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000217.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000216.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000215.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000205.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000219.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000224.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000223.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000195.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000212.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000222.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000200.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000193.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000194.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000225.1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_GL000192.1.varScan.indel.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.vcf
    log: log/vcfUtil/mergeVCF/mergeVCF_Pfeiffer2.varScan.indel.2017-07-07.16-13-07.stderr
    jobid: 15
    wildcards: varTypeMVCF=indel, sampleMVCF=Pfeiffer2, vcfProgramMVCF=varScan, pathMV=output/vcfGenUtil_varScan


rule canonical:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical.summary.html, output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical.summary.genes.txt
    log: log/vcfGenUtil_varScan/canonical/canonical_Pfeiffer3.varScan.snp.2017-07-07.16-13-07.stderr
    jobid: 16
    wildcards: sampleCAN=Pfeiffer3.varScan.snp, pathCAN=vcfGenUtil_varScan


rule dbsnp:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated.vcf
    log: log/vcfGenUtil_varScan/dbsnp/dbsnp_Pfeiffer3.varScan.snp.canonical_annotated.2017-07-07.16-13-07.stderr
    jobid: 12
    wildcards: sampleDbSnp=Pfeiffer3.varScan.snp.canonical_annotated, pathDbSnp=output/vcfGenUtil_varScan


rule canonical:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.canonical_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.canonical.summary.html, output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.canonical.summary.genes.txt
    log: log/vcfGenUtil_varScan/canonical/canonical_Pfeiffer3.varScan.indel.2017-07-07.16-13-07.stderr
    jobid: 10
    wildcards: sampleCAN=Pfeiffer3.varScan.indel, pathCAN=vcfGenUtil_varScan


rule canonical:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.canonical_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.canonical.summary.html, output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.canonical.summary.genes.txt
    log: log/vcfGenUtil_varScan/canonical/canonical_Pfeiffer2.varScan.indel.2017-07-07.16-13-07.stderr
    jobid: 11
    wildcards: sampleCAN=Pfeiffer2.varScan.indel, pathCAN=vcfGenUtil_varScan


rule dbsnp:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated.vcf
    log: log/vcfGenUtil_varScan/dbsnp/dbsnp_Pfeiffer2.varScan.snp.canonical_annotated.2017-07-07.16-13-07.stderr
    jobid: 9
    wildcards: sampleDbSnp=Pfeiffer2.varScan.snp.canonical_annotated, pathDbSnp=output/vcfGenUtil_varScan


rule cosmic:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated.cosmic_annotated.vcf
    log: log/vcfGenUtil_varScan/cosmic/cosmic_Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated.2017-07-07.16-13-07.stderr
    jobid: 8
    wildcards: sampleCOS=Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated, pathCOS=output/vcfGenUtil_varScan


rule indel:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.canonical_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.canonical_annotated.indel_annotated.vcf
    log: log/vcfGenUtil_varScan/indel/indel_Pfeiffer2.varScan.indel.canonical_annotated.2017-07-07.16-13-07.1000g.log, log/vcfGenUtil_varScan/indel/indel_Pfeiffer2.varScan.indel.canonical_annotated.2017-07-07.16-13-07dbsnp.stderr, log/vcfGenUtil_varScan/indel/indel_Pfeiffer2.varScan.indel.canonical_annotated.2017-07-07.16-13-07.mills_100g.log
    jobid: 7
    wildcards: pathIndel=output/vcfGenUtil_varScan, sampleIndel=Pfeiffer2.varScan.indel.canonical_annotated


rule cosmic:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated.cosmic_annotated.vcf
    log: log/vcfGenUtil_varScan/cosmic/cosmic_Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated.2017-07-07.16-13-07.stderr
    jobid: 5
    wildcards: sampleCOS=Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated, pathCOS=output/vcfGenUtil_varScan


rule indel:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.canonical_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.canonical_annotated.indel_annotated.vcf
    log: log/vcfGenUtil_varScan/indel/indel_Pfeiffer3.varScan.indel.canonical_annotated.2017-07-07.16-13-07.1000g.log, log/vcfGenUtil_varScan/indel/indel_Pfeiffer3.varScan.indel.canonical_annotated.2017-07-07.16-13-07dbsnp.stderr, log/vcfGenUtil_varScan/indel/indel_Pfeiffer3.varScan.indel.canonical_annotated.2017-07-07.16-13-07.mills_100g.log
    jobid: 6
    wildcards: pathIndel=output/vcfGenUtil_varScan, sampleIndel=Pfeiffer3.varScan.indel.canonical_annotated


rule getVcfTable:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.canonical_annotated.indel_annotated.vcf
    output: output/vcfGenUtil_varScan/tables/Pfeiffer3.varScan.indel.canonical_annotated.indel_annotated.txt
    log: log/vcfUtil/vcfGetTable_annotateVcfDIR/vcfGetTable_annotateVcfDIR_{wildcards.sampleVCFGT}.2017-07-07.16-13-07.stderr, log/vcfUtil/vcfGetTable_annotateVcfDIR/vcfGetTable_annotateVcfDIR_{wildcards.sampleVCFGT}.2017-07-07.16-13-07.OnePerLine.stderr
    jobid: 2
    wildcards: sampleGVCFT=Pfeiffer3.varScan.indel.canonical_annotated.indel_annotated, pathGVCFT=output/vcfGenUtil_varScan


rule getVcfTable:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated.cosmic_annotated.vcf
    output: output/vcfGenUtil_varScan/tables/Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated.cosmic_annotated.txt
    log: log/vcfUtil/vcfGetTable_annotateVcfDIR/vcfGetTable_annotateVcfDIR_{wildcards.sampleVCFGT}.2017-07-07.16-13-07.stderr, log/vcfUtil/vcfGetTable_annotateVcfDIR/vcfGetTable_annotateVcfDIR_{wildcards.sampleVCFGT}.2017-07-07.16-13-07.OnePerLine.stderr
    jobid: 1
    wildcards: sampleGVCFT=Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated.cosmic_annotated, pathGVCFT=output/vcfGenUtil_varScan


rule getVcfTable:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.canonical_annotated.indel_annotated.vcf
    output: output/vcfGenUtil_varScan/tables/Pfeiffer2.varScan.indel.canonical_annotated.indel_annotated.txt
    log: log/vcfUtil/vcfGetTable_annotateVcfDIR/vcfGetTable_annotateVcfDIR_{wildcards.sampleVCFGT}.2017-07-07.16-13-07.stderr, log/vcfUtil/vcfGetTable_annotateVcfDIR/vcfGetTable_annotateVcfDIR_{wildcards.sampleVCFGT}.2017-07-07.16-13-07.OnePerLine.stderr
    jobid: 3
    wildcards: sampleGVCFT=Pfeiffer2.varScan.indel.canonical_annotated.indel_annotated, pathGVCFT=output/vcfGenUtil_varScan


rule getVcfTable:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated.cosmic_annotated.vcf
    output: output/vcfGenUtil_varScan/tables/Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated.cosmic_annotated.txt
    log: log/vcfUtil/vcfGetTable_annotateVcfDIR/vcfGetTable_annotateVcfDIR_{wildcards.sampleVCFGT}.2017-07-07.16-13-07.stderr, log/vcfUtil/vcfGetTable_annotateVcfDIR/vcfGetTable_annotateVcfDIR_{wildcards.sampleVCFGT}.2017-07-07.16-13-07.OnePerLine.stderr
    jobid: 4
    wildcards: sampleGVCFT=Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated.cosmic_annotated, pathGVCFT=output/vcfGenUtil_varScan


localrule all:
    input: output/vcfGenUtil_varScan/tables/Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated.cosmic_annotated.txt, output/vcfGenUtil_varScan/tables/Pfeiffer2.varScan.indel.canonical_annotated.indel_annotated.txt, output/vcfGenUtil_varScan/tables/Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated.cosmic_annotated.txt, output/vcfGenUtil_varScan/tables/Pfeiffer3.varScan.indel.canonical_annotated.indel_annotated.txt
    jobid: 0

Job counts:
	count	jobs
	1	all
	7	bam2fastq_picard
	168	bam2mpileup
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
	336	mpileup2vcf_single
	7	sortBAM_biobambam
	571
