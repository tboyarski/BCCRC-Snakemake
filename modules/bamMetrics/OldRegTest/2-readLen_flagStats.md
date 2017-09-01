# 1-collect_GCBias_MultM_RNASeq_WGS
This pipeline is to exemplify the default operations of this module.

## Setting up the: buildPipe.py
Users must set the following variable:

 * (Line 13) TYPE = "single"

## Setting up the: Snakefile
Users must set the following submodule "call via" input requirements:

 * GCBias
 * MultM
 * RNASeq
 * WGS

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

## Snakemake dry run output:
```

rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer3.bam
    output: output/fastq/Pfeiffer3.1.fastq, output/fastq/Pfeiffer3.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-07.20-35-46.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-07.20-35-46.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-07.20-35-46.stderr
    jobid: 19
    wildcards: sampleB2FP=Pfeiffer3


rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer2.bam
    output: output/fastq/Pfeiffer2.1.fastq, output/fastq/Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-07.20-35-46.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-07.20-35-46.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-07.20-35-46.stderr
    jobid: 20
    wildcards: sampleB2FP=Pfeiffer2


rule fastq2GZ:
    input: output/fastq/Pfeiffer2.2.fastq
    output: output/fastq/Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.2.2017-07-07.20-35-46.stderr
    jobid: 17
    wildcards: sampleFGZ=Pfeiffer2.2, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Pfeiffer2.1.fastq
    output: output/fastq/Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.1.2017-07-07.20-35-46.stderr
    jobid: 18
    wildcards: sampleFGZ=Pfeiffer2.1, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Pfeiffer3.1.fastq
    output: output/fastq/Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.1.2017-07-07.20-35-46.stderr
    jobid: 16
    wildcards: sampleFGZ=Pfeiffer3.1, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Pfeiffer3.2.fastq
    output: output/fastq/Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.2.2017-07-07.20-35-46.stderr
    jobid: 15
    wildcards: sampleFGZ=Pfeiffer3.2, pathFGZ=output/fastq


rule bamALIGN_bwa:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/fastq/Pfeiffer3.1.fastq.gz, output/fastq/Pfeiffer3.2.fastq.gz, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa
    output: output/bam/Pfeiffer3_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-07.20-35-46.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-07.20-35-46.samtools.stderr
    jobid: 13
    wildcards: sampleBAB=Pfeiffer3


rule bamALIGN_bwa:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/fastq/Pfeiffer2.1.fastq.gz, output/fastq/Pfeiffer2.2.fastq.gz, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa
    output: output/bam/Pfeiffer2_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-07.20-35-46.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-07.20-35-46.samtools.stderr
    jobid: 14
    wildcards: sampleBAB=Pfeiffer2


rule sortBAM_biobambam:
    input: output/bam/Pfeiffer3_Aligned.out.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-07.20-35-46.samtools.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-07.20-35-46.bamsort.stderr
    jobid: 11
    wildcards: sampleSBB=Pfeiffer3_Aligned.out, pathSBB=output/bam


rule sortBAM_biobambam:
    input: output/bam/Pfeiffer2_Aligned.out.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-07.20-35-46.samtools.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-07.20-35-46.bamsort.stderr
    jobid: 12
    wildcards: sampleSBB=Pfeiffer2_Aligned.out, pathSBB=output/bam


rule filteredBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer3_Aligned.out_sorted.2017-07-07.20-35-46.stderr
    jobid: 9
    wildcards: sampleFB=Pfeiffer3_Aligned.out_sorted, pathFB=output/bam


rule filteredBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer2_Aligned.out_sorted.2017-07-07.20-35-46.stderr
    jobid: 10
    wildcards: sampleFB=Pfeiffer2_Aligned.out_sorted, pathFB=output/bam


rule markdupBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    output: output/metrics/Pfeiffer3_Aligned.out_sorted_filtered.dup_metrics, output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer3_Aligned.out_sorted_filtered.2017-07-07.20-35-46.biobammarkdup.stderr
    jobid: 7
    wildcards: outputDIR=output, sampleMDB=Pfeiffer3_Aligned.out_sorted_filtered


rule markdupBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    output: output/metrics/Pfeiffer2_Aligned.out_sorted_filtered.dup_metrics, output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer2_Aligned.out_sorted_filtered.2017-07-07.20-35-46.biobammarkdup.stderr
    jobid: 8
    wildcards: outputDIR=output, sampleMDB=Pfeiffer2_Aligned.out_sorted_filtered


rule indexBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam.bai, output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer2.2017-07-07.20-35-46.stderr
    jobid: 6
    wildcards: outputDIR=output, sampleIB=Pfeiffer2


rule indexBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam.bai, output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer3.2017-07-07.20-35-46.stderr
    jobid: 5
    wildcards: outputDIR=output, sampleIB=Pfeiffer3


rule readLen:
    input: output/bam/Pfeiffer2.bam
    output: output/metrics/Pfeiffer2.readLen
    log: log/bamMetrics/readLen/readLen_Pfeiffer2.2017-07-07.20-35-45.stderr
    jobid: 2
    wildcards: sampleRL=Pfeiffer2


rule flagStats:
    input: output/bam/Pfeiffer3.bam
    output: output/metrics/Pfeiffer3.flagStats
    log: log/bamMetrics/flagStats/flagStats_Pfeiffer3.2017-07-07.20-35-45.stderr
    jobid: 3
    wildcards: sampleFS=Pfeiffer3


rule readLen:
    input: output/bam/Pfeiffer3.bam
    output: output/metrics/Pfeiffer3.readLen
    log: log/bamMetrics/readLen/readLen_Pfeiffer3.2017-07-07.20-35-45.stderr
    jobid: 1
    wildcards: sampleRL=Pfeiffer3


rule flagStats:
    input: output/bam/Pfeiffer2.bam
    output: output/metrics/Pfeiffer2.flagStats
    log: log/bamMetrics/flagStats/flagStats_Pfeiffer2.2017-07-07.20-35-45.stderr
    jobid: 4
    wildcards: sampleFS=Pfeiffer2


localrule all:
    input: output/metrics/Pfeiffer2.readLen, output/metrics/Pfeiffer3.readLen, output/metrics/Pfeiffer2.flagStats, output/metrics/Pfeiffer3.flagStats
    jobid: 0

Job counts:
	count	jobs
	1	all
	2	bam2fastq_picard
	2	bamALIGN_bwa
	4	fastq2GZ
	2	filteredBAM
	2	flagStats
	2	indexBAM
	2	markdupBAM
	2	readLen
	2	sortBAM_biobambam
	21
```

## Snakemake cluster run output:
```

Provided cluster nodes: 100
Job counts:
    count    jobs
    1    all
    2    bam2fastq_picard
    2    bamALIGN_bwa
    4    fastq2GZ
    2    filteredBAM
    2    flagStats
    2    indexBAM
    2    markdupBAM
    2    readLen
    2    sortBAM_biobambam
    21

rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer3.bam
    output: output/fastq/Pfeiffer3.1.fastq, output/fastq/Pfeiffer3.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-07.20-22-38.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-07.20-22-38.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-07.20-22-38.stderr
    jobid: 19
    wildcards: sampleB2FP=Pfeiffer3

Submitted DRMAA job (jobid 8827707)

rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer2.bam
    output: output/fastq/Pfeiffer2.1.fastq, output/fastq/Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-07.20-22-38.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-07.20-22-38.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-07.20-22-38.stderr
    jobid: 20
    wildcards: sampleB2FP=Pfeiffer2

Submitted DRMAA job (jobid 8827709)
Finished job 19.
1 of 21 steps (5%) done

rule fastq2GZ:
    input: output/fastq/Pfeiffer3.1.fastq
    output: output/fastq/Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.1.2017-07-07.20-22-38.stderr
    jobid: 15
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer3.1

Submitted DRMAA job (jobid 8827751)

rule fastq2GZ:
    input: output/fastq/Pfeiffer3.2.fastq
    output: output/fastq/Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.2.2017-07-07.20-22-38.stderr
    jobid: 16
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer3.2

Submitted DRMAA job (jobid 8827752)
Finished job 20.
2 of 21 steps (10%) done

rule fastq2GZ:
    input: output/fastq/Pfeiffer2.1.fastq
    output: output/fastq/Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.1.2017-07-07.20-22-38.stderr
    jobid: 17
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer2.1

Submitted DRMAA job (jobid 8827756)

rule fastq2GZ:
    input: output/fastq/Pfeiffer2.2.fastq
    output: output/fastq/Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.2.2017-07-07.20-22-38.stderr
    jobid: 18
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer2.2

Submitted DRMAA job (jobid 8827757)
Finished job 15.
3 of 21 steps (14%) done
Finished job 17.
4 of 21 steps (19%) done
Finished job 18.
5 of 21 steps (24%) done

rule bamALIGN_bwa:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, output/fastq/Pfeiffer2.1.fastq.gz, output/fastq/Pfeiffer2.2.fastq.gz
    output: output/bam/Pfeiffer2_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-07.20-22-38.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-07.20-22-38.samtools.stderr
    jobid: 14
    wildcards: sampleBAB=Pfeiffer2

Submitted DRMAA job (jobid 8827771)
Finished job 16.
6 of 21 steps (29%) done

rule bamALIGN_bwa:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, output/fastq/Pfeiffer3.1.fastq.gz, output/fastq/Pfeiffer3.2.fastq.gz
    output: output/bam/Pfeiffer3_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-07.20-22-38.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-07.20-22-38.samtools.stderr
    jobid: 13
    wildcards: sampleBAB=Pfeiffer3

Submitted DRMAA job (jobid 8827772)
Finished job 14.
7 of 21 steps (33%) done

rule sortBAM_biobambam:
    input: output/bam/Pfeiffer2_Aligned.out.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-07.20-22-38.samtools.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-07.20-22-38.bamsort.stderr
    jobid: 12
    wildcards: sampleSBB=Pfeiffer2_Aligned.out, pathSBB=output/bam

Submitted DRMAA job (jobid 8827824)
Finished job 13.
8 of 21 steps (38%) done

rule sortBAM_biobambam:
    input: output/bam/Pfeiffer3_Aligned.out.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-07.20-22-38.samtools.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-07.20-22-38.bamsort.stderr
    jobid: 11
    wildcards: sampleSBB=Pfeiffer3_Aligned.out, pathSBB=output/bam

Submitted DRMAA job (jobid 8827829)
Finished job 11.
9 of 21 steps (43%) done

rule filteredBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer3_Aligned.out_sorted.2017-07-07.20-22-38.stderr
    jobid: 9
    wildcards: sampleFB=Pfeiffer3_Aligned.out_sorted, pathFB=output/bam

Submitted DRMAA job (jobid 8827870)
Finished job 12.
10 of 21 steps (48%) done

rule filteredBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer2_Aligned.out_sorted.2017-07-07.20-22-38.stderr
    jobid: 10
    wildcards: sampleFB=Pfeiffer2_Aligned.out_sorted, pathFB=output/bam

Submitted DRMAA job (jobid 8827880)
Finished job 9.
11 of 21 steps (52%) done

rule markdupBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam, output/metrics/Pfeiffer3_Aligned.out_sorted_filtered.dup_metrics
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer3_Aligned.out_sorted_filtered.2017-07-07.20-22-38.biobammarkdup.stderr
    jobid: 7
    wildcards: outputDIR=output, sampleMDB=Pfeiffer3_Aligned.out_sorted_filtered

Submitted DRMAA job (jobid 8827893)
Finished job 10.
12 of 21 steps (57%) done

rule markdupBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam, output/metrics/Pfeiffer2_Aligned.out_sorted_filtered.dup_metrics
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer2_Aligned.out_sorted_filtered.2017-07-07.20-22-38.biobammarkdup.stderr
    jobid: 8
    wildcards: outputDIR=output, sampleMDB=Pfeiffer2_Aligned.out_sorted_filtered

Submitted DRMAA job (jobid 8827900)
Finished job 8.
13 of 21 steps (62%) done

rule indexBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam.bai, output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer2.2017-07-07.20-22-38.stderr
    jobid: 6
    wildcards: outputDIR=output, sampleIB=Pfeiffer2

Submitted DRMAA job (jobid 8827919)
Finished job 7.
14 of 21 steps (67%) done

rule indexBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam.bai, output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer3.2017-07-07.20-22-38.stderr
    jobid: 5
    wildcards: outputDIR=output, sampleIB=Pfeiffer3

Submitted DRMAA job (jobid 8827924)
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/Pfeiffer2.bam. Your Python build does not support it.
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/Pfeiffer2.bam.bai. Your Python build does not support it.
Finished job 6.
15 of 21 steps (71%) done

rule readLen:
    input: output/bam/Pfeiffer2.bam
    output: output/metrics/Pfeiffer2.readLen
    log: log/bamMetrics/readLen/readLen_Pfeiffer2.2017-07-07.20-22-37.stderr
    jobid: 2
    wildcards: sampleRL=Pfeiffer2

Submitted DRMAA job (jobid 8827977)

rule flagStats:
    input: output/bam/Pfeiffer2.bam
    output: output/metrics/Pfeiffer2.flagStats
    log: log/bamMetrics/flagStats/flagStats_Pfeiffer2.2017-07-07.20-22-37.stderr
    jobid: 4
    wildcards: sampleFS=Pfeiffer2

Submitted DRMAA job (jobid 8827978)
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/Pfeiffer3.bam. Your Python build does not support it.
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/Pfeiffer3.bam.bai. Your Python build does not support it.
Finished job 5.
16 of 21 steps (76%) done

rule readLen:
    input: output/bam/Pfeiffer3.bam
    output: output/metrics/Pfeiffer3.readLen
    log: log/bamMetrics/readLen/readLen_Pfeiffer3.2017-07-07.20-22-37.stderr
    jobid: 1
    wildcards: sampleRL=Pfeiffer3

Submitted DRMAA job (jobid 8827982)

rule flagStats:
    input: output/bam/Pfeiffer3.bam
    output: output/metrics/Pfeiffer3.flagStats
    log: log/bamMetrics/flagStats/flagStats_Pfeiffer3.2017-07-07.20-22-37.stderr
    jobid: 3
    wildcards: sampleFS=Pfeiffer3

Submitted DRMAA job (jobid 8827983)
Finished job 4.
17 of 21 steps (81%) done
Finished job 1.
18 of 21 steps (86%) done
Finished job 3.
19 of 21 steps (90%) done
Finished job 2.
20 of 21 steps (95%) done

localrule all:
    input: output/metrics/Pfeiffer2.readLen, output/metrics/Pfeiffer3.readLen, output/metrics/Pfeiffer2.flagStats, output/metrics/Pfeiffer3.flagStats
    jobid: 0

Finished job 0.
21 of 21 steps (100%) done

real    4m34.295s
user    0m1.706s
sys    0m0.288s
```
