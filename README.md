# Overview
This system is utilized to automate much of the processing of biological data for the BC Cancer Agency's Lymphoid Cancer Research Department (LCR).
This repository exists for the continued development of the LCR Snakemake Pipeline System.
This repository has been developed for the purpose of tracking the exploration of 
biological pipelines by leveraging the build-automation software Snakemake.
**Last Updated from Private Repository on September 1st, 2017**

The language's publication can be found here:
* https://academic.oup.com/bioinformatics/article/28/19/2520/290322/Snakemake-a-scalable-bioinformatics-workflow

## Modules:
Snakemake and Python modules are developed and stored here. 

## BuildArea:
Development of pipelines is to occurr here. Can used BuildPipe.py to assist in pipeline development, or
you manually develope a pipeline and include Snakefiles from the Modules directory. 

### condaENV
Contains the conda environments used to run the system on the high-performace computing cluster at the Genome Sciences Center (GSC).

### docs
Contains supporting materials, vignettes and diagrams, to aid in the understanding and development of the system.

## Help (Pipeline) - OLD
* Presentation - This PowerPoint slideshow was presented to the Lympoid Cancer Research Department during their lab meeting on April 7th, 2017
* PipelineVignette -  **Incomplete** - This MS Word document provides detailed instructions on how to generate a pipeline in the LCR system on our SGE Network.
* ModuleVignette - **Incomplete** - This MS Word document provides detailed instructions 
on how to generate a module for the LCR pipeline system our SGE Network.

### Regression Testing:
Originally this was done at a module level. The artifacts produced by this testing have been kept within the repository to act as visual aids for the modules. However, it has since been deteremined it is much easier, and more realistic to test the pipeline in larger segments, with fewer tests. Individual modules can still be tested if needed, however, the newly adopted approach is to test the basic core functionality using a large pipeline, using single and paried samples. Afterwards, the remaining modules are tested by making smaller, meaningful pipelines.

Regression Testing was last attempted on 2017-08-31.

Modules |   Submodules  |   CoreTest_single |   CoreTest_pair   |   A-bamALIGN_star |   B-bwa_trimReads |   C-sam2BAM
:--------: | :-----: | :--------: | :--------: | :--------: | :--------: | :--------:
fastqGEN    |   bam2fastq_picard    |   CoreTest_single |   CoreTest_pair   |       |       |   
fastqUTIL   |   fastq2GZ    |   CoreTest_single |   CoreTest_pair   |       |       |   
fastqUTIL   |   mergeFASTQ  |       |       |   A-bamALIGN_star |       |   
fastqUTIL   |   fastqc  |   CoreTest_single |   CoreTest_pair   |       |       |   
bamGEN  |   bamALIGN_bwa    |   CoreTest_single |       |       |       |   
bamGEN  |   bamALIGN_star   |       |       |   A-bamALIGN_star |       |   
bamGEN  |   bamALIGN_bwa    |       |       |       |   B-bwa_trimReads |   
bamGEN  |   sam2BAM |       |       |       |       |   C-sam2BAM
bamUTIL |   sortBAM_biobambam   |   CoreTest_single |   CoreTest_pair   |       |       |   
bamUTIL |   filteredBAM |   CoreTest_single |   CoreTest_pair   |       |       |   
bamUTIL |   markdupBAM  |   CoreTest_single |   CoreTest_pair   |       |       |   
bamUTIL |   indexBAM    |   CoreTest_single |   CoreTest_pair   |       |       |   
bamUTIL |   namesortBAM_biobambam   |       |       |   A-bamALIGN_star |       |   
bamUTIL |   cleanBAM    |       |       |   A-bamALIGN_star |       |   
bamUTIL |   fixmateBAM  |       |       |   A-bamALIGN_star |       |   
bamUTIL |   rmdupBAM    |       |       |   A-bamALIGN_star |       |   
bamUTIL |   mergeBAM (PreFastq) |       |       |       |   B-bwa_trimReads |   
bamUTIL |   mergeBAM (PostFastq)    |       |       |       |       |   C-sam2BAM
bamUTIL |   sortBAM_samtools    |       |       |       |       |   C-sam2BAM
bamUTIL |   namesortBAM_samtools    |       |       |       |   B-bwa_trimReads |   
mpileupGEN  |   bam2mpileup |   CoreTest_single |   CoreTest_pair   |       |       |   
vcfGenUtil_varScan  |   conSeq  |       |   CoreTest_pair   |       |       |   
vcfGenUtil_varScan  |   copycall    |       |   CoreTest_pair   |       |       |   
vcfGenUtil_varScan  |   copynum |       |   CoreTest_pair   |       |       |   
vcfGenUtil_varScan  |   mpileup2vcf_pair    |       |   CoreTest_pair   |       |       |   
vcfGenUtil_varScan  |   mpileup2vcf_single  |   CoreTest_single |       |       |       |   
vcfANNOTATE |   cosmic  |   CoreTest_single |   CoreTest_pair   |       |       |   
vcfANNOTATE |   indel   |   CoreTest_single |   CoreTest_pair   |       |       |   
vcfANNOTATE |   dbsnp   |   CoreTest_single |   CoreTest_pair   |       |       |   
vcfANNOTATE |   canonical   |   CoreTest_single |   CoreTest_pair   |       |       |   
vcfANNOTATE |   noncanonical    |       |       |   A-bamALIGN_star |       |   
vcfUTIL |   getVcfTable |   CoreTest_single |   CoreTest_pair   |       |       |   
vcfUTIL |   mergeVCF    |   CoreTest_single |       |       |       |   
vcfUTIL |   sortVCF |       |       |   A-bamALIGN_star |       |   
bamMETRICS  |   collectGCBias   |   CoreTest_single |       |       |       |   
bamMETRICS  |   collectMultMetrics  |   CoreTest_single |       |       |       |   
bamMETRICS  |   collectRNASeq   |   CoreTest_single |       |       |       |   
bamMETRICS  |   collectWGS  |   CoreTest_single |       |       |       |   
bamMETRICS  |   collectMERGE_ADAPTOR    |   CoreTest_single |       |       |       |   
bamMETRICS  |   flagStats   |   CoreTest_single |       |       |       |   
bamMETRICS  |   readLen |   CoreTest_single |       |       |       |   
genericUtil |   tableMERGE  |   CoreTest_single |       |       |       |   
starFusion  |   fusion  |       |       |   A-bamALIGN_star |       |   


