# 1-canonical
This pipeline is to exemplify the default operations of this module.

## Setting up the: buildPipe.py
Users must set the following variable:

 * (Line 13) TYPE = "single"

## Setting up the: Snakefile
Users must set the following submodule "call via" input requirements:

 * singleVCF

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
    input: input/rawBam/Pfeiffer3.bam
    output: output/fastq/Pfeiffer3.1.fastq, output/fastq/Pfeiffer3.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-06.00-05-23.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-06.00-05-23.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-06.00-05-23.vendor_failed_reads.log
    jobid: 31
    wildcards: sampleB2FP=Pfeiffer3


rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer2.bam
    output: output/fastq/Pfeiffer2.1.fastq, output/fastq/Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-06.00-05-23.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-06.00-05-23.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-06.00-05-23.vendor_failed_reads.log
    jobid: 32
    wildcards: sampleB2FP=Pfeiffer2


rule fastq2GZ:
    input: output/fastq/Pfeiffer3.2.fastq
    output: output/fastq/Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.2.2017-07-06.00-05-23.stderr
    jobid: 28
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer3.2


rule fastq2GZ:
    input: output/fastq/Pfeiffer2.1.fastq
    output: output/fastq/Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.1.2017-07-06.00-05-23.stderr
    jobid: 29
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer2.1


rule fastq2GZ:
    input: output/fastq/Pfeiffer2.2.fastq
    output: output/fastq/Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.2.2017-07-06.00-05-23.stderr
    jobid: 30
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer2.2


rule fastq2GZ:
    input: output/fastq/Pfeiffer3.1.fastq
    output: output/fastq/Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.1.2017-07-06.00-05-23.stderr
    jobid: 27
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer3.1


rule bamALIGN_bwa:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/fastq/Pfeiffer3.1.fastq.gz, output/fastq/Pfeiffer3.2.fastq.gz, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa
    output: output/bam/Pfeiffer3_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-06.00-05-23.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-06.00-05-23.samtools.stderr
    jobid: 25
    wildcards: sampleBAB=Pfeiffer3


rule bamALIGN_bwa:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/fastq/Pfeiffer2.1.fastq.gz, output/fastq/Pfeiffer2.2.fastq.gz, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa
    output: output/bam/Pfeiffer2_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-06.00-05-23.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-06.00-05-23.samtools.stderr
    jobid: 26
    wildcards: sampleBAB=Pfeiffer2


rule sortBAM_biobambam:
    input: output/bam/Pfeiffer3_Aligned.out.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-06.00-05-23.bamsort.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-06.00-05-23.samtools.stderr
    jobid: 23
    wildcards: sampleSBB=Pfeiffer3_Aligned.out, pathSBB=output/bam


rule sortBAM_biobambam:
    input: output/bam/Pfeiffer2_Aligned.out.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-06.00-05-23.bamsort.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-06.00-05-23.samtools.stderr
    jobid: 24
    wildcards: sampleSBB=Pfeiffer2_Aligned.out, pathSBB=output/bam


rule filteredBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer2_Aligned.out_sorted.2017-07-06.00-05-23.stderr
    jobid: 22
    wildcards: pathFB=output/bam, sampleFB=Pfeiffer2_Aligned.out_sorted


rule filteredBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer3_Aligned.out_sorted.2017-07-06.00-05-23.stderr
    jobid: 21
    wildcards: pathFB=output/bam, sampleFB=Pfeiffer3_Aligned.out_sorted


rule markdupBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    output: output/metrics/Pfeiffer3_Aligned.out_sorted_filtered.dup_metrics, output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer3_Aligned.out_sorted_filtered.2017-07-06.00-05-23.biobammarkdup.stderr
    jobid: 19
    wildcards: outputDIR=output, sampleMDB=Pfeiffer3_Aligned.out_sorted_filtered


rule markdupBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    output: output/metrics/Pfeiffer2_Aligned.out_sorted_filtered.dup_metrics, output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer2_Aligned.out_sorted_filtered.2017-07-06.00-05-23.biobammarkdup.stderr
    jobid: 20
    wildcards: outputDIR=output, sampleMDB=Pfeiffer2_Aligned.out_sorted_filtered


rule indexBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam.bai, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer3.2017-07-06.00-05-23.stderr
    jobid: 17
    wildcards: outputDIR=output, sampleIB=Pfeiffer3


rule indexBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam.bai, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer2.2017-07-06.00-05-23.stderr
    jobid: 18
    wildcards: outputDIR=output, sampleIB=Pfeiffer2


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-06.00-05-23.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-06.00-05-23.view.stderr
    jobid: 14
    wildcards: sampleB2M=Pfeiffer3, chrB2M=


rule bam2mpileup:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-06.00-05-23.mpileup.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-06.00-05-23.view.stderr
    jobid: 16
    wildcards: sampleB2M=Pfeiffer2, chrB2M=


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr.snp.2017-07-06.00-05-23.stderr
    jobid: 15
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=, varTypeMPU2VCFS=snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr.snp.2017-07-06.00-05-23.stderr
    jobid: 13
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=, varTypeMPU2VCFS=snp


rule canonical:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical.summary.genes.txt, output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical.summary.html
    log: log/vcfAnnotate/canonical/canonical_Pfeiffer2.varScan.snp.2017-07-06.00-05-23.stderr
    jobid: 11
    wildcards: pathCAN=vcfGenUtil_varScan, sampleCAN=Pfeiffer2.varScan.snp


rule canonical:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical.summary.genes.txt, output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical.summary.html
    log: log/vcfAnnotate/canonical/canonical_Pfeiffer3.varScan.snp.2017-07-06.00-05-23.stderr
    jobid: 9
    wildcards: pathCAN=vcfGenUtil_varScan, sampleCAN=Pfeiffer3.varScan.snp


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr.indel.2017-07-06.00-05-23.stderr
    jobid: 12
    wildcards: sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=, varTypeMPU2VCFS=indel


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr.indel.2017-07-06.00-05-23.stderr
    jobid: 10
    wildcards: sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=, varTypeMPU2VCFS=indel


rule dbsnp:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated.vcf
    log: log/vcfAnnotate/dbsnp/dbsnp_Pfeiffer3.varScan.snp.canonical_annotated.2017-07-06.00-05-23.stderr
    jobid: 5
    wildcards: pathDbSnp=output/vcfGenUtil_varScan, sampleDbSnp=Pfeiffer3.varScan.snp.canonical_annotated


rule canonical:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.canonical.summary.genes.txt, output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.canonical_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.canonical.summary.html
    log: log/vcfAnnotate/canonical/canonical_Pfeiffer3.varScan.indel.2017-07-06.00-05-23.stderr
    jobid: 6
    wildcards: pathCAN=vcfGenUtil_varScan, sampleCAN=Pfeiffer3.varScan.indel


rule canonical:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.canonical.summary.genes.txt, output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.canonical_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.canonical.summary.html
    log: log/vcfAnnotate/canonical/canonical_Pfeiffer2.varScan.indel.2017-07-06.00-05-23.stderr
    jobid: 8
    wildcards: pathCAN=vcfGenUtil_varScan, sampleCAN=Pfeiffer2.varScan.indel


rule dbsnp:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated.vcf
    log: log/vcfAnnotate/dbsnp/dbsnp_Pfeiffer2.varScan.snp.canonical_annotated.2017-07-06.00-05-23.stderr
    jobid: 7
    wildcards: pathDbSnp=output/vcfGenUtil_varScan, sampleDbSnp=Pfeiffer2.varScan.snp.canonical_annotated


rule cosmic:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated.cosmic_annotated.vcf
    log: log/vcfAnnotate/cosmic/cosmic_Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated.2017-07-06.00-05-23.stderr
    jobid: 1
    wildcards: pathCOS=output/vcfGenUtil_varScan, sampleCOS=Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated


rule cosmic:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated.cosmic_annotated.vcf
    log: log/vcfAnnotate/cosmic/cosmic_Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated.2017-07-06.00-05-23.stderr
    jobid: 3
    wildcards: pathCOS=output/vcfGenUtil_varScan, sampleCOS=Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated


rule indel:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.canonical_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.canonical_annotated.indel_annotated.vcf
    log: log/vcfAnnotate/indel/indel_Pfeiffer3.varScan.indel.canonical_annotated.2017-07-06.00-05-23dbsnp.stderr, log/vcfAnnotate/indel/indel_Pfeiffer3.varScan.indel.canonical_annotated.2017-07-06.00-05-23.1000g.log, log/vcfAnnotate/indel/indel_Pfeiffer3.varScan.indel.canonical_annotated.2017-07-06.00-05-23.mills_100g.log
    jobid: 2
    wildcards: sampleIndel=Pfeiffer3.varScan.indel.canonical_annotated, pathIndel=output/vcfGenUtil_varScan


rule indel:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.canonical_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.canonical_annotated.indel_annotated.vcf
    log: log/vcfAnnotate/indel/indel_Pfeiffer2.varScan.indel.canonical_annotated.2017-07-06.00-05-23dbsnp.stderr, log/vcfAnnotate/indel/indel_Pfeiffer2.varScan.indel.canonical_annotated.2017-07-06.00-05-23.1000g.log, log/vcfAnnotate/indel/indel_Pfeiffer2.varScan.indel.canonical_annotated.2017-07-06.00-05-23.mills_100g.log
    jobid: 4
    wildcards: sampleIndel=Pfeiffer2.varScan.indel.canonical_annotated, pathIndel=output/vcfGenUtil_varScan


localrule all:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated.cosmic_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.canonical_annotated.indel_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated.cosmic_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.canonical_annotated.indel_annotated.vcf
    jobid: 0

Job counts:
	count	jobs
	1	all
	2	bam2fastq_picard
	2	bam2mpileup
	2	bamALIGN_bwa
	4	canonical
	2	cosmic
	2	dbsnp
	4	fastq2GZ
	2	filteredBAM
	2	indel
	2	indexBAM
	2	markdupBAM
	4	mpileup2vcf_single
	2	sortBAM_biobambam
	33
```

## Snakemake cluster run output:
```
Provided cluster nodes: 100
Job counts:
        count   jobs
        1       all
        2       bam2fastq_picard
        2       bam2mpileup
        2       bamALIGN_bwa
        4       canonical
        2       cosmic
        2       dbsnp
        4       fastq2GZ
        2       filteredBAM
        2       indel
        2       indexBAM
        2       markdupBAM
        4       mpileup2vcf_single
        2       sortBAM_biobambam
        33

rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer3.bam
    output: output/fastq/Pfeiffer3.1.fastq, output/fastq/Pfeiffer3.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-06.00-34-33.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-06.00-34-33.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-06.00-34-33.stderr
    jobid: 31
    wildcards: sampleB2FP=Pfeiffer3

Submitted DRMAA job (jobid 8725556)

rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer2.bam
    output: output/fastq/Pfeiffer2.1.fastq, output/fastq/Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-06.00-34-33.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-06.00-34-33.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-06.00-34-33.stderr
    jobid: 32
    wildcards: sampleB2FP=Pfeiffer2

Submitted DRMAA job (jobid 8725557)
Finished job 31.
1 of 33 steps (3%) done

rule fastq2GZ:
    input: output/fastq/Pfeiffer3.1.fastq
    output: output/fastq/Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.1.2017-07-06.00-34-33.stderr
    jobid: 27
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer3.1

Submitted DRMAA job (jobid 8725603)

rule fastq2GZ:
    input: output/fastq/Pfeiffer3.2.fastq
    output: output/fastq/Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.2.2017-07-06.00-34-33.stderr
    jobid: 28
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer3.2

Submitted DRMAA job (jobid 8725604)
Finished job 32.
2 of 33 steps (6%) done

rule fastq2GZ:
    input: output/fastq/Pfeiffer2.2.fastq
    output: output/fastq/Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.2.2017-07-06.00-34-33.stderr
    jobid: 29
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer2.2

Submitted DRMAA job (jobid 8725611)

rule fastq2GZ:
    input: output/fastq/Pfeiffer2.1.fastq
    output: output/fastq/Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.1.2017-07-06.00-34-33.stderr
    jobid: 30
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer2.1

Submitted DRMAA job (jobid 8725612)
Finished job 28.
3 of 33 steps (9%) done
Finished job 29.
4 of 33 steps (12%) done
Finished job 27.
5 of 33 steps (15%) done

rule bamALIGN_bwa:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/fastq/Pfeiffer3.1.fastq.gz, output/fastq/Pfeiffer3.2.fastq.gz
    output: output/bam/Pfeiffer3_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-06.00-34-33.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-06.00-34-33.samtools.stderr
    jobid: 25
    wildcards: sampleBAB=Pfeiffer3

Submitted DRMAA job (jobid 8725632)
Finished job 30.
6 of 33 steps (18%) done

rule bamALIGN_bwa:
    input: /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/fastq/Pfeiffer2.1.fastq.gz, output/fastq/Pfeiffer2.2.fastq.gz
    output: output/bam/Pfeiffer2_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-06.00-34-33.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-06.00-34-33.samtools.stderr
    jobid: 26
    wildcards: sampleBAB=Pfeiffer2

Submitted DRMAA job (jobid 8725633)
Finished job 26.
7 of 33 steps (21%) done

rule sortBAM_biobambam:
    input: output/bam/Pfeiffer2_Aligned.out.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-06.00-34-33.bamsort.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-06.00-34-33.samtools.stderr
    jobid: 24
    wildcards: pathSBB=output/bam, sampleSBB=Pfeiffer2_Aligned.out

Submitted DRMAA job (jobid 8725686)
Finished job 25.
8 of 33 steps (24%) done

rule sortBAM_biobambam:
    input: output/bam/Pfeiffer3_Aligned.out.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-06.00-34-33.bamsort.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-06.00-34-33.samtools.stderr
    jobid: 23
    wildcards: pathSBB=output/bam, sampleSBB=Pfeiffer3_Aligned.out

Submitted DRMAA job (jobid 8725687)
Finished job 23.
9 of 33 steps (27%) done

rule filteredBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer3_Aligned.out_sorted.2017-07-06.00-34-33.stderr
    jobid: 21
    wildcards: pathFB=output/bam, sampleFB=Pfeiffer3_Aligned.out_sorted

Submitted DRMAA job (jobid 8725720)
Finished job 24.
10 of 33 steps (30%) done

rule filteredBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer2_Aligned.out_sorted.2017-07-06.00-34-33.stderr
    jobid: 22
    wildcards: pathFB=output/bam, sampleFB=Pfeiffer2_Aligned.out_sorted

Submitted DRMAA job (jobid 8725728)
Finished job 21.
11 of 33 steps (33%) done

rule markdupBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    output: output/metrics/Pfeiffer3_Aligned.out_sorted_filtered.dup_metrics, output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer3_Aligned.out_sorted_filtered.2017-07-06.00-34-33.biobammarkdup.stderr
    jobid: 19
    wildcards: sampleMDB=Pfeiffer3_Aligned.out_sorted_filtered, outputDIR=output

Submitted DRMAA job (jobid 8725750)
Finished job 22.
12 of 33 steps (36%) done

rule markdupBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    output: output/metrics/Pfeiffer2_Aligned.out_sorted_filtered.dup_metrics, output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer2_Aligned.out_sorted_filtered.2017-07-06.00-34-33.biobammarkdup.stderr
    jobid: 20
    wildcards: sampleMDB=Pfeiffer2_Aligned.out_sorted_filtered, outputDIR=output

Submitted DRMAA job (jobid 8725752)
Finished job 20.
13 of 33 steps (39%) done

rule indexBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam.bai, output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer2.2017-07-06.00-34-33.stderr
    jobid: 18
    wildcards: sampleIB=Pfeiffer2, outputDIR=output

Submitted DRMAA job (jobid 8725779)
Finished job 19.
14 of 33 steps (42%) done

rule indexBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam.bai, output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer3.2017-07-06.00-34-33.stderr
    jobid: 17
    wildcards: sampleIB=Pfeiffer3, outputDIR=output

Submitted DRMAA job (jobid 8725780)
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/Pfeiffer2.bam. Your Python build does not support it.
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/Pfeiffer2.bam.bai. Your Python build does not support it.
Finished job 18.
15 of 33 steps (45%) done

rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer2.bam.bai
    output: output/mpileup/Pfeiffer2.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-06.00-34-33.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-06.00-34-33.mpileup.stderr
    jobid: 15
    wildcards: sampleB2M=Pfeiffer2, chrB2M=

Submitted DRMAA job (jobid 8725791)
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/Pfeiffer3.bam. Your Python build does not support it.
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/Pfeiffer3.bam.bai. Your Python build does not support it.
Finished job 17.
16 of 33 steps (48%) done

rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, output/bam/Pfeiffer3.bam.bai
    output: output/mpileup/Pfeiffer3.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-06.00-34-33.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-06.00-34-33.mpileup.stderr
    jobid: 14
    wildcards: sampleB2M=Pfeiffer3, chrB2M=

Submitted DRMAA job (jobid 8725800)
Finished job 14.
17 of 33 steps (52%) done

rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr.indel.2017-07-06.00-34-33.stderr
    jobid: 10
    wildcards: chrMPU2VCFS=, sampleMPU2VCFS=Pfeiffer3, varTypeMPU2VCFS=indel

Submitted DRMAA job (jobid 8725878)

rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr.snp.2017-07-06.00-34-33.stderr
    jobid: 13
    wildcards: chrMPU2VCFS=, sampleMPU2VCFS=Pfeiffer3, varTypeMPU2VCFS=snp

Submitted DRMAA job (jobid 8725879)
Finished job 15.
18 of 33 steps (55%) done

rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr.indel.2017-07-06.00-34-33.stderr
    jobid: 11
    wildcards: chrMPU2VCFS=, sampleMPU2VCFS=Pfeiffer2, varTypeMPU2VCFS=indel

Submitted DRMAA job (jobid 8725882)

rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr.snp.2017-07-06.00-34-33.stderr
    jobid: 16
    wildcards: chrMPU2VCFS=, sampleMPU2VCFS=Pfeiffer2, varTypeMPU2VCFS=snp

Submitted DRMAA job (jobid 8725883)
Finished job 16.
19 of 33 steps (58%) done

rule canonical:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical.summary.genes.txt, output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical.summary.html
    log: log/vcfAnnotate/canonical/canonical_Pfeiffer2.varScan.snp.2017-07-06.00-34-33.stderr
    jobid: 12
    wildcards: sampleCAN=Pfeiffer2.varScan.snp, pathCAN=vcfGenUtil_varScan

Submitted DRMAA job (jobid 8725978)
Finished job 11.
20 of 33 steps (61%) done

rule canonical:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.canonical_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.canonical.summary.genes.txt, output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.canonical.summary.html
    log: log/vcfAnnotate/canonical/canonical_Pfeiffer2.varScan.indel.2017-07-06.00-34-33.stderr
    jobid: 7
    wildcards: sampleCAN=Pfeiffer2.varScan.indel, pathCAN=vcfGenUtil_varScan

Submitted DRMAA job (jobid 8725979)
Finished job 10.
21 of 33 steps (64%) done

rule canonical:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.canonical_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.canonical.summary.genes.txt, output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.canonical.summary.html
    log: log/vcfAnnotate/canonical/canonical_Pfeiffer3.varScan.indel.2017-07-06.00-34-33.stderr
    jobid: 6
    wildcards: sampleCAN=Pfeiffer3.varScan.indel, pathCAN=vcfGenUtil_varScan

Submitted DRMAA job (jobid 8725980)
Finished job 13.
22 of 33 steps (67%) done

rule canonical:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical.summary.genes.txt, output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical.summary.html
    log: log/vcfAnnotate/canonical/canonical_Pfeiffer3.varScan.snp.2017-07-06.00-34-33.stderr
    jobid: 9
    wildcards: sampleCAN=Pfeiffer3.varScan.snp, pathCAN=vcfGenUtil_varScan

Submitted DRMAA job (jobid 8725981)
Finished job 7.
23 of 33 steps (70%) done

rule indel:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.canonical_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.canonical_annotated.indel_annotated.vcf
    log: log/vcfAnnotate/indel/indel_Pfeiffer2.varScan.indel.canonical_annotated.2017-07-06.00-34-33.mills_100g.log, log/vcfAnnotate/indel/indel_Pfeiffer2.varScan.indel.canonical_annotated.2017-07-06.00-34-33.1000g.log, log/vcfAnnotate/indel/indel_Pfeiffer2.varScan.indel.canonical_annotated.2017-07-06.00-34-33dbsnp.stderr
    jobid: 3
    wildcards: pathIndel=output/vcfGenUtil_varScan, sampleIndel=Pfeiffer2.varScan.indel.canonical_annotated

Submitted DRMAA job (jobid 8726056)
Finished job 6.
24 of 33 steps (73%) done

rule indel:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.canonical_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.canonical_annotated.indel_annotated.vcf
    log: log/vcfAnnotate/indel/indel_Pfeiffer3.varScan.indel.canonical_annotated.2017-07-06.00-34-33.mills_100g.log, log/vcfAnnotate/indel/indel_Pfeiffer3.varScan.indel.canonical_annotated.2017-07-06.00-34-33.1000g.log, log/vcfAnnotate/indel/indel_Pfeiffer3.varScan.indel.canonical_annotated.2017-07-06.00-34-33dbsnp.stderr
    jobid: 2
    wildcards: pathIndel=output/vcfGenUtil_varScan, sampleIndel=Pfeiffer3.varScan.indel.canonical_annotated

Submitted DRMAA job (jobid 8726057)
Finished job 12.
25 of 33 steps (76%) done

rule dbsnp:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated.vcf
    log: log/vcfAnnotate/dbsnp/dbsnp_Pfeiffer2.varScan.snp.canonical_annotated.2017-07-06.00-34-33.stderr
    jobid: 8
    wildcards: pathDbSnp=output/vcfGenUtil_varScan, sampleDbSnp=Pfeiffer2.varScan.snp.canonical_annotated

Submitted DRMAA job (jobid 8726058)
Finished job 9.
26 of 33 steps (79%) done

rule dbsnp:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated.vcf
    log: log/vcfAnnotate/dbsnp/dbsnp_Pfeiffer3.varScan.snp.canonical_annotated.2017-07-06.00-34-33.stderr
    jobid: 5
    wildcards: pathDbSnp=output/vcfGenUtil_varScan, sampleDbSnp=Pfeiffer3.varScan.snp.canonical_annotated

Submitted DRMAA job (jobid 8726071)
Finished job 2.
27 of 33 steps (82%) done
Finished job 8.
28 of 33 steps (85%) done

rule cosmic:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated.cosmic_annotated.vcf
    log: log/vcfAnnotate/cosmic/cosmic_Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated.2017-07-06.00-34-33.stderr
    jobid: 4
    wildcards: pathCOS=output/vcfGenUtil_varScan, sampleCOS=Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated

Submitted DRMAA job (jobid 8726087)
Finished job 3.
29 of 33 steps (88%) done
Finished job 5.
30 of 33 steps (91%) done

rule cosmic:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated.cosmic_annotated.vcf
    log: log/vcfAnnotate/cosmic/cosmic_Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated.2017-07-06.00-34-33.stderr
    jobid: 1
    wildcards: pathCOS=output/vcfGenUtil_varScan, sampleCOS=Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated

Submitted DRMAA job (jobid 8726113)
Finished job 4.
31 of 33 steps (94%) done
Finished job 1.
32 of 33 steps (97%) done

localrule all:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated.cosmic_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.canonical_annotated.indel_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated.cosmic_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.canonical_annotated.indel_annotated.vcf
    jobid: 0

Finished job 0.
33 of 33 steps (100%) done

real    9m54.789s
user    0m1.852s
sys     0m0.347s
```
