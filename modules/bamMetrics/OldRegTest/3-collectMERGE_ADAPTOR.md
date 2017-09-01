# 3-collectMERGE_ADAPTOR
This pipeline is to exemplify the default operations of this module.

## Setting up the: buildPipe.py
Users must set the following variable:

 * (Line 13) TYPE = "single"

## Setting up the: Snakefile
Users must set the following submodule "call via" input requirements:

 * collectMERGE_ADAPTOR

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
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-07.20-56-54.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-07.20-56-54.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-07.20-56-54.namesort.stderr
    jobid: 26
    wildcards: sampleB2FP=Pfeiffer2


rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer3.bam
    output: output/fastq/Pfeiffer3.1.fastq, output/fastq/Pfeiffer3.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-07.20-56-54.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-07.20-56-54.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-07.20-56-54.namesort.stderr
    jobid: 25
    wildcards: sampleB2FP=Pfeiffer3


rule fastq2GZ:
    input: output/fastq/Pfeiffer2.1.fastq
    output: output/fastq/Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.1.2017-07-07.20-56-54.stderr
    jobid: 23
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer2.1


rule fastq2GZ:
    input: output/fastq/Pfeiffer2.2.fastq
    output: output/fastq/Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.2.2017-07-07.20-56-54.stderr
    jobid: 24
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer2.2


rule fastq2GZ:
    input: output/fastq/Pfeiffer3.1.fastq
    output: output/fastq/Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.1.2017-07-07.20-56-54.stderr
    jobid: 21
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer3.1


rule fastq2GZ:
    input: output/fastq/Pfeiffer3.2.fastq
    output: output/fastq/Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.2.2017-07-07.20-56-54.stderr
    jobid: 22
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer3.2


rule bamALIGN_bwa:
    input: output/fastq/Pfeiffer2.1.fastq.gz, output/fastq/Pfeiffer2.2.fastq.gz, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa
    output: output/bam/Pfeiffer2_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-07.20-56-54.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-07.20-56-54.samtools.stderr
    jobid: 20
    wildcards: sampleBAB=Pfeiffer2


rule bamALIGN_bwa:
    input: output/fastq/Pfeiffer3.1.fastq.gz, output/fastq/Pfeiffer3.2.fastq.gz, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa
    output: output/bam/Pfeiffer3_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-07.20-56-54.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-07.20-56-54.samtools.stderr
    jobid: 19
    wildcards: sampleBAB=Pfeiffer3


rule sortBAM_biobambam:
    input: output/bam/Pfeiffer2_Aligned.out.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-07.20-56-54.bamsort.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-07.20-56-54.samtools.stderr
    jobid: 18
    wildcards: pathSBB=output/bam, sampleSBB=Pfeiffer2_Aligned.out


rule sortBAM_biobambam:
    input: output/bam/Pfeiffer3_Aligned.out.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-07.20-56-54.bamsort.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-07.20-56-54.samtools.stderr
    jobid: 17
    wildcards: pathSBB=output/bam, sampleSBB=Pfeiffer3_Aligned.out


rule filteredBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer3_Aligned.out_sorted.2017-07-07.20-56-53.stderr
    jobid: 15
    wildcards: sampleFB=Pfeiffer3_Aligned.out_sorted, pathFB=output/bam


rule filteredBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer2_Aligned.out_sorted.2017-07-07.20-56-53.stderr
    jobid: 16
    wildcards: sampleFB=Pfeiffer2_Aligned.out_sorted, pathFB=output/bam


rule markdupBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam, output/metrics/Pfeiffer3_Aligned.out_sorted_filtered.dup_metrics
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer3_Aligned.out_sorted_filtered.2017-07-07.20-56-54.biobammarkdup.stderr
    jobid: 13
    wildcards: sampleMDB=Pfeiffer3_Aligned.out_sorted_filtered, outputDIR=output


rule markdupBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam, output/metrics/Pfeiffer2_Aligned.out_sorted_filtered.dup_metrics
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer2_Aligned.out_sorted_filtered.2017-07-07.20-56-54.biobammarkdup.stderr
    jobid: 14
    wildcards: sampleMDB=Pfeiffer2_Aligned.out_sorted_filtered, outputDIR=output


rule indexBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam.bai, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer2.2017-07-07.20-56-53.stderr
    jobid: 12
    wildcards: outputDIR=output, sampleIB=Pfeiffer2


rule indexBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam.bai, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer3.2017-07-07.20-56-53.stderr
    jobid: 11
    wildcards: outputDIR=output, sampleIB=Pfeiffer3


rule collectMultMetrics:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/metrics/Pfeiffer2.collectMultMetrics.alignment_summary_metrics, output/metrics/Pfeiffer2.collectMultMetrics.base_distribution_by_cycle_metrics, output/metrics/Pfeiffer2.collectMultMetrics.base_distribution_by_cycle.pdf, output/metrics/Pfeiffer2.collectMultMetrics.insert_size_histogram.pdf, output/metrics/Pfeiffer2.collectMultMetrics.insert_size_metrics, output/metrics/Pfeiffer2.collectMultMetrics.quality_by_cycle_metrics, output/metrics/Pfeiffer2.collectMultMetrics.quality_by_cycle.pdf, output/metrics/Pfeiffer2.collectMultMetrics.quality_distribution_metrics, output/metrics/Pfeiffer2.collectMultMetrics.quality_distribution.pdf
    log: log/bamMetrics/collectMultMetrics/collectMultMetrics_Pfeiffer2.2017-07-07.20-56-53.stderr
    jobid: 9
    wildcards: sampleCMM=Pfeiffer2


rule collectMultMetrics:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/metrics/Pfeiffer3.collectMultMetrics.alignment_summary_metrics, output/metrics/Pfeiffer3.collectMultMetrics.base_distribution_by_cycle_metrics, output/metrics/Pfeiffer3.collectMultMetrics.base_distribution_by_cycle.pdf, output/metrics/Pfeiffer3.collectMultMetrics.insert_size_histogram.pdf, output/metrics/Pfeiffer3.collectMultMetrics.insert_size_metrics, output/metrics/Pfeiffer3.collectMultMetrics.quality_by_cycle_metrics, output/metrics/Pfeiffer3.collectMultMetrics.quality_by_cycle.pdf, output/metrics/Pfeiffer3.collectMultMetrics.quality_distribution_metrics, output/metrics/Pfeiffer3.collectMultMetrics.quality_distribution.pdf
    log: log/bamMetrics/collectMultMetrics/collectMultMetrics_Pfeiffer3.2017-07-07.20-56-53.stderr
    jobid: 10
    wildcards: sampleCMM=Pfeiffer3


rule collectWGS:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/metrics/Pfeiffer2.collectWGS.txt
    log: log/bamMetrics/collectWGS/collectWGS_Pfeiffer2.2017-07-07.20-56-53.stderr
    jobid: 6
    wildcards: sampleCWGS=Pfeiffer2


rule collectRNASeq:
    input: output/bam/Pfeiffer2.bam, /extscratch/clc/references/refseq.hg19.refFlat, /extscratch/clc/references/rRNA.ensg72.hg19.interval_list, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/metrics/Pfeiffer2.collectRNASeq.txt
    log: log/bamMetrics/collectRNASeq
    jobid: 7
    wildcards: sampleCRNAS=Pfeiffer2


rule collectWGS:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/metrics/Pfeiffer3.collectWGS.txt
    log: log/bamMetrics/collectWGS/collectWGS_Pfeiffer3.2017-07-07.20-56-53.stderr
    jobid: 5
    wildcards: sampleCWGS=Pfeiffer3


rule collectRNASeq:
    input: output/bam/Pfeiffer3.bam, /extscratch/clc/references/refseq.hg19.refFlat, /extscratch/clc/references/rRNA.ensg72.hg19.interval_list, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/metrics/Pfeiffer3.collectRNASeq.txt
    log: log/bamMetrics/collectRNASeq
    jobid: 8
    wildcards: sampleCRNAS=Pfeiffer3


rule collectRNASeqMERGE:
    input: output/metrics/Pfeiffer2.collectRNASeq.txt, output/metrics/Pfeiffer3.collectRNASeq.txt
    output: output/metrics/all.rnaseq_metrics
    log: log/bamMetrics/collectRNASeqMERGE/collectRNASeqMERGE.2017-07-07.20-56-53.stderr
    jobid: 2


rule collectWGSMERGE:
    input: output/metrics/Pfeiffer2.collectWGS.txt, output/metrics/Pfeiffer3.collectWGS.txt
    output: output/metrics/all.wgs_metrics
    log: log/bamMetrics/collectAlignmentSummaryMERGE/collectAlignmentSummaryMERGE.2017-07-07.20-56-53.stderr
    jobid: 1


rule collectAlignmentSummaryMERGE:
    input: output/metrics/Pfeiffer2.collectMultMetrics.alignment_summary_metrics, output/metrics/Pfeiffer3.collectMultMetrics.alignment_summary_metrics
    output: output/metrics/all.alignment_summary_metrics
    log: log/bamMetrics/collectAlignmentSummaryMERGE/collectAlignmentSummaryMERGE.2017-07-07.20-56-53.stderr
    jobid: 4


rule collectInsertSizeMERGE:
    input: output/metrics/Pfeiffer2.collectMultMetrics.insert_size_metrics, output/metrics/Pfeiffer3.collectMultMetrics.insert_size_metrics
    output: output/metrics/all.insert_size_metrics
    log: log/bamMetrics/collectInsertSizeMERGE/collectInsertSizeMERGE.2017-07-07.20-56-53.stderr
    jobid: 3


localrule all:
    input: output/metrics/all.rnaseq_metrics, output/metrics/all.wgs_metrics, output/metrics/all.insert_size_metrics, output/metrics/all.alignment_summary_metrics
    jobid: 0

Job counts:
	count	jobs
	1	all
	2	bam2fastq_picard
	2	bamALIGN_bwa
	1	collectAlignmentSummaryMERGE
	1	collectInsertSizeMERGE
	2	collectMultMetrics
	2	collectRNASeq
	1	collectRNASeqMERGE
	2	collectWGS
	1	collectWGSMERGE
	4	fastq2GZ
	2	filteredBAM
	2	indexBAM
	2	markdupBAM
	2	sortBAM_biobambam
	27
```

## Snakemake cluster run output:
```
Provided cluster nodes: 100
Job counts:
    count    jobs
    1    all
    2    bam2fastq_picard
    2    bamALIGN_bwa
    1    collectAlignmentSummaryMERGE
    1    collectInsertSizeMERGE
    2    collectMultMetrics
    2    collectRNASeq
    1    collectRNASeqMERGE
    2    collectWGS
    1    collectWGSMERGE
    4    fastq2GZ
    2    filteredBAM
    2    indexBAM
    2    markdupBAM
    2    sortBAM_biobambam
    27

rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer2.bam
    output: output/fastq/Pfeiffer2.1.fastq, output/fastq/Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-07.20-34-28.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-07.20-34-28.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-07.20-34-28.stderr
    jobid: 26
    wildcards: sampleB2FP=Pfeiffer2

Submitted DRMAA job (jobid 8828370)

rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer3.bam
    output: output/fastq/Pfeiffer3.1.fastq, output/fastq/Pfeiffer3.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-07.20-34-28.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-07.20-34-28.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-07.20-34-28.stderr
    jobid: 25
    wildcards: sampleB2FP=Pfeiffer3

Submitted DRMAA job (jobid 8828371)
Finished job 26.
1 of 27 steps (4%) done

rule fastq2GZ:
    input: output/fastq/Pfeiffer2.1.fastq
    output: output/fastq/Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.1.2017-07-07.20-34-28.stderr
    jobid: 23
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer2.1

Submitted DRMAA job (jobid 8828422)

rule fastq2GZ:
    input: output/fastq/Pfeiffer2.2.fastq
    output: output/fastq/Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.2.2017-07-07.20-34-28.stderr
    jobid: 24
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer2.2

Submitted DRMAA job (jobid 8828423)
Finished job 25.
2 of 27 steps (7%) done

rule fastq2GZ:
    input: output/fastq/Pfeiffer3.1.fastq
    output: output/fastq/Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.1.2017-07-07.20-34-28.stderr
    jobid: 21
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer3.1

Submitted DRMAA job (jobid 8828424)

rule fastq2GZ:
    input: output/fastq/Pfeiffer3.2.fastq
    output: output/fastq/Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.2.2017-07-07.20-34-28.stderr
    jobid: 22
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer3.2

Submitted DRMAA job (jobid 8828425)
Finished job 21.
3 of 27 steps (11%) done
Finished job 23.
4 of 27 steps (15%) done
Finished job 24.
5 of 27 steps (19%) done

rule bamALIGN_bwa:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, output/fastq/Pfeiffer2.1.fastq.gz, output/fastq/Pfeiffer2.2.fastq.gz
    output: output/bam/Pfeiffer2_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-07.20-34-28.samtools.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-07.20-34-28.bwa.stderr
    jobid: 20
    wildcards: sampleBAB=Pfeiffer2

Submitted DRMAA job (jobid 8828442)
Finished job 22.
6 of 27 steps (22%) done

rule bamALIGN_bwa:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, output/fastq/Pfeiffer3.1.fastq.gz, output/fastq/Pfeiffer3.2.fastq.gz
    output: output/bam/Pfeiffer3_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-07.20-34-28.samtools.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-07.20-34-28.bwa.stderr
    jobid: 19
    wildcards: sampleBAB=Pfeiffer3

Submitted DRMAA job (jobid 8828445)
Finished job 19.
7 of 27 steps (26%) done

rule sortBAM_biobambam:
    input: output/bam/Pfeiffer3_Aligned.out.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-07.20-34-27.samtools.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-07.20-34-27.bamsort.stderr
    jobid: 17
    wildcards: pathSBB=output/bam, sampleSBB=Pfeiffer3_Aligned.out

Submitted DRMAA job (jobid 8828484)
Finished job 20.
8 of 27 steps (30%) done

rule sortBAM_biobambam:
    input: output/bam/Pfeiffer2_Aligned.out.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-07.20-34-27.samtools.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-07.20-34-27.bamsort.stderr
    jobid: 18
    wildcards: pathSBB=output/bam, sampleSBB=Pfeiffer2_Aligned.out

Submitted DRMAA job (jobid 8828490)
Finished job 18.
9 of 27 steps (33%) done

rule filteredBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer2_Aligned.out_sorted.2017-07-07.20-34-27.stderr
    jobid: 16
    wildcards: pathFB=output/bam, sampleFB=Pfeiffer2_Aligned.out_sorted

Submitted DRMAA job (jobid 8828521)
Finished job 17.
10 of 27 steps (37%) done

rule filteredBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer3_Aligned.out_sorted.2017-07-07.20-34-27.stderr
    jobid: 15
    wildcards: pathFB=output/bam, sampleFB=Pfeiffer3_Aligned.out_sorted

Submitted DRMAA job (jobid 8828523)
Finished job 15.
11 of 27 steps (41%) done

rule markdupBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    output: output/metrics/Pfeiffer3_Aligned.out_sorted_filtered.dup_metrics, output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer3_Aligned.out_sorted_filtered.2017-07-07.20-34-27.biobammarkdup.stderr
    jobid: 13
    wildcards: outputDIR=output, sampleMDB=Pfeiffer3_Aligned.out_sorted_filtered

Submitted DRMAA job (jobid 8828533)
Finished job 16.
12 of 27 steps (44%) done

rule markdupBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    output: output/metrics/Pfeiffer2_Aligned.out_sorted_filtered.dup_metrics, output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer2_Aligned.out_sorted_filtered.2017-07-07.20-34-27.biobammarkdup.stderr
    jobid: 14
    wildcards: outputDIR=output, sampleMDB=Pfeiffer2_Aligned.out_sorted_filtered

Submitted DRMAA job (jobid 8828550)
Finished job 13.
13 of 27 steps (48%) done

rule indexBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam.bai, output/bam/Pfeiffer3.bam.bai
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer3.2017-07-07.20-34-27.stderr
    jobid: 11
    wildcards: sampleIB=Pfeiffer3, outputDIR=output

Submitted DRMAA job (jobid 8828562)
Finished job 14.
14 of 27 steps (52%) done

rule indexBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam.bai, output/bam/Pfeiffer2.bam.bai
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer2.2017-07-07.20-34-27.stderr
    jobid: 12
    wildcards: sampleIB=Pfeiffer2, outputDIR=output

Submitted DRMAA job (jobid 8828563)
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/Pfeiffer3.bam. Your Python build does not support it.
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/Pfeiffer3.bam.bai. Your Python build does not support it.
Finished job 11.
15 of 27 steps (56%) done

rule collectWGS:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam
    output: output/metrics/Pfeiffer3.collectWGS.txt
    log: log/bamMetrics/collectWGS/collectWGS_Pfeiffer3.2017-07-07.20-34-27.stderr
    jobid: 7
    wildcards: sampleCWGS=Pfeiffer3

Submitted DRMAA job (jobid 8828583)

rule collectRNASeq:
    input: output/bam/Pfeiffer3.bam, /extscratch/clc/references/rRNA.ensg72.hg19.interval_list, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /extscratch/clc/references/refseq.hg19.refFlat
    output: output/metrics/Pfeiffer3.collectRNASeq.txt
    log: log/bamMetrics/collectRNASeq
    jobid: 9
    wildcards: sampleCRNAS=Pfeiffer3

Submitted DRMAA job (jobid 8828584)

rule collectMultMetrics:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam
    output: output/metrics/Pfeiffer3.collectMultMetrics.alignment_summary_metrics, output/metrics/Pfeiffer3.collectMultMetrics.base_distribution_by_cycle_metrics, output/metrics/Pfeiffer3.collectMultMetrics.base_distribution_by_cycle.pdf, output/metrics/Pfeiffer3.collectMultMetrics.insert_size_histogram.pdf, output/metrics/Pfeiffer3.collectMultMetrics.insert_size_metrics, output/metrics/Pfeiffer3.collectMultMetrics.quality_by_cycle_metrics, output/metrics/Pfeiffer3.collectMultMetrics.quality_by_cycle.pdf, output/metrics/Pfeiffer3.collectMultMetrics.quality_distribution_metrics, output/metrics/Pfeiffer3.collectMultMetrics.quality_distribution.pdf
    log: log/bamMetrics/collectMultMetrics/collectMultMetrics_Pfeiffer3.2017-07-07.20-34-26.stderr
    jobid: 5
    wildcards: sampleCMM=Pfeiffer3

Submitted DRMAA job (jobid 8828585)
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/Pfeiffer2.bam. Your Python build does not support it.
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/Pfeiffer2.bam.bai. Your Python build does not support it.
Finished job 12.
16 of 27 steps (59%) done

rule collectMultMetrics:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam
    output: output/metrics/Pfeiffer2.collectMultMetrics.alignment_summary_metrics, output/metrics/Pfeiffer2.collectMultMetrics.base_distribution_by_cycle_metrics, output/metrics/Pfeiffer2.collectMultMetrics.base_distribution_by_cycle.pdf, output/metrics/Pfeiffer2.collectMultMetrics.insert_size_histogram.pdf, output/metrics/Pfeiffer2.collectMultMetrics.insert_size_metrics, output/metrics/Pfeiffer2.collectMultMetrics.quality_by_cycle_metrics, output/metrics/Pfeiffer2.collectMultMetrics.quality_by_cycle.pdf, output/metrics/Pfeiffer2.collectMultMetrics.quality_distribution_metrics, output/metrics/Pfeiffer2.collectMultMetrics.quality_distribution.pdf
    log: log/bamMetrics/collectMultMetrics/collectMultMetrics_Pfeiffer2.2017-07-07.20-34-26.stderr
    jobid: 6
    wildcards: sampleCMM=Pfeiffer2

Submitted DRMAA job (jobid 8828587)

rule collectWGS:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam
    output: output/metrics/Pfeiffer2.collectWGS.txt
    log: log/bamMetrics/collectWGS/collectWGS_Pfeiffer2.2017-07-07.20-34-27.stderr
    jobid: 8
    wildcards: sampleCWGS=Pfeiffer2

Submitted DRMAA job (jobid 8828588)

rule collectRNASeq:
    input: output/bam/Pfeiffer2.bam, /extscratch/clc/references/rRNA.ensg72.hg19.interval_list, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /extscratch/clc/references/refseq.hg19.refFlat
    output: output/metrics/Pfeiffer2.collectRNASeq.txt
    log: log/bamMetrics/collectRNASeq
    jobid: 10
    wildcards: sampleCRNAS=Pfeiffer2

Submitted DRMAA job (jobid 8828589)
Finished job 9.
17 of 27 steps (63%) done
Finished job 10.
18 of 27 steps (67%) done

rule collectRNASeqMERGE:
    input: output/metrics/Pfeiffer2.collectRNASeq.txt, output/metrics/Pfeiffer3.collectRNASeq.txt
    output: output/metrics/all.rnaseq_metrics
    log: log/bamMetrics/collectRNASeqMERGE/collectRNASeqMERGE.2017-07-07.20-34-27.stderr
    jobid: 4

Submitted DRMAA job (jobid 8828636)
Finished job 4.
19 of 27 steps (70%) done
Finished job 5.
20 of 27 steps (74%) done
Finished job 6.
21 of 27 steps (78%) done

rule collectInsertSizeMERGE:
    input: output/metrics/Pfeiffer2.collectMultMetrics.insert_size_metrics, output/metrics/Pfeiffer3.collectMultMetrics.insert_size_metrics
    output: output/metrics/all.insert_size_metrics
    log: log/bamMetrics/collectInsertSizeMERGE/collectInsertSizeMERGE.2017-07-07.20-34-27.stderr
    jobid: 2

Submitted DRMAA job (jobid 8828656)

rule collectAlignmentSummaryMERGE:
    input: output/metrics/Pfeiffer2.collectMultMetrics.alignment_summary_metrics, output/metrics/Pfeiffer3.collectMultMetrics.alignment_summary_metrics
    output: output/metrics/all.alignment_summary_metrics
    log: log/bamMetrics/collectAlignmentSummaryMERGE/collectAlignmentSummaryMERGE.2017-07-07.20-34-27.stderr
    jobid: 1

Submitted DRMAA job (jobid 8828657)
Finished job 2.
22 of 27 steps (81%) done
Finished job 1.
23 of 27 steps (85%) done
Finished job 8.
24 of 27 steps (89%) done
Finished job 7.
25 of 27 steps (93%) done

rule collectWGSMERGE:
    input: output/metrics/Pfeiffer2.collectWGS.txt, output/metrics/Pfeiffer3.collectWGS.txt
    output: output/metrics/all.wgs_metrics
    log: log/bamMetrics/collectAlignmentSummaryMERGE/collectAlignmentSummaryMERGE.2017-07-07.20-34-27.stderr
    jobid: 3

Submitted DRMAA job (jobid 8829161)
Finished job 3.
26 of 27 steps (96%) done

localrule all:
    input: output/metrics/all.rnaseq_metrics, output/metrics/all.wgs_metrics, output/metrics/all.insert_size_metrics, output/metrics/all.alignment_summary_metrics
    jobid: 0

Finished job 0.
27 of 27 steps (100%) done

real    15m45.549s
user    0m2.021s
sys    0m0.292s
```
