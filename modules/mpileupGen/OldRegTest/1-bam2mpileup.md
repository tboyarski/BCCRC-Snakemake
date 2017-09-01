# 1-bam2mpileup
This pipeline is to exemplify the default operations of this module. 

## Setting up the: Snakefile
Users must set the following submodule "call via" input requirements:

 * bam2mpileup

## Setting up the: YAML
Users must set the following "input/config.yaml" variables:

 * None

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
    input: input/rawBam/Pfeiffer2.bam
    output: output/fastq/Pfeiffer2.1.fastq, output/fastq/Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-05.11-04-57.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-05.11-04-57.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-05.11-04-57.vendor_failed_reads.log
    jobid: 186
    wildcards: sampleB2FP=Pfeiffer2


rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer3.bam
    output: output/fastq/Pfeiffer3.1.fastq, output/fastq/Pfeiffer3.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-05.11-04-57.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-05.11-04-57.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-05.11-04-57.vendor_failed_reads.log
    jobid: 185
    wildcards: sampleB2FP=Pfeiffer3


rule fastq2GZ:
    input: output/fastq/Pfeiffer2.2.fastq
    output: output/fastq/Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.2.2017-07-05.11-04-57.stderr
    jobid: 183
    wildcards: sampleFGZ=Pfeiffer2.2, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Pfeiffer2.1.fastq
    output: output/fastq/Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.1.2017-07-05.11-04-57.stderr
    jobid: 184
    wildcards: sampleFGZ=Pfeiffer2.1, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Pfeiffer3.1.fastq
    output: output/fastq/Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.1.2017-07-05.11-04-57.stderr
    jobid: 181
    wildcards: sampleFGZ=Pfeiffer3.1, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Pfeiffer3.2.fastq
    output: output/fastq/Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.2.2017-07-05.11-04-57.stderr
    jobid: 182
    wildcards: sampleFGZ=Pfeiffer3.2, pathFGZ=output/fastq


rule bamALIGN_bwa:
    input: output/fastq/Pfeiffer2.1.fastq.gz, output/fastq/Pfeiffer2.2.fastq.gz, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa
    output: output/bam/Pfeiffer2_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-05.11-04-57.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-05.11-04-57.samtools.stderr
    jobid: 180
    wildcards: sampleBAB=Pfeiffer2


rule bamALIGN_bwa:
    input: output/fastq/Pfeiffer3.1.fastq.gz, output/fastq/Pfeiffer3.2.fastq.gz, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa
    output: output/bam/Pfeiffer3_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-05.11-04-57.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-05.11-04-57.samtools.stderr
    jobid: 179
    wildcards: sampleBAB=Pfeiffer3


rule sortBAM_biobambam:
    input: output/bam/Pfeiffer2_Aligned.out.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-05.11-04-57.bamsort.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-05.11-04-57.samtools.stderr
    jobid: 178
    wildcards: pathSBB=output/bam, sampleSBB=Pfeiffer2_Aligned.out


rule sortBAM_biobambam:
    input: output/bam/Pfeiffer3_Aligned.out.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-05.11-04-57.bamsort.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-05.11-04-57.samtools.stderr
    jobid: 177
    wildcards: pathSBB=output/bam, sampleSBB=Pfeiffer3_Aligned.out


rule filteredBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer2_Aligned.out_sorted.2017-07-05.11-04-57.stderr
    jobid: 176
    wildcards: pathFB=output/bam, sampleFB=Pfeiffer2_Aligned.out_sorted


rule filteredBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer3_Aligned.out_sorted.2017-07-05.11-04-57.stderr
    jobid: 175
    wildcards: pathFB=output/bam, sampleFB=Pfeiffer3_Aligned.out_sorted


rule markdupBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam, output/metrics/Pfeiffer2_Aligned.out_sorted_filtered.dup_metrics
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer2_Aligned.out_sorted_filtered.2017-07-05.11-04-57.biobammarkdup.stderr
    jobid: 174
    wildcards: sampleMDB=Pfeiffer2_Aligned.out_sorted_filtered, outputDIR=output


rule markdupBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam, output/metrics/Pfeiffer3_Aligned.out_sorted_filtered.dup_metrics
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer3_Aligned.out_sorted_filtered.2017-07-05.11-04-57.biobammarkdup.stderr
    jobid: 173
    wildcards: sampleMDB=Pfeiffer3_Aligned.out_sorted_filtered, outputDIR=output


rule indexBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam.bai, output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer3.2017-07-05.11-04-57.stderr
    jobid: 171
    wildcards: sampleIB=Pfeiffer3, outputDIR=output


rule indexBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam.bai, output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer2.2017-07-05.11-04-57.stderr
    jobid: 172
    wildcards: sampleIB=Pfeiffer2, outputDIR=output


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000205.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 3
    wildcards: chrB2M=_GL000205.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000204.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 10
    wildcards: chrB2M=_GL000204.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_6.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 21
    wildcards: chrB2M=_6, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000219.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 22
    wildcards: chrB2M=_GL000219.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000205.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 105
    wildcards: chrB2M=_GL000205.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_12.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 29
    wildcards: chrB2M=_12, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000201.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 32
    wildcards: chrB2M=_GL000201.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000194.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 31
    wildcards: chrB2M=_GL000194.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_MT.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 73
    wildcards: chrB2M=_MT, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_8.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 48
    wildcards: chrB2M=_8, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000193.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 52
    wildcards: chrB2M=_GL000193.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000224.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 69
    wildcards: chrB2M=_GL000224.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000243.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 72
    wildcards: chrB2M=_GL000243.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000218.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 77
    wildcards: chrB2M=_GL000218.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000195.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 86
    wildcards: chrB2M=_GL000195.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000237.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 126
    wildcards: chrB2M=_GL000237.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000236.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 76
    wildcards: chrB2M=_GL000236.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_5.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 107
    wildcards: chrB2M=_5, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_11.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 110
    wildcards: chrB2M=_11, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000234.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 117
    wildcards: chrB2M=_GL000234.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000226.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 118
    wildcards: chrB2M=_GL000226.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000211.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 121
    wildcards: chrB2M=_GL000211.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_4.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 122
    wildcards: chrB2M=_4, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000232.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 132
    wildcards: chrB2M=_GL000232.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_14.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 136
    wildcards: chrB2M=_14, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000209.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 139
    wildcards: chrB2M=_GL000209.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000196.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 145
    wildcards: chrB2M=_GL000196.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000204.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 146
    wildcards: chrB2M=_GL000204.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000201.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 148
    wildcards: chrB2M=_GL000201.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000227.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 149
    wildcards: chrB2M=_GL000227.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000221.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 151
    wildcards: chrB2M=_GL000221.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000217.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 62
    wildcards: chrB2M=_GL000217.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_5.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 153
    wildcards: chrB2M=_5, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000197.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 154
    wildcards: chrB2M=_GL000197.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_13.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 155
    wildcards: chrB2M=_13, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000196.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 91
    wildcards: chrB2M=_GL000196.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_9.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 104
    wildcards: chrB2M=_9, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000219.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 165
    wildcards: chrB2M=_GL000219.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_15.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 170
    wildcards: chrB2M=_15, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000223.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 1
    wildcards: chrB2M=_GL000223.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000222.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 6
    wildcards: chrB2M=_GL000222.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000240.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 9
    wildcards: chrB2M=_GL000240.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_20.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 133
    wildcards: chrB2M=_20, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000245.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 68
    wildcards: chrB2M=_GL000245.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000192.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 12
    wildcards: chrB2M=_GL000192.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000207.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 18
    wildcards: chrB2M=_GL000207.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000214.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 19
    wildcards: chrB2M=_GL000214.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_4.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 23
    wildcards: chrB2M=_4, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000234.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 26
    wildcards: chrB2M=_GL000234.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000218.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 27
    wildcards: chrB2M=_GL000218.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000215.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 152
    wildcards: chrB2M=_GL000215.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_7.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 57
    wildcards: chrB2M=_7, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000194.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 64
    wildcards: chrB2M=_GL000194.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000233.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 49
    wildcards: chrB2M=_GL000233.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_2.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 37
    wildcards: chrB2M=_2, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000248.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 39
    wildcards: chrB2M=_GL000248.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 45
    wildcards: chrB2M=_1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_9.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 46
    wildcards: chrB2M=_9, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000202.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 47
    wildcards: chrB2M=_GL000202.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000209.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 85
    wildcards: chrB2M=_GL000209.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000223.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 54
    wildcards: chrB2M=_GL000223.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000236.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 56
    wildcards: chrB2M=_GL000236.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_22.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 58
    wildcards: chrB2M=_22, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_20.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 59
    wildcards: chrB2M=_20, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000240.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 63
    wildcards: chrB2M=_GL000240.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000191.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 99
    wildcards: chrB2M=_GL000191.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000248.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 75
    wildcards: chrB2M=_GL000248.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_12.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 78
    wildcards: chrB2M=_12, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_6.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 80
    wildcards: chrB2M=_6, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000210.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 130
    wildcards: chrB2M=_GL000210.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_16.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 82
    wildcards: chrB2M=_16, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000230.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 35
    wildcards: chrB2M=_GL000230.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_21.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 94
    wildcards: chrB2M=_21, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000224.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 97
    wildcards: chrB2M=_GL000224.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000249.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 101
    wildcards: chrB2M=_GL000249.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000206.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 106
    wildcards: chrB2M=_GL000206.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000229.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 125
    wildcards: chrB2M=_GL000229.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000215.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 108
    wildcards: chrB2M=_GL000215.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 141
    wildcards: chrB2M=_1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_10.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 131
    wildcards: chrB2M=_10, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000229.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 89
    wildcards: chrB2M=_GL000229.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000213.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 135
    wildcards: chrB2M=_GL000213.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000231.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 142
    wildcards: chrB2M=_GL000231.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000193.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 124
    wildcards: chrB2M=_GL000193.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000243.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 144
    wildcards: chrB2M=_GL000243.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_17.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 55
    wildcards: chrB2M=_17, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_18.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 150
    wildcards: chrB2M=_18, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_21.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 156
    wildcards: chrB2M=_21, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000249.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 83
    wildcards: chrB2M=_GL000249.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000207.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 115
    wildcards: chrB2M=_GL000207.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_19.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 71
    wildcards: chrB2M=_19, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000203.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 166
    wildcards: chrB2M=_GL000203.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_13.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 96
    wildcards: chrB2M=_13, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000191.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 4
    wildcards: chrB2M=_GL000191.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000246.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 7
    wildcards: chrB2M=_GL000246.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000235.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 8
    wildcards: chrB2M=_GL000235.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000237.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 11
    wildcards: chrB2M=_GL000237.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000232.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 13
    wildcards: chrB2M=_GL000232.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000192.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 14
    wildcards: chrB2M=_GL000192.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_X.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 20
    wildcards: chrB2M=_X, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_11.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 25
    wildcards: chrB2M=_11, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000202.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 2
    wildcards: chrB2M=_GL000202.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000228.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 33
    wildcards: chrB2M=_GL000228.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000198.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 38
    wildcards: chrB2M=_GL000198.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_16.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 41
    wildcards: chrB2M=_16, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000195.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 43
    wildcards: chrB2M=_GL000195.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000233.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 44
    wildcards: chrB2M=_GL000233.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000225.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 53
    wildcards: chrB2M=_GL000225.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_18.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 128
    wildcards: chrB2M=_18, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000247.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 61
    wildcards: chrB2M=_GL000247.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000203.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 66
    wildcards: chrB2M=_GL000203.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000239.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 70
    wildcards: chrB2M=_GL000239.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_3.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 127
    wildcards: chrB2M=_3, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000244.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 81
    wildcards: chrB2M=_GL000244.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000244.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 40
    wildcards: chrB2M=_GL000244.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000231.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 88
    wildcards: chrB2M=_GL000231.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000228.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 95
    wildcards: chrB2M=_GL000228.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000220.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 102
    wildcards: chrB2M=_GL000220.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_7.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 100
    wildcards: chrB2M=_7, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_22.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 111
    wildcards: chrB2M=_22, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000222.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 112
    wildcards: chrB2M=_GL000222.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000225.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 79
    wildcards: chrB2M=_GL000225.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000230.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 34
    wildcards: chrB2M=_GL000230.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000241.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 119
    wildcards: chrB2M=_GL000241.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_2.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 123
    wildcards: chrB2M=_2, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000212.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 74
    wildcards: chrB2M=_GL000212.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000242.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 137
    wildcards: chrB2M=_GL000242.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000208.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 138
    wildcards: chrB2M=_GL000208.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000216.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 140
    wildcards: chrB2M=_GL000216.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000200.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 158
    wildcards: chrB2M=_GL000200.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000214.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 163
    wildcards: chrB2M=_GL000214.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000238.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 164
    wildcards: chrB2M=_GL000238.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000199.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 167
    wildcards: chrB2M=_GL000199.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_Y.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 169
    wildcards: chrB2M=_Y, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_MT.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 5
    wildcards: chrB2M=_MT, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000238.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 15
    wildcards: chrB2M=_GL000238.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_15.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 16
    wildcards: chrB2M=_15, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_3.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 17
    wildcards: chrB2M=_3, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 24
    wildcards: chrB2M=, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_17.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 134
    wildcards: chrB2M=_17, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000245.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 28
    wildcards: chrB2M=_GL000245.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_X.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 160
    wildcards: chrB2M=_X, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000242.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 30
    wildcards: chrB2M=_GL000242.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_8.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 36
    wildcards: chrB2M=_8, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000211.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 65
    wildcards: chrB2M=_GL000211.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000198.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 50
    wildcards: chrB2M=_GL000198.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_19.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 51
    wildcards: chrB2M=_19, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000206.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 60
    wildcards: chrB2M=_GL000206.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_Y.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 113
    wildcards: chrB2M=_Y, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000212.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 67
    wildcards: chrB2M=_GL000212.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000217.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 84
    wildcards: chrB2M=_GL000217.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_14.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 87
    wildcards: chrB2M=_14, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000246.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 90
    wildcards: chrB2M=_GL000246.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000210.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 92
    wildcards: chrB2M=_GL000210.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000199.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 93
    wildcards: chrB2M=_GL000199.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000227.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 98
    wildcards: chrB2M=_GL000227.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000220.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 129
    wildcards: chrB2M=_GL000220.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_10.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 103
    wildcards: chrB2M=_10, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000200.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 114
    wildcards: chrB2M=_GL000200.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000226.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 116
    wildcards: chrB2M=_GL000226.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000216.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 157
    wildcards: chrB2M=_GL000216.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000247.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 162
    wildcards: chrB2M=_GL000247.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 42
    wildcards: chrB2M=, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000197.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 143
    wildcards: chrB2M=_GL000197.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000239.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 120
    wildcards: chrB2M=_GL000239.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000235.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 147
    wildcards: chrB2M=_GL000235.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000213.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 109
    wildcards: chrB2M=_GL000213.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2_GL000241.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.11-04-57.view.stderr
    jobid: 159
    wildcards: chrB2M=_GL000241.1, sampleB2M=Pfeiffer2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000208.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 161
    wildcards: chrB2M=_GL000208.1, sampleB2M=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3_GL000221.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.11-04-57.view.stderr
    jobid: 168
    wildcards: chrB2M=_GL000221.1, sampleB2M=Pfeiffer3


localrule all:
    input: output/mpileup/Pfeiffer2.mpileup, output/mpileup/Pfeiffer3.mpileup, output/mpileup/Pfeiffer2_1.mpileup, output/mpileup/Pfeiffer2_2.mpileup, output/mpileup/Pfeiffer2_3.mpileup, output/mpileup/Pfeiffer2_4.mpileup, output/mpileup/Pfeiffer2_5.mpileup, output/mpileup/Pfeiffer2_6.mpileup, output/mpileup/Pfeiffer2_7.mpileup, output/mpileup/Pfeiffer2_8.mpileup, output/mpileup/Pfeiffer2_9.mpileup, output/mpileup/Pfeiffer2_10.mpileup, output/mpileup/Pfeiffer2_11.mpileup, output/mpileup/Pfeiffer2_12.mpileup, output/mpileup/Pfeiffer2_13.mpileup, output/mpileup/Pfeiffer2_14.mpileup, output/mpileup/Pfeiffer2_15.mpileup, output/mpileup/Pfeiffer2_16.mpileup, output/mpileup/Pfeiffer2_17.mpileup, output/mpileup/Pfeiffer2_18.mpileup, output/mpileup/Pfeiffer2_19.mpileup, output/mpileup/Pfeiffer2_20.mpileup, output/mpileup/Pfeiffer2_21.mpileup, output/mpileup/Pfeiffer2_22.mpileup, output/mpileup/Pfeiffer2_X.mpileup, output/mpileup/Pfeiffer2_Y.mpileup, output/mpileup/Pfeiffer2_MT.mpileup, output/mpileup/Pfeiffer2_GL000207.1.mpileup, output/mpileup/Pfeiffer2_GL000226.1.mpileup, output/mpileup/Pfeiffer2_GL000229.1.mpileup, output/mpileup/Pfeiffer2_GL000231.1.mpileup, output/mpileup/Pfeiffer2_GL000210.1.mpileup, output/mpileup/Pfeiffer2_GL000239.1.mpileup, output/mpileup/Pfeiffer2_GL000235.1.mpileup, output/mpileup/Pfeiffer2_GL000201.1.mpileup, output/mpileup/Pfeiffer2_GL000247.1.mpileup, output/mpileup/Pfeiffer2_GL000245.1.mpileup, output/mpileup/Pfeiffer2_GL000197.1.mpileup, output/mpileup/Pfeiffer2_GL000203.1.mpileup, output/mpileup/Pfeiffer2_GL000246.1.mpileup, output/mpileup/Pfeiffer2_GL000249.1.mpileup, output/mpileup/Pfeiffer2_GL000196.1.mpileup, output/mpileup/Pfeiffer2_GL000248.1.mpileup, output/mpileup/Pfeiffer2_GL000244.1.mpileup, output/mpileup/Pfeiffer2_GL000238.1.mpileup, output/mpileup/Pfeiffer2_GL000202.1.mpileup, output/mpileup/Pfeiffer2_GL000234.1.mpileup, output/mpileup/Pfeiffer2_GL000232.1.mpileup, output/mpileup/Pfeiffer2_GL000206.1.mpileup, output/mpileup/Pfeiffer2_GL000240.1.mpileup, output/mpileup/Pfeiffer2_GL000236.1.mpileup, output/mpileup/Pfeiffer2_GL000241.1.mpileup, output/mpileup/Pfeiffer2_GL000243.1.mpileup, output/mpileup/Pfeiffer2_GL000242.1.mpileup, output/mpileup/Pfeiffer2_GL000230.1.mpileup, output/mpileup/Pfeiffer2_GL000237.1.mpileup, output/mpileup/Pfeiffer2_GL000233.1.mpileup, output/mpileup/Pfeiffer2_GL000204.1.mpileup, output/mpileup/Pfeiffer2_GL000198.1.mpileup, output/mpileup/Pfeiffer2_GL000208.1.mpileup, output/mpileup/Pfeiffer2_GL000191.1.mpileup, output/mpileup/Pfeiffer2_GL000227.1.mpileup, output/mpileup/Pfeiffer2_GL000228.1.mpileup, output/mpileup/Pfeiffer2_GL000214.1.mpileup, output/mpileup/Pfeiffer2_GL000221.1.mpileup, output/mpileup/Pfeiffer2_GL000209.1.mpileup, output/mpileup/Pfeiffer2_GL000218.1.mpileup, output/mpileup/Pfeiffer2_GL000220.1.mpileup, output/mpileup/Pfeiffer2_GL000213.1.mpileup, output/mpileup/Pfeiffer2_GL000211.1.mpileup, output/mpileup/Pfeiffer2_GL000199.1.mpileup, output/mpileup/Pfeiffer2_GL000217.1.mpileup, output/mpileup/Pfeiffer2_GL000216.1.mpileup, output/mpileup/Pfeiffer2_GL000215.1.mpileup, output/mpileup/Pfeiffer2_GL000205.1.mpileup, output/mpileup/Pfeiffer2_GL000219.1.mpileup, output/mpileup/Pfeiffer2_GL000224.1.mpileup, output/mpileup/Pfeiffer2_GL000223.1.mpileup, output/mpileup/Pfeiffer2_GL000195.1.mpileup, output/mpileup/Pfeiffer2_GL000212.1.mpileup, output/mpileup/Pfeiffer2_GL000222.1.mpileup, output/mpileup/Pfeiffer2_GL000200.1.mpileup, output/mpileup/Pfeiffer2_GL000193.1.mpileup, output/mpileup/Pfeiffer2_GL000194.1.mpileup, output/mpileup/Pfeiffer2_GL000225.1.mpileup, output/mpileup/Pfeiffer2_GL000192.1.mpileup, output/mpileup/Pfeiffer3_1.mpileup, output/mpileup/Pfeiffer3_2.mpileup, output/mpileup/Pfeiffer3_3.mpileup, output/mpileup/Pfeiffer3_4.mpileup, output/mpileup/Pfeiffer3_5.mpileup, output/mpileup/Pfeiffer3_6.mpileup, output/mpileup/Pfeiffer3_7.mpileup, output/mpileup/Pfeiffer3_8.mpileup, output/mpileup/Pfeiffer3_9.mpileup, output/mpileup/Pfeiffer3_10.mpileup, output/mpileup/Pfeiffer3_11.mpileup, output/mpileup/Pfeiffer3_12.mpileup, output/mpileup/Pfeiffer3_13.mpileup, output/mpileup/Pfeiffer3_14.mpileup, output/mpileup/Pfeiffer3_15.mpileup, output/mpileup/Pfeiffer3_16.mpileup, output/mpileup/Pfeiffer3_17.mpileup, output/mpileup/Pfeiffer3_18.mpileup, output/mpileup/Pfeiffer3_19.mpileup, output/mpileup/Pfeiffer3_20.mpileup, output/mpileup/Pfeiffer3_21.mpileup, output/mpileup/Pfeiffer3_22.mpileup, output/mpileup/Pfeiffer3_X.mpileup, output/mpileup/Pfeiffer3_Y.mpileup, output/mpileup/Pfeiffer3_MT.mpileup, output/mpileup/Pfeiffer3_GL000207.1.mpileup, output/mpileup/Pfeiffer3_GL000226.1.mpileup, output/mpileup/Pfeiffer3_GL000229.1.mpileup, output/mpileup/Pfeiffer3_GL000231.1.mpileup, output/mpileup/Pfeiffer3_GL000210.1.mpileup, output/mpileup/Pfeiffer3_GL000239.1.mpileup, output/mpileup/Pfeiffer3_GL000235.1.mpileup, output/mpileup/Pfeiffer3_GL000201.1.mpileup, output/mpileup/Pfeiffer3_GL000247.1.mpileup, output/mpileup/Pfeiffer3_GL000245.1.mpileup, output/mpileup/Pfeiffer3_GL000197.1.mpileup, output/mpileup/Pfeiffer3_GL000203.1.mpileup, output/mpileup/Pfeiffer3_GL000246.1.mpileup, output/mpileup/Pfeiffer3_GL000249.1.mpileup, output/mpileup/Pfeiffer3_GL000196.1.mpileup, output/mpileup/Pfeiffer3_GL000248.1.mpileup, output/mpileup/Pfeiffer3_GL000244.1.mpileup, output/mpileup/Pfeiffer3_GL000238.1.mpileup, output/mpileup/Pfeiffer3_GL000202.1.mpileup, output/mpileup/Pfeiffer3_GL000234.1.mpileup, output/mpileup/Pfeiffer3_GL000232.1.mpileup, output/mpileup/Pfeiffer3_GL000206.1.mpileup, output/mpileup/Pfeiffer3_GL000240.1.mpileup, output/mpileup/Pfeiffer3_GL000236.1.mpileup, output/mpileup/Pfeiffer3_GL000241.1.mpileup, output/mpileup/Pfeiffer3_GL000243.1.mpileup, output/mpileup/Pfeiffer3_GL000242.1.mpileup, output/mpileup/Pfeiffer3_GL000230.1.mpileup, output/mpileup/Pfeiffer3_GL000237.1.mpileup, output/mpileup/Pfeiffer3_GL000233.1.mpileup, output/mpileup/Pfeiffer3_GL000204.1.mpileup, output/mpileup/Pfeiffer3_GL000198.1.mpileup, output/mpileup/Pfeiffer3_GL000208.1.mpileup, output/mpileup/Pfeiffer3_GL000191.1.mpileup, output/mpileup/Pfeiffer3_GL000227.1.mpileup, output/mpileup/Pfeiffer3_GL000228.1.mpileup, output/mpileup/Pfeiffer3_GL000214.1.mpileup, output/mpileup/Pfeiffer3_GL000221.1.mpileup, output/mpileup/Pfeiffer3_GL000209.1.mpileup, output/mpileup/Pfeiffer3_GL000218.1.mpileup, output/mpileup/Pfeiffer3_GL000220.1.mpileup, output/mpileup/Pfeiffer3_GL000213.1.mpileup, output/mpileup/Pfeiffer3_GL000211.1.mpileup, output/mpileup/Pfeiffer3_GL000199.1.mpileup, output/mpileup/Pfeiffer3_GL000217.1.mpileup, output/mpileup/Pfeiffer3_GL000216.1.mpileup, output/mpileup/Pfeiffer3_GL000215.1.mpileup, output/mpileup/Pfeiffer3_GL000205.1.mpileup, output/mpileup/Pfeiffer3_GL000219.1.mpileup, output/mpileup/Pfeiffer3_GL000224.1.mpileup, output/mpileup/Pfeiffer3_GL000223.1.mpileup, output/mpileup/Pfeiffer3_GL000195.1.mpileup, output/mpileup/Pfeiffer3_GL000212.1.mpileup, output/mpileup/Pfeiffer3_GL000222.1.mpileup, output/mpileup/Pfeiffer3_GL000200.1.mpileup, output/mpileup/Pfeiffer3_GL000193.1.mpileup, output/mpileup/Pfeiffer3_GL000194.1.mpileup, output/mpileup/Pfeiffer3_GL000225.1.mpileup, output/mpileup/Pfeiffer3_GL000192.1.mpileup
    jobid: 0

Job counts:
	count	jobs
	1	all
	2	bam2fastq_picard
	170	bam2mpileup
	2	bamALIGN_bwa
	4	fastq2GZ
	2	filteredBAM
	2	indexBAM
	2	markdupBAM
	2	sortBAM_biobambam
	187
```

## Snakemake cluster run output:
```
