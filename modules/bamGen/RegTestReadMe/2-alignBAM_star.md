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
    input: input/rawBam/Pfeiffer3.bam
    output: output/fastq/Pfeiffer3.1.fastq, output/fastq/Pfeiffer3.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-06-30.16-05-13.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-06-30.16-05-13.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-06-30.16-05-13.vendor_failed_reads.log
    jobid: 8
    wildcards: sampleB2FP=Pfeiffer3


rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer2.bam
    output: output/fastq/Pfeiffer2.1.fastq, output/fastq/Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-06-30.16-05-13.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-06-30.16-05-13.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-06-30.16-05-13.vendor_failed_reads.log
    jobid: 7
    wildcards: sampleB2FP=Pfeiffer2


rule fastq2GZ:
    input: output/fastq/Pfeiffer2.2.fastq
    output: output/fastq/Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.2.2017-06-30.16-05-13.stderr
    jobid: 3
    wildcards: sampleFGZ=Pfeiffer2.2, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Pfeiffer2.1.fastq
    output: output/fastq/Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.1.2017-06-30.16-05-13.stderr
    jobid: 4
    wildcards: sampleFGZ=Pfeiffer2.1, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Pfeiffer3.2.fastq
    output: output/fastq/Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.2.2017-06-30.16-05-13.stderr
    jobid: 5
    wildcards: sampleFGZ=Pfeiffer3.2, pathFGZ=output/fastq


rule fastq2GZ:
    input: output/fastq/Pfeiffer3.1.fastq
    output: output/fastq/Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.1.2017-06-30.16-05-13.stderr
    jobid: 6
    wildcards: sampleFGZ=Pfeiffer3.1, pathFGZ=output/fastq


rule bamALIGN_star:
    input: /genesis/extscratch/clc/references/star/hg19/gencode.v19.annotation.gtf, /genesis/extscratch/clc/references/star/GRCh37/ref_genome.fa.star.idx, output/fastq/Pfeiffer3.1.fastq.gz, output/fastq/Pfeiffer3.2.fastq.gz
    output: output/bam/Pfeiffer3_Chimeric.out.sam, output/bam/Pfeiffer3_Log.final.out, output/bam/Pfeiffer3_Log.out, output/bam/Pfeiffer3_Log.progress.out, output/bam/Pfeiffer3_ReadsPerGene.out.tab, output/bam/Pfeiffer3_SJ.out.tab, output/bam/Pfeiffer3_Chimeric.out.junction, output/bam/junctions/Pfeiffer3_junctions.txt, output/bam/Pfeiffer3_Aligned.out.bam
    log: log/bamGen/alignBAM_star/alignBAM_star_Pfeiffer3.2017-06-30.16-05-13.stderr
    jobid: 2
    wildcards: sampleBAS=Pfeiffer3


rule bamALIGN_star:
    input: /genesis/extscratch/clc/references/star/hg19/gencode.v19.annotation.gtf, /genesis/extscratch/clc/references/star/GRCh37/ref_genome.fa.star.idx, output/fastq/Pfeiffer2.1.fastq.gz, output/fastq/Pfeiffer2.2.fastq.gz
    output: output/bam/Pfeiffer2_Chimeric.out.sam, output/bam/Pfeiffer2_Log.final.out, output/bam/Pfeiffer2_Log.out, output/bam/Pfeiffer2_Log.progress.out, output/bam/Pfeiffer2_ReadsPerGene.out.tab, output/bam/Pfeiffer2_SJ.out.tab, output/bam/Pfeiffer2_Chimeric.out.junction, output/bam/junctions/Pfeiffer2_junctions.txt, output/bam/Pfeiffer2_Aligned.out.bam
    log: log/bamGen/alignBAM_star/alignBAM_star_Pfeiffer2.2017-06-30.16-05-13.stderr
    jobid: 1
    wildcards: sampleBAS=Pfeiffer2


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

## Snakemake cluster run output:
```
Provided cluster nodes: 100
Job counts:
    count    jobs
    1    all
    2    bam2fastq_picard
    2    bamALIGN_star
    4    fastq2GZ
    9

rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer3.bam
    output: output/fastq/Pfeiffer3.1.fastq, output/fastq/Pfeiffer3.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-06-30.16-26-08.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-06-30.16-26-08.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-06-30.16-26-08.stderr
    jobid: 7
    wildcards: sampleB2FP=Pfeiffer3

Submitted DRMAA job (jobid 8627520)

rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer2.bam
    output: output/fastq/Pfeiffer2.1.fastq, output/fastq/Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-06-30.16-26-08.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-06-30.16-26-08.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-06-30.16-26-08.stderr
    jobid: 8
    wildcards: sampleB2FP=Pfeiffer2

Submitted DRMAA job (jobid 8627521)
Finished job 7.
1 of 9 steps (11%) done

rule fastq2GZ:
    input: output/fastq/Pfeiffer3.2.fastq
    output: output/fastq/Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.2.2017-06-30.16-26-08.stderr
    jobid: 3
    wildcards: sampleFGZ=Pfeiffer3.2, pathFGZ=output/fastq

Submitted DRMAA job (jobid 8627538)

rule fastq2GZ:
    input: output/fastq/Pfeiffer3.1.fastq
    output: output/fastq/Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.1.2017-06-30.16-26-08.stderr
    jobid: 4
    wildcards: sampleFGZ=Pfeiffer3.1, pathFGZ=output/fastq

Submitted DRMAA job (jobid 8627539)
Finished job 8.
2 of 9 steps (22%) done

rule fastq2GZ:
    input: output/fastq/Pfeiffer2.1.fastq
    output: output/fastq/Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.1.2017-06-30.16-26-08.stderr
    jobid: 5
    wildcards: sampleFGZ=Pfeiffer2.1, pathFGZ=output/fastq

Submitted DRMAA job (jobid 8627549)

rule fastq2GZ:
    input: output/fastq/Pfeiffer2.2.fastq
    output: output/fastq/Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.2.2017-06-30.16-26-08.stderr
    jobid: 6
    wildcards: sampleFGZ=Pfeiffer2.2, pathFGZ=output/fastq

Submitted DRMAA job (jobid 8627550)
Finished job 4.
3 of 9 steps (33%) done
Finished job 5.
4 of 9 steps (44%) done
Finished job 6.
5 of 9 steps (56%) done

rule bamALIGN_star:
    input: /genesis/extscratch/clc/references/star/GRCh37/ref_genome.fa.star.idx, output/fastq/Pfeiffer2.1.fastq.gz, output/fastq/Pfeiffer2.2.fastq.gz, /genesis/extscratch/clc/references/star/hg19/gencode.v19.annotation.gtf
    output: output/bam/junctions/Pfeiffer2_junctions.txt, output/bam/Pfeiffer2_Chimeric.out.sam, output/bam/Pfeiffer2_Log.final.out, output/bam/Pfeiffer2_Log.out, output/bam/Pfeiffer2_Log.progress.out, output/bam/Pfeiffer2_ReadsPerGene.out.tab, output/bam/Pfeiffer2_SJ.out.tab, output/bam/Pfeiffer2_Chimeric.out.junction, output/bam/Pfeiffer2_Aligned.out.bam
    log: log/bamGen/alignBAM_star/alignBAM_star_Pfeiffer2.2017-06-30.16-26-08.stderr
    jobid: 2
    wildcards: sampleBAS=Pfeiffer2

Submitted DRMAA job (jobid 8627566)
Finished job 3.
6 of 9 steps (67%) done

rule bamALIGN_star:
    input: /genesis/extscratch/clc/references/star/GRCh37/ref_genome.fa.star.idx, output/fastq/Pfeiffer3.1.fastq.gz, output/fastq/Pfeiffer3.2.fastq.gz, /genesis/extscratch/clc/references/star/hg19/gencode.v19.annotation.gtf
    output: output/bam/junctions/Pfeiffer3_junctions.txt, output/bam/Pfeiffer3_Chimeric.out.sam, output/bam/Pfeiffer3_Log.final.out, output/bam/Pfeiffer3_Log.out, output/bam/Pfeiffer3_Log.progress.out, output/bam/Pfeiffer3_ReadsPerGene.out.tab, output/bam/Pfeiffer3_SJ.out.tab, output/bam/Pfeiffer3_Chimeric.out.junction, output/bam/Pfeiffer3_Aligned.out.bam
    log: log/bamGen/alignBAM_star/alignBAM_star_Pfeiffer3.2017-06-30.16-26-08.stderr
    jobid: 1
    wildcards: sampleBAS=Pfeiffer3

Submitted DRMAA job (jobid 8627567)
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/junctions/Pfeiffer2_junctions.txt. Your Python build does not support it.
Finished job 2.
7 of 9 steps (78%) done
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/junctions/Pfeiffer3_junctions.txt. Your Python build does not support it.
Finished job 1.
8 of 9 steps (89%) done

localrule all:
    input: output/bam/Pfeiffer2_Aligned.out.bam, output/bam/Pfeiffer3_Aligned.out.bam
    jobid: 0

Finished job 0.
9 of 9 steps (100%) done
```
