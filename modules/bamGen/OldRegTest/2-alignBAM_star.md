# 2-bamALIGN_star
This pipeline is to exemplify the default operations of this module. 

## Setting up the: Snakefile
Users must set the following submodule "call via" input requirements:

 * bamALIGN_star

## Setting up the: YAML
Users must set the following "input/config.yaml" variables:

 * (Line 75) SoftwareChoiceFlag: STAR

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
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-08-30.12-27-25.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-08-30.12-27-25.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-08-30.12-27-25.namesort.stderr
    jobid: 8
    wildcards: sampleB2FP=Pfeiffer2


rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer3.bam
    output: output/fastq/Pfeiffer3.1.fastq, output/fastq/Pfeiffer3.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-08-30.12-27-25.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-08-30.12-27-25.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-08-30.12-27-25.namesort.stderr
    jobid: 7
    wildcards: sampleB2FP=Pfeiffer3


rule fastq2GZ:
    input: output/fastq/Pfeiffer2.1.fastq
    output: output/fastq/Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.1.2017-08-30.12-27-25.stderr
    jobid: 5
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer2.1


rule fastq2GZ:
    input: output/fastq/Pfeiffer3.2.fastq
    output: output/fastq/Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.2.2017-08-30.12-27-25.stderr
    jobid: 3
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer3.2


rule fastq2GZ:
    input: output/fastq/Pfeiffer2.2.fastq
    output: output/fastq/Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.2.2017-08-30.12-27-25.stderr
    jobid: 6
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer2.2


rule bamALIGN_star:
    input: /genesis/extscratch/clc/references/star/GRCh37/ref_genome.fa.star.idx, output/fastq/Pfeiffer2.1.fastq.gz, output/fastq/Pfeiffer2.2.fastq.gz, /genesis/extscratch/clc/references/star/GRCh37/ref_annot.gtf
    output: output/bam/Pfeiffer2_Aligned.out.bam, output/bam/Pfeiffer2_Chimeric.out.junction, output/bam/junctions/Pfeiffer2_junctions.txt, output/bam/Pfeiffer2_Chimeric.out.sam, output/bam/Pfeiffer2_Log.final.out, output/bam/Pfeiffer2_Log.out, output/bam/Pfeiffer2_Log.progress.out, output/bam/Pfeiffer2_ReadsPerGene.out.tab, output/bam/Pfeiffer2_SJ.out.tab
    log: log/bamGen/bamALIGN_star/bamALIGN_star_Pfeiffer2.2017-08-30.12-27-25.stderr
    jobid: 2
    wildcards: sampleBAS=Pfeiffer2


rule fastq2GZ:
    input: output/fastq/Pfeiffer3.1.fastq
    output: output/fastq/Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.1.2017-08-30.12-27-25.stderr
    jobid: 4
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer3.1


rule bamALIGN_star:
    input: /genesis/extscratch/clc/references/star/GRCh37/ref_genome.fa.star.idx, output/fastq/Pfeiffer3.1.fastq.gz, output/fastq/Pfeiffer3.2.fastq.gz, /genesis/extscratch/clc/references/star/GRCh37/ref_annot.gtf
    output: output/bam/Pfeiffer3_Aligned.out.bam, output/bam/Pfeiffer3_Chimeric.out.junction, output/bam/junctions/Pfeiffer3_junctions.txt, output/bam/Pfeiffer3_Chimeric.out.sam, output/bam/Pfeiffer3_Log.final.out, output/bam/Pfeiffer3_Log.out, output/bam/Pfeiffer3_Log.progress.out, output/bam/Pfeiffer3_ReadsPerGene.out.tab, output/bam/Pfeiffer3_SJ.out.tab
    log: log/bamGen/bamALIGN_star/bamALIGN_star_Pfeiffer3.2017-08-30.12-27-25.stderr
    jobid: 1
    wildcards: sampleBAS=Pfeiffer3


localrule all:
    input: output/bam/Pfeiffer2_Aligned.out.bam, output/bam/Pfeiffer3_Aligned.out.bam
    jobid: 0

Job counts:
	count	jobs
	1	all
	2	bam2fastq_picard
	2	bamALIGN_star
	4	fastq2GZ
	9
```
