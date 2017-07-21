# 3-PreFastqBamMerge2MergedVcfTable
This pipeline is to exemplify the default operations of this module.

**NOTE** This does not currently work due to the inability of the raw sample files to be merged.
Current testing is just using the same '.bam' file, copied multiple times, to generate multiple
identical pars. The identical nature of the '.bam' files is problematic. Need to re-run this 
regression test once actual lane specific (non-identical) '.bam' files can be used.


## Setting up the: buildPipe.py
Users must set the following variable:

 * (Line 13) TYPE = "single"

## Setting up the: Snakefile
Users must set the following submodule "call via" input requirements:

 * getVcfTable

## Setting up the: YAML
Users must set the following "input/config.yaml" variables:

 * (Line 15) intermediateKEEP = True
 * (Line 158) bamMergeRootDIR = input/rawBam
 * (Line 159) bamMergeSuffix = ''
 * (Line 18) chrLIST: ['1','2','3','4']

## Setting up the: output directory

 * None

```
input
    /rawBam
        Pfeiffer2.bam
        Pfeiffer3.bam
```
```

## Snakemake cluster run output:
```

## Snakemake dry run output:
```

rule mergeBAM:
    input: input/rawBam/Part1-Pfeiffer2.bam, input/rawBam/Part2-Pfeiffer2.bam, input/rawBam/Part3-Pfeiffer2.bam, input/rawBam/Part4-Pfeiffer2.bam
    output: input/rawBam/Pfeiffer2.bam
    log: log/bamUtil/mergeBAM/mergeBAM.2017-07-07.16-19-08.stderr
    jobid: 60
    wildcards: sampleMB=Pfeiffer2


rule mergeBAM:
    input: input/rawBam/Part1-Pfeiffer3.bam, input/rawBam/Part2-Pfeiffer3.bam, input/rawBam/Part3-Pfeiffer3.bam
    output: input/rawBam/Pfeiffer3.bam
    log: log/bamUtil/mergeBAM/mergeBAM.2017-07-07.16-19-08.stderr
    jobid: 59
    wildcards: sampleMB=Pfeiffer3


rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer2.bam
    output: output/fastq/Pfeiffer2.1.fastq, output/fastq/Pfeiffer2.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-07.16-19-08.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-07.16-19-08.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer2.2017-07-07.16-19-08.stderr
    jobid: 58
    wildcards: sampleB2FP=Pfeiffer2


rule bam2fastq_picard:
    input: input/rawBam/Pfeiffer3.bam
    output: output/fastq/Pfeiffer3.1.fastq, output/fastq/Pfeiffer3.2.fastq
    log: log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-07.16-19-08.namesort.stderr, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-07.16-19-08.vendor_failed_reads.log, log/fastqGen/bam2fastq_picard/bam2fastq_picard_Pfeiffer3.2017-07-07.16-19-08.stderr
    jobid: 57
    wildcards: sampleB2FP=Pfeiffer3


rule fastq2GZ:
    input: output/fastq/Pfeiffer2.1.fastq
    output: output/fastq/Pfeiffer2.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.1.2017-07-07.16-19-08.stderr
    jobid: 55
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer2.1


rule fastq2GZ:
    input: output/fastq/Pfeiffer3.2.fastq
    output: output/fastq/Pfeiffer3.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.2.2017-07-07.16-19-08.stderr
    jobid: 53
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer3.2


rule fastq2GZ:
    input: output/fastq/Pfeiffer2.2.fastq
    output: output/fastq/Pfeiffer2.2.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer2.2.2017-07-07.16-19-08.stderr
    jobid: 56
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer2.2


rule fastq2GZ:
    input: output/fastq/Pfeiffer3.1.fastq
    output: output/fastq/Pfeiffer3.1.fastq.gz
    log: log/fastqUtil/fastq2GZ/fastq2GZ_Pfeiffer3.1.2017-07-07.16-19-08.stderr
    jobid: 54
    wildcards: pathFGZ=output/fastq, sampleFGZ=Pfeiffer3.1


rule bamALIGN_bwa:
    input: output/fastq/Pfeiffer2.1.fastq.gz, output/fastq/Pfeiffer2.2.fastq.gz, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa
    output: output/bam/Pfeiffer2_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-07.16-19-08.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer2.2017-07-07.16-19-08.samtools.stderr
    jobid: 52
    wildcards: sampleBAB=Pfeiffer2


rule bamALIGN_bwa:
    input: output/fastq/Pfeiffer3.1.fastq.gz, output/fastq/Pfeiffer3.2.fastq.gz, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.dict, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.amb, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.ann, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.bwt, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.fai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.pac, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa.sa
    output: output/bam/Pfeiffer3_Aligned.out.bam
    log: log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-07.16-19-08.bwa.stderr, log/bamGen/bamALIGN_bwa/bamALIGN_bwa_Pfeiffer3.2017-07-07.16-19-08.samtools.stderr
    jobid: 51
    wildcards: sampleBAB=Pfeiffer3


rule sortBAM_biobambam:
    input: output/bam/Pfeiffer3_Aligned.out.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-07.16-19-08.samtools.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer3_Aligned.out.2017-07-07.16-19-08.bamsort.stderr
    jobid: 49
    wildcards: sampleSBB=Pfeiffer3_Aligned.out, pathSBB=output/bam


rule sortBAM_biobambam:
    input: output/bam/Pfeiffer2_Aligned.out.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted.bam
    log: log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-07.16-19-08.samtools.stderr, log/bamUtil/sortBAM_biobambam/sortBAM_biobambam_Pfeiffer2_Aligned.out.2017-07-07.16-19-08.bamsort.stderr
    jobid: 50
    wildcards: sampleSBB=Pfeiffer2_Aligned.out, pathSBB=output/bam


rule filteredBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer3_Aligned.out_sorted.2017-07-07.16-19-08.stderr
    jobid: 47
    wildcards: pathFB=output/bam, sampleFB=Pfeiffer3_Aligned.out_sorted


rule filteredBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    log: log/bamUtil/filteredBAM/filteredBAM_Pfeiffer2_Aligned.out_sorted.2017-07-07.16-19-08.stderr
    jobid: 48
    wildcards: pathFB=output/bam, sampleFB=Pfeiffer2_Aligned.out_sorted


rule markdupBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam, output/metrics/Pfeiffer2_Aligned.out_sorted_filtered.dup_metrics
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer2_Aligned.out_sorted_filtered.2017-07-07.16-19-08.biobammarkdup.stderr
    jobid: 46
    wildcards: sampleMDB=Pfeiffer2_Aligned.out_sorted_filtered, outputDIR=output


rule markdupBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam, output/metrics/Pfeiffer3_Aligned.out_sorted_filtered.dup_metrics
    log: log/bamUtil/markdupBAM/markdupBAM_Pfeiffer3_Aligned.out_sorted_filtered.2017-07-07.16-19-08.biobammarkdup.stderr
    jobid: 45
    wildcards: sampleMDB=Pfeiffer3_Aligned.out_sorted_filtered, outputDIR=output


rule indexBAM:
    input: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer2_Aligned.out_sorted_filtered_markdup.bam.bai, output/bam/Pfeiffer2.bam.bai, output/bam/Pfeiffer2.bam
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer2.2017-07-07.16-19-08.stderr
    jobid: 44
    wildcards: outputDIR=output, sampleIB=Pfeiffer2


rule indexBAM:
    input: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam
    output: output/bam/Pfeiffer3_Aligned.out_sorted_filtered_markdup.bam.bai, output/bam/Pfeiffer3.bam.bai, output/bam/Pfeiffer3.bam
    log: log/bamUtil/indexBAM/indexBAM_Pfeiffer3.2017-07-07.16-19-08.stderr
    jobid: 43
    wildcards: outputDIR=output, sampleIB=Pfeiffer3


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_2.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-19-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-19-08.mpileup.stderr
    jobid: 28
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-19-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-19-08.mpileup.stderr
    jobid: 29
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_1


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_3.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-19-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-19-08.mpileup.stderr
    jobid: 30
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_1.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-19-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-19-08.mpileup.stderr
    jobid: 37
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_1


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_2.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-19-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-19-08.mpileup.stderr
    jobid: 38
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_2


rule bam2mpileup:
    input: output/bam/Pfeiffer3.bam, output/bam/Pfeiffer3.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer3_4.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-19-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer3.2017-07-07.16-19-08.mpileup.stderr
    jobid: 27
    wildcards: sampleB2M=Pfeiffer3, chrB2M=_4


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_3.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-19-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-19-08.mpileup.stderr
    jobid: 36
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_3


rule bam2mpileup:
    input: output/bam/Pfeiffer2.bam, output/bam/Pfeiffer2.bam.bai, /genesis/extscratch/clc/references/genomes/gsc/bwa-0.7.5a/GRCh37-lite.fa
    output: output/mpileup/Pfeiffer2_4.mpileup
    log: log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-19-08.view.stderr, log/mpileupGen/bam2mpileup/bam2mpileup_Pfeiffer2.2017-07-07.16-19-08.mpileup.stderr
    jobid: 35
    wildcards: sampleB2M=Pfeiffer2, chrB2M=_4


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_1.snp.2017-07-07.16-19-08.stderr
    jobid: 42
    wildcards: varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_1


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_2.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_2.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_2.snp.2017-07-07.16-19-08.stderr
    jobid: 32
    wildcards: varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_2.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_2.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_2.snp.2017-07-07.16-19-08.stderr
    jobid: 40
    wildcards: varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_4.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_4.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_4.snp.2017-07-07.16-19-08.stderr
    jobid: 31
    wildcards: varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_4


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_3.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_3.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_3.snp.2017-07-07.16-19-08.stderr
    jobid: 33
    wildcards: varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_4.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_4.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_4.snp.2017-07-07.16-19-08.stderr
    jobid: 41
    wildcards: varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_4


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_3.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_3.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_3.snp.2017-07-07.16-19-08.stderr
    jobid: 39
    wildcards: varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_1.varScan.snp.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_1.snp.2017-07-07.16-19-08.stderr
    jobid: 34
    wildcards: varTypeMPU2VCFS=snp, sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_1


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_1.indel.2017-07-07.16-19-08.stderr
    jobid: 24
    wildcards: varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_1


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_2.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_2.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_2.indel.2017-07-07.16-19-08.stderr
    jobid: 25
    wildcards: varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_2


rule mergeVCF:
    input: output/vcfGenUtil_varScan/Pfeiffer3_1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_2.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_3.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer3_4.varScan.snp.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.vcf
    log: log/vcfUtil/mergeVCF/mergeVCF_Pfeiffer3.varScan.snp.2017-07-07.16-19-07.stderr
    jobid: 21
    wildcards: varTypeMVCF=snp, vcfProgramMVCF=varScan, sampleMVCF=Pfeiffer3, pathMV=output/vcfGenUtil_varScan


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_2.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_2.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_2.indel.2017-07-07.16-19-08.stderr
    jobid: 18
    wildcards: varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_2


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_3.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_3.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_3.indel.2017-07-07.16-19-08.stderr
    jobid: 23
    wildcards: varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_3.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_3.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_3.indel.2017-07-07.16-19-08.stderr
    jobid: 20
    wildcards: varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_3


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_4.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_4.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_4.indel.2017-07-07.16-19-08.stderr
    jobid: 17
    wildcards: varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_4


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer2_4.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer2_4.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer2_chr_4.indel.2017-07-07.16-19-08.stderr
    jobid: 22
    wildcards: varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer2, chrMPU2VCFS=_4


rule mpileup2vcf_single:
    input: output/mpileup/Pfeiffer3_1.mpileup
    output: output/vcfGenUtil_varScan/Pfeiffer3_1.varScan.indel.vcf
    log: log/vcfGenUtil_varScan/mpileup2vcf_pair/mpileup2vcf_pair_Pfeiffer3_chr_1.indel.2017-07-07.16-19-08.stderr
    jobid: 19
    wildcards: varTypeMPU2VCFS=indel, sampleMPU2VCFS=Pfeiffer3, chrMPU2VCFS=_1


rule mergeVCF:
    input: output/vcfGenUtil_varScan/Pfeiffer2_1.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_2.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_3.varScan.snp.vcf, output/vcfGenUtil_varScan/Pfeiffer2_4.varScan.snp.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.vcf
    log: log/vcfUtil/mergeVCF/mergeVCF_Pfeiffer2.varScan.snp.2017-07-07.16-19-07.stderr
    jobid: 26
    wildcards: varTypeMVCF=snp, vcfProgramMVCF=varScan, sampleMVCF=Pfeiffer2, pathMV=output/vcfGenUtil_varScan


rule canonical:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical.summary.genes.txt, output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical.summary.html
    log: log/vcfGenUtil_varScan/canonical/canonical_Pfeiffer2.varScan.snp.2017-07-07.16-19-07.stderr
    jobid: 16
    wildcards: sampleCAN=Pfeiffer2.varScan.snp, pathCAN=vcfGenUtil_varScan


rule mergeVCF:
    input: output/vcfGenUtil_varScan/Pfeiffer3_1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_2.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_3.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer3_4.varScan.indel.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.vcf
    log: log/vcfUtil/mergeVCF/mergeVCF_Pfeiffer3.varScan.indel.2017-07-07.16-19-07.stderr
    jobid: 13
    wildcards: varTypeMVCF=indel, vcfProgramMVCF=varScan, sampleMVCF=Pfeiffer3, pathMV=output/vcfGenUtil_varScan


rule canonical:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical.summary.genes.txt, output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical.summary.html
    log: log/vcfGenUtil_varScan/canonical/canonical_Pfeiffer3.varScan.snp.2017-07-07.16-19-07.stderr
    jobid: 14
    wildcards: sampleCAN=Pfeiffer3.varScan.snp, pathCAN=vcfGenUtil_varScan


rule mergeVCF:
    input: output/vcfGenUtil_varScan/Pfeiffer2_1.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_2.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_3.varScan.indel.vcf, output/vcfGenUtil_varScan/Pfeiffer2_4.varScan.indel.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.vcf
    log: log/vcfUtil/mergeVCF/mergeVCF_Pfeiffer2.varScan.indel.2017-07-07.16-19-07.stderr
    jobid: 15
    wildcards: varTypeMVCF=indel, vcfProgramMVCF=varScan, sampleMVCF=Pfeiffer2, pathMV=output/vcfGenUtil_varScan


rule canonical:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.canonical_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.canonical.summary.genes.txt, output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.canonical.summary.html
    log: log/vcfGenUtil_varScan/canonical/canonical_Pfeiffer2.varScan.indel.2017-07-07.16-19-07.stderr
    jobid: 11
    wildcards: sampleCAN=Pfeiffer2.varScan.indel, pathCAN=vcfGenUtil_varScan


rule dbsnp:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated.vcf
    log: log/vcfGenUtil_varScan/dbsnp/dbsnp_Pfeiffer3.varScan.snp.canonical_annotated.2017-07-07.16-19-07.stderr
    jobid: 10
    wildcards: sampleDbSnp=Pfeiffer3.varScan.snp.canonical_annotated, pathDbSnp=output/vcfGenUtil_varScan


rule canonical:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.canonical_annotated.vcf, output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.canonical.summary.genes.txt, output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.canonical.summary.html
    log: log/vcfGenUtil_varScan/canonical/canonical_Pfeiffer3.varScan.indel.2017-07-07.16-19-07.stderr
    jobid: 9
    wildcards: sampleCAN=Pfeiffer3.varScan.indel, pathCAN=vcfGenUtil_varScan


rule dbsnp:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated.vcf
    log: log/vcfGenUtil_varScan/dbsnp/dbsnp_Pfeiffer2.varScan.snp.canonical_annotated.2017-07-07.16-19-07.stderr
    jobid: 12
    wildcards: sampleDbSnp=Pfeiffer2.varScan.snp.canonical_annotated, pathDbSnp=output/vcfGenUtil_varScan


rule cosmic:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated.cosmic_annotated.vcf
    log: log/vcfGenUtil_varScan/cosmic/cosmic_Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated.2017-07-07.16-19-07.stderr
    jobid: 6
    wildcards: sampleCOS=Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated, pathCOS=output/vcfGenUtil_varScan


rule indel:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.canonical_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.canonical_annotated.indel_annotated.vcf
    log: log/vcfGenUtil_varScan/indel/indel_Pfeiffer2.varScan.indel.canonical_annotated.2017-07-07.16-19-07dbsnp.stderr, log/vcfGenUtil_varScan/indel/indel_Pfeiffer2.varScan.indel.canonical_annotated.2017-07-07.16-19-07.1000g.log, log/vcfGenUtil_varScan/indel/indel_Pfeiffer2.varScan.indel.canonical_annotated.2017-07-07.16-19-07.mills_100g.log
    jobid: 7
    wildcards: pathIndel=output/vcfGenUtil_varScan, sampleIndel=Pfeiffer2.varScan.indel.canonical_annotated


rule cosmic:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated.cosmic_annotated.vcf
    log: log/vcfGenUtil_varScan/cosmic/cosmic_Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated.2017-07-07.16-19-07.stderr
    jobid: 8
    wildcards: sampleCOS=Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated, pathCOS=output/vcfGenUtil_varScan


rule indel:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.canonical_annotated.vcf
    output: output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.canonical_annotated.indel_annotated.vcf
    log: log/vcfGenUtil_varScan/indel/indel_Pfeiffer3.varScan.indel.canonical_annotated.2017-07-07.16-19-07dbsnp.stderr, log/vcfGenUtil_varScan/indel/indel_Pfeiffer3.varScan.indel.canonical_annotated.2017-07-07.16-19-07.1000g.log, log/vcfGenUtil_varScan/indel/indel_Pfeiffer3.varScan.indel.canonical_annotated.2017-07-07.16-19-07.mills_100g.log
    jobid: 5
    wildcards: pathIndel=output/vcfGenUtil_varScan, sampleIndel=Pfeiffer3.varScan.indel.canonical_annotated


rule getVcfTable:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.indel.canonical_annotated.indel_annotated.vcf
    output: output/vcfGenUtil_varScan/tables/Pfeiffer3.varScan.indel.canonical_annotated.indel_annotated.txt
    log: log/vcfUtil/vcfGetTable_annotateVcfDIR/vcfGetTable_annotateVcfDIR_{wildcards.sampleVCFGT}.2017-07-07.16-19-07.OnePerLine.stderr, log/vcfUtil/vcfGetTable_annotateVcfDIR/vcfGetTable_annotateVcfDIR_{wildcards.sampleVCFGT}.2017-07-07.16-19-07.stderr
    jobid: 1
    wildcards: pathGVCFT=output/vcfGenUtil_varScan, sampleGVCFT=Pfeiffer3.varScan.indel.canonical_annotated.indel_annotated


rule getVcfTable:
    input: output/vcfGenUtil_varScan/Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated.cosmic_annotated.vcf
    output: output/vcfGenUtil_varScan/tables/Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated.cosmic_annotated.txt
    log: log/vcfUtil/vcfGetTable_annotateVcfDIR/vcfGetTable_annotateVcfDIR_{wildcards.sampleVCFGT}.2017-07-07.16-19-07.OnePerLine.stderr, log/vcfUtil/vcfGetTable_annotateVcfDIR/vcfGetTable_annotateVcfDIR_{wildcards.sampleVCFGT}.2017-07-07.16-19-07.stderr
    jobid: 2
    wildcards: pathGVCFT=output/vcfGenUtil_varScan, sampleGVCFT=Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated.cosmic_annotated


rule getVcfTable:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated.cosmic_annotated.vcf
    output: output/vcfGenUtil_varScan/tables/Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated.cosmic_annotated.txt
    log: log/vcfUtil/vcfGetTable_annotateVcfDIR/vcfGetTable_annotateVcfDIR_{wildcards.sampleVCFGT}.2017-07-07.16-19-07.OnePerLine.stderr, log/vcfUtil/vcfGetTable_annotateVcfDIR/vcfGetTable_annotateVcfDIR_{wildcards.sampleVCFGT}.2017-07-07.16-19-07.stderr
    jobid: 4
    wildcards: pathGVCFT=output/vcfGenUtil_varScan, sampleGVCFT=Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated.cosmic_annotated


rule getVcfTable:
    input: output/vcfGenUtil_varScan/Pfeiffer2.varScan.indel.canonical_annotated.indel_annotated.vcf
    output: output/vcfGenUtil_varScan/tables/Pfeiffer2.varScan.indel.canonical_annotated.indel_annotated.txt
    log: log/vcfUtil/vcfGetTable_annotateVcfDIR/vcfGetTable_annotateVcfDIR_{wildcards.sampleVCFGT}.2017-07-07.16-19-07.OnePerLine.stderr, log/vcfUtil/vcfGetTable_annotateVcfDIR/vcfGetTable_annotateVcfDIR_{wildcards.sampleVCFGT}.2017-07-07.16-19-07.stderr
    jobid: 3
    wildcards: pathGVCFT=output/vcfGenUtil_varScan, sampleGVCFT=Pfeiffer2.varScan.indel.canonical_annotated.indel_annotated


localrule all:
    input: output/vcfGenUtil_varScan/tables/Pfeiffer2.varScan.snp.canonical_annotated.dbsnp_annotated.cosmic_annotated.txt, output/vcfGenUtil_varScan/tables/Pfeiffer2.varScan.indel.canonical_annotated.indel_annotated.txt, output/vcfGenUtil_varScan/tables/Pfeiffer3.varScan.snp.canonical_annotated.dbsnp_annotated.cosmic_annotated.txt, output/vcfGenUtil_varScan/tables/Pfeiffer3.varScan.indel.canonical_annotated.indel_annotated.txt
    jobid: 0

Job counts:
	count	jobs
	1	all
	2	bam2fastq_picard
	8	bam2mpileup
	2	bamALIGN_bwa
	4	canonical
	2	cosmic
	2	dbsnp
	4	fastq2GZ
	2	filteredBAM
	4	getVcfTable
	2	indel
	2	indexBAM
	2	markdupBAM
	2	mergeBAM
	4	mergeVCF
	16	mpileup2vcf_single
	2	sortBAM_biobambam
	61
