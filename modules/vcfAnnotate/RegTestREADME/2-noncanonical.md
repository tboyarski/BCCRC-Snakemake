# 2-noncanonical
This pipeline is to exemplify the 'noncanonical'  operations of this module.

## Setting up the: buildPipe.py
Users must set the following variable:

 * (Line 13) TYPE = "single"

## Setting up the: Snakefile
Users must set the following submodule "call via" input requirements:

 * singleVCF

## Setting up the: YAML
Users must set the following "input/config.yaml" variables:

 * (Line 15) intermediateKEEP = True
 * (Line 41) sampleFORM = "varType annotated\nsnp .noncanonical_annotated.dbsnp_annotated.cosmic_annotated\nindel .noncanonical_annotated.indel_annotated"
 * (Line 42) vcfAnnotateDIR = "vcfGenUtil_varScan"

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
    input: input/rawBam/Pfeiffer3.bam
    output: output/fastq/Pfeiffer3.1.fastq, output/fastq/Pfeiffer3.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-07.09-13-55.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-07.09-13-55.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-07.09-13-55.stderr
    jobid: 31
    wildcards: sampleB2FP=Pfeiffer3


rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer2.bam
    output: output/fastq/Pfeiffer2.1.fastq, output/fastq/Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-07.09-13-55.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-07.09-13-55.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-07.09-13-55.stderr
    jobid: 32
    wildcards: sampleB2FP=Pfeiffer2


rule fastq2GZ:
    input: output/fastq/Pfeiffer2.2.fastq
    output: output/fastq/Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.2.2017-07-07.09-13-55.stderr
    jobid: 29
    wildcards: sampleFGZ=Pfeiffer2.2, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Pfeiffer3.2.fastq
    output: output/fastq/Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.2.2017-07-07.09-13-55.stderr
    jobid: 27
    wildcards: sampleFGZ=Pfeiffer3.2, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Pfeiffer2.1.fastq
    output: output/fastq/Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.1.2017-07-07.09-13-55.stderr
    jobid: 30
    wildcards: sampleFGZ=Pfeiffer2.1, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Pfeiffer3.1.fastq
    output: output/fastq/Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.1.2017-07-07.09-13-55.stderr
    jobid: 28
    wildcards: sampleFGZ=Pfeiffer3.1, pathFGZ=output/fastq


rule bamALIGN_bwa:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, output/fastq/Pfeiffer2.1.fastq.gz, output/fastq/Pfeiffer2.2.fastq.gz
    output: output/bam/Pfeiffer2_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-07.09-13-55.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-07.09-13-55.samtools.stderr
    jobid: 26
    wildcards: sampleBAB=Pfeiffer2


rule bamALIGN_bwa:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, output/fastq/Pfeiffer3.1.fastq.gz, output/fastq/Pfeiffer3.2.fastq.gz
    output: output/bam/Pfeiffer3_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-07.09-13-55.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-07.09-13-55.samtools.stderr
    jobid: 25
    wildcards: sampleBAB=Pfeiffer3


rule sortBAM_biobambam:
    input: output/bam/Pfeiffer2_Aligned.out.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-07.09-13-55.bamsort.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-07.09-13-55.samtools.stderr
    jobid: 24
    wildcards: pathSBB=output/bam, sampleSBB=Pfeiffer2_Aligned.out


rule sortBAM_biobambam:
    input: output/bam/Pfeiffer3_Aligned.out.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-07.09-13-55.bamsort.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-07.09-13-55.samtools.stderr
    jobid: 23
    wildcards: pathSBB=output/bam, sampleSBB=Pfeiffer3_Aligned.out


rule filteredBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer3_Aligned.out_sorted.2017-07-07.09-13-55.stderr
    jobid: 21
    wildcards: sampleFB=Pfeiffer3_Aligned.out_sorted, pathFB=output/bam


rule filteredBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer2_Aligned.out_sorted.2017-07-07.09-13-55.stderr
    jobid: 22
    wildcards: sampleFB=Pfeiffer2_Aligned.out_sorted, pathFB=output/bam


rule markdupBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam, output/metrics/Pfeiffer2_Aligned.out_sorted_filtered.dup_metrics
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer2_Aligned.out_sorted_filtered.2017-07-07.09-13-55.biobammarkdup.stderr
    jobid: 20
    wildcards: sampleMDB=Pfeiffer2_Aligned.out_sorted_filtered, outputDIR=output


rule markdupBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam, output/metrics/Pfeiffer3_Aligned.out_sorted_filtered.dup_metrics
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer3_Aligned.out_sorted_filtered.2017-07-07.09-13-55.biobammarkdup.stderr
    jobid: 19
    wildcards: sampleMDB=Pfeiffer3_Aligned.out_sorted_filtered, outputDIR=output


rule indexBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam.bai, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer3.2017-07-07.09-13-55.stderr
    jobid: 17
    wildcards: sampleIB=Pfeiffer3, outputDIR=output


rule indexBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam.bai, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer2.2017-07-07.09-13-55.stderr
    jobid: 18
    wildcards: sampleIB=Pfeiffer2, outputDIR=output


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.09-13-55.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.09-13-55.mpileup.stderr
    jobid: 16
    wildcards: sampleB2M=Pfeiffer2, chrB2M=


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.09-13-55.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.09-13-55.mpileup.stderr
    jobid: 13
    wildcards: sampleB2M=Pfeiffer3, chrB2M=


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr.snp.2017-07-07.09-13-55.stderr
    jobid: 14
    wildcards: sampleMPU2VCFS=Pfeiffer2, varTypeMPU2VCFS=snp, chrMPU2VCFS=


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr.snp.2017-07-07.09-13-55.stderr
    jobid: 15
    wildcards: sampleMPU2VCFS=Pfeiffer3, varTypeMPU2VCFS=snp, chrMPU2VCFS=


rule noncanonical:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical.summary.html, output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.noncanonical_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical.summary.genes.txt
    log: log/vcfAnnotate/noncanonical/noncanonical_Pfeiffer2.varScan.snp.2017-07-07.09-13-55.stderr
    jobid: 10
    wildcards: pathNCAN=output/vcfGenUtil_varScan, sampleNCAN=Pfeiffer2.varScan.snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr.indel.2017-07-07.09-13-55.stderr
    jobid: 12
    wildcards: sampleMPU2VCFS=Pfeiffer2, varTypeMPU2VCFS=indel, chrMPU2VCFS=


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr.indel.2017-07-07.09-13-55.stderr
    jobid: 9
    wildcards: sampleMPU2VCFS=Pfeiffer3, varTypeMPU2VCFS=indel, chrMPU2VCFS=


rule noncanonical:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical.summary.html, output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.noncanonical_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical.summary.genes.txt
    log: log/vcfAnnotate/noncanonical/noncanonical_Pfeiffer3.varScan.snp.2017-07-07.09-13-55.stderr
    jobid: 11
    wildcards: pathNCAN=output/vcfGenUtil_varScan, sampleNCAN=Pfeiffer3.varScan.snp


rule dbsnp:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.noncanonical_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.noncanonical_annotated.dbsnp_annotated.vcf
    log: log/vcfAnnotate/dbsnp/dbsnp_Pfeiffer2.varScan.snp.noncanonical_annotated.2017-07-07.09-13-55.stderr
    jobid: 6
    wildcards: pathDbSnp=output/vcfGenUtil_varScan, sampleDbSnp=Pfeiffer2.varScan.snp.noncanonical_annotated


rule noncanonical:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.canonical.summary.html, output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.noncanonical_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.canonical.summary.genes.txt
    log: log/vcfAnnotate/noncanonical/noncanonical_Pfeiffer2.varScan.indel.2017-07-07.09-13-55.stderr
    jobid: 8
    wildcards: pathNCAN=output/vcfGenUtil_varScan, sampleNCAN=Pfeiffer2.varScan.indel


rule dbsnp:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.noncanonical_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.noncanonical_annotated.dbsnp_annotated.vcf
    log: log/vcfAnnotate/dbsnp/dbsnp_Pfeiffer3.varScan.snp.noncanonical_annotated.2017-07-07.09-13-55.stderr
    jobid: 7
    wildcards: pathDbSnp=output/vcfGenUtil_varScan, sampleDbSnp=Pfeiffer3.varScan.snp.noncanonical_annotated


rule noncanonical:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.canonical.summary.html, output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.noncanonical_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.canonical.summary.genes.txt
    log: log/vcfAnnotate/noncanonical/noncanonical_Pfeiffer3.varScan.indel.2017-07-07.09-13-55.stderr
    jobid: 5
    wildcards: pathNCAN=output/vcfGenUtil_varScan, sampleNCAN=Pfeiffer3.varScan.indel


rule indel:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.noncanonical_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.noncanonical_annotated.indel_annotated.vcf
    log: log/vcfAnnotate/indel/indel_Pfeiffer3.varScan.indel.noncanonical_annotated.2017-07-07.09-13-55.1000g.log, log/vcfAnnotate/indel/indel_Pfeiffer3.varScan.indel.noncanonical_annotated.2017-07-07.09-13-55.mills_100g.log, log/vcfAnnotate/indel/indel_Pfeiffer3.varScan.indel.noncanonical_annotated.2017-07-07.09-13-55dbsnp.stderr
    jobid: 1
    wildcards: pathIndel=output/vcfGenUtil_varScan, sampleIndel=Pfeiffer3.varScan.indel.noncanonical_annotated


rule cosmic:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.noncanonical_annotated.dbsnp_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.noncanonical_annotated.dbsnp_annotated.cosmic_annotated.vcf
    log: log/vcfAnnotate/cosmic/cosmic_Pfeiffer2.varScan.snp.noncanonical_annotated.dbsnp_annotated.2017-07-07.09-13-55.stderr
    jobid: 2
    wildcards: sampleCOS=Pfeiffer2.varScan.snp.noncanonical_annotated.dbsnp_annotated, pathCOS=output/vcfGenUtil_varScan


rule cosmic:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.noncanonical_annotated.dbsnp_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.noncanonical_annotated.dbsnp_annotated.cosmic_annotated.vcf
    log: log/vcfAnnotate/cosmic/cosmic_Pfeiffer3.varScan.snp.noncanonical_annotated.dbsnp_annotated.2017-07-07.09-13-55.stderr
    jobid: 3
    wildcards: sampleCOS=Pfeiffer3.varScan.snp.noncanonical_annotated.dbsnp_annotated, pathCOS=output/vcfGenUtil_varScan


rule indel:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.noncanonical_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.noncanonical_annotated.indel_annotated.vcf
    log: log/vcfAnnotate/indel/indel_Pfeiffer2.varScan.indel.noncanonical_annotated.2017-07-07.09-13-55.1000g.log, log/vcfAnnotate/indel/indel_Pfeiffer2.varScan.indel.noncanonical_annotated.2017-07-07.09-13-55.mills_100g.log, log/vcfAnnotate/indel/indel_Pfeiffer2.varScan.indel.noncanonical_annotated.2017-07-07.09-13-55dbsnp.stderr
    jobid: 4
    wildcards: pathIndel=output/vcfGenUtil_varScan, sampleIndel=Pfeiffer2.varScan.indel.noncanonical_annotated


localrule all:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.noncanonical_annotated.dbsnp_annotated.cosmic_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.noncanonical_annotated.indel_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.noncanonical_annotated.dbsnp_annotated.cosmic_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.noncanonical_annotated.indel_annotated.vcf
    jobid: 0

Job counts:
	count	jobs
	1	all
	2	bam2fastq_picard
	2	bam2mpileup
	2	bamALIGN_bwa
	2	cosmic
	2	dbsnp
	4	fastq2GZ
	2	filteredBAM
	2	indel
	2	indexBAM
	2	markdupBAM
	4	mpileup2vcf_single
	4	noncanonical
	2	sortBAM_biobambam
	33
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
    2    cosmic
    2    dbsnp
    4    fastq2GZ
    2    filteredBAM
    2    indel
    2    indexBAM
    2    markdupBAM
    4    mpileup2vcf_single
    4    noncanonical
    2    sortBAM_biobambam
    33

rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer2.bam
    output: output/fastq/Pfeiffer2.1.fastq, output/fastq/Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-07.09-17-00.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-07.09-17-00.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-07.09-17-00.vendor_failed_reads.log
    jobid: 32
    wildcards: sampleB2FP=Pfeiffer2

Submitted DRMAA job (jobid 8800239)

rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer3.bam
    output: output/fastq/Pfeiffer3.1.fastq, output/fastq/Pfeiffer3.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-07.09-17-00.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-07.09-17-00.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-07.09-17-00.vendor_failed_reads.log
    jobid: 31
    wildcards: sampleB2FP=Pfeiffer3

Submitted DRMAA job (jobid 8800240)
Finished job 31.
1 of 33 steps (3%) done

rule fastq2GZ:
    input: output/fastq/Pfeiffer3.2.fastq
    output: output/fastq/Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.2.2017-07-07.09-17-00.stderr
    jobid: 27
    wildcards: sampleFGZ=Pfeiffer3.2, pathFGZ=output/fastq

Submitted DRMAA job (jobid 8800311)

rule fastq2GZ:
    input: output/fastq/Pfeiffer3.1.fastq
    output: output/fastq/Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.1.2017-07-07.09-17-00.stderr
    jobid: 28
    wildcards: sampleFGZ=Pfeiffer3.1, pathFGZ=output/fastq

Submitted DRMAA job (jobid 8800312)
Finished job 32.
2 of 33 steps (6%) done

rule fastq2GZ:
    input: output/fastq/Pfeiffer2.2.fastq
    output: output/fastq/Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.2.2017-07-07.09-17-00.stderr
    jobid: 29
    wildcards: sampleFGZ=Pfeiffer2.2, pathFGZ=output/fastq

Submitted DRMAA job (jobid 8800371)

rule fastq2GZ:
    input: output/fastq/Pfeiffer2.1.fastq
    output: output/fastq/Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.1.2017-07-07.09-17-00.stderr
    jobid: 30
    wildcards: sampleFGZ=Pfeiffer2.1, pathFGZ=output/fastq

Submitted DRMAA job (jobid 8800372)
Finished job 27.
3 of 33 steps (9%) done
Finished job 28.
4 of 33 steps (12%) done

rule bamALIGN_bwa:
    input: output/fastq/Pfeiffer3.1.fastq.gz, output/fastq/Pfeiffer3.2.fastq.gz, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa
    output: output/bam/Pfeiffer3_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-07.09-17-00.samtools.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-07.09-17-00.bwa.stderr
    jobid: 25
    wildcards: sampleBAB=Pfeiffer3

Submitted DRMAA job (jobid 8800380)
Finished job 30.
5 of 33 steps (15%) done
Finished job 29.
6 of 33 steps (18%) done

rule bamALIGN_bwa:
    input: output/fastq/Pfeiffer2.1.fastq.gz, output/fastq/Pfeiffer2.2.fastq.gz, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa
    output: output/bam/Pfeiffer2_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-07.09-17-00.samtools.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-07.09-17-00.bwa.stderr
    jobid: 26
    wildcards: sampleBAB=Pfeiffer2

Submitted DRMAA job (jobid 8800399)
Finished job 25.
7 of 33 steps (21%) done

rule sortBAM_biobambam:
    input: output/bam/Pfeiffer3_Aligned.out.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-07.09-17-00.bamsort.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-07.09-17-00.samtools.stderr
    jobid: 23
    wildcards: sampleSBB=Pfeiffer3_Aligned.out, pathSBB=output/bam

Submitted DRMAA job (jobid 8800503)
Finished job 26.
8 of 33 steps (24%) done

rule sortBAM_biobambam:
    input: output/bam/Pfeiffer2_Aligned.out.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-07.09-17-00.bamsort.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-07.09-17-00.samtools.stderr
    jobid: 24
    wildcards: sampleSBB=Pfeiffer2_Aligned.out, pathSBB=output/bam

Submitted DRMAA job (jobid 8800573)
Finished job 23.
9 of 33 steps (27%) done

rule filteredBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer3_Aligned.out_sorted.2017-07-07.09-17-00.stderr
    jobid: 21
    wildcards: pathFB=output/bam, sampleFB=Pfeiffer3_Aligned.out_sorted

Submitted DRMAA job (jobid 8800599)
Finished job 24.
10 of 33 steps (30%) done

rule filteredBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer2_Aligned.out_sorted.2017-07-07.09-17-00.stderr
    jobid: 22
    wildcards: pathFB=output/bam, sampleFB=Pfeiffer2_Aligned.out_sorted

Submitted DRMAA job (jobid 8800614)
Finished job 22.
11 of 33 steps (33%) done

rule markdupBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    output: output/metrics/Pfeiffer2_Aligned.out_sorted_filtered.dup_metrics, output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer2_Aligned.out_sorted_filtered.2017-07-07.09-17-00.biobammarkdup.stderr
    jobid: 20
    wildcards: sampleMDB=Pfeiffer2_Aligned.out_sorted_filtered, outputDIR=output

Submitted DRMAA job (jobid 8800658)
Finished job 21.
12 of 33 steps (36%) done

rule markdupBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    output: output/metrics/Pfeiffer3_Aligned.out_sorted_filtered.dup_metrics, output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer3_Aligned.out_sorted_filtered.2017-07-07.09-17-00.biobammarkdup.stderr
    jobid: 19
    wildcards: sampleMDB=Pfeiffer3_Aligned.out_sorted_filtered, outputDIR=output

Submitted DRMAA job (jobid 8800664)
Finished job 19.
13 of 33 steps (39%) done

rule indexBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam.bai, output/bam/Pfeiffer3.bam.bai
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer3.2017-07-07.09-17-00.stderr
    jobid: 17
    wildcards: sampleIB=Pfeiffer3, outputDIR=output

Submitted DRMAA job (jobid 8800714)
Finished job 20.
14 of 33 steps (42%) done

rule indexBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam.bai, output/bam/Pfeiffer2.bam.bai
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer2.2017-07-07.09-17-00.stderr
    jobid: 18
    wildcards: sampleIB=Pfeiffer2, outputDIR=output

Submitted DRMAA job (jobid 8800715)
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/Pfeiffer2.bam. Your Python build does not support it.
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/Pfeiffer2.bam.bai. Your Python build does not support it.
Finished job 18.
15 of 33 steps (45%) done

rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam
    output: output/mpileup/Pfeiffer2.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.09-17-00.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.09-17-00.view.stderr
    jobid: 16
    wildcards: sampleB2M=Pfeiffer2, chrB2M=

Submitted DRMAA job (jobid 8800740)
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/Pfeiffer3.bam. Your Python build does not support it.
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/Pfeiffer3.bam.bai. Your Python build does not support it.
Finished job 17.
16 of 33 steps (48%) done

rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam
    output: output/mpileup/Pfeiffer3.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.09-17-00.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.09-17-00.view.stderr
    jobid: 15
    wildcards: sampleB2M=Pfeiffer3, chrB2M=

Submitted DRMAA job (jobid 8800760)
Finished job 16.
17 of 33 steps (52%) done

rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr.snp.2017-07-07.09-17-00.stderr
    jobid: 14
    wildcards: sampleMPU2VCFS=Pfeiffer2, varTypeMPU2VCFS=snp, chrMPU2VCFS=

Submitted DRMAA job (jobid 8800914)

rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr.indel.2017-07-07.09-17-00.stderr
    jobid: 12
    wildcards: sampleMPU2VCFS=Pfeiffer2, varTypeMPU2VCFS=indel, chrMPU2VCFS=

Submitted DRMAA job (jobid 8800915)
Finished job 15.
18 of 33 steps (55%) done

rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr.indel.2017-07-07.09-17-00.stderr
    jobid: 11
    wildcards: sampleMPU2VCFS=Pfeiffer3, varTypeMPU2VCFS=indel, chrMPU2VCFS=

Submitted DRMAA job (jobid 8800916)

rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr.snp.2017-07-07.09-17-00.stderr
    jobid: 13
    wildcards: sampleMPU2VCFS=Pfeiffer3, varTypeMPU2VCFS=snp, chrMPU2VCFS=

Submitted DRMAA job (jobid 8800917)
Finished job 11.
19 of 33 steps (58%) done

rule noncanonical:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.canonical.summary.html, output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.noncanonical_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.canonical.summary.genes.txt
    log: log/vcfAnnotate/noncanonical/noncanonical_Pfeiffer3.varScan.indel.2017-07-07.09-16-59.stderr
    jobid: 7
    wildcards: sampleNCAN=Pfeiffer3.varScan.indel, pathNCAN=output/vcfGenUtil_varScan

Submitted DRMAA job (jobid 8801008)
Finished job 14.
20 of 33 steps (61%) done

rule noncanonical:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical.summary.html, output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.noncanonical_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical.summary.genes.txt
    log: log/vcfAnnotate/noncanonical/noncanonical_Pfeiffer2.varScan.snp.2017-07-07.09-16-59.stderr
    jobid: 10
    wildcards: sampleNCAN=Pfeiffer2.varScan.snp, pathNCAN=output/vcfGenUtil_varScan

Submitted DRMAA job (jobid 8801009)
Finished job 13.
21 of 33 steps (64%) done

rule noncanonical:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical.summary.html, output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.noncanonical_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical.summary.genes.txt
    log: log/vcfAnnotate/noncanonical/noncanonical_Pfeiffer3.varScan.snp.2017-07-07.09-16-59.stderr
    jobid: 9
    wildcards: sampleNCAN=Pfeiffer3.varScan.snp, pathNCAN=output/vcfGenUtil_varScan

Submitted DRMAA job (jobid 8801014)
Finished job 12.
22 of 33 steps (67%) done

rule noncanonical:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.canonical.summary.html, output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.noncanonical_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.canonical.summary.genes.txt
    log: log/vcfAnnotate/noncanonical/noncanonical_Pfeiffer2.varScan.indel.2017-07-07.09-16-59.stderr
    jobid: 8
    wildcards: sampleNCAN=Pfeiffer2.varScan.indel, pathNCAN=output/vcfGenUtil_varScan

Submitted DRMAA job (jobid 8801020)
Finished job 8.
23 of 33 steps (70%) done

rule indel:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.noncanonical_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.noncanonical_annotated.indel_annotated.vcf
    log: log/vcfAnnotate/indel/indel_Pfeiffer2.varScan.indel.noncanonical_annotated.2017-07-07.09-16-59dbsnp.stderr, log/vcfAnnotate/indel/indel_Pfeiffer2.varScan.indel.noncanonical_annotated.2017-07-07.09-16-59.mills_100g.log, log/vcfAnnotate/indel/indel_Pfeiffer2.varScan.indel.noncanonical_annotated.2017-07-07.09-16-59.1000g.log
    jobid: 4
    wildcards: sampleIndel=Pfeiffer2.varScan.indel.noncanonical_annotated, pathIndel=output/vcfGenUtil_varScan

Submitted DRMAA job (jobid 8801081)
Finished job 7.
24 of 33 steps (73%) done

rule indel:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.noncanonical_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.noncanonical_annotated.indel_annotated.vcf
    log: log/vcfAnnotate/indel/indel_Pfeiffer3.varScan.indel.noncanonical_annotated.2017-07-07.09-16-59dbsnp.stderr, log/vcfAnnotate/indel/indel_Pfeiffer3.varScan.indel.noncanonical_annotated.2017-07-07.09-16-59.mills_100g.log, log/vcfAnnotate/indel/indel_Pfeiffer3.varScan.indel.noncanonical_annotated.2017-07-07.09-16-59.1000g.log
    jobid: 3
    wildcards: sampleIndel=Pfeiffer3.varScan.indel.noncanonical_annotated, pathIndel=output/vcfGenUtil_varScan

Submitted DRMAA job (jobid 8801082)
Finished job 9.
25 of 33 steps (76%) done

rule dbsnp:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.noncanonical_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.noncanonical_annotated.dbsnp_annotated.vcf
    log: log/vcfAnnotate/dbsnp/dbsnp_Pfeiffer3.varScan.snp.noncanonical_annotated.2017-07-07.09-16-59.stderr
    jobid: 5
    wildcards: pathDbSnp=output/vcfGenUtil_varScan, sampleDbSnp=Pfeiffer3.varScan.snp.noncanonical_annotated

Submitted DRMAA job (jobid 8801083)
Finished job 10.
26 of 33 steps (79%) done

rule dbsnp:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.noncanonical_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.noncanonical_annotated.dbsnp_annotated.vcf
    log: log/vcfAnnotate/dbsnp/dbsnp_Pfeiffer2.varScan.snp.noncanonical_annotated.2017-07-07.09-16-59.stderr
    jobid: 6
    wildcards: pathDbSnp=output/vcfGenUtil_varScan, sampleDbSnp=Pfeiffer2.varScan.snp.noncanonical_annotated

Submitted DRMAA job (jobid 8801084)
Finished job 3.
27 of 33 steps (82%) done
Finished job 6.
28 of 33 steps (85%) done

rule cosmic:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.noncanonical_annotated.dbsnp_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.noncanonical_annotated.dbsnp_annotated.cosmic_annotated.vcf
    log: log/vcfAnnotate/cosmic/cosmic_Pfeiffer2.varScan.snp.noncanonical_annotated.dbsnp_annotated.2017-07-07.09-16-59.stderr
    jobid: 2
    wildcards: sampleCOS=Pfeiffer2.varScan.snp.noncanonical_annotated.dbsnp_annotated, pathCOS=output/vcfGenUtil_varScan

Submitted DRMAA job (jobid 8801132)
Finished job 4.
29 of 33 steps (88%) done
Finished job 5.
30 of 33 steps (91%) done

rule cosmic:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.noncanonical_annotated.dbsnp_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.noncanonical_annotated.dbsnp_annotated.cosmic_annotated.vcf
    log: log/vcfAnnotate/cosmic/cosmic_Pfeiffer3.varScan.snp.noncanonical_annotated.dbsnp_annotated.2017-07-07.09-16-59.stderr
    jobid: 1
    wildcards: sampleCOS=Pfeiffer3.varScan.snp.noncanonical_annotated.dbsnp_annotated, pathCOS=output/vcfGenUtil_varScan

Submitted DRMAA job (jobid 8801133)
Finished job 1.
31 of 33 steps (94%) done
Finished job 2.
32 of 33 steps (97%) done

localrule all:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.noncanonical_annotated.dbsnp_annotated.cosmic_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.noncanonical_annotated.indel_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.noncanonical_annotated.dbsnp_annotated.cosmic_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.noncanonical_annotated.indel_annotated.vcf
    jobid: 0

Finished job 0.
33 of 33 steps (100%) done

real    10m30.873s
user    0m1.816s
sys    0m0.354s
```
