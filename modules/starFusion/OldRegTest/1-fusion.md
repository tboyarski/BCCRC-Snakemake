# 1-fusion
This pipeline is to exemplify the default operations of this module.

## Setting up the: Snakefile
Users must set the following submodule "call via" input requirements:

 * fusion

## Setting up the: YAML
Users must set the following "input/config.yaml" variables:

 * (Line 103) SoftwareChoiceFLAG_alignBAM = STAR

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
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-10.17-55-11.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-10.17-55-11.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-10.17-55-11.namesort.stderr
    jobid: 5
    wildcards: sampleB2FP=Pfeiffer2


rule fastq2GZ:
    input: output/fastq/Pfeiffer2.1.fastq
    output: output/fastq/Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.1.2017-07-10.17-55-11.stderr
    jobid: 3
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer2.1


rule fastq2GZ:
    input: output/fastq/Pfeiffer2.2.fastq
    output: output/fastq/Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.2.2017-07-10.17-55-11.stderr
    jobid: 4
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer2.2


rule bamALIGN_star:
    input: /genesis/extscratch/clc/references/star/GRCh37/ref_genome.fa.star.idx, output/fastq/Pfeiffer2.1.fastq.gz, output/fastq/Pfeiffer2.2.fastq.gz, /genesis/extscratch/clc/references/star/hg19/gencode.v19.annotation.gtf
    output: output/bam/Pfeiffer2_Aligned.out.bam, output/bam/Pfeiffer2_Chimeric.out.junction, output/bam/junctions/Pfeiffer2_junctions.txt, output/bam/Pfeiffer2_Chimeric.out.sam, output/bam/Pfeiffer2_Log.final.out, output/bam/Pfeiffer2_Log.out, output/bam/Pfeiffer2_Log.progress.out, output/bam/Pfeiffer2_ReadsPerGene.out.tab, output/bam/Pfeiffer2_SJ.out.tab
    log: log/bamGen/alignBAM_star/alignBAM_star_Pfeiffer2.2017-07-10.17-55-11.stderr
    jobid: 2
    wildcards: sampleBAS=Pfeiffer2


rule fusion:
    input: output/bam/junctions/Pfeiffer2_junctions.txt, /extscratch/clc/references/star/GRCh37
    output: output/starFusion/fusions/Pfeiffer2_fusions.txt, output/starFusion/Pfeiffer2/star-fusion.fusion_candidates.final.abridged
    log: log/starFusion/starFusion/fusion_Pfeiffer2.2017-07-10.17-55-11.stderr
    jobid: 1
    wildcards: sampleSAF=Pfeiffer2


localrule all:
    input: output/starFusion/fusions/Pfeiffer2_fusions.txt
    jobid: 0

Job counts:
	count	jobs
	1	all
	1	bam2fastq_picard
	1	bamALIGN_star
	2	fastq2GZ
	1	fusion
	6
```

## Snakemake cluster run output:
```
Provided cluster nodes: 100
Job counts:
    count    jobs
    1    all
    1    bam2fastq_picard
    1    bamALIGN_star
    2    fastq2GZ
    1    fusion
    6

rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer2.bam
    output: output/fastq/Pfeiffer2.1.fastq, output/fastq/Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-10.17-59-37.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-10.17-59-37.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-10.17-59-37.namesort.stderr
    jobid: 5
    wildcards: sampleB2FP=Pfeiffer2

Submitted DRMAA job (jobid 8891991)
Finished job 5.
1 of 6 steps (17%) done

rule fastq2GZ:
    input: output/fastq/Pfeiffer2.1.fastq
    output: output/fastq/Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.1.2017-07-10.17-59-37.stderr
    jobid: 3
    wildcards: sampleFGZ=Pfeiffer2.1, pathFGZ=output/fastq

Submitted DRMAA job (jobid 8892002)

rule fastq2GZ:
    input: output/fastq/Pfeiffer2.2.fastq
    output: output/fastq/Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.2.2017-07-10.17-59-37.stderr
    jobid: 4
    wildcards: sampleFGZ=Pfeiffer2.2, pathFGZ=output/fastq

Submitted DRMAA job (jobid 8892003)
Finished job 4.
2 of 6 steps (33%) done
Finished job 3.
3 of 6 steps (50%) done

rule bamALIGN_star:
    input: /genesis/extscratch/clc/references/star/hg19/gencode.v19.annotation.gtf, output/fastq/Pfeiffer2.1.fastq.gz, output/fastq/Pfeiffer2.2.fastq.gz, /genesis/extscratch/clc/references/star/GRCh37/ref_genome.fa.star.idx
    output: output/bam/Pfeiffer2_Aligned.out.bam, output/bam/junctions/Pfeiffer2_junctions.txt, output/bam/Pfeiffer2_Chimeric.out.sam, output/bam/Pfeiffer2_Log.final.out, output/bam/Pfeiffer2_Log.out, output/bam/Pfeiffer2_Log.progress.out, output/bam/Pfeiffer2_ReadsPerGene.out.tab, output/bam/Pfeiffer2_SJ.out.tab, output/bam/Pfeiffer2_Chimeric.out.junction
    log: log/bamGen/alignBAM_star/alignBAM_star_Pfeiffer2.2017-07-10.17-59-37.stderr
    jobid: 2
    wildcards: sampleBAS=Pfeiffer2

Submitted DRMAA job (jobid 8892015)
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/bam/junctions/Pfeiffer2_junctions.txt. Your Python build does not support it.
Finished job 2.
4 of 6 steps (67%) done

rule fusion:
    input: output/bam/junctions/Pfeiffer2_junctions.txt, /extscratch/clc/references/star/GRCh37
    output: output/starFusion/fusions/Pfeiffer2_fusions.txt, output/starFusion/Pfeiffer2/star-fusion.fusion_candidates.final.abridged
    log: log/starFusion/starFusion/fusion_Pfeiffer2.2017-07-10.17-59-37.stderr
    jobid: 1
    wildcards: sampleSAF=Pfeiffer2

Submitted DRMAA job (jobid 8892408)
touch: invalid option -- h
Try `touch --help' for more information.
Unable to set utime on symlink output/starFusion/fusions/Pfeiffer2_fusions.txt. Your Python build does not support it.
Finished job 1.
5 of 6 steps (83%) done

localrule all:
    input: output/starFusion/fusions/Pfeiffer2_fusions.txt
    jobid: 0

Finished job 0.
6 of 6 steps (100%) done

real    28m7.994s
user    0m1.178s
sys    0m0.214s
```
