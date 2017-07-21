# 2-namesortBAM_cleanBAM_fixmateBAM_rmdupBAM
This pipeline is to exemplify the remaining processing submodules in this module.
Specifically with respect to namesortBAM, we will be using the default version
which performs the sorting using 'biobambam'.

## Setting up the: Snakefile
Users must set the following submodule "call via" input requirements:

 * indexBAM 

## Setting up the: YAML
Users must set the following "input/config.yaml" variables:

 * (Line 49) bamMergeSuffix: _Aligned.out_namesort_sorted_clean_fixmate_rmdup_filtered
 * (Line 55) fileTag: _Aligned.out_namesort_sorted_clean_fixmate_rmdup_filtered

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
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-05.09-07-26.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-05.09-07-26.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-05.09-07-26.stderr
    jobid: 22
    wildcards: sampleB2FP=Pfeiffer3


rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer2.bam
    output: output/fastq/Pfeiffer2.1.fastq, output/fastq/Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-05.09-07-26.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-05.09-07-26.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-05.09-07-26.stderr
    jobid: 21
    wildcards: sampleB2FP=Pfeiffer2


rule fastq2GZ:
    input: output/fastq/Pfeiffer3.1.fastq
    output: output/fastq/Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.1.2017-07-05.09-07-25.stderr
    jobid: 19
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer3.1


rule fastq2GZ:
    input: output/fastq/Pfeiffer2.2.fastq
    output: output/fastq/Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.2.2017-07-05.09-07-25.stderr
    jobid: 17
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer2.2


rule fastq2GZ:
    input: output/fastq/Pfeiffer3.2.fastq
    output: output/fastq/Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.2.2017-07-05.09-07-25.stderr
    jobid: 20
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer3.2


rule fastq2GZ:
    input: output/fastq/Pfeiffer2.1.fastq
    output: output/fastq/Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.1.2017-07-05.09-07-25.stderr
    jobid: 18
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer2.1


rule bamALIGN_bwa:
    input: output/fastq/Pfeiffer3.1.fastq.gz, output/fastq/Pfeiffer3.2.fastq.gz, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa
    output: output/bam/Pfeiffer3_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-05.09-07-25.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-05.09-07-25.samtools.stderr
    jobid: 16
    wildcards: sampleBAB=Pfeiffer3


rule bamALIGN_bwa:
    input: output/fastq/Pfeiffer2.1.fastq.gz, output/fastq/Pfeiffer2.2.fastq.gz, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa
    output: output/bam/Pfeiffer2_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-05.09-07-25.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-05.09-07-25.samtools.stderr
    jobid: 15
    wildcards: sampleBAB=Pfeiffer2


rule namesortBAM_biobambam:
    input: output/bam/Pfeiffer3_Aligned.out.bam
    output: output/bam/Pfeiffer3_Aligned.out_namesort.bam
    log: log/bam/namesortBAM_biobambam/namesortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-05.09-07-25.bamsort.stderr, log/bam/namesortBAM_biobambam/namesortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-05.09-07-25.samtools.stderr
    jobid: 14
    wildcards: sampleNSBB=Pfeiffer3_Aligned.out, pathNSBB=output/bam


rule namesortBAM_biobambam:
    input: output/bam/Pfeiffer2_Aligned.out.bam
    output: output/bam/Pfeiffer2_Aligned.out_namesort.bam
    log: log/bam/namesortBAM_biobambam/namesortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-05.09-07-25.bamsort.stderr, log/bam/namesortBAM_biobambam/namesortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-05.09-07-25.samtools.stderr
    jobid: 13
    wildcards: sampleNSBB=Pfeiffer2_Aligned.out, pathNSBB=output/bam


rule cleanBAM:
    input: output/bam/Pfeiffer3_Aligned.out_namesort.bam
    output: output/bam/Pfeiffer3_Aligned.out_namesort_clean.bam
    log: log/bam/cleanBAM/cleaBAM_Pfeiffer3_Aligned.out_namesort.2017-07-05.09-07-25.stderr
    jobid: 12
    wildcards: pathCB=output/bam, sampleCB=Pfeiffer3_Aligned.out_namesort


rule cleanBAM:
    input: output/bam/Pfeiffer2_Aligned.out_namesort.bam
    output: output/bam/Pfeiffer2_Aligned.out_namesort_clean.bam
    log: log/bam/cleanBAM/cleaBAM_Pfeiffer2_Aligned.out_namesort.2017-07-05.09-07-25.stderr
    jobid: 11
    wildcards: pathCB=output/bam, sampleCB=Pfeiffer2_Aligned.out_namesort


rule fixmateBAM:
    input: output/bam/Pfeiffer3_Aligned.out_namesort_clean.bam
    output: output/bam/Pfeiffer3_Aligned.out_namesort_clean_fixmate.bam
    log: log/bam/fixmateBAM/fixmateBAM_Pfeiffer3_Aligned.out_namesort_clean.2017-07-05.09-07-25.stderr
    jobid: 10
    wildcards: pathFMB=output/bam, sampleFMB=Pfeiffer3_Aligned.out_namesort_clean


rule fixmateBAM:
    input: output/bam/Pfeiffer2_Aligned.out_namesort_clean.bam
    output: output/bam/Pfeiffer2_Aligned.out_namesort_clean_fixmate.bam
    log: log/bam/fixmateBAM/fixmateBAM_Pfeiffer2_Aligned.out_namesort_clean.2017-07-05.09-07-25.stderr
    jobid: 9
    wildcards: pathFMB=output/bam, sampleFMB=Pfeiffer2_Aligned.out_namesort_clean


rule rmdupBAM:
    input: output/bam/Pfeiffer3_Aligned.out_namesort_clean_fixmate.bam
    output: output/bam/Pfeiffer3_Aligned.out_namesort_clean_fixmate_rmdup.bam
    log: log/bam/rmdupBAM/rmdupBAM_Pfeiffer3_Aligned.out_namesort_clean_fixmate.2017-07-05.09-07-25.stderr
    jobid: 8
    wildcards: pathRDB=output/bam, sampleRDB=Pfeiffer3_Aligned.out_namesort_clean_fixmate


rule rmdupBAM:
    input: output/bam/Pfeiffer2_Aligned.out_namesort_clean_fixmate.bam
    output: output/bam/Pfeiffer2_Aligned.out_namesort_clean_fixmate_rmdup.bam
    log: log/bam/rmdupBAM/rmdupBAM_Pfeiffer2_Aligned.out_namesort_clean_fixmate.2017-07-05.09-07-25.stderr
    jobid: 7
    wildcards: pathRDB=output/bam, sampleRDB=Pfeiffer2_Aligned.out_namesort_clean_fixmate


rule sortBAM_biobambam:
    input: output/bam/Pfeiffer3_Aligned.out_namesort_clean_fixmate_rmdup.bam
    output: output/bam/Pfeiffer3_Aligned.out_namesort_clean_fixmate_rmdup_sorted.bam
    log: log/bamGen/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out_namesort_clean_fixmate_rmdup.2017-07-05.09-07-25.bamsort.stderr, log/bamGen/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out_namesort_clean_fixmate_rmdup.2017-07-05.09-07-25.samtools.stderr
    jobid: 6
    wildcards: pathSBB=output/bam, sampleSBB=Pfeiffer3_Aligned.out_namesort_clean_fixmate_rmdup


rule sortBAM_biobambam:
    input: output/bam/Pfeiffer2_Aligned.out_namesort_clean_fixmate_rmdup.bam
    output: output/bam/Pfeiffer2_Aligned.out_namesort_clean_fixmate_rmdup_sorted.bam
    log: log/bamGen/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out_namesort_clean_fixmate_rmdup.2017-07-05.09-07-25.bamsort.stderr, log/bamGen/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out_namesort_clean_fixmate_rmdup.2017-07-05.09-07-25.samtools.stderr
    jobid: 5
    wildcards: pathSBB=output/bam, sampleSBB=Pfeiffer2_Aligned.out_namesort_clean_fixmate_rmdup


rule filteredBAM:
    input: output/bam/Pfeiffer3_Aligned.out_namesort_clean_fixmate_rmdup_sorted.bam
    output: output/bam/Pfeiffer3_Aligned.out_namesort_clean_fixmate_rmdup_sorted_filtered.bam
    log: log/bam/filteredBAM/filteredBAM_Pfeiffer3_Aligned.out_namesort_clean_fixmate_rmdup_sorted.2017-07-05.09-07-25.stderr
    jobid: 4
    wildcards: pathFB=output/bam, sampleFB=Pfeiffer3_Aligned.out_namesort_clean_fixmate_rmdup_sorted


rule filteredBAM:
    input: output/bam/Pfeiffer2_Aligned.out_namesort_clean_fixmate_rmdup_sorted.bam
    output: output/bam/Pfeiffer2_Aligned.out_namesort_clean_fixmate_rmdup_sorted_filtered.bam
    log: log/bam/filteredBAM/filteredBAM_Pfeiffer2_Aligned.out_namesort_clean_fixmate_rmdup_sorted.2017-07-05.09-07-25.stderr
    jobid: 3
    wildcards: pathFB=output/bam, sampleFB=Pfeiffer2_Aligned.out_namesort_clean_fixmate_rmdup_sorted


rule indexBAM:
    input: output/bam/Pfeiffer2_Aligned.out_namesort_clean_fixmate_rmdup_sorted_filtered.bam
    output: output/bam/Pfeiffer2_Aligned.out_namesort_clean_fixmate_rmdup_sorted_filtered.bam.bai, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    log: log/bam/indexBAM/indexBAM_Pfeiffer2.2017-07-05.09-07-25.stderr
    jobid: 1
    wildcards: outputDIR=output, sampleIB=Pfeiffer2


rule indexBAM:
    input: output/bam/Pfeiffer3_Aligned.out_namesort_clean_fixmate_rmdup_sorted_filtered.bam
    output: output/bam/Pfeiffer3_Aligned.out_namesort_clean_fixmate_rmdup_sorted_filtered.bam.bai, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    log: log/bam/indexBAM/indexBAM_Pfeiffer3.2017-07-05.09-07-25.stderr
    jobid: 2
    wildcards: outputDIR=output, sampleIB=Pfeiffer3


localrule all:
    input: output/bam/Pfeiffer2_Aligned.out_namesort_clean_fixmate_rmdup_sorted_filtered.bam.bai, output/bam/Pfeiffer3_Aligned.out_namesort_clean_fixmate_rmdup_sorted_filtered.bam.bai
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
	2	namesortBAM_biobambam
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
    2    namesortBAM_biobambam
    2    rmdupBAM
    2    sortBAM_biobambam
    23

rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer2.bam
    output: output/fastq/Pfeiffer2.1.fastq, output/fastq/Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-05.09-07-28.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-05.09-07-28.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-05.09-07-28.namesort.stderr
    jobid: 22
    wildcards: sampleB2FP=Pfeiffer2

Submitted DRMAA job (jobid 8684069)

rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer3.bam
    output: output/fastq/Pfeiffer3.1.fastq, output/fastq/Pfeiffer3.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-05.09-07-28.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-05.09-07-28.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-05.09-07-28.namesort.stderr
    jobid: 21
    wildcards: sampleB2FP=Pfeiffer3

Submitted DRMAA job (jobid 8684070)
Finished job 22.
1 of 23 steps (4%) done

rule fastq2GZ:
    input: output/fastq/Pfeiffer2.1.fastq
    output: output/fastq/Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.1.2017-07-05.09-07-28.stderr
    jobid: 19
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer2.1

Submitted DRMAA job (jobid 8684071)

rule fastq2GZ:
    input: output/fastq/Pfeiffer2.2.fastq
    output: output/fastq/Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.2.2017-07-05.09-07-28.stderr
    jobid: 20
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer2.2

Submitted DRMAA job (jobid 8684072)
Finished job 21.
2 of 23 steps (9%) done

rule fastq2GZ:
    input: output/fastq/Pfeiffer3.2.fastq
    output: output/fastq/Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.2.2017-07-05.09-07-28.stderr
    jobid: 17
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer3.2

Submitted DRMAA job (jobid 8684073)

rule fastq2GZ:
    input: output/fastq/Pfeiffer3.1.fastq
    output: output/fastq/Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.1.2017-07-05.09-07-28.stderr
    jobid: 18
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer3.1

Submitted DRMAA job (jobid 8684074)
Finished job 17.
3 of 23 steps (13%) done
Finished job 20.
4 of 23 steps (17%) done
Finished job 18.
5 of 23 steps (22%) done

rule bamALIGN_bwa:
    input: output/fastq/Pfeiffer3.1.fastq.gz, output/fastq/Pfeiffer3.2.fastq.gz, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/bam/Pfeiffer3_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-05.09-07-28.samtools.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-05.09-07-28.bwa.stderr
    jobid: 15
    wildcards: sampleBAB=Pfeiffer3

Submitted DRMAA job (jobid 8684075)
Finished job 19.
6 of 23 steps (26%) done

rule bamALIGN_bwa:
    input: output/fastq/Pfeiffer2.1.fastq.gz, output/fastq/Pfeiffer2.2.fastq.gz, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/bam/Pfeiffer2_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-05.09-07-28.samtools.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-05.09-07-28.bwa.stderr
    jobid: 16
    wildcards: sampleBAB=Pfeiffer2

Submitted DRMAA job (jobid 8684076)
Finished job 15.
7 of 23 steps (30%) done

rule namesortBAM_biobambam:
    input: output/bam/Pfeiffer3_Aligned.out.bam
    output: output/bam/Pfeiffer3_Aligned.out_namesort.bam
    log: log/bam/namesortBAM_biobambam/namesortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-05.09-07-28.bamsort.stderr, log/bam/namesortBAM_biobambam/namesortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-05.09-07-28.samtools.stderr
    jobid: 13
    wildcards: pathNSBB=output/bam, sampleNSBB=Pfeiffer3_Aligned.out

Submitted DRMAA job (jobid 8684077)
Finished job 16.
8 of 23 steps (35%) done

rule namesortBAM_biobambam:
    input: output/bam/Pfeiffer2_Aligned.out.bam
    output: output/bam/Pfeiffer2_Aligned.out_namesort.bam
    log: log/bam/namesortBAM_biobambam/namesortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-05.09-07-28.bamsort.stderr, log/bam/namesortBAM_biobambam/namesortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-05.09-07-28.samtools.stderr
    jobid: 14
    wildcards: pathNSBB=output/bam, sampleNSBB=Pfeiffer2_Aligned.out

Submitted DRMAA job (jobid 8684078)
Finished job 14.
9 of 23 steps (39%) done

rule cleanBAM:
    input: output/bam/Pfeiffer2_Aligned.out_namesort.bam
    output: output/bam/Pfeiffer2_Aligned.out_namesort_clean.bam
    log: log/bam/cleanBAM/cleaBAM_Pfeiffer2_Aligned.out_namesort.2017-07-05.09-07-28.stderr
    jobid: 12
    wildcards: pathCB=output/bam, sampleCB=Pfeiffer2_Aligned.out_namesort

Submitted DRMAA job (jobid 8684080)
Finished job 13.
10 of 23 steps (43%) done

rule cleanBAM:
    input: output/bam/Pfeiffer3_Aligned.out_namesort.bam
    output: output/bam/Pfeiffer3_Aligned.out_namesort_clean.bam
    log: log/bam/cleanBAM/cleaBAM_Pfeiffer3_Aligned.out_namesort.2017-07-05.09-07-28.stderr
    jobid: 11
    wildcards: pathCB=output/bam, sampleCB=Pfeiffer3_Aligned.out_namesort

Submitted DRMAA job (jobid 8684081)
Finished job 12.
11 of 23 steps (48%) done

rule fixmateBAM:
    input: output/bam/Pfeiffer2_Aligned.out_namesort_clean.bam
    output: output/bam/Pfeiffer2_Aligned.out_namesort_clean_fixmate.bam
    log: log/bam/fixmateBAM/fixmateBAM_Pfeiffer2_Aligned.out_namesort_clean.2017-07-05.09-07-28.stderr
    jobid: 10
    wildcards: pathFMB=output/bam, sampleFMB=Pfeiffer2_Aligned.out_namesort_clean

Submitted DRMAA job (jobid 8684082)
Finished job 11.
12 of 23 steps (52%) done

rule fixmateBAM:
    input: output/bam/Pfeiffer3_Aligned.out_namesort_clean.bam
    output: output/bam/Pfeiffer3_Aligned.out_namesort_clean_fixmate.bam
    log: log/bam/fixmateBAM/fixmateBAM_Pfeiffer3_Aligned.out_namesort_clean.2017-07-05.09-07-28.stderr
    jobid: 9
    wildcards: pathFMB=output/bam, sampleFMB=Pfeiffer3_Aligned.out_namesort_clean

Submitted DRMAA job (jobid 8684083)
Finished job 9.
13 of 23 steps (57%) done

rule rmdupBAM:
    input: output/bam/Pfeiffer3_Aligned.out_namesort_clean_fixmate.bam
    output: output/bam/Pfeiffer3_Aligned.out_namesort_clean_fixmate_rmdup.bam
    log: log/bam/rmdupBAM/rmdupBAM_Pfeiffer3_Aligned.out_namesort_clean_fixmate.2017-07-05.09-07-28.stderr
    jobid: 7
    wildcards: pathRDB=output/bam, sampleRDB=Pfeiffer3_Aligned.out_namesort_clean_fixmate

Submitted DRMAA job (jobid 8684084)
Finished job 10.
14 of 23 steps (61%) done

rule rmdupBAM:
    input: output/bam/Pfeiffer2_Aligned.out_namesort_clean_fixmate.bam
    output: output/bam/Pfeiffer2_Aligned.out_namesort_clean_fixmate_rmdup.bam
    log: log/bam/rmdupBAM/rmdupBAM_Pfeiffer2_Aligned.out_namesort_clean_fixmate.2017-07-05.09-07-28.stderr
    jobid: 8
    wildcards: pathRDB=output/bam, sampleRDB=Pfeiffer2_Aligned.out_namesort_clean_fixmate

Submitted DRMAA job (jobid 8684085)
Finished job 8.
15 of 23 steps (65%) done

rule sortBAM_biobambam:
    input: output/bam/Pfeiffer2_Aligned.out_namesort_clean_fixmate_rmdup.bam
    output: output/bam/Pfeiffer2_Aligned.out_namesort_clean_fixmate_rmdup_sorted.bam
    log: log/bamGen/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out_namesort_clean_fixmate_rmdup.2017-07-05.09-07-28.bamsort.stderr, log/bamGen/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out_namesort_clean_fixmate_rmdup.2017-07-05.09-07-28.samtools.stderr
    jobid: 6
    wildcards: sampleSBB=Pfeiffer2_Aligned.out_namesort_clean_fixmate_rmdup, pathSBB=output/bam

Submitted DRMAA job (jobid 8684086)
Finished job 7.
16 of 23 steps (70%) done

rule sortBAM_biobambam:
    input: output/bam/Pfeiffer3_Aligned.out_namesort_clean_fixmate_rmdup.bam
    output: output/bam/Pfeiffer3_Aligned.out_namesort_clean_fixmate_rmdup_sorted.bam
    log: log/bamGen/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out_namesort_clean_fixmate_rmdup.2017-07-05.09-07-28.bamsort.stderr, log/bamGen/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out_namesort_clean_fixmate_rmdup.2017-07-05.09-07-28.samtools.stderr
    jobid: 5
    wildcards: sampleSBB=Pfeiffer3_Aligned.out_namesort_clean_fixmate_rmdup, pathSBB=output/bam

Submitted DRMAA job (jobid 8684087)
Finished job 6.
17 of 23 steps (74%) done

rule filteredBAM:
    input: output/bam/Pfeiffer2_Aligned.out_namesort_clean_fixmate_rmdup_sorted.bam
    output: output/bam/Pfeiffer2_Aligned.out_namesort_clean_fixmate_rmdup_sorted_filtered.bam
    log: log/bam/filteredBAM/filteredBAM_Pfeiffer2_Aligned.out_namesort_clean_fixmate_rmdup_sorted.2017-07-05.09-07-28.stderr
    jobid: 4
    wildcards: pathFB=output/bam, sampleFB=Pfeiffer2_Aligned.out_namesort_clean_fixmate_rmdup_sorted

Submitted DRMAA job (jobid 8684088)
Finished job 5.
18 of 23 steps (78%) done

rule filteredBAM:
    input: output/bam/Pfeiffer3_Aligned.out_namesort_clean_fixmate_rmdup_sorted.bam
    output: output/bam/Pfeiffer3_Aligned.out_namesort_clean_fixmate_rmdup_sorted_filtered.bam
    log: log/bam/filteredBAM/filteredBAM_Pfeiffer3_Aligned.out_namesort_clean_fixmate_rmdup_sorted.2017-07-05.09-07-28.stderr
    jobid: 3
    wildcards: pathFB=output/bam, sampleFB=Pfeiffer3_Aligned.out_namesort_clean_fixmate_rmdup_sorted

Submitted DRMAA job (jobid 8684089)
Finished job 4.
19 of 23 steps (83%) done

rule indexBAM:
    input: output/bam/Pfeiffer2_Aligned.out_namesort_clean_fixmate_rmdup_sorted_filtered.bam
    output: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2_Aligned.out_namesort_clean_fixmate_rmdup_sorted_filtered.bam.bai
    log: log/bam/indexBAM/indexBAM_Pfeiffer2.2017-07-05.09-07-28.stderr
    jobid: 2
    wildcards: outputDIR=output, sampleIB=Pfeiffer2

Submitted DRMAA job (jobid 8684090)
Finished job 3.
20 of 23 steps (87%) done

rule indexBAM:
    input: output/bam/Pfeiffer3_Aligned.out_namesort_clean_fixmate_rmdup_sorted_filtered.bam
    output: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3_Aligned.out_namesort_clean_fixmate_rmdup_sorted_filtered.bam.bai
    log: log/bam/indexBAM/indexBAM_Pfeiffer3.2017-07-05.09-07-28.stderr
    jobid: 1
    wildcards: outputDIR=output, sampleIB=Pfeiffer3

Submitted DRMAA job (jobid 8684091)
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/Pfeiffer2.bam. Your Python build does not support it.
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/Pfeiffer2.bam.bai. Your Python build does not support it.
Finished job 2.
21 of 23 steps (91%) done
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/Pfeiffer3.bam. Your Python build does not support it.
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/Pfeiffer3.bam.bai. Your Python build does not support it.
Finished job 1.
22 of 23 steps (96%) done

localrule all:
    input: output/bam/Pfeiffer2_Aligned.out_namesort_clean_fixmate_rmdup_sorted_filtered.bam.bai, output/bam/Pfeiffer3_Aligned.out_namesort_clean_fixmate_rmdup_sorted_filtered.bam.bai
    jobid: 0

Finished job 0.
23 of 23 steps (100%) done
```
