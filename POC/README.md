# Proof of Concept: Pipelines
They require certain files to exist, depending on which phases of the pipeline you are running.

## Directories required:
    bam/        Do not share; Files created here
    ref/        Sharable: Read-Only
    fastq/      Do not share; Files created here

### Pipeline Phases:
* Phase 0: The pipeline starts with an original BAM file, located in the BAM directory.
* Phase 1: Reassembling the FASTQ files from the provided BAM file.
* Phase 2: Generating a new BAM file, "_realigned.BAM", from the FASTQ files.
* Phase 3: Sorting the newely generated BAM file "_realigned.BAM" to make "_realigned_sorted.BAM"
* Phase 4: Indexing of "_realigned_sorted.BAM" to produce "_realigned_sorted.bam.bai"

The original BAM file used to generate this pipeline from sratch, is located on Genesis here:
        /extscratch/clc/projects/lchong/makefile_practice/bam/bam/Pfeiffer.bam

The original .FA file used as a reference in this pipeline, it is a symlink and is located on Genesis here:
        /extscratch/clc/projects/lchong/makefile_practice/ref/GRCh37-lite.fa

For the purpose of this pipeline, it is permitted to symlink to these files.
