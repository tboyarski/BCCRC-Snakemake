# 4-mergeBAM_PostFastq
This pipeline is to exemplify the default operations of this module. 

## Setting up the: Snakefile
Users must set the following submodule "call via" input requirements:

 * indexBAM

## Setting up the: YAML
Users must set the following "input/config.yaml" variables:

 * (Line 48) bamMergeRootDIR: output/bam
 * (Line 49) bamMergeSuffix: _Aligned.out_sorted_filtered
 * (Line 112) mergeFastqRootDIR: ''

## Setting up the: output directory

 * None

```
input/
    /rawBam
        Part1-PfeifferSubset.bam
        Part2-PfeifferSubset.bam
        Part3-PfeifferSubset.bam
```

```

## Snakemake cluster run output:
```
## Snakemake dry run output:
```

rule bam2fastq_picard:
    input: input/rawBam/Part2-PfeifferSubSet.bam
    output: output/fastq/Part2-PfeifferSubSet.1.fastq, output/fastq/Part2-PfeifferSubSet.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part2-PfeifferSubSet.2017-07-12.19-52-25.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part2-PfeifferSubSet.2017-07-12.19-52-25.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part2-PfeifferSubSet.2017-07-12.19-52-25.stderr
    jobid: 21
    wildcards: sampleB2FP=Part2-PfeifferSubSet


rule fastq2GZ:
    input: output/fastq/Part2-PfeifferSubSet.2.fastq
    output: output/fastq/Part2-PfeifferSubSet.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part2-PfeifferSubSet.2.2017-07-12.19-52-25.stderr
    jobid: 17
    wildcards: pathFGZ=output/fastq, sampleFGZ=Part2-PfeifferSubSet.2


rule fastq2GZ:
    input: output/fastq/Part2-PfeifferSubSet.1.fastq
    output: output/fastq/Part2-PfeifferSubSet.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part2-PfeifferSubSet.1.2017-07-12.19-52-25.stderr
    jobid: 18
    wildcards: pathFGZ=output/fastq, sampleFGZ=Part2-PfeifferSubSet.1


rule bamALIGN_bwa:
    input: /reference/genomes/9606/hg19a/genome/GRCh37-lite.fa, output/fastq/Part2-PfeifferSubSet.1.fastq.gz, output/fastq/Part2-PfeifferSubSet.2.fastq.gz, /reference/genomes/9606/hg19a/genome/GRCh37-lite.dict, /reference/genomes/9606/hg19a/genome/GRCh37-lite.fa.amb, /reference/genomes/9606/hg19a/genome/GRCh37-lite.fa.ann, /reference/genomes/9606/hg19a/genome/GRCh37-lite.fa.bwt, /reference/genomes/9606/hg19a/genome/GRCh37-lite.fa.fai, /reference/genomes/9606/hg19a/genome/GRCh37-lite.fa.pac, /reference/genomes/9606/hg19a/genome/GRCh37-lite.fa.sa
    output: output/bam/Part2-PfeifferSubSet_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Part2-PfeifferSubSet.2017-07-12.19-52-25.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Part2-PfeifferSubSet.2017-07-12.19-52-25.samtools.stderr
    jobid: 12
    wildcards: sampleBAB=Part2-PfeifferSubSet


rule sortBAM_biobambam:
    input: output/bam/Part2-PfeifferSubSet_Aligned.out.bam
    output: output/bam/Part2-PfeifferSubSet_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Part2-PfeifferSubSet_Aligned.out.2017-07-12.19-52-25.bamsort.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Part2-PfeifferSubSet_Aligned.out.2017-07-12.19-52-25.samtools.stderr
    jobid: 9
    wildcards: sampleSBB=Part2-PfeifferSubSet_Aligned.out, pathSBB=output/bam


rule filteredBAM:
    input: output/bam/Part2-PfeifferSubSet_Aligned.out_sorted.bam
    output: output/bam/Part2-PfeifferSubSet_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Part2-PfeifferSubSet_Aligned.out_sorted.2017-07-12.19-52-25.stderr
    jobid: 6
    wildcards: pathFB=output/bam, sampleFB=Part2-PfeifferSubSet_Aligned.out_sorted


rule bam2fastq_picard:
    input: input/rawBam/Part1-PfeifferSubSet.bam
    output: output/fastq/Part1-PfeifferSubSet.1.fastq, output/fastq/Part1-PfeifferSubSet.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part1-PfeifferSubSet.2017-07-12.19-52-25.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part1-PfeifferSubSet.2017-07-12.19-52-25.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part1-PfeifferSubSet.2017-07-12.19-52-25.stderr
    jobid: 20
    wildcards: sampleB2FP=Part1-PfeifferSubSet


rule fastq2GZ:
    input: output/fastq/Part1-PfeifferSubSet.2.fastq
    output: output/fastq/Part1-PfeifferSubSet.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part1-PfeifferSubSet.2.2017-07-12.19-52-25.stderr
    jobid: 16
    wildcards: pathFGZ=output/fastq, sampleFGZ=Part1-PfeifferSubSet.2


rule fastq2GZ:
    input: output/fastq/Part1-PfeifferSubSet.1.fastq
    output: output/fastq/Part1-PfeifferSubSet.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part1-PfeifferSubSet.1.2017-07-12.19-52-25.stderr
    jobid: 15
    wildcards: pathFGZ=output/fastq, sampleFGZ=Part1-PfeifferSubSet.1


rule bamALIGN_bwa:
    input: /reference/genomes/9606/hg19a/genome/GRCh37-lite.fa, output/fastq/Part1-PfeifferSubSet.1.fastq.gz, output/fastq/Part1-PfeifferSubSet.2.fastq.gz, /reference/genomes/9606/hg19a/genome/GRCh37-lite.dict, /reference/genomes/9606/hg19a/genome/GRCh37-lite.fa.amb, /reference/genomes/9606/hg19a/genome/GRCh37-lite.fa.ann, /reference/genomes/9606/hg19a/genome/GRCh37-lite.fa.bwt, /reference/genomes/9606/hg19a/genome/GRCh37-lite.fa.fai, /reference/genomes/9606/hg19a/genome/GRCh37-lite.fa.pac, /reference/genomes/9606/hg19a/genome/GRCh37-lite.fa.sa
    output: output/bam/Part1-PfeifferSubSet_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Part1-PfeifferSubSet.2017-07-12.19-52-25.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Part1-PfeifferSubSet.2017-07-12.19-52-25.samtools.stderr
    jobid: 11
    wildcards: sampleBAB=Part1-PfeifferSubSet


rule sortBAM_biobambam:
    input: output/bam/Part1-PfeifferSubSet_Aligned.out.bam
    output: output/bam/Part1-PfeifferSubSet_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Part1-PfeifferSubSet_Aligned.out.2017-07-12.19-52-25.bamsort.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Part1-PfeifferSubSet_Aligned.out.2017-07-12.19-52-25.samtools.stderr
    jobid: 8
    wildcards: sampleSBB=Part1-PfeifferSubSet_Aligned.out, pathSBB=output/bam


rule filteredBAM:
    input: output/bam/Part1-PfeifferSubSet_Aligned.out_sorted.bam
    output: output/bam/Part1-PfeifferSubSet_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Part1-PfeifferSubSet_Aligned.out_sorted.2017-07-12.19-52-25.stderr
    jobid: 5
    wildcards: pathFB=output/bam, sampleFB=Part1-PfeifferSubSet_Aligned.out_sorted


rule bam2fastq_picard:
    input: input/rawBam/Part3-PfeifferSubSet.bam
    output: output/fastq/Part3-PfeifferSubSet.1.fastq, output/fastq/Part3-PfeifferSubSet.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part3-PfeifferSubSet.2017-07-12.19-52-25.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part3-PfeifferSubSet.2017-07-12.19-52-25.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Part3-PfeifferSubSet.2017-07-12.19-52-25.stderr
    jobid: 19
    wildcards: sampleB2FP=Part3-PfeifferSubSet


rule fastq2GZ:
    input: output/fastq/Part3-PfeifferSubSet.2.fastq
    output: output/fastq/Part3-PfeifferSubSet.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part3-PfeifferSubSet.2.2017-07-12.19-52-25.stderr
    jobid: 13
    wildcards: pathFGZ=output/fastq, sampleFGZ=Part3-PfeifferSubSet.2


rule fastq2GZ:
    input: output/fastq/Part3-PfeifferSubSet.1.fastq
    output: output/fastq/Part3-PfeifferSubSet.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Part3-PfeifferSubSet.1.2017-07-12.19-52-25.stderr
    jobid: 14
    wildcards: pathFGZ=output/fastq, sampleFGZ=Part3-PfeifferSubSet.1


rule bamALIGN_bwa:
    input: /reference/genomes/9606/hg19a/genome/GRCh37-lite.fa, output/fastq/Part3-PfeifferSubSet.1.fastq.gz, output/fastq/Part3-PfeifferSubSet.2.fastq.gz, /reference/genomes/9606/hg19a/genome/GRCh37-lite.dict, /reference/genomes/9606/hg19a/genome/GRCh37-lite.fa.amb, /reference/genomes/9606/hg19a/genome/GRCh37-lite.fa.ann, /reference/genomes/9606/hg19a/genome/GRCh37-lite.fa.bwt, /reference/genomes/9606/hg19a/genome/GRCh37-lite.fa.fai, /reference/genomes/9606/hg19a/genome/GRCh37-lite.fa.pac, /reference/genomes/9606/hg19a/genome/GRCh37-lite.fa.sa
    output: output/bam/Part3-PfeifferSubSet_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Part3-PfeifferSubSet.2017-07-12.19-52-25.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Part3-PfeifferSubSet.2017-07-12.19-52-25.samtools.stderr
    jobid: 10
    wildcards: sampleBAB=Part3-PfeifferSubSet


rule sortBAM_biobambam:
    input: output/bam/Part3-PfeifferSubSet_Aligned.out.bam
    output: output/bam/Part3-PfeifferSubSet_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Part3-PfeifferSubSet_Aligned.out.2017-07-12.19-52-25.bamsort.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Part3-PfeifferSubSet_Aligned.out.2017-07-12.19-52-25.samtools.stderr
    jobid: 7
    wildcards: sampleSBB=Part3-PfeifferSubSet_Aligned.out, pathSBB=output/bam


rule filteredBAM:
    input: output/bam/Part3-PfeifferSubSet_Aligned.out_sorted.bam
    output: output/bam/Part3-PfeifferSubSet_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Part3-PfeifferSubSet_Aligned.out_sorted.2017-07-12.19-52-25.stderr
    jobid: 4
    wildcards: pathFB=output/bam, sampleFB=Part3-PfeifferSubSet_Aligned.out_sorted


rule mergeBAM:
    input: output/bam/Part1-PfeifferSubSet_Aligned.out_sorted_filtered.bam, output/bam/Part2-PfeifferSubSet_Aligned.out_sorted_filtered.bam, output/bam/Part3-PfeifferSubSet_Aligned.out_sorted_filtered.bam
    output: output/bam/PfeifferSubset_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/mergeBAM/mergeBAM.2017-07-12.19-52-25.stderr
    jobid: 3
    wildcards: sampleMB=PfeifferSubset


rule markdupBAM:
    input: output/bam/PfeifferSubset_Aligned.out_sorted_filtered.bam
    output: output/bam/PfeifferSubset_Aligned.out_sorted_filtered_markdup.bam, output/metrics/PfeifferSubset_Aligned.out_sorted_filtered.dup_metrics
    log: log/bamUtil/markdupBAM/markdupBAM_PfeifferSubset_Aligned.out_sorted_filtered.2017-07-12.19-52-25.biobammarkdup.stderr
    jobid: 2
    wildcards: sampleMDB=PfeifferSubset_Aligned.out_sorted_filtered, outputDIR=output


rule indexBAM:
    input: output/bam/PfeifferSubset_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/PfeifferSubset.bam.bai, output/bam/PfeifferSubset_Aligned.out_sorted_filtered_markdup.bam.bai, output/bam/PfeifferSubset.bam
    log: log/bamUtil/indexBAM/indexBAM_PfeifferSubset.2017-07-12.19-52-25.stderr
    jobid: 1
    wildcards: sampleIB=PfeifferSubset, outputDIR=output


localrule all:
    input: output/bam/PfeifferSubset_Aligned.out_sorted_filtered_markdup.bam.bai
    jobid: 0

Job counts:
	count	jobs
	1	all
	3	bam2fastq_picard
	3	bamALIGN_bwa
	6	fastq2GZ
	3	filteredBAM
	1	indexBAM
	1	markdupBAM
	1	mergeBAM
	3	sortBAM_biobambam
	22
