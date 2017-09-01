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
    input: input/rawBam/Pfeiffer2.bam
    output: output/fastq/Pfeiffer2.1.fastq, output/fastq/Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-07.20-37-58.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-07.20-37-58.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-07.20-37-58.namesort.stderr
    jobid: 23
    wildcards: sampleB2FP=Pfeiffer2


rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer3.bam
    output: output/fastq/Pfeiffer3.1.fastq, output/fastq/Pfeiffer3.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-07.20-37-58.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-07.20-37-58.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-07.20-37-58.namesort.stderr
    jobid: 24
    wildcards: sampleB2FP=Pfeiffer3


rule fastq2GZ:
    input: output/fastq/Pfeiffer3.1.fastq
    output: output/fastq/Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.1.2017-07-07.20-37-58.stderr
    jobid: 21
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer3.1


rule fastq2GZ:
    input: output/fastq/Pfeiffer3.2.fastq
    output: output/fastq/Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.2.2017-07-07.20-37-58.stderr
    jobid: 22
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer3.2


rule fastq2GZ:
    input: output/fastq/Pfeiffer2.1.fastq
    output: output/fastq/Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.1.2017-07-07.20-37-58.stderr
    jobid: 20
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer2.1


rule fastq2GZ:
    input: output/fastq/Pfeiffer2.2.fastq
    output: output/fastq/Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.2.2017-07-07.20-37-58.stderr
    jobid: 19
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer2.2


rule bamALIGN_bwa:
    input: output/fastq/Pfeiffer3.1.fastq.gz, output/fastq/Pfeiffer3.2.fastq.gz, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa
    output: output/bam/Pfeiffer3_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-07.20-37-58.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-07.20-37-58.samtools.stderr
    jobid: 18
    wildcards: sampleBAB=Pfeiffer3


rule bamALIGN_bwa:
    input: output/fastq/Pfeiffer2.1.fastq.gz, output/fastq/Pfeiffer2.2.fastq.gz, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa
    output: output/bam/Pfeiffer2_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-07.20-37-58.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-07.20-37-58.samtools.stderr
    jobid: 17
    wildcards: sampleBAB=Pfeiffer2


rule sortBAM_biobambam:
    input: output/bam/Pfeiffer2_Aligned.out.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-07.20-37-58.bamsort.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-07.20-37-58.samtools.stderr
    jobid: 15
    wildcards: sampleSBB=Pfeiffer2_Aligned.out, pathSBB=output/bam


rule sortBAM_biobambam:
    input: output/bam/Pfeiffer3_Aligned.out.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-07.20-37-58.bamsort.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-07.20-37-58.samtools.stderr
    jobid: 16
    wildcards: sampleSBB=Pfeiffer3_Aligned.out, pathSBB=output/bam


rule filteredBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer3_Aligned.out_sorted.2017-07-07.20-37-58.stderr
    jobid: 14
    wildcards: pathFB=output/bam, sampleFB=Pfeiffer3_Aligned.out_sorted


rule filteredBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer2_Aligned.out_sorted.2017-07-07.20-37-58.stderr
    jobid: 13
    wildcards: pathFB=output/bam, sampleFB=Pfeiffer2_Aligned.out_sorted


rule markdupBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam, output/metrics/Pfeiffer2_Aligned.out_sorted_filtered.dup_metrics
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer2_Aligned.out_sorted_filtered.2017-07-07.20-37-58.biobammarkdup.stderr
    jobid: 11
    wildcards: sampleMDB=Pfeiffer2_Aligned.out_sorted_filtered, outputDIR=output


rule markdupBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam, output/metrics/Pfeiffer3_Aligned.out_sorted_filtered.dup_metrics
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer3_Aligned.out_sorted_filtered.2017-07-07.20-37-58.biobammarkdup.stderr
    jobid: 12
    wildcards: sampleMDB=Pfeiffer3_Aligned.out_sorted_filtered, outputDIR=output


rule indexBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam.bai
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer2.2017-07-07.20-37-58.stderr
    jobid: 9
    wildcards: sampleIB=Pfeiffer2, outputDIR=output


rule indexBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam.bai
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer3.2017-07-07.20-37-58.stderr
    jobid: 10
    wildcards: sampleIB=Pfeiffer3, outputDIR=output


rule collectMultMetrics:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/metrics/Pfeiffer2.collectMultMetrics.alignment_summary_metrics, output/metrics/Pfeiffer2.collectMultMetrics.base_distribution_by_cycle_metrics, output/metrics/Pfeiffer2.collectMultMetrics.base_distribution_by_cycle.pdf, output/metrics/Pfeiffer2.collectMultMetrics.insert_size_histogram.pdf, output/metrics/Pfeiffer2.collectMultMetrics.insert_size_metrics, output/metrics/Pfeiffer2.collectMultMetrics.quality_by_cycle_metrics, output/metrics/Pfeiffer2.collectMultMetrics.quality_by_cycle.pdf, output/metrics/Pfeiffer2.collectMultMetrics.quality_distribution_metrics, output/metrics/Pfeiffer2.collectMultMetrics.quality_distribution.pdf
    log: log/bamMetrics/collectMultMetrics/collectMultMetrics_Pfeiffer2.2017-07-07.20-37-58.stderr
    jobid: 8
    wildcards: sampleCMM=Pfeiffer2


rule collectMultMetrics:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/metrics/Pfeiffer3.collectMultMetrics.alignment_summary_metrics, output/metrics/Pfeiffer3.collectMultMetrics.base_distribution_by_cycle_metrics, output/metrics/Pfeiffer3.collectMultMetrics.base_distribution_by_cycle.pdf, output/metrics/Pfeiffer3.collectMultMetrics.insert_size_histogram.pdf, output/metrics/Pfeiffer3.collectMultMetrics.insert_size_metrics, output/metrics/Pfeiffer3.collectMultMetrics.quality_by_cycle_metrics, output/metrics/Pfeiffer3.collectMultMetrics.quality_by_cycle.pdf, output/metrics/Pfeiffer3.collectMultMetrics.quality_distribution_metrics, output/metrics/Pfeiffer3.collectMultMetrics.quality_distribution.pdf
    log: log/bamMetrics/collectMultMetrics/collectMultMetrics_Pfeiffer3.2017-07-07.20-37-58.stderr
    jobid: 7
    wildcards: sampleCMM=Pfeiffer3


rule collectWGS:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/metrics/Pfeiffer2.collectWGS.txt
    log: log/bamMetrics/collectWGS/collectWGS_Pfeiffer2.2017-07-07.20-37-58.stderr
    jobid: 1
    wildcards: sampleCWGS=Pfeiffer2


rule collectRNASeq:
    input: /extscratch/clc/references/refseq.hg19.refFlat, output/bam/Pfeiffer3.bam, /extscratch/clc/references/rRNA.ensg72.hg19.interval_list, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/metrics/Pfeiffer3.collectRNASeq.txt
    log: log/bamMetrics/collectRNASeq
    jobid: 2
    wildcards: sampleCRNAS=Pfeiffer3


rule collectRNASeq:
    input: /extscratch/clc/references/refseq.hg19.refFlat, output/bam/Pfeiffer2.bam, /extscratch/clc/references/rRNA.ensg72.hg19.interval_list, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/metrics/Pfeiffer2.collectRNASeq.txt
    log: log/bamMetrics/collectRNASeq
    jobid: 3
    wildcards: sampleCRNAS=Pfeiffer2


rule collectGCBias:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/metrics/Pfeiffer2.collectGCBias.txt
    log: log/bamMetrics/collectGCBias/collectGCBias_Pfeiffer2.2017-07-07.20-37-58.stderr
    jobid: 5
    wildcards: sampleCGCB=Pfeiffer2


rule collectGCBias:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/metrics/Pfeiffer3.collectGCBias.txt
    log: log/bamMetrics/collectGCBias/collectGCBias_Pfeiffer3.2017-07-07.20-37-58.stderr
    jobid: 4
    wildcards: sampleCGCB=Pfeiffer3


rule collectWGS:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/metrics/Pfeiffer3.collectWGS.txt
    log: log/bamMetrics/collectWGS/collectWGS_Pfeiffer3.2017-07-07.20-37-58.stderr
    jobid: 6
    wildcards: sampleCWGS=Pfeiffer3


localrule all:
    input: output/metrics/Pfeiffer2.collectGCBias.txt, output/metrics/Pfeiffer3.collectGCBias.txt, output/metrics/Pfeiffer2.collectMultMetrics.quality_distribution.pdf, output/metrics/Pfeiffer3.collectMultMetrics.quality_distribution.pdf, output/metrics/Pfeiffer2.collectRNASeq.txt, output/metrics/Pfeiffer3.collectRNASeq.txt, output/metrics/Pfeiffer2.collectWGS.txt, output/metrics/Pfeiffer3.collectWGS.txt
    jobid: 0

Job counts:
	count	jobs
	1	all
	2	bam2fastq_picard
	2	bamALIGN_bwa
	2	collectGCBias
	2	collectMultMetrics
	2	collectRNASeq
	2	collectWGS
	4	fastq2GZ
	2	filteredBAM
	2	indexBAM
	2	markdupBAM
	2	sortBAM_biobambam
	25
```

## Snakemake cluster run output:
```
Provided cluster nodes: 100
Job counts:
    count    jobs
    1    all
    2    bam2fastq_picard
    2    bamALIGN_bwa
    2    collectGCBias
    2    collectMultMetrics
    2    collectRNASeq
    2    collectWGS
    4    fastq2GZ
    2    filteredBAM
    2    indexBAM
    2    markdupBAM
    2    sortBAM_biobambam
    25

rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer3.bam
    output: output/fastq/Pfeiffer3.1.fastq, output/fastq/Pfeiffer3.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-07.20-22-35.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-07.20-22-35.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-07.20-22-35.stderr
    jobid: 24
    wildcards: sampleB2FP=Pfeiffer3

Submitted DRMAA job (jobid 8827702)

rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer2.bam
    output: output/fastq/Pfeiffer2.1.fastq, output/fastq/Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-07.20-22-35.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-07.20-22-35.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-07.20-22-35.stderr
    jobid: 23
    wildcards: sampleB2FP=Pfeiffer2

Submitted DRMAA job (jobid 8827703)
Finished job 23.
1 of 25 steps (4%) done

rule fastq2GZ:
    input: output/fastq/Pfeiffer2.2.fastq
    output: output/fastq/Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.2.2017-07-07.20-22-35.stderr
    jobid: 19
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer2.2

Submitted DRMAA job (jobid 8827747)

rule fastq2GZ:
    input: output/fastq/Pfeiffer2.1.fastq
    output: output/fastq/Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.1.2017-07-07.20-22-35.stderr
    jobid: 20
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer2.1

Submitted DRMAA job (jobid 8827748)
Finished job 24.
2 of 25 steps (8%) done

rule fastq2GZ:
    input: output/fastq/Pfeiffer3.2.fastq
    output: output/fastq/Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.2.2017-07-07.20-22-35.stderr
    jobid: 22
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer3.2

Submitted DRMAA job (jobid 8827754)

rule fastq2GZ:
    input: output/fastq/Pfeiffer3.1.fastq
    output: output/fastq/Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.1.2017-07-07.20-22-35.stderr
    jobid: 21
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer3.1

Submitted DRMAA job (jobid 8827755)
Finished job 19.
3 of 25 steps (12%) done
Finished job 21.
4 of 25 steps (16%) done
Finished job 20.
5 of 25 steps (20%) done

rule bamALIGN_bwa:
    input: output/fastq/Pfeiffer2.1.fastq.gz, output/fastq/Pfeiffer2.2.fastq.gz, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/bam/Pfeiffer2_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-07.20-22-35.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-07.20-22-35.samtools.stderr
    jobid: 17
    wildcards: sampleBAB=Pfeiffer2

Submitted DRMAA job (jobid 8827780)
Finished job 22.
6 of 25 steps (24%) done

rule bamALIGN_bwa:
    input: output/fastq/Pfeiffer3.1.fastq.gz, output/fastq/Pfeiffer3.2.fastq.gz, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/bam/Pfeiffer3_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-07.20-22-35.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-07.20-22-35.samtools.stderr
    jobid: 18
    wildcards: sampleBAB=Pfeiffer3

Submitted DRMAA job (jobid 8827789)
Finished job 17.
7 of 25 steps (28%) done

rule sortBAM_biobambam:
    input: output/bam/Pfeiffer2_Aligned.out.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-07.20-22-35.samtools.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-07.20-22-35.bamsort.stderr
    jobid: 15
    wildcards: sampleSBB=Pfeiffer2_Aligned.out, pathSBB=output/bam

Submitted DRMAA job (jobid 8827825)
Finished job 18.
8 of 25 steps (32%) done

rule sortBAM_biobambam:
    input: output/bam/Pfeiffer3_Aligned.out.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-07.20-22-35.samtools.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-07.20-22-35.bamsort.stderr
    jobid: 16
    wildcards: sampleSBB=Pfeiffer3_Aligned.out, pathSBB=output/bam

Submitted DRMAA job (jobid 8827836)
Finished job 15.
9 of 25 steps (36%) done

rule filteredBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer2_Aligned.out_sorted.2017-07-07.20-22-35.stderr
    jobid: 13
    wildcards: sampleFB=Pfeiffer2_Aligned.out_sorted, pathFB=output/bam

Submitted DRMAA job (jobid 8827868)
Finished job 16.
10 of 25 steps (40%) done

rule filteredBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer3_Aligned.out_sorted.2017-07-07.20-22-35.stderr
    jobid: 14
    wildcards: sampleFB=Pfeiffer3_Aligned.out_sorted, pathFB=output/bam

Submitted DRMAA job (jobid 8827873)
Finished job 13.
11 of 25 steps (44%) done

rule markdupBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    output: output/metrics/Pfeiffer2_Aligned.out_sorted_filtered.dup_metrics, output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer2_Aligned.out_sorted_filtered.2017-07-07.20-22-35.biobammarkdup.stderr
    jobid: 11
    wildcards: outputDIR=output, sampleMDB=Pfeiffer2_Aligned.out_sorted_filtered

Finished job 14.
12 of 25 steps (48%) done
Submitted DRMAA job (jobid 8827891)

rule markdupBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    output: output/metrics/Pfeiffer3_Aligned.out_sorted_filtered.dup_metrics, output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer3_Aligned.out_sorted_filtered.2017-07-07.20-22-35.biobammarkdup.stderr
    jobid: 12
    wildcards: outputDIR=output, sampleMDB=Pfeiffer3_Aligned.out_sorted_filtered

Submitted DRMAA job (jobid 8827892)
Finished job 12.
13 of 25 steps (52%) done

rule indexBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam.bai
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer3.2017-07-07.20-22-35.stderr
    jobid: 10
    wildcards: outputDIR=output, sampleIB=Pfeiffer3

Submitted DRMAA job (jobid 8827928)
Finished job 11.
14 of 25 steps (56%) done

rule indexBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam.bai
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer2.2017-07-07.20-22-35.stderr
    jobid: 9
    wildcards: outputDIR=output, sampleIB=Pfeiffer2

Submitted DRMAA job (jobid 8827934)
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/Pfeiffer2.bam. Your Python build does not support it.
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/Pfeiffer2.bam.bai. Your Python build does not support it.
Finished job 9.
15 of 25 steps (60%) done

rule collectMultMetrics:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/metrics/Pfeiffer2.collectMultMetrics.alignment_summary_metrics, output/metrics/Pfeiffer2.collectMultMetrics.base_distribution_by_cycle_metrics, output/metrics/Pfeiffer2.collectMultMetrics.base_distribution_by_cycle.pdf, output/metrics/Pfeiffer2.collectMultMetrics.insert_size_histogram.pdf, output/metrics/Pfeiffer2.collectMultMetrics.insert_size_metrics, output/metrics/Pfeiffer2.collectMultMetrics.quality_by_cycle_metrics, output/metrics/Pfeiffer2.collectMultMetrics.quality_by_cycle.pdf, output/metrics/Pfeiffer2.collectMultMetrics.quality_distribution_metrics, output/metrics/Pfeiffer2.collectMultMetrics.quality_distribution.pdf
    log: log/bamMetrics/collectMultMetrics/collectMultMetrics_Pfeiffer2.2017-07-07.20-22-34.stderr
    jobid: 1
    wildcards: sampleCMM=Pfeiffer2

Submitted DRMAA job (jobid 8827957)

rule collectRNASeq:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam, /extscratch/clc/references/rRNA.ensg72.hg19.interval_list, /extscratch/clc/references/refseq.hg19.refFlat
    output: output/metrics/Pfeiffer2.collectRNASeq.txt
    log: log/bamMetrics/collectRNASeq
    jobid: 2
    wildcards: sampleCRNAS=Pfeiffer2

Submitted DRMAA job (jobid 8827958)

rule collectWGS:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/metrics/Pfeiffer2.collectWGS.txt
    log: log/bamMetrics/collectWGS/collectWGS_Pfeiffer2.2017-07-07.20-22-34.stderr
    jobid: 3
    wildcards: sampleCWGS=Pfeiffer2

Submitted DRMAA job (jobid 8827959)

rule collectGCBias:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/metrics/Pfeiffer2.collectGCBias.txt
    log: log/bamMetrics/collectGCBias/collectGCBias_Pfeiffer2.2017-07-07.20-22-34.stderr
    jobid: 7
    wildcards: sampleCGCB=Pfeiffer2

Submitted DRMAA job (jobid 8827960)
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/Pfeiffer3.bam. Your Python build does not support it.
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/Pfeiffer3.bam.bai. Your Python build does not support it.
Finished job 10.
16 of 25 steps (64%) done

rule collectRNASeq:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam, /extscratch/clc/references/rRNA.ensg72.hg19.interval_list, /extscratch/clc/references/refseq.hg19.refFlat
    output: output/metrics/Pfeiffer3.collectRNASeq.txt
    log: log/bamMetrics/collectRNASeq
    jobid: 4
    wildcards: sampleCRNAS=Pfeiffer3

Submitted DRMAA job (jobid 8827961)

rule collectMultMetrics:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/metrics/Pfeiffer3.collectMultMetrics.alignment_summary_metrics, output/metrics/Pfeiffer3.collectMultMetrics.base_distribution_by_cycle_metrics, output/metrics/Pfeiffer3.collectMultMetrics.base_distribution_by_cycle.pdf, output/metrics/Pfeiffer3.collectMultMetrics.insert_size_histogram.pdf, output/metrics/Pfeiffer3.collectMultMetrics.insert_size_metrics, output/metrics/Pfeiffer3.collectMultMetrics.quality_by_cycle_metrics, output/metrics/Pfeiffer3.collectMultMetrics.quality_by_cycle.pdf, output/metrics/Pfeiffer3.collectMultMetrics.quality_distribution_metrics, output/metrics/Pfeiffer3.collectMultMetrics.quality_distribution.pdf
    log: log/bamMetrics/collectMultMetrics/collectMultMetrics_Pfeiffer3.2017-07-07.20-22-34.stderr
    jobid: 6
    wildcards: sampleCMM=Pfeiffer3

Submitted DRMAA job (jobid 8827962)

rule collectGCBias:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/metrics/Pfeiffer3.collectGCBias.txt
    log: log/bamMetrics/collectGCBias/collectGCBias_Pfeiffer3.2017-07-07.20-22-34.stderr
    jobid: 5
    wildcards: sampleCGCB=Pfeiffer3

Submitted DRMAA job (jobid 8827963)

rule collectWGS:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/metrics/Pfeiffer3.collectWGS.txt
    log: log/bamMetrics/collectWGS/collectWGS_Pfeiffer3.2017-07-07.20-22-34.stderr
    jobid: 8
    wildcards: sampleCWGS=Pfeiffer3

Submitted DRMAA job (jobid 8827964)
Finished job 4.
17 of 25 steps (68%) done
Finished job 2.
18 of 25 steps (72%) done
Finished job 1.
19 of 25 steps (76%) done
Finished job 6.
20 of 25 steps (80%) done
Finished job 7.
21 of 25 steps (84%) done
Finished job 5.
22 of 25 steps (88%) done
Finished job 3.
23 of 25 steps (92%) done
Finished job 8.
24 of 25 steps (96%) done

localrule all:
    input: output/metrics/Pfeiffer2.collectGCBias.txt, output/metrics/Pfeiffer3.collectGCBias.txt, output/metrics/Pfeiffer2.collectMultMetrics.quality_distribution.pdf, output/metrics/Pfeiffer3.collectMultMetrics.quality_distribution.pdf, output/metrics/Pfeiffer2.collectRNASeq.txt, output/metrics/Pfeiffer3.collectRNASeq.txt, output/metrics/Pfeiffer2.collectWGS.txt, output/metrics/Pfeiffer3.collectWGS.txt
    jobid: 0

Finished job 0.
25 of 25 steps (100%) done

real    14m48.487s
user    0m1.770s
sys    0m0.283s
```
