# 6-namesortBAM_samtools
This pipeline is to exemplify alternative version of namesortBAM. We will be using the
non-defualt version which performs the sorting using 'samtools'.

## Setting up the: Snakefile
Users must set the following submodule "call via" input requirements:

 * namesortBAM

## Setting up the: YAML
Users must set the following "input/config.yaml" variables:

 * (Line 41) SoftwareChoiceFLAG_namesortBAM = samtools

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
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-10.11-28-34.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-10.11-28-34.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-10.11-28-34.namesort.stderr
    jobid: 22
    wildcards: sampleB2FP=Pfeiffer3


rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer2.bam
    output: output/fastq/Pfeiffer2.1.fastq, output/fastq/Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-10.11-28-34.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-10.11-28-34.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-10.11-28-34.namesort.stderr
    jobid: 21
    wildcards: sampleB2FP=Pfeiffer2


rule fastq2GZ:
    input: output/fastq/Pfeiffer2.1.fastq
    output: output/fastq/Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.1.2017-07-10.11-28-34.stderr
    jobid: 17
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer2.1


rule fastq2GZ:
    input: output/fastq/Pfeiffer3.2.fastq
    output: output/fastq/Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.2.2017-07-10.11-28-34.stderr
    jobid: 19
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer3.2


rule fastq2GZ:
    input: output/fastq/Pfeiffer3.1.fastq
    output: output/fastq/Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.1.2017-07-10.11-28-34.stderr
    jobid: 20
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer3.1


rule fastq2GZ:
    input: output/fastq/Pfeiffer2.2.fastq
    output: output/fastq/Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.2.2017-07-10.11-28-34.stderr
    jobid: 18
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer2.2


rule bamALIGN_bwa:
    input: output/fastq/Pfeiffer2.1.fastq.gz, output/fastq/Pfeiffer2.2.fastq.gz, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/bam/Pfeiffer2_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-10.11-28-34.samtools.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-10.11-28-34.bwa.stderr
    jobid: 15
    wildcards: sampleBAB=Pfeiffer2


rule bamALIGN_bwa:
    input: output/fastq/Pfeiffer3.1.fastq.gz, output/fastq/Pfeiffer3.2.fastq.gz, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/bam/Pfeiffer3_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-10.11-28-34.samtools.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-10.11-28-34.bwa.stderr
    jobid: 16
    wildcards: sampleBAB=Pfeiffer3


rule namesortBAM_samtools:
    input: output/bam/Pfeiffer3_Aligned.out.bam
    output: output/bam/Pfeiffer3_Aligned.out_namesort.bam
    log: log/bam/namesortBAM_samtools/namesortBAM_samtools_Pfeiffer3_Aligned.out.2017-07-10.11-28-34.samtools.stderr
    jobid: 14
    wildcards: pathNSBS=output/bam, sampleNSBS=Pfeiffer3_Aligned.out


rule namesortBAM_samtools:
    input: output/bam/Pfeiffer2_Aligned.out.bam
    output: output/bam/Pfeiffer2_Aligned.out_namesort.bam
    log: log/bam/namesortBAM_samtools/namesortBAM_samtools_Pfeiffer2_Aligned.out.2017-07-10.11-28-34.samtools.stderr
    jobid: 13
    wildcards: pathNSBS=output/bam, sampleNSBS=Pfeiffer2_Aligned.out


rule sortBAM_biobambam:
    input: output/bam/Pfeiffer2_Aligned.out_namesort.bam
    output: output/bam/Pfeiffer2_Aligned.out_namesort_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out_namesort.2017-07-10.11-28-34.bamsort.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out_namesort.2017-07-10.11-28-34.samtools.stderr
    jobid: 11
    wildcards: sampleSBB=Pfeiffer2_Aligned.out_namesort, pathSBB=output/bam


rule sortBAM_biobambam:
    input: output/bam/Pfeiffer3_Aligned.out_namesort.bam
    output: output/bam/Pfeiffer3_Aligned.out_namesort_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out_namesort.2017-07-10.11-28-34.bamsort.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out_namesort.2017-07-10.11-28-34.samtools.stderr
    jobid: 12
    wildcards: sampleSBB=Pfeiffer3_Aligned.out_namesort, pathSBB=output/bam


rule cleanBAM:
    input: output/bam/Pfeiffer2_Aligned.out_namesort_sorted.bam
    output: output/bam/Pfeiffer2_Aligned.out_namesort_sorted_clean.bam
    log: log/bamUtil/cleanBAM/cleaBAM_Pfeiffer2_Aligned.out_namesort_sorted.2017-07-10.11-28-34.stderr
    jobid: 9
    wildcards: sampleCB=Pfeiffer2_Aligned.out_namesort_sorted, pathCB=output/bam


rule cleanBAM:
    input: output/bam/Pfeiffer3_Aligned.out_namesort_sorted.bam
    output: output/bam/Pfeiffer3_Aligned.out_namesort_sorted_clean.bam
    log: log/bamUtil/cleanBAM/cleaBAM_Pfeiffer3_Aligned.out_namesort_sorted.2017-07-10.11-28-34.stderr
    jobid: 10
    wildcards: sampleCB=Pfeiffer3_Aligned.out_namesort_sorted, pathCB=output/bam


rule fixmateBAM:
    input: output/bam/Pfeiffer2_Aligned.out_namesort_sorted_clean.bam
    output: output/bam/Pfeiffer2_Aligned.out_namesort_sorted_clean_fixmate.bam
    log: log/bamUtil/fixmateBAM/fixmateBAM_Pfeiffer2_Aligned.out_namesort_sorted_clean.2017-07-10.11-28-34.stderr
    jobid: 7
    wildcards: pathFMB=output/bam, sampleFMB=Pfeiffer2_Aligned.out_namesort_sorted_clean


rule fixmateBAM:
    input: output/bam/Pfeiffer3_Aligned.out_namesort_sorted_clean.bam
    output: output/bam/Pfeiffer3_Aligned.out_namesort_sorted_clean_fixmate.bam
    log: log/bamUtil/fixmateBAM/fixmateBAM_Pfeiffer3_Aligned.out_namesort_sorted_clean.2017-07-10.11-28-34.stderr
    jobid: 8
    wildcards: pathFMB=output/bam, sampleFMB=Pfeiffer3_Aligned.out_namesort_sorted_clean


rule rmdupBAM:
    input: output/bam/Pfeiffer3_Aligned.out_namesort_sorted_clean_fixmate.bam
    output: output/bam/Pfeiffer3_Aligned.out_namesort_sorted_clean_fixmate_rmdup.bam
    log: log/bamUtil/rmdupBAM/rmdupBAM_Pfeiffer3_Aligned.out_namesort_sorted_clean_fixmate.2017-07-10.11-28-34.stderr
    jobid: 6
    wildcards: sampleRDB=Pfeiffer3_Aligned.out_namesort_sorted_clean_fixmate, pathRDB=output/bam


rule rmdupBAM:
    input: output/bam/Pfeiffer2_Aligned.out_namesort_sorted_clean_fixmate.bam
    output: output/bam/Pfeiffer2_Aligned.out_namesort_sorted_clean_fixmate_rmdup.bam
    log: log/bamUtil/rmdupBAM/rmdupBAM_Pfeiffer2_Aligned.out_namesort_sorted_clean_fixmate.2017-07-10.11-28-34.stderr
    jobid: 5
    wildcards: sampleRDB=Pfeiffer2_Aligned.out_namesort_sorted_clean_fixmate, pathRDB=output/bam


rule filteredBAM:
    input: output/bam/Pfeiffer2_Aligned.out_namesort_sorted_clean_fixmate_rmdup.bam
    output: output/bam/Pfeiffer2_Aligned.out_namesort_sorted_clean_fixmate_rmdup_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer2_Aligned.out_namesort_sorted_clean_fixmate_rmdup.2017-07-10.11-28-34.stderr
    jobid: 3
    wildcards: sampleFB=Pfeiffer2_Aligned.out_namesort_sorted_clean_fixmate_rmdup, pathFB=output/bam


rule filteredBAM:
    input: output/bam/Pfeiffer3_Aligned.out_namesort_sorted_clean_fixmate_rmdup.bam
    output: output/bam/Pfeiffer3_Aligned.out_namesort_sorted_clean_fixmate_rmdup_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer3_Aligned.out_namesort_sorted_clean_fixmate_rmdup.2017-07-10.11-28-34.stderr
    jobid: 4
    wildcards: sampleFB=Pfeiffer3_Aligned.out_namesort_sorted_clean_fixmate_rmdup, pathFB=output/bam


rule indexBAM:
    input: output/bam/Pfeiffer2_Aligned.out_namesort_sorted_clean_fixmate_rmdup_filtered.bam
    output: output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2_Aligned.out_namesort_sorted_clean_fixmate_rmdup_filtered.bam.bai
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer2.2017-07-10.11-28-34.stderr
    jobid: 1
    wildcards: sampleIB=Pfeiffer2, outputDIR=output


rule indexBAM:
    input: output/bam/Pfeiffer3_Aligned.out_namesort_sorted_clean_fixmate_rmdup_filtered.bam
    output: output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3_Aligned.out_namesort_sorted_clean_fixmate_rmdup_filtered.bam.bai
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer3.2017-07-10.11-28-34.stderr
    jobid: 2
    wildcards: sampleIB=Pfeiffer3, outputDIR=output


localrule all:
    input: output/bam/Pfeiffer2_Aligned.out_namesort_sorted_clean_fixmate_rmdup_filtered.bam.bai, output/bam/Pfeiffer3_Aligned.out_namesort_sorted_clean_fixmate_rmdup_filtered.bam.bai
    jobid: 0

Job counts:
	count	jobs
	1	all
	2	bam2fastq_picard
	2	bamALIGN_bwa
	2	cleanBAM
	4	fastq2GZ
	2	filteredBAM
	2	fixmateBAM
	2	indexBAM
	2	namesortBAM_samtools
	2	rmdupBAM
	2	sortBAM_biobambam
	23
```

## Snakemake cluster run output:
```
Provided cluster nodes: 100
Job counts:
    count    jobs
    1    all
    2    bam2fastq_picard
    2    bamALIGN_bwa
    2    cleanBAM
    4    fastq2GZ
    2    filteredBAM
    2    fixmateBAM
    2    indexBAM
    2    namesortBAM_samtools
    2    rmdupBAM
    2    sortBAM_biobambam
    23

rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer2.bam
    output: output/fastq/Pfeiffer2.1.fastq, output/fastq/Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-10.11-28-39.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-10.11-28-39.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-10.11-28-39.stderr
    jobid: 21
    wildcards: sampleB2FP=Pfeiffer2

Submitted DRMAA job (jobid 8877545)

rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer3.bam
    output: output/fastq/Pfeiffer3.1.fastq, output/fastq/Pfeiffer3.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-10.11-28-39.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-10.11-28-39.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-10.11-28-39.stderr
    jobid: 22
    wildcards: sampleB2FP=Pfeiffer3

Submitted DRMAA job (jobid 8877546)
Finished job 21.
1 of 23 steps (4%) done

rule fastq2GZ:
    input: output/fastq/Pfeiffer2.1.fastq
    output: output/fastq/Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.1.2017-07-10.11-28-39.stderr
    jobid: 17
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer2.1

Submitted DRMAA job (jobid 8877551)

rule fastq2GZ:
    input: output/fastq/Pfeiffer2.2.fastq
    output: output/fastq/Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.2.2017-07-10.11-28-39.stderr
    jobid: 18
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer2.2

Submitted DRMAA job (jobid 8877552)
Finished job 22.
2 of 23 steps (9%) done

rule fastq2GZ:
    input: output/fastq/Pfeiffer3.2.fastq
    output: output/fastq/Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.2.2017-07-10.11-28-39.stderr
    jobid: 19
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer3.2

Submitted DRMAA job (jobid 8877553)

rule fastq2GZ:
    input: output/fastq/Pfeiffer3.1.fastq
    output: output/fastq/Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.1.2017-07-10.11-28-39.stderr
    jobid: 20
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer3.1

Submitted DRMAA job (jobid 8877554)
Finished job 17.
3 of 23 steps (13%) done
Finished job 18.
4 of 23 steps (17%) done

rule bamALIGN_bwa:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, output/fastq/Pfeiffer2.1.fastq.gz, output/fastq/Pfeiffer2.2.fastq.gz, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/bam/Pfeiffer2_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-10.11-28-39.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-10.11-28-39.samtools.stderr
    jobid: 15
    wildcards: sampleBAB=Pfeiffer2

Submitted DRMAA job (jobid 8877555)
Finished job 19.
5 of 23 steps (22%) done
Finished job 20.
6 of 23 steps (26%) done

rule bamALIGN_bwa:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, output/fastq/Pfeiffer3.1.fastq.gz, output/fastq/Pfeiffer3.2.fastq.gz, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/bam/Pfeiffer3_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-10.11-28-39.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-10.11-28-39.samtools.stderr
    jobid: 16
    wildcards: sampleBAB=Pfeiffer3

Submitted DRMAA job (jobid 8877561)
Finished job 15.
7 of 23 steps (30%) done

rule namesortBAM_samtools:
    input: output/bam/Pfeiffer2_Aligned.out.bam
    output: output/bam/Pfeiffer2_Aligned.out_namesort.bam
    log: log/bam/namesortBAM_samtools/namesortBAM_samtools_Pfeiffer2_Aligned.out.2017-07-10.11-28-39.samtools.stderr
    jobid: 13
    wildcards: sampleNSBS=Pfeiffer2_Aligned.out, pathNSBS=output/bam

Submitted DRMAA job (jobid 8877562)
Finished job 16.
8 of 23 steps (35%) done

rule namesortBAM_samtools:
    input: output/bam/Pfeiffer3_Aligned.out.bam
    output: output/bam/Pfeiffer3_Aligned.out_namesort.bam
    log: log/bam/namesortBAM_samtools/namesortBAM_samtools_Pfeiffer3_Aligned.out.2017-07-10.11-28-39.samtools.stderr
    jobid: 14
    wildcards: sampleNSBS=Pfeiffer3_Aligned.out, pathNSBS=output/bam

Submitted DRMAA job (jobid 8877565)
Finished job 13.
9 of 23 steps (39%) done

rule sortBAM_biobambam:
    input: output/bam/Pfeiffer2_Aligned.out_namesort.bam
    output: output/bam/Pfeiffer2_Aligned.out_namesort_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out_namesort.2017-07-10.11-28-39.samtools.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out_namesort.2017-07-10.11-28-39.bamsort.stderr
    jobid: 11
    wildcards: pathSBB=output/bam, sampleSBB=Pfeiffer2_Aligned.out_namesort

Submitted DRMAA job (jobid 8877566)
Finished job 14.
10 of 23 steps (43%) done

rule sortBAM_biobambam:
    input: output/bam/Pfeiffer3_Aligned.out_namesort.bam
    output: output/bam/Pfeiffer3_Aligned.out_namesort_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out_namesort.2017-07-10.11-28-39.samtools.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out_namesort.2017-07-10.11-28-39.bamsort.stderr
    jobid: 12
    wildcards: pathSBB=output/bam, sampleSBB=Pfeiffer3_Aligned.out_namesort

Submitted DRMAA job (jobid 8877567)
Finished job 11.
11 of 23 steps (48%) done

rule cleanBAM:
    input: output/bam/Pfeiffer2_Aligned.out_namesort_sorted.bam
    output: output/bam/Pfeiffer2_Aligned.out_namesort_sorted_clean.bam
    log: log/bamUtil/cleanBAM/cleaBAM_Pfeiffer2_Aligned.out_namesort_sorted.2017-07-10.11-28-39.stderr
    jobid: 9
    wildcards: sampleCB=Pfeiffer2_Aligned.out_namesort_sorted, pathCB=output/bam

Submitted DRMAA job (jobid 8877568)
Finished job 12.
12 of 23 steps (52%) done

rule cleanBAM:
    input: output/bam/Pfeiffer3_Aligned.out_namesort_sorted.bam
    output: output/bam/Pfeiffer3_Aligned.out_namesort_sorted_clean.bam
    log: log/bamUtil/cleanBAM/cleaBAM_Pfeiffer3_Aligned.out_namesort_sorted.2017-07-10.11-28-39.stderr
    jobid: 10
    wildcards: sampleCB=Pfeiffer3_Aligned.out_namesort_sorted, pathCB=output/bam

Submitted DRMAA job (jobid 8877569)
Finished job 9.
13 of 23 steps (57%) done

rule fixmateBAM:
    input: output/bam/Pfeiffer2_Aligned.out_namesort_sorted_clean.bam
    output: output/bam/Pfeiffer2_Aligned.out_namesort_sorted_clean_fixmate.bam
    log: log/bamUtil/fixmateBAM/fixmateBAM_Pfeiffer2_Aligned.out_namesort_sorted_clean.2017-07-10.11-28-39.stderr
    jobid: 7
    wildcards: sampleFMB=Pfeiffer2_Aligned.out_namesort_sorted_clean, pathFMB=output/bam

Submitted DRMAA job (jobid 8877570)
Finished job 10.
14 of 23 steps (61%) done

rule fixmateBAM:
    input: output/bam/Pfeiffer3_Aligned.out_namesort_sorted_clean.bam
    output: output/bam/Pfeiffer3_Aligned.out_namesort_sorted_clean_fixmate.bam
    log: log/bamUtil/fixmateBAM/fixmateBAM_Pfeiffer3_Aligned.out_namesort_sorted_clean.2017-07-10.11-28-39.stderr
    jobid: 8
    wildcards: sampleFMB=Pfeiffer3_Aligned.out_namesort_sorted_clean, pathFMB=output/bam

Submitted DRMAA job (jobid 8877571)
Finished job 7.
15 of 23 steps (65%) done

rule rmdupBAM:
    input: output/bam/Pfeiffer2_Aligned.out_namesort_sorted_clean_fixmate.bam
    output: output/bam/Pfeiffer2_Aligned.out_namesort_sorted_clean_fixmate_rmdup.bam
    log: log/bamUtil/rmdupBAM/rmdupBAM_Pfeiffer2_Aligned.out_namesort_sorted_clean_fixmate.2017-07-10.11-28-39.stderr
    jobid: 5
    wildcards: pathRDB=output/bam, sampleRDB=Pfeiffer2_Aligned.out_namesort_sorted_clean_fixmate

Submitted DRMAA job (jobid 8877572)
Finished job 5.
16 of 23 steps (70%) done

rule filteredBAM:
    input: output/bam/Pfeiffer2_Aligned.out_namesort_sorted_clean_fixmate_rmdup.bam
    output: output/bam/Pfeiffer2_Aligned.out_namesort_sorted_clean_fixmate_rmdup_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer2_Aligned.out_namesort_sorted_clean_fixmate_rmdup.2017-07-10.11-28-39.stderr
    jobid: 3
    wildcards: pathFB=output/bam, sampleFB=Pfeiffer2_Aligned.out_namesort_sorted_clean_fixmate_rmdup

Submitted DRMAA job (jobid 8877573)
Finished job 8.
17 of 23 steps (74%) done

rule rmdupBAM:
    input: output/bam/Pfeiffer3_Aligned.out_namesort_sorted_clean_fixmate.bam
    output: output/bam/Pfeiffer3_Aligned.out_namesort_sorted_clean_fixmate_rmdup.bam
    log: log/bamUtil/rmdupBAM/rmdupBAM_Pfeiffer3_Aligned.out_namesort_sorted_clean_fixmate.2017-07-10.11-28-39.stderr
    jobid: 6
    wildcards: pathRDB=output/bam, sampleRDB=Pfeiffer3_Aligned.out_namesort_sorted_clean_fixmate

Submitted DRMAA job (jobid 8877574)
Finished job 6.
18 of 23 steps (78%) done

rule filteredBAM:
    input: output/bam/Pfeiffer3_Aligned.out_namesort_sorted_clean_fixmate_rmdup.bam
    output: output/bam/Pfeiffer3_Aligned.out_namesort_sorted_clean_fixmate_rmdup_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer3_Aligned.out_namesort_sorted_clean_fixmate_rmdup.2017-07-10.11-28-39.stderr
    jobid: 4
    wildcards: pathFB=output/bam, sampleFB=Pfeiffer3_Aligned.out_namesort_sorted_clean_fixmate_rmdup

Submitted DRMAA job (jobid 8877575)
Finished job 3.
19 of 23 steps (83%) done

rule indexBAM:
    input: output/bam/Pfeiffer2_Aligned.out_namesort_sorted_clean_fixmate_rmdup_filtered.bam
    output: output/bam/Pfeiffer2_Aligned.out_namesort_sorted_clean_fixmate_rmdup_filtered.bam.bai, output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer2.2017-07-10.11-28-39.stderr
    jobid: 1
    wildcards: outputDIR=output, sampleIB=Pfeiffer2

Submitted DRMAA job (jobid 8877576)
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/Pfeiffer2.bam. Your Python build does not support it.
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/Pfeiffer2.bam.bai. Your Python build does not support it.
Finished job 1.
20 of 23 steps (87%) done
Finished job 4.
21 of 23 steps (91%) done

rule indexBAM:
    input: output/bam/Pfeiffer3_Aligned.out_namesort_sorted_clean_fixmate_rmdup_filtered.bam
    output: output/bam/Pfeiffer3_Aligned.out_namesort_sorted_clean_fixmate_rmdup_filtered.bam.bai, output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer3.2017-07-10.11-28-39.stderr
    jobid: 2
    wildcards: outputDIR=output, sampleIB=Pfeiffer3

Submitted DRMAA job (jobid 8877577)
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/Pfeiffer3.bam. Your Python build does not support it.
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/Pfeiffer3.bam.bai. Your Python build does not support it.
Finished job 2.
22 of 23 steps (96%) done

localrule all:
    input: output/bam/Pfeiffer2_Aligned.out_namesort_sorted_clean_fixmate_rmdup_filtered.bam.bai, output/bam/Pfeiffer3_Aligned.out_namesort_sorted_clean_fixmate_rmdup_filtered.bam.bai
    jobid: 0

Finished job 0.
23 of 23 steps (100%) done

real    6m10.067s
user    0m1.309s
sys    0m0.269s
```
