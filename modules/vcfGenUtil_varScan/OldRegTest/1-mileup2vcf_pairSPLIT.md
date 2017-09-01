# 1-mpileup2vcf_pairSPLIT
This pipeline is to exemplify the default operations of this module.

## Setting up the: buildPipe.py
Users must set the following variable:

 * (Line 13) TYPE = "pair"

## Setting up the: Snakefile
Users must set the following submodule "call via" input requirements:

 * pairSPLIT

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
    input: input/rawBam/Pfeiffer2.bam
    output: output/fastq/Pfeiffer2.1.fastq, output/fastq/Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-05.18-53-24.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-05.18-53-24.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-05.18-53-24.vendor_failed_reads.log
    jobid: 267
    wildcards: sampleB2FP=Pfeiffer2


rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer3.bam
    output: output/fastq/Pfeiffer3.1.fastq, output/fastq/Pfeiffer3.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-05.18-53-24.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-05.18-53-24.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-05.18-53-24.vendor_failed_reads.log
    jobid: 268
    wildcards: sampleB2FP=Pfeiffer3


rule fastq2GZ:
    input: output/fastq/Pfeiffer2.2.fastq
    output: output/fastq/Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.2.2017-07-05.18-53-24.stderr
    jobid: 263
    wildcards: sampleFGZ=Pfeiffer2.2, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Pfeiffer3.1.fastq
    output: output/fastq/Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.1.2017-07-05.18-53-24.stderr
    jobid: 265
    wildcards: sampleFGZ=Pfeiffer3.1, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Pfeiffer2.1.fastq
    output: output/fastq/Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.1.2017-07-05.18-53-24.stderr
    jobid: 264
    wildcards: sampleFGZ=Pfeiffer2.1, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Pfeiffer3.2.fastq
    output: output/fastq/Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.2.2017-07-05.18-53-24.stderr
    jobid: 266
    wildcards: sampleFGZ=Pfeiffer3.2, pathFGZ=output/fastq


rule bamALIGN_bwa:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/fastq/Pfeiffer2.1.fastq.gz, output/fastq/Pfeiffer2.2.fastq.gz, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa
    output: output/bam/Pfeiffer2_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-05.18-53-24.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-05.18-53-24.samtools.stderr
    jobid: 261
    wildcards: sampleBAB=Pfeiffer2


rule bamALIGN_bwa:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/fastq/Pfeiffer3.1.fastq.gz, output/fastq/Pfeiffer3.2.fastq.gz, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa
    output: output/bam/Pfeiffer3_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-05.18-53-24.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-05.18-53-24.samtools.stderr
    jobid: 262
    wildcards: sampleBAB=Pfeiffer3


rule sortBAM_biobambam:
    input: output/bam/Pfeiffer2_Aligned.out.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-05.18-53-24.samtools.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-05.18-53-24.bamsort.stderr
    jobid: 259
    wildcards: sampleSBB=Pfeiffer2_Aligned.out, pathSBB=output/bam


rule sortBAM_biobambam:
    input: output/bam/Pfeiffer3_Aligned.out.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-05.18-53-24.samtools.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-05.18-53-24.bamsort.stderr
    jobid: 260
    wildcards: sampleSBB=Pfeiffer3_Aligned.out, pathSBB=output/bam


rule filteredBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer2_Aligned.out_sorted.2017-07-05.18-53-24.stderr
    jobid: 257
    wildcards: sampleFB=Pfeiffer2_Aligned.out_sorted, pathFB=output/bam


rule filteredBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer3_Aligned.out_sorted.2017-07-05.18-53-24.stderr
    jobid: 258
    wildcards: sampleFB=Pfeiffer3_Aligned.out_sorted, pathFB=output/bam


rule markdupBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam, output/metrics/Pfeiffer3_Aligned.out_sorted_filtered.dup_metrics
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer3_Aligned.out_sorted_filtered.2017-07-05.18-53-24.biobammarkdup.stderr
    jobid: 256
    wildcards: outputDIR=output, sampleMDB=Pfeiffer3_Aligned.out_sorted_filtered


rule markdupBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam, output/metrics/Pfeiffer2_Aligned.out_sorted_filtered.dup_metrics
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer2_Aligned.out_sorted_filtered.2017-07-05.18-53-24.biobammarkdup.stderr
    jobid: 255
    wildcards: outputDIR=output, sampleMDB=Pfeiffer2_Aligned.out_sorted_filtered


rule indexBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam.bai
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer3.2017-07-05.18-53-24.stderr
    jobid: 254
    wildcards: sampleIB=Pfeiffer3, outputDIR=output


rule indexBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam.bai
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer2.2017-07-05.18-53-24.stderr
    jobid: 253
    wildcards: sampleIB=Pfeiffer2, outputDIR=output


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000249.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 217
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000249.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000229.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 154
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000229.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 118
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_21.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 184
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_21


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000235.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 145
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000235.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000214.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 221
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000214.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000200.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 172
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000200.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000227.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 180
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000227.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000246.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 137
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000246.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_MT.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 133
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_MT


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000231.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 165
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000231.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_12.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 98
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_12


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000223.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 106
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000223.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000215.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 223
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000215.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000207.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 213
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000207.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000237.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 178
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000237.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000219.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 148
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000219.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000233.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 196
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000233.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000202.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 187
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000202.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000231.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 166
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000231.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000220.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 132
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000220.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000242.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 219
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000242.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000211.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 237
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000211.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000245.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 141
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000245.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000248.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 136
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000248.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000196.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 241
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000196.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000220.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 131
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000220.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_17.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 193
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_17


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000243.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 93
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000243.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_22.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 156
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_22


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000246.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 138
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000246.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000204.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 89
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000204.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_Y.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 205
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_Y


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_9.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 92
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_9


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_16.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 115
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_16


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_13.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 140
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_13


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000218.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 126
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000218.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_14.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 110
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_14


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_10.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 189
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_10


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_22.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 155
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_22


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_11.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 123
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_11


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000192.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 229
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000192.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000234.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 128
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000234.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000209.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 248
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000209.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000207.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 214
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000207.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000217.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 88
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000217.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000213.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 85
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000213.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_5.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 143
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_5


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000222.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 96
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000222.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000195.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 157
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000195.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000230.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 103
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000230.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_8.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 150
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_8


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000240.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 233
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000240.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000206.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 251
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000206.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_20.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 174
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_20


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000213.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 86
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000213.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000242.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 220
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000242.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_3.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 152
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_6.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 250
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_6


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_11.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 124
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_11


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000247.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 197
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000247.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_8.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 149
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_8


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_3.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 151
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000214.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 222
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000214.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 117
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_19.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 235
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_19


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000221.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 129
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000221.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000245.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 142
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000245.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000234.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 127
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000234.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000201.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 231
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000201.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000244.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 170
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000244.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000199.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 240
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000199.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_13.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 139
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_13


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_18.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 168
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_18


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000219.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 147
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000219.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000241.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 176
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000241.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000193.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 200
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000193.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000194.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 226
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000194.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000248.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 135
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000248.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000217.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 87
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000217.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000218.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 125
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000218.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000191.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 212
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000191.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000225.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 191
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000225.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_15.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 245
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_15


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_12.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 97
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_12


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000210.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 101
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000210.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000198.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 203
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000198.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_4.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 107
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_4


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_2.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 215
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_20.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 173
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_20


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000238.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 186
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000238.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000199.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 239
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000199.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000203.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 181
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000203.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_4.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 108
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_4


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000237.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 177
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000237.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000244.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 169
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000244.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_6.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 249
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_6


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_21.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 183
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_21


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000232.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 114
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000232.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000210.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 102
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000210.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000194.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 225
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000194.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000229.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 153
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000229.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_9.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 91
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_9


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000238.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 185
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000238.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000216.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 122
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000216.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000235.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 146
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000235.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000205.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 111
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000205.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000208.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 207
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000208.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000191.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 211
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000191.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000243.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 94
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000243.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000202.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 188
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000202.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_7.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 120
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_7


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000224.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 164
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000224.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_10.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 190
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_10


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000215.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 224
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000215.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000226.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 228
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000226.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000197.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 100
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000197.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000195.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 158
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000195.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000206.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 252
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000206.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000230.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 104
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000230.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000200.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 171
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000200.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_MT.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 134
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_MT


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_19.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 236
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_19


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000236.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 244
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000236.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000226.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 227
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000226.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000221.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 130
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000221.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_X.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 209
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_X


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000228.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 201
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000228.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000211.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 238
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000211.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000201.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 232
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000201.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_2.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 216
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_2


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000240.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 234
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000240.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000232.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 113
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000232.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000239.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 162
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000239.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000209.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 247
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000209.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000228.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 202
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000228.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_X.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 210
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_X


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000222.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 95
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000222.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000205.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 112
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000205.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000212.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 159
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000212.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_18.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 167
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_18


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_7.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 119
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_7


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000197.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 99
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000197.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_Y.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 206
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_Y


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000224.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 163
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000224.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000249.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 218
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000249.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000225.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 192
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000225.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000193.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 199
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000193.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000192.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 230
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000192.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000196.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 242
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000196.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_17.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 194
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_17


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_15.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 246
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_15


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000208.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 208
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000208.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000239.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 161
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000239.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000204.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 90
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000204.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000212.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 160
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000212.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000216.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 121
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000216.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_14.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 109
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_14


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000227.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 179
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000227.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000233.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 195
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000233.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_GL000203.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 182
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_GL000203.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000223.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 105
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000223.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000241.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 175
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000241.1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_5.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.18-53-24.mpileup.stderr
    jobid: 144
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_5


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_16.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 116
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_16


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000236.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 243
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000236.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000247.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 198
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000247.1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_GL000198.1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.18-53-24.mpileup.stderr
    jobid: 204
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_GL000198.1


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000204.1.mpileup, output/mpileup/Pfeiffer2_GL000204.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000204.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000204.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000204.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 3
    wildcards: chrMPU2VCFP=_GL000204.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_12.mpileup, output/mpileup/Pfeiffer2_12.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_12.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_12.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_12.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 7
    wildcards: chrMPU2VCFP=_12, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000225.1.mpileup, output/mpileup/Pfeiffer2_GL000225.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000225.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000225.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000225.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 54
    wildcards: chrMPU2VCFP=_GL000225.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000246.1.mpileup, output/mpileup/Pfeiffer2_GL000246.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000246.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000246.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000246.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 27
    wildcards: chrMPU2VCFP=_GL000246.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_14.mpileup, output/mpileup/Pfeiffer2_14.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_14.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_14.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_14.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 13
    wildcards: chrMPU2VCFP=_14, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000239.1.mpileup, output/mpileup/Pfeiffer2_GL000239.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000239.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000239.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000239.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 39
    wildcards: chrMPU2VCFP=_GL000239.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000224.1.mpileup, output/mpileup/Pfeiffer2_GL000224.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000224.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000224.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000224.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 40
    wildcards: chrMPU2VCFP=_GL000224.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000211.1.mpileup, output/mpileup/Pfeiffer2_GL000211.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000211.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000211.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000211.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 77
    wildcards: chrMPU2VCFP=_GL000211.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_1.mpileup, output/mpileup/Pfeiffer2_1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 17
    wildcards: chrMPU2VCFP=_1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000208.1.mpileup, output/mpileup/Pfeiffer2_GL000208.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000208.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000208.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000208.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 62
    wildcards: chrMPU2VCFP=_GL000208.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_8.mpileup, output/mpileup/Pfeiffer2_8.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_8.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_8.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_8.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 33
    wildcards: chrMPU2VCFP=_8, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000240.1.mpileup, output/mpileup/Pfeiffer2_GL000240.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000240.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000240.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000240.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 75
    wildcards: chrMPU2VCFP=_GL000240.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000196.1.mpileup, output/mpileup/Pfeiffer2_GL000196.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000196.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000196.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000196.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 79
    wildcards: chrMPU2VCFP=_GL000196.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000193.1.mpileup, output/mpileup/Pfeiffer2_GL000193.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000193.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000193.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000193.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 58
    wildcards: chrMPU2VCFP=_GL000193.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_15.mpileup, output/mpileup/Pfeiffer2_15.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_15.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_15.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_15.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 81
    wildcards: chrMPU2VCFP=_15, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_19.mpileup, output/mpileup/Pfeiffer2_19.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_19.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_19.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_19.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 76
    wildcards: chrMPU2VCFP=_19, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000222.1.mpileup, output/mpileup/Pfeiffer2_GL000222.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000222.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000222.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000222.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 6
    wildcards: chrMPU2VCFP=_GL000222.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000216.1.mpileup, output/mpileup/Pfeiffer2_GL000216.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000216.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000216.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000216.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 19
    wildcards: chrMPU2VCFP=_GL000216.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000220.1.mpileup, output/mpileup/Pfeiffer2_GL000220.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000220.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000220.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000220.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 24
    wildcards: chrMPU2VCFP=_GL000220.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000245.1.mpileup, output/mpileup/Pfeiffer2_GL000245.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000245.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000245.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000245.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 29
    wildcards: chrMPU2VCFP=_GL000245.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000219.1.mpileup, output/mpileup/Pfeiffer2_GL000219.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000219.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000219.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000219.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 32
    wildcards: chrMPU2VCFP=_GL000219.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000244.1.mpileup, output/mpileup/Pfeiffer2_GL000244.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000244.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000244.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000244.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 43
    wildcards: chrMPU2VCFP=_GL000244.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_Y.mpileup, output/mpileup/Pfeiffer2_Y.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_Y.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_Y.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_Y.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 61
    wildcards: chrMPU2VCFP=_Y, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000217.1.mpileup, output/mpileup/Pfeiffer2_GL000217.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000217.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000217.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000217.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 2
    wildcards: chrMPU2VCFP=_GL000217.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000210.1.mpileup, output/mpileup/Pfeiffer2_GL000210.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000210.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000210.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000210.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 9
    wildcards: chrMPU2VCFP=_GL000210.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_13.mpileup, output/mpileup/Pfeiffer2_13.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_13.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_13.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_13.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 28
    wildcards: chrMPU2VCFP=_13, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_11.mpileup, output/mpileup/Pfeiffer2_11.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_11.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_11.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_11.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 20
    wildcards: chrMPU2VCFP=_11, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000223.1.mpileup, output/mpileup/Pfeiffer2_GL000223.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000223.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000223.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000223.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 11
    wildcards: chrMPU2VCFP=_GL000223.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_21.mpileup, output/mpileup/Pfeiffer2_21.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_21.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_21.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_21.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 50
    wildcards: chrMPU2VCFP=_21, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000195.1.mpileup, output/mpileup/Pfeiffer2_GL000195.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000195.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000195.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000195.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 37
    wildcards: chrMPU2VCFP=_GL000195.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000228.1.mpileup, output/mpileup/Pfeiffer2_GL000228.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000228.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000228.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000228.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 59
    wildcards: chrMPU2VCFP=_GL000228.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000207.1.mpileup, output/mpileup/Pfeiffer2_GL000207.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000207.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000207.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000207.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 65
    wildcards: chrMPU2VCFP=_GL000207.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000248.1.mpileup, output/mpileup/Pfeiffer2_GL000248.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000248.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000248.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000248.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 26
    wildcards: chrMPU2VCFP=_GL000248.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000199.1.mpileup, output/mpileup/Pfeiffer2_GL000199.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000199.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000199.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000199.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 78
    wildcards: chrMPU2VCFP=_GL000199.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000249.1.mpileup, output/mpileup/Pfeiffer2_GL000249.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000249.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000249.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000249.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 67
    wildcards: chrMPU2VCFP=_GL000249.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000194.1.mpileup, output/mpileup/Pfeiffer2_GL000194.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000194.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000194.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000194.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 71
    wildcards: chrMPU2VCFP=_GL000194.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_7.mpileup, output/mpileup/Pfeiffer2_7.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_7.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_7.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_7.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 18
    wildcards: chrMPU2VCFP=_7, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000218.1.mpileup, output/mpileup/Pfeiffer2_GL000218.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000218.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000218.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000218.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 21
    wildcards: chrMPU2VCFP=_GL000218.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000221.1.mpileup, output/mpileup/Pfeiffer2_GL000221.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000221.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000221.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000221.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 23
    wildcards: chrMPU2VCFP=_GL000221.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_16.mpileup, output/mpileup/Pfeiffer2_16.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_16.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_16.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_16.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 16
    wildcards: chrMPU2VCFP=_16, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_5.mpileup, output/mpileup/Pfeiffer2_5.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_5.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_5.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_5.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 30
    wildcards: chrMPU2VCFP=_5, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000212.1.mpileup, output/mpileup/Pfeiffer2_GL000212.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000212.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000212.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000212.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 38
    wildcards: chrMPU2VCFP=_GL000212.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000231.1.mpileup, output/mpileup/Pfeiffer2_GL000231.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000231.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000231.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000231.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 41
    wildcards: chrMPU2VCFP=_GL000231.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000227.1.mpileup, output/mpileup/Pfeiffer2_GL000227.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000227.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000227.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000227.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 48
    wildcards: chrMPU2VCFP=_GL000227.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000236.1.mpileup, output/mpileup/Pfeiffer2_GL000236.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000236.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000236.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000236.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 80
    wildcards: chrMPU2VCFP=_GL000236.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000215.1.mpileup, output/mpileup/Pfeiffer2_GL000215.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000215.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000215.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000215.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 70
    wildcards: chrMPU2VCFP=_GL000215.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_6.mpileup, output/mpileup/Pfeiffer2_6.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_6.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_6.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_6.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 83
    wildcards: chrMPU2VCFP=_6, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000243.1.mpileup, output/mpileup/Pfeiffer2_GL000243.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000243.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000243.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000243.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 5
    wildcards: chrMPU2VCFP=_GL000243.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_22.mpileup, output/mpileup/Pfeiffer2_22.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_22.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_22.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_22.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 36
    wildcards: chrMPU2VCFP=_22, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_20.mpileup, output/mpileup/Pfeiffer2_20.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_20.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_20.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_20.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 45
    wildcards: chrMPU2VCFP=_20, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_10.mpileup, output/mpileup/Pfeiffer2_10.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_10.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_10.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_10.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 53
    wildcards: chrMPU2VCFP=_10, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000214.1.mpileup, output/mpileup/Pfeiffer2_GL000214.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000214.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000214.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000214.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 69
    wildcards: chrMPU2VCFP=_GL000214.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000235.1.mpileup, output/mpileup/Pfeiffer2_GL000235.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000235.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000235.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000235.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 31
    wildcards: chrMPU2VCFP=_GL000235.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_18.mpileup, output/mpileup/Pfeiffer2_18.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_18.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_18.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_18.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 42
    wildcards: chrMPU2VCFP=_18, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000191.1.mpileup, output/mpileup/Pfeiffer2_GL000191.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000191.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000191.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000191.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 64
    wildcards: chrMPU2VCFP=_GL000191.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000229.1.mpileup, output/mpileup/Pfeiffer2_GL000229.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000229.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000229.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000229.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 35
    wildcards: chrMPU2VCFP=_GL000229.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000226.1.mpileup, output/mpileup/Pfeiffer2_GL000226.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000226.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000226.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000226.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 72
    wildcards: chrMPU2VCFP=_GL000226.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000203.1.mpileup, output/mpileup/Pfeiffer2_GL000203.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000203.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000203.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000203.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 49
    wildcards: chrMPU2VCFP=_GL000203.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000238.1.mpileup, output/mpileup/Pfeiffer2_GL000238.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000238.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000238.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000238.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 51
    wildcards: chrMPU2VCFP=_GL000238.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_17.mpileup, output/mpileup/Pfeiffer2_17.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_17.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_17.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_17.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 55
    wildcards: chrMPU2VCFP=_17, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000192.1.mpileup, output/mpileup/Pfeiffer2_GL000192.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000192.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000192.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000192.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 73
    wildcards: chrMPU2VCFP=_GL000192.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_MT.mpileup, output/mpileup/Pfeiffer2_MT.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_MT.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_MT.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_MT.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 25
    wildcards: chrMPU2VCFP=_MT, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_4.mpileup, output/mpileup/Pfeiffer2_4.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_4.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_4.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_4.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 12
    wildcards: chrMPU2VCFP=_4, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_9.mpileup, output/mpileup/Pfeiffer2_9.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_9.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_9.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_9.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 4
    wildcards: chrMPU2VCFP=_9, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000213.1.mpileup, output/mpileup/Pfeiffer2_GL000213.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000213.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000213.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000213.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 1
    wildcards: chrMPU2VCFP=_GL000213.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000197.1.mpileup, output/mpileup/Pfeiffer2_GL000197.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000197.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000197.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000197.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 8
    wildcards: chrMPU2VCFP=_GL000197.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000230.1.mpileup, output/mpileup/Pfeiffer2_GL000230.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000230.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000230.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000230.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 10
    wildcards: chrMPU2VCFP=_GL000230.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000232.1.mpileup, output/mpileup/Pfeiffer2_GL000232.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000232.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000232.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000232.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 15
    wildcards: chrMPU2VCFP=_GL000232.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000234.1.mpileup, output/mpileup/Pfeiffer2_GL000234.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000234.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000234.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000234.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 22
    wildcards: chrMPU2VCFP=_GL000234.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_3.mpileup, output/mpileup/Pfeiffer2_3.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_3.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_3.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_3.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 34
    wildcards: chrMPU2VCFP=_3, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000241.1.mpileup, output/mpileup/Pfeiffer2_GL000241.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000241.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000241.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000241.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 46
    wildcards: chrMPU2VCFP=_GL000241.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000247.1.mpileup, output/mpileup/Pfeiffer2_GL000247.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000247.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000247.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000247.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 57
    wildcards: chrMPU2VCFP=_GL000247.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_2.mpileup, output/mpileup/Pfeiffer2_2.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_2.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_2.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_2.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 66
    wildcards: chrMPU2VCFP=_2, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000201.1.mpileup, output/mpileup/Pfeiffer2_GL000201.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000201.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000201.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000201.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 74
    wildcards: chrMPU2VCFP=_GL000201.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000233.1.mpileup, output/mpileup/Pfeiffer2_GL000233.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000233.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000233.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000233.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 56
    wildcards: chrMPU2VCFP=_GL000233.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000209.1.mpileup, output/mpileup/Pfeiffer2_GL000209.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000209.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000209.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000209.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 82
    wildcards: chrMPU2VCFP=_GL000209.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000206.1.mpileup, output/mpileup/Pfeiffer2_GL000206.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000206.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000206.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000206.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 84
    wildcards: chrMPU2VCFP=_GL000206.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000205.1.mpileup, output/mpileup/Pfeiffer2_GL000205.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000205.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000205.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000205.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 14
    wildcards: chrMPU2VCFP=_GL000205.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000200.1.mpileup, output/mpileup/Pfeiffer2_GL000200.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000200.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000200.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000200.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 44
    wildcards: chrMPU2VCFP=_GL000200.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000237.1.mpileup, output/mpileup/Pfeiffer2_GL000237.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000237.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000237.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000237.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 47
    wildcards: chrMPU2VCFP=_GL000237.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000198.1.mpileup, output/mpileup/Pfeiffer2_GL000198.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000198.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000198.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000198.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 60
    wildcards: chrMPU2VCFP=_GL000198.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_X.mpileup, output/mpileup/Pfeiffer2_X.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_X.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_X.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_X.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 63
    wildcards: chrMPU2VCFP=_X, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000242.1.mpileup, output/mpileup/Pfeiffer2_GL000242.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000242.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000242.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000242.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 68
    wildcards: chrMPU2VCFP=_GL000242.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer3_GL000202.1.mpileup, output/mpileup/Pfeiffer2_GL000202.1.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2_GL000202.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000202.1.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr_GL000202.1.SNPandINDEL.2017-07-05.18-53-24.stderr
    jobid: 52
    wildcards: chrMPU2VCFP=_GL000202.1, sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2


localrule all:
    input: output/varScan/Pfeiffer3_Pfeiffer2_1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_2.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_3.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_4.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_5.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_6.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_7.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_8.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_9.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_10.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_11.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_12.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_13.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_14.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_15.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_16.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_17.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_18.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_19.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_20.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_21.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_22.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_X.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_Y.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_MT.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000207.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000226.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000229.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000231.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000210.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000239.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000235.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000201.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000247.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000245.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000197.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000203.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000246.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000249.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000196.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000248.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000244.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000238.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000202.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000234.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000232.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000206.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000240.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000236.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000241.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000243.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000242.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000230.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000237.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000233.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000204.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000198.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000208.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000191.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000227.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000228.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000214.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000221.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000209.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000218.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000220.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000213.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000211.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000199.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000217.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000216.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000215.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000205.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000219.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000224.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000223.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000195.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000212.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000222.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000200.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000193.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000194.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000225.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000192.1.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2_1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_2.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_3.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_4.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_5.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_6.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_7.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_8.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_9.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_10.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_11.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_12.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_13.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_14.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_15.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_16.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_17.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_18.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_19.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_20.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_21.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_22.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_X.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_Y.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_MT.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000207.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000226.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000229.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000231.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000210.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000239.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000235.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000201.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000247.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000245.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000197.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000203.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000246.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000249.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000196.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000248.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000244.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000238.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000202.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000234.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000232.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000206.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000240.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000236.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000241.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000243.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000242.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000230.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000237.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000233.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000204.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000198.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000208.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000191.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000227.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000228.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000214.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000221.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000209.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000218.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000220.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000213.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000211.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000199.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000217.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000216.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000215.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000205.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000219.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000224.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000223.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000195.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000212.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000222.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000200.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000193.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000194.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000225.1.varScan.indel.vcf, output/varScan/Pfeiffer3_Pfeiffer2_GL000192.1.varScan.indel.vcf
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
	84	mpileup2vcf_pair
	2	sortBAM_biobambam
	269
