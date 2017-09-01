# 1-copycall_copynum_cns
This pipeline is to exemplify the default operations of this module. Please note that 
the buildPipe.py module must be set to "Pair".

## Setting up the: buildPipe.py
Users must set the following variable:

 * (Line 13) TYPE = "pair"


## Setting up the: Snakefile
Users must set the following submodule "call via" input requirements:

 * copycall
 * copynum
 * cns

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
    input: input/rawBam/Pfeiffer3.bam
    output: output/fastq/Pfeiffer3.1.fastq, output/fastq/Pfeiffer3.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-05.21-03-17.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-05.21-03-17.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-05.21-03-17.namesort.stderr
    jobid: 21
    wildcards: sampleB2FP=Pfeiffer3


rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer2.bam
    output: output/fastq/Pfeiffer2.1.fastq, output/fastq/Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-05.21-03-17.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-05.21-03-17.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-05.21-03-17.namesort.stderr
    jobid: 22
    wildcards: sampleB2FP=Pfeiffer2


rule fastq2GZ:
    input: output/fastq/Pfeiffer3.2.fastq
    output: output/fastq/Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.2.2017-07-05.21-03-17.stderr
    jobid: 17
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer3.2


rule fastq2GZ:
    input: output/fastq/Pfeiffer3.1.fastq
    output: output/fastq/Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.1.2017-07-05.21-03-17.stderr
    jobid: 18
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer3.1


rule fastq2GZ:
    input: output/fastq/Pfeiffer2.2.fastq
    output: output/fastq/Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.2.2017-07-05.21-03-17.stderr
    jobid: 20
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer2.2


rule fastq2GZ:
    input: output/fastq/Pfeiffer2.1.fastq
    output: output/fastq/Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.1.2017-07-05.21-03-17.stderr
    jobid: 19
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer2.1


rule bamALIGN_bwa:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, output/fastq/Pfeiffer2.1.fastq.gz, output/fastq/Pfeiffer2.2.fastq.gz, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/bam/Pfeiffer2_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-05.21-03-17.samtools.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-05.21-03-17.bwa.stderr
    jobid: 16
    wildcards: sampleBAB=Pfeiffer2


rule bamALIGN_bwa:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, output/fastq/Pfeiffer3.1.fastq.gz, output/fastq/Pfeiffer3.2.fastq.gz, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/bam/Pfeiffer3_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-05.21-03-17.samtools.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-05.21-03-17.bwa.stderr
    jobid: 15
    wildcards: sampleBAB=Pfeiffer3


rule sortBAM_biobambam:
    input: output/bam/Pfeiffer3_Aligned.out.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-05.21-03-17.samtools.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-05.21-03-17.bamsort.stderr
    jobid: 13
    wildcards: sampleSBB=Pfeiffer3_Aligned.out, pathSBB=output/bam


rule sortBAM_biobambam:
    input: output/bam/Pfeiffer2_Aligned.out.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-05.21-03-17.samtools.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-05.21-03-17.bamsort.stderr
    jobid: 14
    wildcards: sampleSBB=Pfeiffer2_Aligned.out, pathSBB=output/bam


rule filteredBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer3_Aligned.out_sorted.2017-07-05.21-03-17.stderr
    jobid: 11
    wildcards: pathFB=output/bam, sampleFB=Pfeiffer3_Aligned.out_sorted


rule filteredBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer2_Aligned.out_sorted.2017-07-05.21-03-17.stderr
    jobid: 12
    wildcards: pathFB=output/bam, sampleFB=Pfeiffer2_Aligned.out_sorted


rule markdupBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam, output/metrics/Pfeiffer3_Aligned.out_sorted_filtered.dup_metrics
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer3_Aligned.out_sorted_filtered.2017-07-05.21-03-17.biobammarkdup.stderr
    jobid: 9
    wildcards: outputDIR=output, sampleMDB=Pfeiffer3_Aligned.out_sorted_filtered


rule markdupBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam, output/metrics/Pfeiffer2_Aligned.out_sorted_filtered.dup_metrics
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer2_Aligned.out_sorted_filtered.2017-07-05.21-03-17.biobammarkdup.stderr
    jobid: 10
    wildcards: outputDIR=output, sampleMDB=Pfeiffer2_Aligned.out_sorted_filtered


rule indexBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam.bai, output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer2.2017-07-05.21-03-17.stderr
    jobid: 8
    wildcards: outputDIR=output, sampleIB=Pfeiffer2


rule indexBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam.bai, output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer3.2017-07-05.21-03-17.stderr
    jobid: 7
    wildcards: outputDIR=output, sampleIB=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.21-03-17.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.21-03-17.mpileup.stderr
    jobid: 5
    wildcards: sampleB2M=Pfeiffer2, chrB2M=


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.21-03-17.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.21-03-17.mpileup.stderr
    jobid: 6
    wildcards: sampleB2M=Pfeiffer3, chrB2M=


rule copynum:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/vcfGenUtil_varScan/Pfeiffer3_Pfeiffer2.varScan.copynumber
    log: log/vcfGenUtil_varScan/copynum/copynum_Pfeiffer3_Pfeiffer2.2017-07-05.21-03-17.stderr
    jobid: 4
    wildcards: sampletCN=Pfeiffer3, samplenCN=Pfeiffer2


rule conSeq:
    input: output/mpileup/Pfeiffer2.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.mpileup2cns
    log: log/vcfGenUtil_varScan/conSeq/conSeq_Pfeiffer2.2017-07-05.21-03-17.stderr
    jobid: 1
    wildcards: sampleCS=Pfeiffer2


rule conSeq:
    input: output/mpileup/Pfeiffer3.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.mpileup2cns
    log: log/vcfGenUtil_varScan/conSeq/conSeq_Pfeiffer3.2017-07-05.21-03-17.stderr
    jobid: 2
    wildcards: sampleCS=Pfeiffer3


rule copycall:
    input: output/vcfGenUtil_varScan/Pfeiffer3_Pfeiffer2.varScan.copynumber
    output: output/vcfGenUtil_varScan/Pfeiffer3_Pfeiffer2.varScan.copycall
    log: log/vcfGenUtil_varScan/copycall/copycall_Pfeiffer3_Pfeiffer2.2017-07-05.21-03-17.stderr
    jobid: 3
    wildcards: samplenCC=Pfeiffer2, sampletCC=Pfeiffer3


localrule all:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.mpileup2cns, output/vcfGenUtil_varScan/Pfeiffer2.varScan.mpileup2cns, output/vcfGenUtil_varScan/Pfeiffer3_Pfeiffer2.varScan.copycall, output/vcfGenUtil_varScan/Pfeiffer3_Pfeiffer2.varScan.copynumber
    jobid: 0

Job counts:
	count	jobs
	1	all
	2	bam2fastq_picard
	2	bam2mpileup
	2	bamALIGN_bwa
	2	conSeq
	1	copycall
	1	copynum
	4	fastq2GZ
	2	filteredBAM
	2	indexBAM
	2	markdupBAM
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
    2    bam2mpileup
    2    bamALIGN_bwa
    2    conSeq
    1    copycall
    1    copynum
    4    fastq2GZ
    2    filteredBAM
    2    indexBAM
    2    markdupBAM
    2    sortBAM_biobambam
    23

rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer3.bam
    output: output/fastq/Pfeiffer3.1.fastq, output/fastq/Pfeiffer3.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-05.21-03-33.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-05.21-03-33.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-05.21-03-33.namesort.stderr
    jobid: 22
    wildcards: sampleB2FP=Pfeiffer3

Submitted DRMAA job (jobid 8717108)

rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer2.bam
    output: output/fastq/Pfeiffer2.1.fastq, output/fastq/Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-05.21-03-33.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-05.21-03-33.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-05.21-03-33.namesort.stderr
    jobid: 21
    wildcards: sampleB2FP=Pfeiffer2

Submitted DRMAA job (jobid 8717109)
Finished job 21.
1 of 23 steps (4%) done

rule fastq2GZ:
    input: output/fastq/Pfeiffer2.2.fastq
    output: output/fastq/Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.2.2017-07-05.21-03-33.stderr
    jobid: 17
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer2.2

Submitted DRMAA job (jobid 8717141)

rule fastq2GZ:
    input: output/fastq/Pfeiffer2.1.fastq
    output: output/fastq/Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.1.2017-07-05.21-03-33.stderr
    jobid: 18
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer2.1

Submitted DRMAA job (jobid 8717142)
Finished job 22.
2 of 23 steps (9%) done

rule fastq2GZ:
    input: output/fastq/Pfeiffer3.1.fastq
    output: output/fastq/Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.1.2017-07-05.21-03-33.stderr
    jobid: 20
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer3.1

Submitted DRMAA job (jobid 8717146)

rule fastq2GZ:
    input: output/fastq/Pfeiffer3.2.fastq
    output: output/fastq/Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.2.2017-07-05.21-03-33.stderr
    jobid: 19
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer3.2

Submitted DRMAA job (jobid 8717147)
Finished job 18.
3 of 23 steps (13%) done
Finished job 17.
4 of 23 steps (17%) done

rule bamALIGN_bwa:
    input: output/fastq/Pfeiffer2.1.fastq.gz, output/fastq/Pfeiffer2.2.fastq.gz, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa
    output: output/bam/Pfeiffer2_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-05.21-03-33.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-05.21-03-33.samtools.stderr
    jobid: 15
    wildcards: sampleBAB=Pfeiffer2

Submitted DRMAA job (jobid 8717166)
Finished job 20.
5 of 23 steps (22%) done
Finished job 19.
6 of 23 steps (26%) done

rule bamALIGN_bwa:
    input: output/fastq/Pfeiffer3.1.fastq.gz, output/fastq/Pfeiffer3.2.fastq.gz, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa
    output: output/bam/Pfeiffer3_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-05.21-03-33.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-05.21-03-33.samtools.stderr
    jobid: 16
    wildcards: sampleBAB=Pfeiffer3

Submitted DRMAA job (jobid 8717167)
Finished job 16.
7 of 23 steps (30%) done

rule sortBAM_biobambam:
    input: output/bam/Pfeiffer3_Aligned.out.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-05.21-03-33.bamsort.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-05.21-03-33.samtools.stderr
    jobid: 14
    wildcards: pathSBB=output/bam, sampleSBB=Pfeiffer3_Aligned.out

Submitted DRMAA job (jobid 8717208)
Finished job 15.
8 of 23 steps (35%) done

rule sortBAM_biobambam:
    input: output/bam/Pfeiffer2_Aligned.out.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-05.21-03-33.bamsort.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-05.21-03-33.samtools.stderr
    jobid: 13
    wildcards: pathSBB=output/bam, sampleSBB=Pfeiffer2_Aligned.out

Submitted DRMAA job (jobid 8717212)
Finished job 14.
9 of 23 steps (39%) done

rule filteredBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer3_Aligned.out_sorted.2017-07-05.21-03-32.stderr
    jobid: 12
    wildcards: pathFB=output/bam, sampleFB=Pfeiffer3_Aligned.out_sorted

Submitted DRMAA job (jobid 8717235)
Finished job 13.
10 of 23 steps (43%) done

rule filteredBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer2_Aligned.out_sorted.2017-07-05.21-03-32.stderr
    jobid: 11
    wildcards: pathFB=output/bam, sampleFB=Pfeiffer2_Aligned.out_sorted

Submitted DRMAA job (jobid 8717241)
Finished job 11.
11 of 23 steps (48%) done

rule markdupBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    output: output/metrics/Pfeiffer2_Aligned.out_sorted_filtered.dup_metrics, output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer2_Aligned.out_sorted_filtered.2017-07-05.21-03-32.biobammarkdup.stderr
    jobid: 9
    wildcards: sampleMDB=Pfeiffer2_Aligned.out_sorted_filtered, outputDIR=output

Submitted DRMAA job (jobid 8717257)
Finished job 12.
12 of 23 steps (52%) done

rule markdupBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    output: output/metrics/Pfeiffer3_Aligned.out_sorted_filtered.dup_metrics, output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer3_Aligned.out_sorted_filtered.2017-07-05.21-03-32.biobammarkdup.stderr
    jobid: 10
    wildcards: sampleMDB=Pfeiffer3_Aligned.out_sorted_filtered, outputDIR=output

Submitted DRMAA job (jobid 8717261)
Finished job 10.
13 of 23 steps (57%) done

rule indexBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam.bai
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer3.2017-07-05.21-03-32.stderr
    jobid: 6
    wildcards: outputDIR=output, sampleIB=Pfeiffer3

Submitted DRMAA job (jobid 8717281)
Finished job 9.
14 of 23 steps (61%) done

rule indexBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam.bai
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer2.2017-07-05.21-03-32.stderr
    jobid: 5
    wildcards: outputDIR=output, sampleIB=Pfeiffer2

Submitted DRMAA job (jobid 8717282)
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/Pfeiffer2.bam.bai. Your Python build does not support it.
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/Pfeiffer2.bam. Your Python build does not support it.
Finished job 5.
15 of 23 steps (65%) done

rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.21-03-32.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-05.21-03-32.view.stderr
    jobid: 8
    wildcards: sampleB2M=Pfeiffer2, chrB2M=

Submitted DRMAA job (jobid 8717294)
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/Pfeiffer3.bam.bai. Your Python build does not support it.
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/Pfeiffer3.bam. Your Python build does not support it.
Finished job 6.
16 of 23 steps (70%) done

rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.21-03-32.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-05.21-03-32.view.stderr
    jobid: 7
    wildcards: sampleB2M=Pfeiffer3, chrB2M=

Submitted DRMAA job (jobid 8717304)

rule copynum:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa
    output: output/vcfGenUtil_varScan/Pfeiffer3_Pfeiffer2.varScan.copynumber
    log: log/vcfGenUtil_varScan/copynum/copynum_Pfeiffer3_Pfeiffer2.2017-07-05.21-03-32.stderr
    jobid: 1
    wildcards: samplenCN=Pfeiffer2, sampletCN=Pfeiffer3

Submitted DRMAA job (jobid 8717305)
Finished job 8.
17 of 23 steps (74%) done

rule conSeq:
    input: output/mpileup/Pfeiffer2.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.mpileup2cns
    log: log/vcfGenUtil_varScan/conSeq/conSeq_Pfeiffer2.2017-07-05.21-03-32.stderr
    jobid: 3
    wildcards: sampleCS=Pfeiffer2

Submitted DRMAA job (jobid 8717356)
Finished job 7.
18 of 23 steps (78%) done

rule conSeq:
    input: output/mpileup/Pfeiffer3.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.mpileup2cns
    log: log/vcfGenUtil_varScan/conSeq/conSeq_Pfeiffer3.2017-07-05.21-03-32.stderr
    jobid: 2
    wildcards: sampleCS=Pfeiffer3

Submitted DRMAA job (jobid 8717358)
Finished job 1.
19 of 23 steps (83%) done

rule copycall:
    input: output/vcfGenUtil_varScan/Pfeiffer3_Pfeiffer2.varScan.copynumber
    output: output/vcfGenUtil_varScan/Pfeiffer3_Pfeiffer2.varScan.copycall
    log: log/vcfGenUtil_varScan/copycall/copycall_Pfeiffer3_Pfeiffer2.2017-07-05.21-03-32.stderr
    jobid: 4
    wildcards: sampletCC=Pfeiffer3, samplenCC=Pfeiffer2

Submitted DRMAA job (jobid 8717395)
Finished job 4.
20 of 23 steps (87%) done
Finished job 3.
21 of 23 steps (91%) done
Finished job 2.
22 of 23 steps (96%) done

localrule all:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.mpileup2cns, output/vcfGenUtil_varScan/Pfeiffer2.varScan.mpileup2cns, output/vcfGenUtil_varScan/Pfeiffer3_Pfeiffer2.varScan.copycall, output/vcfGenUtil_varScan/Pfeiffer3_Pfeiffer2.varScan.copynumber
    jobid: 0

Finished job 0.
23 of 23 steps (100%) done

real    12m23.452s
user    0m1.442s
sys    0m0.271s
```
