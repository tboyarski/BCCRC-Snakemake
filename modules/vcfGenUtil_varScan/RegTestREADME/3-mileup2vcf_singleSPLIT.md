# 5-mpileup2vcf_singleWITHSPLIT
This pipeline is to exemplify the default operations of this module. 

## Setting up the: buildPipe.py
Users must set the following variable:

 * (Line 13) TYPE = "single"

## Setting up the: Snakefile
Users must set the following submodule "call via" input requirements:

 * singleSPLIT

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

rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer3.bam
    output: output/fastq/Pfeiffer3.1.fastq, output/fastq/Pfeiffer3.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-05.19-06-27.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-05.19-06-27.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-05.19-06-27.stderr
    jobid: 520
    wildcards: sampleB2FP=Pfeiffer3


rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer2.bam
    output: output/fastq/Pfeiffer2.1.fastq, output/fastq/Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-05.19-06-27.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-05.19-06-27.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-05.19-06-27.stderr
    jobid: 519
    wildcards: sampleB2FP=Pfeiffer2


rule fastq2GZ:
    input: output/fastq/Pfeiffer2.1.fastq
    output: output/fastq/Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.1.2017-07-05.19-06-27.stderr
    jobid: 515
    wildcards: sampleFGZ=Pfeiffer2.1, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Pfeiffer3.1.fastq
    output: output/fastq/Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.1.2017-07-05.19-06-27.stderr
    jobid: 518
    wildcards: sampleFGZ=Pfeiffer3.1, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Pfeiffer2.2.fastq
    output: output/fastq/Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.2.2017-07-05.19-06-27.stderr
    jobid: 516
    wildcards: sampleFGZ=Pfeiffer2.2, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Pfeiffer3.2.fastq
    output: output/fastq/Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.2.2017-07-05.19-06-27.stderr
    jobid: 517
    wildcards: sampleFGZ=Pfeiffer3.2, pathFGZ=output/fastq


rule bamALIGN_bwa:
    input: output/fastq/Pfeiffer2.1.fastq.gz, output/fastq/Pfeiffer2.2.fastq.gz, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/bam/Pfeiffer2_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-05.19-06-27.samtools.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-05.19-06-27.bwa.stderr
    jobid: 513
    wildcards: sampleBAB=Pfeiffer2


rule bamALIGN_bwa:
    input: output/fastq/Pfeiffer3.1.fastq.gz, output/fastq/Pfeiffer3.2.fastq.gz, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/bam/Pfeiffer3_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-05.19-06-27.samtools.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-05.19-06-27.bwa.stderr
    jobid: 514
    wildcards: sampleBAB=Pfeiffer3


rule sortBAM_biobambam:
    input: output/bam/Pfeiffer2_Aligned.out.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-05.19-06-27.samtools.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-05.19-06-27.bamsort.stderr
    jobid: 511
    wildcards: pathSBB=output/bam, sampleSBB=Pfeiffer2_Aligned.out


rule sortBAM_biobambam:
    input: output/bam/Pfeiffer3_Aligned.out.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-05.19-06-27.samtools.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-05.19-06-27.bamsort.stderr
    jobid: 512
    wildcards: pathSBB=output/bam, sampleSBB=Pfeiffer3_Aligned.out


rule filteredBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer2_Aligned.out_sorted.2017-07-05.19-06-27.stderr
    jobid: 509
    wildcards: pathFB=output/bam, sampleFB=Pfeiffer2_Aligned.out_sorted


rule filteredBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer3_Aligned.out_sorted.2017-07-05.19-06-27.stderr
    jobid: 510
    wildcards: pathFB=output/bam, sampleFB=Pfeiffer3_Aligned.out_sorted


rule markdupBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    output: output/metrics/Pfeiffer3_Aligned.out_sorted_filtered.dup_metrics, output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer3_Aligned.out_sorted_filtered.2017-07-05.19-06-27.biobammarkdup.stderr
    jobid: 508
    wildcards: sampleMDB=Pfeiffer3_Aligned.out_sorted_filtered, outputDIR=output


rule markdupBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    output: output/metrics/Pfeiffer2_Aligned.out_sorted_filtered.dup_metrics, output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer2_Aligned.out_sorted_filtered.2017-07-05.19-06-27.biobammarkdup.stderr
    jobid: 507
    wildcards: sampleMDB=Pfeiffer2_Aligned.out_sorted_filtered, outputDIR=output


rule indexBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam.bai
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer2.2017-07-05.19-06-27.stderr
    jobid: 505
    wildcards: outputDIR=output, sampleIB=Pfeiffer2


rule indexBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam.bai
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer3.2017-07-05.19-06-27.stderr
    jobid: 506
    wildcards: outputDIR=output, sampleIB=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_16.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 451
    wildcards: chrB2M=_16, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000248.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 478
    wildcards: chrB2M=_GL000248.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_21.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 351
    wildcards: chrB2M=_21, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000228.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 493
    wildcards: chrB2M=_GL000228.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_7.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 360
    wildcards: chrB2M=_7, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000205.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 401
    wildcards: chrB2M=_GL000205.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000197.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 483
    wildcards: chrB2M=_GL000197.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000232.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 482
    wildcards: chrB2M=_GL000232.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000245.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 408
    wildcards: chrB2M=_GL000245.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000203.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 440
    wildcards: chrB2M=_GL000203.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000239.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 367
    wildcards: chrB2M=_GL000239.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000202.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 393
    wildcards: chrB2M=_GL000202.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000247.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 432
    wildcards: chrB2M=_GL000247.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000198.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 447
    wildcards: chrB2M=_GL000198.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000212.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 464
    wildcards: chrB2M=_GL000212.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000245.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 394
    wildcards: chrB2M=_GL000245.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_7.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 376
    wildcards: chrB2M=_7, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_20.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 479
    wildcards: chrB2M=_20, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000192.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 371
    wildcards: chrB2M=_GL000192.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000196.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 391
    wildcards: chrB2M=_GL000196.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000225.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 374
    wildcards: chrB2M=_GL000225.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000195.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 442
    wildcards: chrB2M=_GL000195.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_20.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 429
    wildcards: chrB2M=_20, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000227.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 362
    wildcards: chrB2M=_GL000227.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000232.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 381
    wildcards: chrB2M=_GL000232.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000248.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 415
    wildcards: chrB2M=_GL000248.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_MT.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 387
    wildcards: chrB2M=_MT, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000194.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 437
    wildcards: chrB2M=_GL000194.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000233.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 348
    wildcards: chrB2M=_GL000233.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_8.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 347
    wildcards: chrB2M=_8, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000211.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 438
    wildcards: chrB2M=_GL000211.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000234.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 412
    wildcards: chrB2M=_GL000234.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_19.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 431
    wildcards: chrB2M=_19, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000222.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 359
    wildcards: chrB2M=_GL000222.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000213.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 434
    wildcards: chrB2M=_GL000213.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000220.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 416
    wildcards: chrB2M=_GL000220.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_5.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 419
    wildcards: chrB2M=_5, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000218.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 498
    wildcards: chrB2M=_GL000218.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000195.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 403
    wildcards: chrB2M=_GL000195.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000233.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 406
    wildcards: chrB2M=_GL000233.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000229.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 418
    wildcards: chrB2M=_GL000229.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000208.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 450
    wildcards: chrB2M=_GL000208.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 501
    wildcards: chrB2M=_1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000201.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 500
    wildcards: chrB2M=_GL000201.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_8.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 427
    wildcards: chrB2M=_8, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_10.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 473
    wildcards: chrB2M=_10, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_5.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 339
    wildcards: chrB2M=_5, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_2.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 417
    wildcards: chrB2M=_2, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000246.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 402
    wildcards: chrB2M=_GL000246.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000240.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 404
    wildcards: chrB2M=_GL000240.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_14.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 384
    wildcards: chrB2M=_14, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000249.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 383
    wildcards: chrB2M=_GL000249.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000215.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 458
    wildcards: chrB2M=_GL000215.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_Y.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 502
    wildcards: chrB2M=_Y, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000209.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 380
    wildcards: chrB2M=_GL000209.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000241.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 441
    wildcards: chrB2M=_GL000241.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000237.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 365
    wildcards: chrB2M=_GL000237.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000206.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 345
    wildcards: chrB2M=_GL000206.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 407
    wildcards: chrB2M=_1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000200.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 504
    wildcards: chrB2M=_GL000200.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000193.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 388
    wildcards: chrB2M=_GL000193.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000226.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 400
    wildcards: chrB2M=_GL000226.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_13.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 495
    wildcards: chrB2M=_13, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000225.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 413
    wildcards: chrB2M=_GL000225.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000231.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 363
    wildcards: chrB2M=_GL000231.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000197.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 379
    wildcards: chrB2M=_GL000197.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_6.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 395
    wildcards: chrB2M=_6, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000205.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 477
    wildcards: chrB2M=_GL000205.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_19.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 346
    wildcards: chrB2M=_19, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000214.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 389
    wildcards: chrB2M=_GL000214.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000216.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 497
    wildcards: chrB2M=_GL000216.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000204.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 463
    wildcards: chrB2M=_GL000204.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_18.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 385
    wildcards: chrB2M=_18, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000200.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 354
    wildcards: chrB2M=_GL000200.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000210.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 472
    wildcards: chrB2M=_GL000210.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_17.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 457
    wildcards: chrB2M=_17, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000192.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 366
    wildcards: chrB2M=_GL000192.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_10.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 378
    wildcards: chrB2M=_10, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_X.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 340
    wildcards: chrB2M=_X, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000212.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 466
    wildcards: chrB2M=_GL000212.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000220.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 484
    wildcards: chrB2M=_GL000220.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_X.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 352
    wildcards: chrB2M=_X, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000222.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 488
    wildcards: chrB2M=_GL000222.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000209.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 499
    wildcards: chrB2M=_GL000209.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000223.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 338
    wildcards: chrB2M=_GL000223.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000214.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 397
    wildcards: chrB2M=_GL000214.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_9.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 475
    wildcards: chrB2M=_9, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_17.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 454
    wildcards: chrB2M=_17, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000217.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 377
    wildcards: chrB2M=_GL000217.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_18.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 420
    wildcards: chrB2M=_18, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_11.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 430
    wildcards: chrB2M=_11, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000191.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 337
    wildcards: chrB2M=_GL000191.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000235.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 462
    wildcards: chrB2M=_GL000235.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000247.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 436
    wildcards: chrB2M=_GL000247.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000211.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 494
    wildcards: chrB2M=_GL000211.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000246.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 468
    wildcards: chrB2M=_GL000246.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000199.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 424
    wildcards: chrB2M=_GL000199.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000199.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 353
    wildcards: chrB2M=_GL000199.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000238.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 489
    wildcards: chrB2M=_GL000238.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000207.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 370
    wildcards: chrB2M=_GL000207.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_22.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 411
    wildcards: chrB2M=_22, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_16.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 390
    wildcards: chrB2M=_16, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000219.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 453
    wildcards: chrB2M=_GL000219.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000213.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 496
    wildcards: chrB2M=_GL000213.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_MT.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 386
    wildcards: chrB2M=_MT, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_3.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 444
    wildcards: chrB2M=_3, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000231.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 443
    wildcards: chrB2M=_GL000231.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000224.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 342
    wildcards: chrB2M=_GL000224.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000235.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 467
    wildcards: chrB2M=_GL000235.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_13.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 349
    wildcards: chrB2M=_13, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000191.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 382
    wildcards: chrB2M=_GL000191.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000219.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 465
    wildcards: chrB2M=_GL000219.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000244.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 474
    wildcards: chrB2M=_GL000244.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000203.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 375
    wildcards: chrB2M=_GL000203.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000208.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 361
    wildcards: chrB2M=_GL000208.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000193.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 480
    wildcards: chrB2M=_GL000193.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000242.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 396
    wildcards: chrB2M=_GL000242.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000236.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 355
    wildcards: chrB2M=_GL000236.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_21.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 491
    wildcards: chrB2M=_21, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000227.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 459
    wildcards: chrB2M=_GL000227.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000202.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 487
    wildcards: chrB2M=_GL000202.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000198.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 486
    wildcards: chrB2M=_GL000198.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000242.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 409
    wildcards: chrB2M=_GL000242.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000216.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 421
    wildcards: chrB2M=_GL000216.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000218.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 439
    wildcards: chrB2M=_GL000218.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000215.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 469
    wildcards: chrB2M=_GL000215.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000238.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 372
    wildcards: chrB2M=_GL000238.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000239.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 428
    wildcards: chrB2M=_GL000239.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000236.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 455
    wildcards: chrB2M=_GL000236.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000243.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 368
    wildcards: chrB2M=_GL000243.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000230.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 414
    wildcards: chrB2M=_GL000230.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_4.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 392
    wildcards: chrB2M=_4, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000243.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 446
    wildcards: chrB2M=_GL000243.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_14.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 433
    wildcards: chrB2M=_14, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000217.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 460
    wildcards: chrB2M=_GL000217.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000204.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 425
    wildcards: chrB2M=_GL000204.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000241.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 344
    wildcards: chrB2M=_GL000241.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000221.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 448
    wildcards: chrB2M=_GL000221.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000249.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 369
    wildcards: chrB2M=_GL000249.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_6.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 456
    wildcards: chrB2M=_6, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_2.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 435
    wildcards: chrB2M=_2, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000194.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 426
    wildcards: chrB2M=_GL000194.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_15.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 490
    wildcards: chrB2M=_15, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000226.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 357
    wildcards: chrB2M=_GL000226.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_9.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 503
    wildcards: chrB2M=_9, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_22.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 399
    wildcards: chrB2M=_22, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000240.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 341
    wildcards: chrB2M=_GL000240.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000229.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 364
    wildcards: chrB2M=_GL000229.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000237.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 471
    wildcards: chrB2M=_GL000237.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000244.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 358
    wildcards: chrB2M=_GL000244.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000210.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 476
    wildcards: chrB2M=_GL000210.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_3.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 405
    wildcards: chrB2M=_3, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000207.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 445
    wildcards: chrB2M=_GL000207.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_15.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 422
    wildcards: chrB2M=_15, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000221.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 350
    wildcards: chrB2M=_GL000221.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_12.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 461
    wildcards: chrB2M=_12, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_11.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 343
    wildcards: chrB2M=_11, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_Y.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 356
    wildcards: chrB2M=_Y, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_12.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 449
    wildcards: chrB2M=_12, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000234.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 492
    wildcards: chrB2M=_GL000234.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000196.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 485
    wildcards: chrB2M=_GL000196.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000224.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 423
    wildcards: chrB2M=_GL000224.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000206.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 410
    wildcards: chrB2M=_GL000206.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000201.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 481
    wildcards: chrB2M=_GL000201.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000228.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 470
    wildcards: chrB2M=_GL000228.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_4.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-06-27.mpileup.stderr
    jobid: 373
    wildcards: chrB2M=_4, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000230.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 398
    wildcards: chrB2M=_GL000230.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000223.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-06-27.mpileup.stderr
    jobid: 452
    wildcards: chrB2M=_GL000223.1, sampleB2M=Pfeiffer2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_5.mpileup
    output: output/varScan/Pfeiffer2_5.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_5.snp.2017-07-05.19-06-27.stderr
    jobid: 3
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_5, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_X.mpileup
    output: output/varScan/Pfeiffer3_X.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_X.snp.2017-07-05.19-06-27.stderr
    jobid: 4
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_X, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000224.1.mpileup
    output: output/varScan/Pfeiffer3_GL000224.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000224.1.indel.2017-07-05.19-06-27.stderr
    jobid: 6
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000224.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000241.1.mpileup
    output: output/varScan/Pfeiffer2_GL000241.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000241.1.snp.2017-07-05.19-06-27.stderr
    jobid: 8
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000241.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000206.1.mpileup
    output: output/varScan/Pfeiffer3_GL000206.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000206.1.snp.2017-07-05.19-06-27.stderr
    jobid: 9
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000206.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_Y.mpileup
    output: output/varScan/Pfeiffer3_Y.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_Y.snp.2017-07-05.19-06-27.stderr
    jobid: 20
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_Y, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000208.1.mpileup
    output: output/varScan/Pfeiffer2_GL000208.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000208.1.indel.2017-07-05.19-06-27.stderr
    jobid: 25
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000208.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000229.1.mpileup
    output: output/varScan/Pfeiffer3_GL000229.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000229.1.indel.2017-07-05.19-06-27.stderr
    jobid: 28
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000229.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000233.1.mpileup
    output: output/varScan/Pfeiffer3_GL000233.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000233.1.indel.2017-07-05.19-06-27.stderr
    jobid: 29
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000233.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000203.1.mpileup
    output: output/varScan/Pfeiffer2_GL000203.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000203.1.snp.2017-07-05.19-06-27.stderr
    jobid: 41
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000203.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_7.mpileup
    output: output/varScan/Pfeiffer3_7.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_7.snp.2017-07-05.19-06-27.stderr
    jobid: 42
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_7, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_16.mpileup
    output: output/varScan/Pfeiffer2_16.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_16.snp.2017-07-05.19-06-27.stderr
    jobid: 58
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_16, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000204.1.mpileup
    output: output/varScan/Pfeiffer2_GL000204.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000204.1.snp.2017-07-05.19-06-27.stderr
    jobid: 309
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000204.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000195.1.mpileup
    output: output/varScan/Pfeiffer2_GL000195.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000195.1.snp.2017-07-05.19-06-27.stderr
    jobid: 72
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000195.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000240.1.mpileup
    output: output/varScan/Pfeiffer2_GL000240.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000240.1.snp.2017-07-05.19-06-27.stderr
    jobid: 73
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000240.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_3.mpileup
    output: output/varScan/Pfeiffer3_3.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_3.indel.2017-07-05.19-06-27.stderr
    jobid: 74
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_3, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000233.1.mpileup
    output: output/varScan/Pfeiffer2_GL000233.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000233.1.snp.2017-07-05.19-06-27.stderr
    jobid: 75
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000233.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000246.1.mpileup
    output: output/varScan/Pfeiffer3_GL000246.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000246.1.indel.2017-07-05.19-06-27.stderr
    jobid: 281
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000246.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000245.1.mpileup
    output: output/varScan/Pfeiffer3_GL000245.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000245.1.indel.2017-07-05.19-06-27.stderr
    jobid: 77
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000245.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000194.1.mpileup
    output: output/varScan/Pfeiffer3_GL000194.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000194.1.snp.2017-07-05.19-06-27.stderr
    jobid: 118
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000194.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000225.1.mpileup
    output: output/varScan/Pfeiffer3_GL000225.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000225.1.snp.2017-07-05.19-06-27.stderr
    jobid: 83
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000225.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_2.mpileup
    output: output/varScan/Pfeiffer3_2.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_2.snp.2017-07-05.19-06-27.stderr
    jobid: 89
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_2, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_5.mpileup
    output: output/varScan/Pfeiffer3_5.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_5.snp.2017-07-05.19-06-27.stderr
    jobid: 92
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_5, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_16.mpileup
    output: output/varScan/Pfeiffer2_16.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_16.indel.2017-07-05.19-06-27.stderr
    jobid: 177
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_16, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000224.1.mpileup
    output: output/varScan/Pfeiffer2_GL000224.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000224.1.snp.2017-07-05.19-06-27.stderr
    jobid: 97
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000224.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000194.1.mpileup
    output: output/varScan/Pfeiffer2_GL000194.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000194.1.indel.2017-07-05.19-06-27.stderr
    jobid: 104
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000194.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_18.mpileup
    output: output/varScan/Pfeiffer3_18.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_18.snp.2017-07-05.19-06-27.stderr
    jobid: 109
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_18, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000211.1.mpileup
    output: output/varScan/Pfeiffer3_GL000211.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000211.1.snp.2017-07-05.19-06-27.stderr
    jobid: 119
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000211.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000200.1.mpileup
    output: output/varScan/Pfeiffer2_GL000200.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000200.1.snp.2017-07-05.19-06-27.stderr
    jobid: 57
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000200.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000218.1.mpileup
    output: output/varScan/Pfeiffer3_GL000218.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000218.1.snp.2017-07-05.19-06-27.stderr
    jobid: 121
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000218.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_8.mpileup
    output: output/varScan/Pfeiffer3_8.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_8.indel.2017-07-05.19-06-27.stderr
    jobid: 136
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_8, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_Y.mpileup
    output: output/varScan/Pfeiffer3_Y.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_Y.indel.2017-07-05.19-06-27.stderr
    jobid: 127
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_Y, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_2.mpileup
    output: output/varScan/Pfeiffer3_2.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_2.indel.2017-07-05.19-06-27.stderr
    jobid: 144
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_2, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000195.1.mpileup
    output: output/varScan/Pfeiffer3_GL000195.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000195.1.snp.2017-07-05.19-06-27.stderr
    jobid: 131
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000195.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000234.1.mpileup
    output: output/varScan/Pfeiffer2_GL000234.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000234.1.snp.2017-07-05.19-06-27.stderr
    jobid: 260
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000234.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000207.1.mpileup
    output: output/varScan/Pfeiffer3_GL000207.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000207.1.snp.2017-07-05.19-06-27.stderr
    jobid: 137
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000207.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000229.1.mpileup
    output: output/varScan/Pfeiffer2_GL000229.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000229.1.snp.2017-07-05.19-06-27.stderr
    jobid: 140
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000229.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000237.1.mpileup
    output: output/varScan/Pfeiffer3_GL000237.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000237.1.snp.2017-07-05.19-06-27.stderr
    jobid: 191
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000237.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000208.1.mpileup
    output: output/varScan/Pfeiffer2_GL000208.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000208.1.snp.2017-07-05.19-06-27.stderr
    jobid: 147
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000208.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000238.1.mpileup
    output: output/varScan/Pfeiffer2_GL000238.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000238.1.snp.2017-07-05.19-06-27.stderr
    jobid: 241
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000238.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000219.1.mpileup
    output: output/varScan/Pfeiffer3_GL000219.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000219.1.indel.2017-07-05.19-06-27.stderr
    jobid: 153
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000219.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000223.1.mpileup
    output: output/varScan/Pfeiffer2_GL000223.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000223.1.snp.2017-07-05.19-06-27.stderr
    jobid: 152
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000223.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_17.mpileup
    output: output/varScan/Pfeiffer3_17.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_17.snp.2017-07-05.19-06-27.stderr
    jobid: 155
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_17, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_17.mpileup
    output: output/varScan/Pfeiffer2_17.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_17.indel.2017-07-05.19-06-27.stderr
    jobid: 159
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_17, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000231.1.mpileup
    output: output/varScan/Pfeiffer3_GL000231.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000231.1.snp.2017-07-05.19-06-27.stderr
    jobid: 164
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000231.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_12.mpileup
    output: output/varScan/Pfeiffer3_12.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_12.indel.2017-07-05.19-06-27.stderr
    jobid: 166
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_12, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000216.1.mpileup
    output: output/varScan/Pfeiffer3_GL000216.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000216.1.indel.2017-07-05.19-06-27.stderr
    jobid: 171
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000216.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000240.1.mpileup
    output: output/varScan/Pfeiffer3_GL000240.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000240.1.indel.2017-07-05.19-06-27.stderr
    jobid: 263
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000240.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000223.1.mpileup
    output: output/varScan/Pfeiffer2_GL000223.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000223.1.indel.2017-07-05.19-06-27.stderr
    jobid: 172
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000223.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000204.1.mpileup
    output: output/varScan/Pfeiffer3_GL000204.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000204.1.indel.2017-07-05.19-06-27.stderr
    jobid: 175
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000204.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000243.1.mpileup
    output: output/varScan/Pfeiffer2_GL000243.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000243.1.indel.2017-07-05.19-06-27.stderr
    jobid: 33
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000243.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000246.1.mpileup
    output: output/varScan/Pfeiffer3_GL000246.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000246.1.snp.2017-07-05.19-06-27.stderr
    jobid: 183
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000246.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_10.mpileup
    output: output/varScan/Pfeiffer2_10.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_10.indel.2017-07-05.19-06-27.stderr
    jobid: 184
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_10, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000249.1.mpileup
    output: output/varScan/Pfeiffer2_GL000249.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000249.1.indel.2017-07-05.19-06-27.stderr
    jobid: 101
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000249.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_10.mpileup
    output: output/varScan/Pfeiffer3_10.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_10.snp.2017-07-05.19-06-27.stderr
    jobid: 193
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_10, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000205.1.mpileup
    output: output/varScan/Pfeiffer3_GL000205.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000205.1.indel.2017-07-05.19-06-27.stderr
    jobid: 200
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000205.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_2.mpileup
    output: output/varScan/Pfeiffer2_2.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_2.indel.2017-07-05.19-06-27.stderr
    jobid: 205
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_2, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000208.1.mpileup
    output: output/varScan/Pfeiffer3_GL000208.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000208.1.indel.2017-07-05.19-06-27.stderr
    jobid: 207
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000208.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000228.1.mpileup
    output: output/varScan/Pfeiffer3_GL000228.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000228.1.indel.2017-07-05.19-06-27.stderr
    jobid: 209
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000228.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000193.1.mpileup
    output: output/varScan/Pfeiffer2_GL000193.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000193.1.snp.2017-07-05.19-06-27.stderr
    jobid: 213
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000193.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000228.1.mpileup
    output: output/varScan/Pfeiffer2_GL000228.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000228.1.indel.2017-07-05.19-06-27.stderr
    jobid: 247
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000228.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000197.1.mpileup
    output: output/varScan/Pfeiffer3_GL000197.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000197.1.indel.2017-07-05.19-06-27.stderr
    jobid: 218
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000197.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_20.mpileup
    output: output/varScan/Pfeiffer2_20.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_20.indel.2017-07-05.19-06-27.stderr
    jobid: 221
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_20, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000207.1.mpileup
    output: output/varScan/Pfeiffer2_GL000207.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000207.1.snp.2017-07-05.19-06-27.stderr
    jobid: 35
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000207.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000201.1.mpileup
    output: output/varScan/Pfeiffer3_GL000201.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000201.1.snp.2017-07-05.19-06-27.stderr
    jobid: 216
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000201.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000231.1.mpileup
    output: output/varScan/Pfeiffer2_GL000231.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000231.1.indel.2017-07-05.19-06-27.stderr
    jobid: 27
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000231.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000207.1.mpileup
    output: output/varScan/Pfeiffer3_GL000207.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000207.1.indel.2017-07-05.19-06-27.stderr
    jobid: 197
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000207.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000225.1.mpileup
    output: output/varScan/Pfeiffer2_GL000225.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000225.1.snp.2017-07-05.19-06-27.stderr
    jobid: 236
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000225.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000205.1.mpileup
    output: output/varScan/Pfeiffer3_GL000205.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000205.1.snp.2017-07-05.19-06-27.stderr
    jobid: 240
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000205.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_17.mpileup
    output: output/varScan/Pfeiffer3_17.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_17.indel.2017-07-05.19-06-27.stderr
    jobid: 230
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_17, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000211.1.mpileup
    output: output/varScan/Pfeiffer2_GL000211.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000211.1.indel.2017-07-05.19-06-27.stderr
    jobid: 251
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000211.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000196.1.mpileup
    output: output/varScan/Pfeiffer2_GL000196.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000196.1.snp.2017-07-05.19-06-27.stderr
    jobid: 255
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000196.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000247.1.mpileup
    output: output/varScan/Pfeiffer2_GL000247.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000247.1.indel.2017-07-05.19-06-27.stderr
    jobid: 265
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000247.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000234.1.mpileup
    output: output/varScan/Pfeiffer3_GL000234.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000234.1.snp.2017-07-05.19-06-27.stderr
    jobid: 269
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000234.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000240.1.mpileup
    output: output/varScan/Pfeiffer3_GL000240.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000240.1.snp.2017-07-05.19-06-27.stderr
    jobid: 5
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000240.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000213.1.mpileup
    output: output/varScan/Pfeiffer3_GL000213.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000213.1.snp.2017-07-05.19-06-27.stderr
    jobid: 288
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000213.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_6.mpileup
    output: output/varScan/Pfeiffer2_6.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_6.indel.2017-07-05.19-06-27.stderr
    jobid: 63
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_6, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000210.1.mpileup
    output: output/varScan/Pfeiffer3_GL000210.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000210.1.indel.2017-07-05.19-06-27.stderr
    jobid: 294
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000210.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_MT.mpileup
    output: output/varScan/Pfeiffer3_MT.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_MT.snp.2017-07-05.19-06-27.stderr
    jobid: 295
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_MT, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000210.1.mpileup
    output: output/varScan/Pfeiffer3_GL000210.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000210.1.snp.2017-07-05.19-06-27.stderr
    jobid: 192
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000210.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000219.1.mpileup
    output: output/varScan/Pfeiffer2_GL000219.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000219.1.snp.2017-07-05.19-06-27.stderr
    jobid: 301
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000219.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000246.1.mpileup
    output: output/varScan/Pfeiffer2_GL000246.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000246.1.snp.2017-07-05.19-06-27.stderr
    jobid: 303
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000246.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000201.1.mpileup
    output: output/varScan/Pfeiffer2_GL000201.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000201.1.snp.2017-07-05.19-06-27.stderr
    jobid: 313
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000201.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000201.1.mpileup
    output: output/varScan/Pfeiffer3_GL000201.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000201.1.indel.2017-07-05.19-06-27.stderr
    jobid: 314
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000201.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000198.1.mpileup
    output: output/varScan/Pfeiffer2_GL000198.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000198.1.indel.2017-07-05.19-06-27.stderr
    jobid: 224
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000198.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_6.mpileup
    output: output/varScan/Pfeiffer3_6.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_6.snp.2017-07-05.19-06-27.stderr
    jobid: 316
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_6, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000218.1.mpileup
    output: output/varScan/Pfeiffer2_GL000218.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000218.1.indel.2017-07-05.19-06-27.stderr
    jobid: 326
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000218.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_9.mpileup
    output: output/varScan/Pfeiffer2_9.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_9.indel.2017-07-05.19-06-27.stderr
    jobid: 331
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_9, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000214.1.mpileup
    output: output/varScan/Pfeiffer2_GL000214.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000214.1.snp.2017-07-05.19-06-27.stderr
    jobid: 334
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000214.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_15.mpileup
    output: output/varScan/Pfeiffer3_15.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_15.snp.2017-07-05.19-06-27.stderr
    jobid: 223
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_15, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000195.1.mpileup
    output: output/varScan/Pfeiffer2_GL000195.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000195.1.indel.2017-07-05.19-06-27.stderr
    jobid: 276
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000195.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_11.mpileup
    output: output/varScan/Pfeiffer3_11.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_11.snp.2017-07-05.19-06-27.stderr
    jobid: 7
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_11, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000221.1.mpileup
    output: output/varScan/Pfeiffer2_GL000221.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000221.1.indel.2017-07-05.19-06-27.stderr
    jobid: 14
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000221.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000244.1.mpileup
    output: output/varScan/Pfeiffer2_GL000244.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000244.1.snp.2017-07-05.19-06-27.stderr
    jobid: 22
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000244.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000237.1.mpileup
    output: output/varScan/Pfeiffer2_GL000237.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000237.1.indel.2017-07-05.19-06-27.stderr
    jobid: 30
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000237.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000223.1.mpileup
    output: output/varScan/Pfeiffer3_GL000223.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000223.1.snp.2017-07-05.19-06-27.stderr
    jobid: 181
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000223.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000249.1.mpileup
    output: output/varScan/Pfeiffer2_GL000249.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000249.1.snp.2017-07-05.19-06-27.stderr
    jobid: 34
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000249.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000238.1.mpileup
    output: output/varScan/Pfeiffer3_GL000238.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000238.1.snp.2017-07-05.19-06-27.stderr
    jobid: 38
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000238.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_13.mpileup
    output: output/varScan/Pfeiffer3_13.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_13.indel.2017-07-05.19-06-27.stderr
    jobid: 252
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_13, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000217.1.mpileup
    output: output/varScan/Pfeiffer3_GL000217.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000217.1.snp.2017-07-05.19-06-27.stderr
    jobid: 43
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000217.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000209.1.mpileup
    output: output/varScan/Pfeiffer3_GL000209.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000209.1.indel.2017-07-05.19-06-27.stderr
    jobid: 47
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000209.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000232.1.mpileup
    output: output/varScan/Pfeiffer2_GL000232.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000232.1.indel.2017-07-05.19-06-27.stderr
    jobid: 48
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000232.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_MT.mpileup
    output: output/varScan/Pfeiffer2_MT.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_MT.indel.2017-07-05.19-06-27.stderr
    jobid: 53
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_MT, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_MT.mpileup
    output: output/varScan/Pfeiffer3_MT.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_MT.indel.2017-07-05.19-06-27.stderr
    jobid: 54
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_MT, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000214.1.mpileup
    output: output/varScan/Pfeiffer3_GL000214.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000214.1.indel.2017-07-05.19-06-27.stderr
    jobid: 56
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000214.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000202.1.mpileup
    output: output/varScan/Pfeiffer3_GL000202.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000202.1.indel.2017-07-05.19-06-27.stderr
    jobid: 61
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000202.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000214.1.mpileup
    output: output/varScan/Pfeiffer2_GL000214.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000214.1.indel.2017-07-05.19-06-27.stderr
    jobid: 66
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000214.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000230.1.mpileup
    output: output/varScan/Pfeiffer2_GL000230.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000230.1.snp.2017-07-05.19-06-27.stderr
    jobid: 67
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000230.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000248.1.mpileup
    output: output/varScan/Pfeiffer3_GL000248.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000248.1.indel.2017-07-05.19-06-27.stderr
    jobid: 203
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000248.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000236.1.mpileup
    output: output/varScan/Pfeiffer3_GL000236.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000236.1.snp.2017-07-05.19-06-27.stderr
    jobid: 222
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000236.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000246.1.mpileup
    output: output/varScan/Pfeiffer2_GL000246.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000246.1.indel.2017-07-05.19-06-27.stderr
    jobid: 71
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000246.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_MT.mpileup
    output: output/varScan/Pfeiffer2_MT.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_MT.snp.2017-07-05.19-06-27.stderr
    jobid: 239
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_MT, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000206.1.mpileup
    output: output/varScan/Pfeiffer2_GL000206.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000206.1.snp.2017-07-05.19-06-27.stderr
    jobid: 79
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000206.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000231.1.mpileup
    output: output/varScan/Pfeiffer2_GL000231.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000231.1.snp.2017-07-05.19-06-27.stderr
    jobid: 82
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000231.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_11.mpileup
    output: output/varScan/Pfeiffer3_11.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_11.indel.2017-07-05.19-06-27.stderr
    jobid: 84
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_11, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000229.1.mpileup
    output: output/varScan/Pfeiffer2_GL000229.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000229.1.indel.2017-07-05.19-06-27.stderr
    jobid: 90
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000229.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_18.mpileup
    output: output/varScan/Pfeiffer3_18.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_18.indel.2017-07-05.19-06-27.stderr
    jobid: 93
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_18, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000216.1.mpileup
    output: output/varScan/Pfeiffer3_GL000216.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000216.1.snp.2017-07-05.19-06-27.stderr
    jobid: 94
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000216.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_15.mpileup
    output: output/varScan/Pfeiffer3_15.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_15.indel.2017-07-05.19-06-27.stderr
    jobid: 96
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_15, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000204.1.mpileup
    output: output/varScan/Pfeiffer2_GL000204.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000204.1.indel.2017-07-05.19-06-27.stderr
    jobid: 100
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000204.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000248.1.mpileup
    output: output/varScan/Pfeiffer2_GL000248.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000248.1.indel.2017-07-05.19-06-27.stderr
    jobid: 107
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000248.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_19.mpileup
    output: output/varScan/Pfeiffer3_19.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_19.indel.2017-07-05.19-06-27.stderr
    jobid: 111
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_19, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000218.1.mpileup
    output: output/varScan/Pfeiffer3_GL000218.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000218.1.indel.2017-07-05.19-06-27.stderr
    jobid: 120
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000218.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000203.1.mpileup
    output: output/varScan/Pfeiffer3_GL000203.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000203.1.snp.2017-07-05.19-06-27.stderr
    jobid: 123
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000203.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_14.mpileup
    output: output/varScan/Pfeiffer2_14.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_14.indel.2017-07-05.19-06-27.stderr
    jobid: 125
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_14, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000211.1.mpileup
    output: output/varScan/Pfeiffer3_GL000211.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000211.1.indel.2017-07-05.19-06-27.stderr
    jobid: 126
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000211.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000243.1.mpileup
    output: output/varScan/Pfeiffer2_GL000243.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000243.1.snp.2017-07-05.19-06-27.stderr
    jobid: 158
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000243.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_7.mpileup
    output: output/varScan/Pfeiffer2_7.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_7.snp.2017-07-05.19-06-27.stderr
    jobid: 143
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_7, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000191.1.mpileup
    output: output/varScan/Pfeiffer2_GL000191.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000191.1.snp.2017-07-05.19-06-27.stderr
    jobid: 174
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000191.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_16.mpileup
    output: output/varScan/Pfeiffer3_16.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_16.indel.2017-07-05.19-06-27.stderr
    jobid: 149
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_16, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_21.mpileup
    output: output/varScan/Pfeiffer3_21.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_21.indel.2017-07-05.19-06-27.stderr
    jobid: 244
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_21, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000241.1.mpileup
    output: output/varScan/Pfeiffer2_GL000241.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000241.1.indel.2017-07-05.19-06-27.stderr
    jobid: 267
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000241.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000227.1.mpileup
    output: output/varScan/Pfeiffer3_GL000227.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000227.1.snp.2017-07-05.19-06-27.stderr
    jobid: 163
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000227.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000212.1.mpileup
    output: output/varScan/Pfeiffer2_GL000212.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000212.1.snp.2017-07-05.19-06-27.stderr
    jobid: 176
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000212.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000203.1.mpileup
    output: output/varScan/Pfeiffer3_GL000203.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000203.1.indel.2017-07-05.19-06-27.stderr
    jobid: 178
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000203.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000249.1.mpileup
    output: output/varScan/Pfeiffer3_GL000249.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000249.1.indel.2017-07-05.19-06-27.stderr
    jobid: 50
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000249.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_21.mpileup
    output: output/varScan/Pfeiffer2_21.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_21.snp.2017-07-05.19-06-27.stderr
    jobid: 15
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_21, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_22.mpileup
    output: output/varScan/Pfeiffer3_22.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_22.indel.2017-07-05.19-06-27.stderr
    jobid: 80
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_22, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000227.1.mpileup
    output: output/varScan/Pfeiffer3_GL000227.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000227.1.indel.2017-07-05.19-06-27.stderr
    jobid: 187
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000227.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000219.1.mpileup
    output: output/varScan/Pfeiffer2_GL000219.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000219.1.indel.2017-07-05.19-06-27.stderr
    jobid: 179
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000219.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000220.1.mpileup
    output: output/varScan/Pfeiffer2_GL000220.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000220.1.snp.2017-07-05.19-06-27.stderr
    jobid: 321
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000220.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000210.1.mpileup
    output: output/varScan/Pfeiffer2_GL000210.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000210.1.indel.2017-07-05.19-06-27.stderr
    jobid: 199
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000210.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_20.mpileup
    output: output/varScan/Pfeiffer2_20.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_20.snp.2017-07-05.19-06-27.stderr
    jobid: 206
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_20, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000202.1.mpileup
    output: output/varScan/Pfeiffer2_GL000202.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000202.1.indel.2017-07-05.19-06-27.stderr
    jobid: 237
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000202.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000203.1.mpileup
    output: output/varScan/Pfeiffer2_GL000203.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000203.1.indel.2017-07-05.19-06-27.stderr
    jobid: 225
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000203.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_7.mpileup
    output: output/varScan/Pfeiffer2_7.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_7.indel.2017-07-05.19-06-27.stderr
    jobid: 24
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_7, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_12.mpileup
    output: output/varScan/Pfeiffer2_12.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_12.indel.2017-07-05.19-06-27.stderr
    jobid: 232
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_12, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000206.1.mpileup
    output: output/varScan/Pfeiffer2_GL000206.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000206.1.indel.2017-07-05.19-06-27.stderr
    jobid: 231
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000206.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000192.1.mpileup
    output: output/varScan/Pfeiffer2_GL000192.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000192.1.snp.2017-07-05.19-06-27.stderr
    jobid: 36
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000192.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_3.mpileup
    output: output/varScan/Pfeiffer3_3.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_3.snp.2017-07-05.19-06-27.stderr
    jobid: 238
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_3, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000249.1.mpileup
    output: output/varScan/Pfeiffer3_GL000249.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000249.1.snp.2017-07-05.19-06-27.stderr
    jobid: 242
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000249.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000209.1.mpileup
    output: output/varScan/Pfeiffer3_GL000209.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000209.1.snp.2017-07-05.19-06-27.stderr
    jobid: 65
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000209.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000221.1.mpileup
    output: output/varScan/Pfeiffer3_GL000221.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000221.1.indel.2017-07-05.19-06-27.stderr
    jobid: 248
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000221.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000194.1.mpileup
    output: output/varScan/Pfeiffer3_GL000194.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000194.1.indel.2017-07-05.19-06-27.stderr
    jobid: 253
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000194.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000222.1.mpileup
    output: output/varScan/Pfeiffer3_GL000222.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000222.1.snp.2017-07-05.19-06-27.stderr
    jobid: 227
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000222.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000204.1.mpileup
    output: output/varScan/Pfeiffer3_GL000204.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000204.1.snp.2017-07-05.19-06-27.stderr
    jobid: 250
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000204.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000209.1.mpileup
    output: output/varScan/Pfeiffer2_GL000209.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000209.1.snp.2017-07-05.19-06-27.stderr
    jobid: 274
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000209.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000210.1.mpileup
    output: output/varScan/Pfeiffer2_GL000210.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000210.1.snp.2017-07-05.19-06-27.stderr
    jobid: 283
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000210.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_12.mpileup
    output: output/varScan/Pfeiffer3_12.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_12.snp.2017-07-05.19-06-27.stderr
    jobid: 212
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_12, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000242.1.mpileup
    output: output/varScan/Pfeiffer3_GL000242.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000242.1.indel.2017-07-05.19-06-27.stderr
    jobid: 64
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000242.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000212.1.mpileup
    output: output/varScan/Pfeiffer3_GL000212.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000212.1.snp.2017-07-05.19-06-27.stderr
    jobid: 292
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000212.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000200.1.mpileup
    output: output/varScan/Pfeiffer2_GL000200.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000200.1.indel.2017-07-05.19-06-27.stderr
    jobid: 18
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000200.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000242.1.mpileup
    output: output/varScan/Pfeiffer3_GL000242.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000242.1.snp.2017-07-05.19-06-27.stderr
    jobid: 300
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000242.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000244.1.mpileup
    output: output/varScan/Pfeiffer3_GL000244.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000244.1.snp.2017-07-05.19-06-27.stderr
    jobid: 304
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000244.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000217.1.mpileup
    output: output/varScan/Pfeiffer3_GL000217.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000217.1.indel.2017-07-05.19-06-27.stderr
    jobid: 315
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000217.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000209.1.mpileup
    output: output/varScan/Pfeiffer2_GL000209.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000209.1.indel.2017-07-05.19-06-27.stderr
    jobid: 324
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000209.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_14.mpileup
    output: output/varScan/Pfeiffer3_14.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_14.snp.2017-07-05.19-06-27.stderr
    jobid: 328
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_14, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000205.1.mpileup
    output: output/varScan/Pfeiffer2_GL000205.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000205.1.indel.2017-07-05.19-06-27.stderr
    jobid: 332
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000205.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_10.mpileup
    output: output/varScan/Pfeiffer2_10.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_10.snp.2017-07-05.19-06-27.stderr
    jobid: 45
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_10, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_19.mpileup
    output: output/varScan/Pfeiffer2_19.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_19.snp.2017-07-05.19-06-27.stderr
    jobid: 10
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_19, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000205.1.mpileup
    output: output/varScan/Pfeiffer2_GL000205.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000205.1.snp.2017-07-05.19-06-27.stderr
    jobid: 70
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000205.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000229.1.mpileup
    output: output/varScan/Pfeiffer3_GL000229.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000229.1.snp.2017-07-05.19-06-27.stderr
    jobid: 37
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000229.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000238.1.mpileup
    output: output/varScan/Pfeiffer3_GL000238.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000238.1.indel.2017-07-05.19-06-27.stderr
    jobid: 44
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000238.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000197.1.mpileup
    output: output/varScan/Pfeiffer2_GL000197.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000197.1.snp.2017-07-05.19-06-27.stderr
    jobid: 46
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000197.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000193.1.mpileup
    output: output/varScan/Pfeiffer3_GL000193.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000193.1.indel.2017-07-05.19-06-27.stderr
    jobid: 55
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000193.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000196.1.mpileup
    output: output/varScan/Pfeiffer2_GL000196.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000196.1.indel.2017-07-05.19-06-27.stderr
    jobid: 59
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000196.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000245.1.mpileup
    output: output/varScan/Pfeiffer2_GL000245.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000245.1.snp.2017-07-05.19-06-27.stderr
    jobid: 62
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000245.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_18.mpileup
    output: output/varScan/Pfeiffer2_18.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_18.indel.2017-07-05.19-06-27.stderr
    jobid: 52
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_18, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_22.mpileup
    output: output/varScan/Pfeiffer2_22.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_22.snp.2017-07-05.19-06-27.stderr
    jobid: 68
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_22, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000206.1.mpileup
    output: output/varScan/Pfeiffer3_GL000206.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000206.1.indel.2017-07-05.19-06-27.stderr
    jobid: 233
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000206.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_4.mpileup
    output: output/varScan/Pfeiffer3_4.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_4.indel.2017-07-05.19-06-27.stderr
    jobid: 39
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_4, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_1.mpileup
    output: output/varScan/Pfeiffer2_1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_1.indel.2017-07-05.19-06-27.stderr
    jobid: 76
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000242.1.mpileup
    output: output/varScan/Pfeiffer2_GL000242.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000242.1.snp.2017-07-05.19-06-27.stderr
    jobid: 78
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000242.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000234.1.mpileup
    output: output/varScan/Pfeiffer3_GL000234.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000234.1.indel.2017-07-05.19-06-27.stderr
    jobid: 81
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000234.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000217.1.mpileup
    output: output/varScan/Pfeiffer2_GL000217.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000217.1.snp.2017-07-05.19-06-27.stderr
    jobid: 234
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000217.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_4.mpileup
    output: output/varScan/Pfeiffer3_4.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_4.snp.2017-07-05.19-06-27.stderr
    jobid: 88
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_4, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000239.1.mpileup
    output: output/varScan/Pfeiffer3_GL000239.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000239.1.snp.2017-07-05.19-06-27.stderr
    jobid: 95
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000239.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000194.1.mpileup
    output: output/varScan/Pfeiffer2_GL000194.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000194.1.snp.2017-07-05.19-06-27.stderr
    jobid: 102
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000194.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000222.1.mpileup
    output: output/varScan/Pfeiffer2_GL000222.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000222.1.snp.2017-07-05.19-06-27.stderr
    jobid: 103
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000222.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000200.1.mpileup
    output: output/varScan/Pfeiffer3_GL000200.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000200.1.snp.2017-07-05.19-06-27.stderr
    jobid: 327
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000200.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000247.1.mpileup
    output: output/varScan/Pfeiffer3_GL000247.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000247.1.indel.2017-07-05.19-06-27.stderr
    jobid: 112
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000247.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000213.1.mpileup
    output: output/varScan/Pfeiffer3_GL000213.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000213.1.indel.2017-07-05.19-06-27.stderr
    jobid: 114
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000213.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000208.1.mpileup
    output: output/varScan/Pfeiffer3_GL000208.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000208.1.snp.2017-07-05.19-06-27.stderr
    jobid: 148
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000208.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_18.mpileup
    output: output/varScan/Pfeiffer2_18.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_18.snp.2017-07-05.19-06-27.stderr
    jobid: 129
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_18, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000230.1.mpileup
    output: output/varScan/Pfeiffer3_GL000230.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000230.1.indel.2017-07-05.19-06-27.stderr
    jobid: 130
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000230.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000232.1.mpileup
    output: output/varScan/Pfeiffer3_GL000232.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000232.1.snp.2017-07-05.19-06-27.stderr
    jobid: 217
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000232.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000248.1.mpileup
    output: output/varScan/Pfeiffer2_GL000248.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000248.1.snp.2017-07-05.19-06-27.stderr
    jobid: 86
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000248.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_2.mpileup
    output: output/varScan/Pfeiffer2_2.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_2.snp.2017-07-05.19-06-27.stderr
    jobid: 116
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_2, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000226.1.mpileup
    output: output/varScan/Pfeiffer2_GL000226.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000226.1.indel.2017-07-05.19-06-27.stderr
    jobid: 138
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000226.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_12.mpileup
    output: output/varScan/Pfeiffer2_12.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_12.snp.2017-07-05.19-06-27.stderr
    jobid: 146
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_12, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_7.mpileup
    output: output/varScan/Pfeiffer3_7.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_7.indel.2017-07-05.19-06-27.stderr
    jobid: 150
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_7, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_8.mpileup
    output: output/varScan/Pfeiffer2_8.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_8.indel.2017-07-05.19-06-27.stderr
    jobid: 151
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_8, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000191.1.mpileup
    output: output/varScan/Pfeiffer3_GL000191.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000191.1.indel.2017-07-05.19-06-27.stderr
    jobid: 235
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000191.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000247.1.mpileup
    output: output/varScan/Pfeiffer3_GL000247.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000247.1.snp.2017-07-05.19-06-27.stderr
    jobid: 154
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000247.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000224.1.mpileup
    output: output/varScan/Pfeiffer3_GL000224.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000224.1.snp.2017-07-05.19-06-27.stderr
    jobid: 99
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000224.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_21.mpileup
    output: output/varScan/Pfeiffer3_21.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_21.snp.2017-07-05.19-06-27.stderr
    jobid: 262
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_21, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000219.1.mpileup
    output: output/varScan/Pfeiffer3_GL000219.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000219.1.snp.2017-07-05.19-06-27.stderr
    jobid: 161
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000219.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_17.mpileup
    output: output/varScan/Pfeiffer2_17.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_17.snp.2017-07-05.19-06-27.stderr
    jobid: 170
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_17, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000214.1.mpileup
    output: output/varScan/Pfeiffer3_GL000214.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000214.1.snp.2017-07-05.19-06-27.stderr
    jobid: 173
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000214.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000198.1.mpileup
    output: output/varScan/Pfeiffer2_GL000198.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000198.1.snp.2017-07-05.19-06-27.stderr
    jobid: 320
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000198.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000212.1.mpileup
    output: output/varScan/Pfeiffer3_GL000212.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000212.1.indel.2017-07-05.19-06-27.stderr
    jobid: 180
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000212.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000207.1.mpileup
    output: output/varScan/Pfeiffer2_GL000207.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000207.1.indel.2017-07-05.19-06-27.stderr
    jobid: 198
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000207.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_22.mpileup
    output: output/varScan/Pfeiffer3_22.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_22.snp.2017-07-05.19-06-27.stderr
    jobid: 188
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_22, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000230.1.mpileup
    output: output/varScan/Pfeiffer2_GL000230.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000230.1.indel.2017-07-05.19-06-27.stderr
    jobid: 189
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000230.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000222.1.mpileup
    output: output/varScan/Pfeiffer2_GL000222.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000222.1.indel.2017-07-05.19-06-27.stderr
    jobid: 23
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000222.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_6.mpileup
    output: output/varScan/Pfeiffer2_6.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_6.snp.2017-07-05.19-06-27.stderr
    jobid: 201
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_6, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000235.1.mpileup
    output: output/varScan/Pfeiffer3_GL000235.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000235.1.snp.2017-07-05.19-06-27.stderr
    jobid: 204
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000235.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_21.mpileup
    output: output/varScan/Pfeiffer2_21.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_21.indel.2017-07-05.19-06-27.stderr
    jobid: 202
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_21, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000235.1.mpileup
    output: output/varScan/Pfeiffer2_GL000235.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000235.1.indel.2017-07-05.19-06-27.stderr
    jobid: 208
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000235.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000198.1.mpileup
    output: output/varScan/Pfeiffer3_GL000198.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000198.1.indel.2017-07-05.19-06-27.stderr
    jobid: 211
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000198.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_22.mpileup
    output: output/varScan/Pfeiffer2_22.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_22.indel.2017-07-05.19-06-27.stderr
    jobid: 214
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_22, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000241.1.mpileup
    output: output/varScan/Pfeiffer3_GL000241.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000241.1.snp.2017-07-05.19-06-27.stderr
    jobid: 215
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000241.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_11.mpileup
    output: output/varScan/Pfeiffer2_11.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_11.snp.2017-07-05.19-06-27.stderr
    jobid: 110
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_11, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000202.1.mpileup
    output: output/varScan/Pfeiffer2_GL000202.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000202.1.snp.2017-07-05.19-06-27.stderr
    jobid: 226
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000202.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000213.1.mpileup
    output: output/varScan/Pfeiffer2_GL000213.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000213.1.indel.2017-07-05.19-06-27.stderr
    jobid: 256
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000213.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_3.mpileup
    output: output/varScan/Pfeiffer2_3.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_3.indel.2017-07-05.19-06-27.stderr
    jobid: 257
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_3, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000232.1.mpileup
    output: output/varScan/Pfeiffer2_GL000232.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000232.1.snp.2017-07-05.19-06-27.stderr
    jobid: 266
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000232.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000211.1.mpileup
    output: output/varScan/Pfeiffer2_GL000211.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000211.1.snp.2017-07-05.19-06-27.stderr
    jobid: 268
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000211.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_11.mpileup
    output: output/varScan/Pfeiffer2_11.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_11.indel.2017-07-05.19-06-27.stderr
    jobid: 245
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_11, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000192.1.mpileup
    output: output/varScan/Pfeiffer2_GL000192.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000192.1.indel.2017-07-05.19-06-27.stderr
    jobid: 270
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000192.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000201.1.mpileup
    output: output/varScan/Pfeiffer2_GL000201.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000201.1.indel.2017-07-05.19-06-27.stderr
    jobid: 275
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000201.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_16.mpileup
    output: output/varScan/Pfeiffer3_16.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_16.snp.2017-07-05.19-06-27.stderr
    jobid: 277
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_16, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_5.mpileup
    output: output/varScan/Pfeiffer3_5.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_5.indel.2017-07-05.19-06-27.stderr
    jobid: 323
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_5, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_X.mpileup
    output: output/varScan/Pfeiffer3_X.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_X.indel.2017-07-05.19-06-27.stderr
    jobid: 278
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_X, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000213.1.mpileup
    output: output/varScan/Pfeiffer2_GL000213.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000213.1.snp.2017-07-05.19-06-27.stderr
    jobid: 284
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000213.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000197.1.mpileup
    output: output/varScan/Pfeiffer3_GL000197.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000197.1.snp.2017-07-05.19-06-27.stderr
    jobid: 285
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000197.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000238.1.mpileup
    output: output/varScan/Pfeiffer2_GL000238.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000238.1.indel.2017-07-05.19-06-27.stderr
    jobid: 286
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000238.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000245.1.mpileup
    output: output/varScan/Pfeiffer3_GL000245.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000245.1.snp.2017-07-05.19-06-27.stderr
    jobid: 296
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000245.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000227.1.mpileup
    output: output/varScan/Pfeiffer2_GL000227.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000227.1.snp.2017-07-05.19-06-27.stderr
    jobid: 91
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000227.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_10.mpileup
    output: output/varScan/Pfeiffer3_10.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_10.indel.2017-07-05.19-06-27.stderr
    jobid: 259
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_10, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000239.1.mpileup
    output: output/varScan/Pfeiffer2_GL000239.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000239.1.snp.2017-07-05.19-06-27.stderr
    jobid: 106
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000239.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000232.1.mpileup
    output: output/varScan/Pfeiffer3_GL000232.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000232.1.indel.2017-07-05.19-06-27.stderr
    jobid: 228
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000232.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_1.mpileup
    output: output/varScan/Pfeiffer3_1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_1.snp.2017-07-05.19-06-27.stderr
    jobid: 305
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000215.1.mpileup
    output: output/varScan/Pfeiffer3_GL000215.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000215.1.snp.2017-07-05.19-06-27.stderr
    jobid: 185
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000215.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000212.1.mpileup
    output: output/varScan/Pfeiffer2_GL000212.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000212.1.indel.2017-07-05.19-06-27.stderr
    jobid: 310
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000212.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_1.mpileup
    output: output/varScan/Pfeiffer2_1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_1.snp.2017-07-05.19-06-27.stderr
    jobid: 299
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000245.1.mpileup
    output: output/varScan/Pfeiffer2_GL000245.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000245.1.indel.2017-07-05.19-06-27.stderr
    jobid: 312
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000245.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000215.1.mpileup
    output: output/varScan/Pfeiffer3_GL000215.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000215.1.indel.2017-07-05.19-06-27.stderr
    jobid: 311
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000215.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000228.1.mpileup
    output: output/varScan/Pfeiffer3_GL000228.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000228.1.snp.2017-07-05.19-06-27.stderr
    jobid: 186
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000228.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000242.1.mpileup
    output: output/varScan/Pfeiffer2_GL000242.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000242.1.indel.2017-07-05.19-06-27.stderr
    jobid: 317
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000242.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_9.mpileup
    output: output/varScan/Pfeiffer2_9.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_9.snp.2017-07-05.19-06-27.stderr
    jobid: 322
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_9, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_14.mpileup
    output: output/varScan/Pfeiffer3_14.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_14.indel.2017-07-05.19-06-27.stderr
    jobid: 51
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_14, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000241.1.mpileup
    output: output/varScan/Pfeiffer3_GL000241.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000241.1.indel.2017-07-05.19-06-27.stderr
    jobid: 128
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000241.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_4.mpileup
    output: output/varScan/Pfeiffer2_4.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_4.indel.2017-07-05.19-06-27.stderr
    jobid: 333
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_4, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_5.mpileup
    output: output/varScan/Pfeiffer2_5.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_5.indel.2017-07-05.19-06-27.stderr
    jobid: 325
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_5, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000197.1.mpileup
    output: output/varScan/Pfeiffer2_GL000197.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000197.1.indel.2017-07-05.19-06-27.stderr
    jobid: 336
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000197.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000223.1.mpileup
    output: output/varScan/Pfeiffer3_GL000223.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000223.1.indel.2017-07-05.19-06-27.stderr
    jobid: 2
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000223.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_8.mpileup
    output: output/varScan/Pfeiffer3_8.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_8.snp.2017-07-05.19-06-27.stderr
    jobid: 11
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_8, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000199.1.mpileup
    output: output/varScan/Pfeiffer2_GL000199.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000199.1.indel.2017-07-05.19-06-27.stderr
    jobid: 17
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000199.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000236.1.mpileup
    output: output/varScan/Pfeiffer3_GL000236.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000236.1.indel.2017-07-05.19-06-27.stderr
    jobid: 19
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000236.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000233.1.mpileup
    output: output/varScan/Pfeiffer2_GL000233.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000233.1.indel.2017-07-05.19-06-27.stderr
    jobid: 115
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000233.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000226.1.mpileup
    output: output/varScan/Pfeiffer3_GL000226.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000226.1.indel.2017-07-05.19-06-27.stderr
    jobid: 21
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000226.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000199.1.mpileup
    output: output/varScan/Pfeiffer3_GL000199.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000199.1.indel.2017-07-05.19-06-27.stderr
    jobid: 249
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000199.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000227.1.mpileup
    output: output/varScan/Pfeiffer2_GL000227.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000227.1.indel.2017-07-05.19-06-27.stderr
    jobid: 26
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000227.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000192.1.mpileup
    output: output/varScan/Pfeiffer3_GL000192.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000192.1.indel.2017-07-05.19-06-27.stderr
    jobid: 31
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000192.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000239.1.mpileup
    output: output/varScan/Pfeiffer3_GL000239.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000239.1.indel.2017-07-05.19-06-27.stderr
    jobid: 32
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000239.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000196.1.mpileup
    output: output/varScan/Pfeiffer3_GL000196.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000196.1.indel.2017-07-05.19-06-27.stderr
    jobid: 298
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000196.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_4.mpileup
    output: output/varScan/Pfeiffer2_4.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_4.snp.2017-07-05.19-06-27.stderr
    jobid: 60
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_4, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000226.1.mpileup
    output: output/varScan/Pfeiffer2_GL000226.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000226.1.snp.2017-07-05.19-06-27.stderr
    jobid: 69
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000226.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000220.1.mpileup
    output: output/varScan/Pfeiffer2_GL000220.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000220.1.indel.2017-07-05.19-06-27.stderr
    jobid: 87
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000220.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000234.1.mpileup
    output: output/varScan/Pfeiffer2_GL000234.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000234.1.indel.2017-07-05.19-06-27.stderr
    jobid: 246
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000234.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000199.1.mpileup
    output: output/varScan/Pfeiffer3_GL000199.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000199.1.snp.2017-07-05.19-06-27.stderr
    jobid: 98
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000199.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_8.mpileup
    output: output/varScan/Pfeiffer2_8.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_8.snp.2017-07-05.19-06-27.stderr
    jobid: 105
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_8, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_20.mpileup
    output: output/varScan/Pfeiffer3_20.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_20.snp.2017-07-05.19-06-27.stderr
    jobid: 108
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_20, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000191.1.mpileup
    output: output/varScan/Pfeiffer2_GL000191.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000191.1.indel.2017-07-05.19-06-27.stderr
    jobid: 1
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000191.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_X.mpileup
    output: output/varScan/Pfeiffer2_X.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_X.indel.2017-07-05.19-06-27.stderr
    jobid: 16
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_X, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000247.1.mpileup
    output: output/varScan/Pfeiffer2_GL000247.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000247.1.snp.2017-07-05.19-06-27.stderr
    jobid: 117
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000247.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000192.1.mpileup
    output: output/varScan/Pfeiffer3_GL000192.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000192.1.snp.2017-07-05.19-06-27.stderr
    jobid: 122
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000192.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000230.1.mpileup
    output: output/varScan/Pfeiffer3_GL000230.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000230.1.snp.2017-07-05.19-06-27.stderr
    jobid: 85
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000230.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000233.1.mpileup
    output: output/varScan/Pfeiffer3_GL000233.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000233.1.snp.2017-07-05.19-06-27.stderr
    jobid: 12
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000233.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000193.1.mpileup
    output: output/varScan/Pfeiffer3_GL000193.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000193.1.snp.2017-07-05.19-06-27.stderr
    jobid: 132
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000193.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000231.1.mpileup
    output: output/varScan/Pfeiffer3_GL000231.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000231.1.indel.2017-07-05.19-06-27.stderr
    jobid: 133
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000231.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000221.1.mpileup
    output: output/varScan/Pfeiffer2_GL000221.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000221.1.snp.2017-07-05.19-06-27.stderr
    jobid: 134
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000221.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_3.mpileup
    output: output/varScan/Pfeiffer2_3.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_3.snp.2017-07-05.19-06-27.stderr
    jobid: 135
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_3, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_19.mpileup
    output: output/varScan/Pfeiffer3_19.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_19.snp.2017-07-05.19-06-27.stderr
    jobid: 141
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_19, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000198.1.mpileup
    output: output/varScan/Pfeiffer3_GL000198.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000198.1.snp.2017-07-05.19-06-27.stderr
    jobid: 142
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000198.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000235.1.mpileup
    output: output/varScan/Pfeiffer3_GL000235.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000235.1.indel.2017-07-05.19-06-27.stderr
    jobid: 182
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000235.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000221.1.mpileup
    output: output/varScan/Pfeiffer3_GL000221.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000221.1.snp.2017-07-05.19-06-27.stderr
    jobid: 145
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000221.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000236.1.mpileup
    output: output/varScan/Pfeiffer2_GL000236.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000236.1.snp.2017-07-05.19-06-27.stderr
    jobid: 156
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000236.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_6.mpileup
    output: output/varScan/Pfeiffer3_6.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_6.indel.2017-07-05.19-06-27.stderr
    jobid: 157
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_6, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000243.1.mpileup
    output: output/varScan/Pfeiffer3_GL000243.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000243.1.snp.2017-07-05.19-06-27.stderr
    jobid: 160
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000243.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000215.1.mpileup
    output: output/varScan/Pfeiffer2_GL000215.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000215.1.snp.2017-07-05.19-06-27.stderr
    jobid: 162
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000215.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000217.1.mpileup
    output: output/varScan/Pfeiffer2_GL000217.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000217.1.indel.2017-07-05.19-06-27.stderr
    jobid: 165
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000217.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000235.1.mpileup
    output: output/varScan/Pfeiffer2_GL000235.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000235.1.snp.2017-07-05.19-06-27.stderr
    jobid: 167
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000235.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000199.1.mpileup
    output: output/varScan/Pfeiffer2_GL000199.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000199.1.snp.2017-07-05.19-06-27.stderr
    jobid: 168
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000199.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_13.mpileup
    output: output/varScan/Pfeiffer2_13.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_13.indel.2017-07-05.19-06-27.stderr
    jobid: 169
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_13, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000225.1.mpileup
    output: output/varScan/Pfeiffer2_GL000225.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000225.1.indel.2017-07-05.19-06-27.stderr
    jobid: 40
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000225.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000191.1.mpileup
    output: output/varScan/Pfeiffer3_GL000191.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000191.1.snp.2017-07-05.19-06-27.stderr
    jobid: 49
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000191.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000220.1.mpileup
    output: output/varScan/Pfeiffer3_GL000220.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000220.1.indel.2017-07-05.19-06-27.stderr
    jobid: 271
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000220.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000237.1.mpileup
    output: output/varScan/Pfeiffer2_GL000237.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000237.1.snp.2017-07-05.19-06-27.stderr
    jobid: 190
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000237.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000244.1.mpileup
    output: output/varScan/Pfeiffer3_GL000244.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000244.1.indel.2017-07-05.19-06-27.stderr
    jobid: 194
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000244.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000195.1.mpileup
    output: output/varScan/Pfeiffer3_GL000195.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000195.1.indel.2017-07-05.19-06-27.stderr
    jobid: 195
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000195.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_9.mpileup
    output: output/varScan/Pfeiffer3_9.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_9.snp.2017-07-05.19-06-27.stderr
    jobid: 196
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_9, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000244.1.mpileup
    output: output/varScan/Pfeiffer2_GL000244.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000244.1.indel.2017-07-05.19-06-27.stderr
    jobid: 124
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000244.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_20.mpileup
    output: output/varScan/Pfeiffer3_20.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_20.indel.2017-07-05.19-06-27.stderr
    jobid: 210
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_20, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000220.1.mpileup
    output: output/varScan/Pfeiffer3_GL000220.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000220.1.snp.2017-07-05.19-06-27.stderr
    jobid: 219
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000220.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000196.1.mpileup
    output: output/varScan/Pfeiffer3_GL000196.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000196.1.snp.2017-07-05.19-06-27.stderr
    jobid: 220
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000196.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000226.1.mpileup
    output: output/varScan/Pfeiffer3_GL000226.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000226.1.snp.2017-07-05.19-06-27.stderr
    jobid: 329
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000226.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000202.1.mpileup
    output: output/varScan/Pfeiffer3_GL000202.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000202.1.snp.2017-07-05.19-06-27.stderr
    jobid: 229
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000202.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_13.mpileup
    output: output/varScan/Pfeiffer2_13.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_13.snp.2017-07-05.19-06-27.stderr
    jobid: 13
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_13, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_15.mpileup
    output: output/varScan/Pfeiffer2_15.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_15.snp.2017-07-05.19-06-27.stderr
    jobid: 243
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_15, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_14.mpileup
    output: output/varScan/Pfeiffer2_14.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_14.snp.2017-07-05.19-06-27.stderr
    jobid: 113
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_14, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_15.mpileup
    output: output/varScan/Pfeiffer2_15.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_15.indel.2017-07-05.19-06-27.stderr
    jobid: 254
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_15, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000216.1.mpileup
    output: output/varScan/Pfeiffer2_GL000216.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000216.1.indel.2017-07-05.19-06-27.stderr
    jobid: 258
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000216.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000215.1.mpileup
    output: output/varScan/Pfeiffer2_GL000215.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000215.1.indel.2017-07-05.19-06-27.stderr
    jobid: 261
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000215.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000240.1.mpileup
    output: output/varScan/Pfeiffer2_GL000240.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000240.1.indel.2017-07-05.19-06-27.stderr
    jobid: 272
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000240.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000218.1.mpileup
    output: output/varScan/Pfeiffer2_GL000218.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000218.1.snp.2017-07-05.19-06-27.stderr
    jobid: 273
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000218.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000248.1.mpileup
    output: output/varScan/Pfeiffer3_GL000248.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000248.1.snp.2017-07-05.19-06-27.stderr
    jobid: 291
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000248.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000222.1.mpileup
    output: output/varScan/Pfeiffer3_GL000222.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000222.1.indel.2017-07-05.19-06-27.stderr
    jobid: 308
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000222.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000224.1.mpileup
    output: output/varScan/Pfeiffer2_GL000224.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000224.1.indel.2017-07-05.19-06-27.stderr
    jobid: 318
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000224.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000239.1.mpileup
    output: output/varScan/Pfeiffer2_GL000239.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000239.1.indel.2017-07-05.19-06-27.stderr
    jobid: 279
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000239.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_13.mpileup
    output: output/varScan/Pfeiffer3_13.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_13.snp.2017-07-05.19-06-27.stderr
    jobid: 280
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_13, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000228.1.mpileup
    output: output/varScan/Pfeiffer2_GL000228.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000228.1.snp.2017-07-05.19-06-27.stderr
    jobid: 282
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000228.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000193.1.mpileup
    output: output/varScan/Pfeiffer2_GL000193.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000193.1.indel.2017-07-05.19-06-27.stderr
    jobid: 287
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000193.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000236.1.mpileup
    output: output/varScan/Pfeiffer2_GL000236.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000236.1.indel.2017-07-05.19-06-27.stderr
    jobid: 289
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000236.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000237.1.mpileup
    output: output/varScan/Pfeiffer3_GL000237.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000237.1.indel.2017-07-05.19-06-27.stderr
    jobid: 290
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000237.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_1.mpileup
    output: output/varScan/Pfeiffer3_1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_1.indel.2017-07-05.19-06-27.stderr
    jobid: 293
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_9.mpileup
    output: output/varScan/Pfeiffer3_9.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_9.indel.2017-07-05.19-06-27.stderr
    jobid: 297
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_9, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000243.1.mpileup
    output: output/varScan/Pfeiffer3_GL000243.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000243.1.indel.2017-07-05.19-06-27.stderr
    jobid: 139
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000243.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_19.mpileup
    output: output/varScan/Pfeiffer2_19.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_19.indel.2017-07-05.19-06-27.stderr
    jobid: 302
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_19, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_GL000216.1.mpileup
    output: output/varScan/Pfeiffer2_GL000216.1.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_GL000216.1.snp.2017-07-05.19-06-27.stderr
    jobid: 306
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_GL000216.1, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_Y.mpileup
    output: output/varScan/Pfeiffer2_Y.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_Y.indel.2017-07-05.19-06-27.stderr
    jobid: 307
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_Y, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_X.mpileup
    output: output/varScan/Pfeiffer2_X.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_X.snp.2017-07-05.19-06-27.stderr
    jobid: 319
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_X, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000225.1.mpileup
    output: output/varScan/Pfeiffer3_GL000225.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000225.1.indel.2017-07-05.19-06-27.stderr
    jobid: 264
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000225.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_GL000200.1.mpileup
    output: output/varScan/Pfeiffer3_GL000200.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_GL000200.1.indel.2017-07-05.19-06-27.stderr
    jobid: 330
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_GL000200.1, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_Y.mpileup
    output: output/varScan/Pfeiffer2_Y.varScan.snp.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_Y.snp.2017-07-05.19-06-27.stderr
    jobid: 335
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_Y, varTypeMPU2VCFS=snp


localrule all:
    input: output/varScan/Pfeiffer2_1.varScan.snp.vcf, output/varScan/Pfeiffer2_2.varScan.snp.vcf, output/varScan/Pfeiffer2_3.varScan.snp.vcf, output/varScan/Pfeiffer2_4.varScan.snp.vcf, output/varScan/Pfeiffer2_5.varScan.snp.vcf, output/varScan/Pfeiffer2_6.varScan.snp.vcf, output/varScan/Pfeiffer2_7.varScan.snp.vcf, output/varScan/Pfeiffer2_8.varScan.snp.vcf, output/varScan/Pfeiffer2_9.varScan.snp.vcf, output/varScan/Pfeiffer2_10.varScan.snp.vcf, output/varScan/Pfeiffer2_11.varScan.snp.vcf, output/varScan/Pfeiffer2_12.varScan.snp.vcf, output/varScan/Pfeiffer2_13.varScan.snp.vcf, output/varScan/Pfeiffer2_14.varScan.snp.vcf, output/varScan/Pfeiffer2_15.varScan.snp.vcf, output/varScan/Pfeiffer2_16.varScan.snp.vcf, output/varScan/Pfeiffer2_17.varScan.snp.vcf, output/varScan/Pfeiffer2_18.varScan.snp.vcf, output/varScan/Pfeiffer2_19.varScan.snp.vcf, output/varScan/Pfeiffer2_20.varScan.snp.vcf, output/varScan/Pfeiffer2_21.varScan.snp.vcf, output/varScan/Pfeiffer2_22.varScan.snp.vcf, output/varScan/Pfeiffer2_X.varScan.snp.vcf, output/varScan/Pfeiffer2_Y.varScan.snp.vcf, output/varScan/Pfeiffer2_MT.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000207.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000226.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000229.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000231.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000210.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000239.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000235.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000201.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000247.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000245.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000197.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000203.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000246.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000249.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000196.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000248.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000244.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000238.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000202.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000234.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000232.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000206.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000240.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000236.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000241.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000243.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000242.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000230.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000237.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000233.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000204.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000198.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000208.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000191.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000227.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000228.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000214.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000221.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000209.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000218.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000220.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000213.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000211.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000199.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000217.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000216.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000215.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000205.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000219.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000224.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000223.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000195.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000212.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000222.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000200.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000193.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000194.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000225.1.varScan.snp.vcf, output/varScan/Pfeiffer2_GL000192.1.varScan.snp.vcf, output/varScan/Pfeiffer2_1.varScan.indel.vcf, output/varScan/Pfeiffer2_2.varScan.indel.vcf, output/varScan/Pfeiffer2_3.varScan.indel.vcf, output/varScan/Pfeiffer2_4.varScan.indel.vcf, output/varScan/Pfeiffer2_5.varScan.indel.vcf, output/varScan/Pfeiffer2_6.varScan.indel.vcf, output/varScan/Pfeiffer2_7.varScan.indel.vcf, output/varScan/Pfeiffer2_8.varScan.indel.vcf, output/varScan/Pfeiffer2_9.varScan.indel.vcf, output/varScan/Pfeiffer2_10.varScan.indel.vcf, output/varScan/Pfeiffer2_11.varScan.indel.vcf, output/varScan/Pfeiffer2_12.varScan.indel.vcf, output/varScan/Pfeiffer2_13.varScan.indel.vcf, output/varScan/Pfeiffer2_14.varScan.indel.vcf, output/varScan/Pfeiffer2_15.varScan.indel.vcf, output/varScan/Pfeiffer2_16.varScan.indel.vcf, output/varScan/Pfeiffer2_17.varScan.indel.vcf, output/varScan/Pfeiffer2_18.varScan.indel.vcf, output/varScan/Pfeiffer2_19.varScan.indel.vcf, output/varScan/Pfeiffer2_20.varScan.indel.vcf, output/varScan/Pfeiffer2_21.varScan.indel.vcf, output/varScan/Pfeiffer2_22.varScan.indel.vcf, output/varScan/Pfeiffer2_X.varScan.indel.vcf, output/varScan/Pfeiffer2_Y.varScan.indel.vcf, output/varScan/Pfeiffer2_MT.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000207.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000226.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000229.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000231.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000210.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000239.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000235.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000201.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000247.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000245.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000197.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000203.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000246.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000249.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000196.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000248.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000244.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000238.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000202.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000234.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000232.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000206.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000240.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000236.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000241.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000243.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000242.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000230.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000237.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000233.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000204.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000198.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000208.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000191.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000227.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000228.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000214.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000221.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000209.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000218.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000220.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000213.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000211.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000199.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000217.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000216.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000215.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000205.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000219.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000224.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000223.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000195.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000212.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000222.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000200.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000193.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000194.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000225.1.varScan.indel.vcf, output/varScan/Pfeiffer2_GL000192.1.varScan.indel.vcf, output/varScan/Pfeiffer3_1.varScan.snp.vcf, output/varScan/Pfeiffer3_2.varScan.snp.vcf, output/varScan/Pfeiffer3_3.varScan.snp.vcf, output/varScan/Pfeiffer3_4.varScan.snp.vcf, output/varScan/Pfeiffer3_5.varScan.snp.vcf, output/varScan/Pfeiffer3_6.varScan.snp.vcf, output/varScan/Pfeiffer3_7.varScan.snp.vcf, output/varScan/Pfeiffer3_8.varScan.snp.vcf, output/varScan/Pfeiffer3_9.varScan.snp.vcf, output/varScan/Pfeiffer3_10.varScan.snp.vcf, output/varScan/Pfeiffer3_11.varScan.snp.vcf, output/varScan/Pfeiffer3_12.varScan.snp.vcf, output/varScan/Pfeiffer3_13.varScan.snp.vcf, output/varScan/Pfeiffer3_14.varScan.snp.vcf, output/varScan/Pfeiffer3_15.varScan.snp.vcf, output/varScan/Pfeiffer3_16.varScan.snp.vcf, output/varScan/Pfeiffer3_17.varScan.snp.vcf, output/varScan/Pfeiffer3_18.varScan.snp.vcf, output/varScan/Pfeiffer3_19.varScan.snp.vcf, output/varScan/Pfeiffer3_20.varScan.snp.vcf, output/varScan/Pfeiffer3_21.varScan.snp.vcf, output/varScan/Pfeiffer3_22.varScan.snp.vcf, output/varScan/Pfeiffer3_X.varScan.snp.vcf, output/varScan/Pfeiffer3_Y.varScan.snp.vcf, output/varScan/Pfeiffer3_MT.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000207.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000226.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000229.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000231.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000210.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000239.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000235.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000201.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000247.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000245.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000197.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000203.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000246.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000249.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000196.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000248.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000244.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000238.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000202.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000234.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000232.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000206.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000240.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000236.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000241.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000243.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000242.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000230.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000237.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000233.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000204.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000198.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000208.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000191.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000227.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000228.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000214.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000221.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000209.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000218.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000220.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000213.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000211.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000199.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000217.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000216.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000215.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000205.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000219.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000224.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000223.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000195.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000212.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000222.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000200.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000193.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000194.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000225.1.varScan.snp.vcf, output/varScan/Pfeiffer3_GL000192.1.varScan.snp.vcf, output/varScan/Pfeiffer3_1.varScan.indel.vcf, output/varScan/Pfeiffer3_2.varScan.indel.vcf, output/varScan/Pfeiffer3_3.varScan.indel.vcf, output/varScan/Pfeiffer3_4.varScan.indel.vcf, output/varScan/Pfeiffer3_5.varScan.indel.vcf, output/varScan/Pfeiffer3_6.varScan.indel.vcf, output/varScan/Pfeiffer3_7.varScan.indel.vcf, output/varScan/Pfeiffer3_8.varScan.indel.vcf, output/varScan/Pfeiffer3_9.varScan.indel.vcf, output/varScan/Pfeiffer3_10.varScan.indel.vcf, output/varScan/Pfeiffer3_11.varScan.indel.vcf, output/varScan/Pfeiffer3_12.varScan.indel.vcf, output/varScan/Pfeiffer3_13.varScan.indel.vcf, output/varScan/Pfeiffer3_14.varScan.indel.vcf, output/varScan/Pfeiffer3_15.varScan.indel.vcf, output/varScan/Pfeiffer3_16.varScan.indel.vcf, output/varScan/Pfeiffer3_17.varScan.indel.vcf, output/varScan/Pfeiffer3_18.varScan.indel.vcf, output/varScan/Pfeiffer3_19.varScan.indel.vcf, output/varScan/Pfeiffer3_20.varScan.indel.vcf, output/varScan/Pfeiffer3_21.varScan.indel.vcf, output/varScan/Pfeiffer3_22.varScan.indel.vcf, output/varScan/Pfeiffer3_X.varScan.indel.vcf, output/varScan/Pfeiffer3_Y.varScan.indel.vcf, output/varScan/Pfeiffer3_MT.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000207.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000226.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000229.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000231.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000210.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000239.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000235.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000201.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000247.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000245.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000197.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000203.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000246.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000249.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000196.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000248.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000244.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000238.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000202.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000234.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000232.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000206.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000240.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000236.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000241.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000243.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000242.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000230.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000237.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000233.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000204.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000198.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000208.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000191.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000227.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000228.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000214.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000221.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000209.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000218.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000220.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000213.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000211.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000199.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000217.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000216.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000215.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000205.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000219.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000224.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000223.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000195.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000212.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000222.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000200.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000193.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000194.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000225.1.varScan.indel.vcf, output/varScan/Pfeiffer3_GL000192.1.varScan.indel.vcf
    jobid: 0

Job counts:
	count	jobs
	1	all
	2	bam2fastq_picard
	168	bam2mpileup
	2	bamALIGN_bwa
	4	fastq2GZ
	2	filteredBAM
	2	indexBAM
	2	markdupBAM
	336	mpileup2vcf_single
	2	sortBAM_biobambam
	521
