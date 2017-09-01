# 2-mpileup2vcf_pairUNSPLIT
This pipeline is to exemplify the default operations of this module.

## Setting up the: buildPipe.py
Users must set the following variable:

 * (Line 13) TYPE = "pair"

## Setting up the: Snakefile
Users must set the following submodule "call via" input requirements:

 * pairUNSPLIT

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
``
rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer2.bam
    output: output/fastq/Pfeiffer2.1.fastq, output/fastq/Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-05.19-05-21.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-05.19-05-21.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-05.19-05-21.namesort.stderr
    jobid: 19
    wildcards: sampleB2FP=Pfeiffer2


rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer3.bam
    output: output/fastq/Pfeiffer3.1.fastq, output/fastq/Pfeiffer3.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-05.19-05-21.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-05.19-05-21.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-05.19-05-21.namesort.stderr
    jobid: 18
    wildcards: sampleB2FP=Pfeiffer3


rule fastq2GZ:
    input: output/fastq/Pfeiffer2.2.fastq
    output: output/fastq/Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.2.2017-07-05.19-05-21.stderr
    jobid: 16
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer2.2


rule fastq2GZ:
    input: output/fastq/Pfeiffer3.2.fastq
    output: output/fastq/Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.2.2017-07-05.19-05-21.stderr
    jobid: 14
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer3.2


rule fastq2GZ:
    input: output/fastq/Pfeiffer2.1.fastq
    output: output/fastq/Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.1.2017-07-05.19-05-21.stderr
    jobid: 17
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer2.1


rule fastq2GZ:
    input: output/fastq/Pfeiffer3.1.fastq
    output: output/fastq/Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.1.2017-07-05.19-05-21.stderr
    jobid: 15
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer3.1


rule bamALIGN_bwa:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, output/fastq/Pfeiffer3.1.fastq.gz, output/fastq/Pfeiffer3.2.fastq.gz
    output: output/bam/Pfeiffer3_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-05.19-05-21.samtools.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-05.19-05-21.bwa.stderr
    jobid: 12
    wildcards: sampleBAB=Pfeiffer3


rule bamALIGN_bwa:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, output/fastq/Pfeiffer2.1.fastq.gz, output/fastq/Pfeiffer2.2.fastq.gz
    output: output/bam/Pfeiffer2_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-05.19-05-21.samtools.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-05.19-05-21.bwa.stderr
    jobid: 13
    wildcards: sampleBAB=Pfeiffer2


rule sortBAM_biobambam:
    input: output/bam/Pfeiffer2_Aligned.out.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-05.19-05-21.samtools.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-05.19-05-21.bamsort.stderr
    jobid: 11
    wildcards: sampleSBB=Pfeiffer2_Aligned.out, pathSBB=output/bam


rule sortBAM_biobambam:
    input: output/bam/Pfeiffer3_Aligned.out.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-05.19-05-21.samtools.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-05.19-05-21.bamsort.stderr
    jobid: 10
    wildcards: sampleSBB=Pfeiffer3_Aligned.out, pathSBB=output/bam


rule filteredBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer2_Aligned.out_sorted.2017-07-05.19-05-21.stderr
    jobid: 9
    wildcards: pathFB=output/bam, sampleFB=Pfeiffer2_Aligned.out_sorted


rule filteredBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer3_Aligned.out_sorted.2017-07-05.19-05-21.stderr
    jobid: 8
    wildcards: pathFB=output/bam, sampleFB=Pfeiffer3_Aligned.out_sorted


rule markdupBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam, output/metrics/Pfeiffer3_Aligned.out_sorted_filtered.dup_metrics
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer3_Aligned.out_sorted_filtered.2017-07-05.19-05-21.biobammarkdup.stderr
    jobid: 6
    wildcards: outputDIR=output, sampleMDB=Pfeiffer3_Aligned.out_sorted_filtered


rule markdupBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam, output/metrics/Pfeiffer2_Aligned.out_sorted_filtered.dup_metrics
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer2_Aligned.out_sorted_filtered.2017-07-05.19-05-21.biobammarkdup.stderr
    jobid: 7
    wildcards: outputDIR=output, sampleMDB=Pfeiffer2_Aligned.out_sorted_filtered


rule indexBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam.bai, output/bam/Pfeiffer3.bam
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer3.2017-07-05.19-05-21.stderr
    jobid: 4
    wildcards: sampleIB=Pfeiffer3, outputDIR=output


rule indexBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam.bai, output/bam/Pfeiffer2.bam
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer2.2017-07-05.19-05-21.stderr
    jobid: 5
    wildcards: sampleIB=Pfeiffer2, outputDIR=output


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-05-21.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-05-21.mpileup.stderr
    jobid: 2
    wildcards: sampleB2M=Pfeiffer3, chrB2M=


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-05-21.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-05-21.mpileup.stderr
    jobid: 3
    wildcards: sampleB2M=Pfeiffer2, chrB2M=


rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer2.mpileup, output/mpileup/Pfeiffer3.mpileup
    output: output/varScan/Pfeiffer3_Pfeiffer2.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2.varScan.indel.vcf
    log: log/varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr.SNPandINDEL.2017-07-05.19-05-21.stderr
    jobid: 1
    wildcards: samplenMPU2VCFP=Pfeiffer2, sampletMPU2VCFP=Pfeiffer3, chrMPU2VCFP=


localrule all:
    input: output/varScan/Pfeiffer3_Pfeiffer2.varScan.snp.vcf, output/varScan/Pfeiffer3_Pfeiffer2.varScan.indel.vcf
    jobid: 0

Job counts:
	count	jobs
	1	all
	2	bam2fastq_picard
	2	bam2mpileup
	2	bamALIGN_bwa
	4	fastq2GZ
	2	filteredBAM
	2	indexBAM
	2	markdupBAM
	1	mpileup2vcf_pair
	2	sortBAM_biobambam
	20
```

## Snakemake cluster run output:
```
Provided cluster nodes: 100
Job counts:
    count    jobs
    1    all
    2    bam2fastq_picard
    2    bam2mpileup
    2    bamALIGN_bwa
    4    fastq2GZ
    2    filteredBAM
    2    indexBAM
    2    markdupBAM
    1    mpileup2vcf_pair
    2    sortBAM_biobambam
    20

rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer3.bam
    output: output/fastq/Pfeiffer3.1.fastq, output/fastq/Pfeiffer3.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-05.19-47-28.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-05.19-47-28.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-05.19-47-28.stderr
    jobid: 18
    wildcards: sampleB2FP=Pfeiffer3

Submitted DRMAA job (jobid 8712420)

rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer2.bam
    output: output/fastq/Pfeiffer2.1.fastq, output/fastq/Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-05.19-47-28.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-05.19-47-28.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-05.19-47-28.stderr
    jobid: 19
    wildcards: sampleB2FP=Pfeiffer2

Submitted DRMAA job (jobid 8712422)
Finished job 18.
1 of 20 steps (5%) done

rule fastq2GZ:
    input: output/fastq/Pfeiffer3.1.fastq
    output: output/fastq/Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.1.2017-07-05.19-47-28.stderr
    jobid: 14
    wildcards: sampleFGZ=Pfeiffer3.1, pathFGZ=output/fastq

Submitted DRMAA job (jobid 8712679)
Finished job 19.
2 of 20 steps (10%) done

rule fastq2GZ:
    input: output/fastq/Pfeiffer3.2.fastq
    output: output/fastq/Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.2.2017-07-05.19-47-28.stderr
    jobid: 15
    wildcards: sampleFGZ=Pfeiffer3.2, pathFGZ=output/fastq

Submitted DRMAA job (jobid 8712680)

rule fastq2GZ:
    input: output/fastq/Pfeiffer2.2.fastq
    output: output/fastq/Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.2.2017-07-05.19-47-28.stderr
    jobid: 16
    wildcards: sampleFGZ=Pfeiffer2.2, pathFGZ=output/fastq

Submitted DRMAA job (jobid 8712681)

rule fastq2GZ:
    input: output/fastq/Pfeiffer2.1.fastq
    output: output/fastq/Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.1.2017-07-05.19-47-28.stderr
    jobid: 17
    wildcards: sampleFGZ=Pfeiffer2.1, pathFGZ=output/fastq

Submitted DRMAA job (jobid 8712682)
Finished job 16.
3 of 20 steps (15%) done
Finished job 17.
4 of 20 steps (20%) done

rule bamALIGN_bwa:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, output/fastq/Pfeiffer2.1.fastq.gz, output/fastq/Pfeiffer2.2.fastq.gz
    output: output/bam/Pfeiffer2_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-05.19-47-28.samtools.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-05.19-47-28.bwa.stderr
    jobid: 13
    wildcards: sampleBAB=Pfeiffer2

Submitted DRMAA job (jobid 8712853)
Finished job 15.
5 of 20 steps (25%) done
Finished job 14.
6 of 20 steps (30%) done

rule bamALIGN_bwa:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, output/fastq/Pfeiffer3.1.fastq.gz, output/fastq/Pfeiffer3.2.fastq.gz
    output: output/bam/Pfeiffer3_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-05.19-47-28.samtools.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-05.19-47-28.bwa.stderr
    jobid: 12
    wildcards: sampleBAB=Pfeiffer3

Submitted DRMAA job (jobid 8712919)
Finished job 13.
7 of 20 steps (35%) done

rule sortBAM_biobambam:
    input: output/bam/Pfeiffer2_Aligned.out.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-05.19-47-28.bamsort.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-05.19-47-28.samtools.stderr
    jobid: 11
    wildcards: pathSBB=output/bam, sampleSBB=Pfeiffer2_Aligned.out

Submitted DRMAA job (jobid 8713185)
Finished job 12.
8 of 20 steps (40%) done

rule sortBAM_biobambam:
    input: output/bam/Pfeiffer3_Aligned.out.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-05.19-47-28.bamsort.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-05.19-47-28.samtools.stderr
    jobid: 10
    wildcards: pathSBB=output/bam, sampleSBB=Pfeiffer3_Aligned.out

Submitted DRMAA job (jobid 8713198)
Finished job 11.
9 of 20 steps (45%) done

rule filteredBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer2_Aligned.out_sorted.2017-07-05.19-47-28.stderr
    jobid: 9
    wildcards: pathFB=output/bam, sampleFB=Pfeiffer2_Aligned.out_sorted

Submitted DRMAA job (jobid 8713407)
Finished job 10.
10 of 20 steps (50%) done

rule filteredBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer3_Aligned.out_sorted.2017-07-05.19-47-28.stderr
    jobid: 8
    wildcards: pathFB=output/bam, sampleFB=Pfeiffer3_Aligned.out_sorted

Submitted DRMAA job (jobid 8713432)
Finished job 9.
11 of 20 steps (55%) done

rule markdupBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    output: output/metrics/Pfeiffer2_Aligned.out_sorted_filtered.dup_metrics, output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer2_Aligned.out_sorted_filtered.2017-07-05.19-47-28.biobammarkdup.stderr
    jobid: 7
    wildcards: outputDIR=output, sampleMDB=Pfeiffer2_Aligned.out_sorted_filtered

Submitted DRMAA job (jobid 8713510)
Finished job 8.
12 of 20 steps (60%) done

rule markdupBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    output: output/metrics/Pfeiffer3_Aligned.out_sorted_filtered.dup_metrics, output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer3_Aligned.out_sorted_filtered.2017-07-05.19-47-28.biobammarkdup.stderr
    jobid: 6
    wildcards: outputDIR=output, sampleMDB=Pfeiffer3_Aligned.out_sorted_filtered

Submitted DRMAA job (jobid 8713528)
Finished job 7.
13 of 20 steps (65%) done

 + 2-mileup2vcf_pairUNSPLIT.md
rule indexBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam.bai
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer2.2017-07-05.19-47-28.stderr
    jobid: 5
    wildcards: outputDIR=output, sampleIB=Pfeiffer2

Submitted DRMAA job (jobid 8713572)
Finished job 6.
14 of 20 steps (70%) done

rule indexBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam.bai
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer3.2017-07-05.19-47-28.stderr
    jobid: 4
    wildcards: outputDIR=output, sampleIB=Pfeiffer3

Submitted DRMAA job (jobid 8713578)
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/Pfeiffer3.bam.bai. Your Python build does not support it.
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/Pfeiffer3.bam. Your Python build does not support it.
Finished job 4.
15 of 20 steps (75%) done

rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-47-28.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.19-47-28.mpileup.stderr
    jobid: 2
    wildcards: chrB2M=, sampleB2M=Pfeiffer3

Submitted DRMAA job (jobid 8713589)
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/Pfeiffer2.bam.bai. Your Python build does not support it.
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/Pfeiffer2.bam. Your Python build does not support it.
Finished job 5.
16 of 20 steps (80%) done

rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-47-28.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.19-47-28.mpileup.stderr
    jobid: 3
    wildcards: chrB2M=, sampleB2M=Pfeiffer2

Submitted DRMAA job (jobid 8713606)
Finished job 3.
17 of 20 steps (85%) done
Finished job 2.
18 of 20 steps (90%) done

rule mpileup2vcf_pair:
    input: output/mpileup/Pfeiffer2.mpileup, output/mpileup/Pfeiffer3.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_Pfeiffer2.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_Pfeiffer2.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_Pfeiffer2_chr.SNPandINDEL.2017-07-05.19-47-28.stderr
    jobid: 1
    wildcards: sampletMPU2VCFP=Pfeiffer3, samplenMPU2VCFP=Pfeiffer2, chrMPU2VCFP=

Submitted DRMAA job (jobid 8713675)
Finished job 1.
19 of 20 steps (95%) done

localrule all:
    input: output/vcfGenUtil_varScan/Pfeiffer3_Pfeiffer2.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_Pfeiffer2.varScan.indel.vcf
    jobid: 0

Finished job 0.
20 of 20 steps (100%) done
```
