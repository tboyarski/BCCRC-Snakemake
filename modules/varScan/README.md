# varScan Module (Snakemake)
This directory contains the varScan module. It is a single-module system.

## Modules:
See invidual files for expanded explanations of their purpose and the manner in which they accomplish it.
* mpile2snp: Generate '.VCF' file from a '.mpileup' file.
* somatic: Unfinished
* varScan_INCLUDE: Generate '.VCF' file from a '.mpileup' file.

## Logging:
Will be stored in: "log/varScan"

## Global Directories:
* outputDIR = Directory to contain all file generated by the pipeline
* mpileDIR = Directory to contain the '.mpilup' file.
* vcfDIR = Directory to contain the '.VCF' files.

## Global Paramters:
Module | Argument | Default Value | Description
:--------: | :--------: | :--------: | :--------
mPileSPLIT | chrLIST | ['chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8', 'chr9', 'chr10', 'chr11', 'chr12', 'chr13', 'chr14', 'chr15', 'chr16', 'chr17', 'chr18', 'chr19', 'chr20', 'chr21', 'chr22', 'chrM', 'chrX', 'chrY'] | List of human chomosomes

## Module Specific Paramters:
Module |Argument | Default Value | Description
:--------: | :--------: | :--------: | :--------
All | varScanDIR | varScan | Log directory to store log files.
All | minCOV | --min-coverage 20 | Minimum read depth at a position to make a call
All | minFREQ | --min-var-freq 0.01 | Minimum variant allele frequency threshold
All | pVALUE | --p-value 0.05 | Default p-value threshold for calling variants
All | strandFILT | --strand-filter 0 | Ignore variants with >90% support on one strand
snp/indel | minREAD | --min-reads2 10 | Minimum supporting reads at a position to call variants
snp/indel | minQUAL | --min-avg-qual 20 | Minimum base quality at a position to count a read
snp/indel | outVCF | --output-vcf 1 | If set to 1, outputs in VCF format
snp/indel | varScanChrSplit | True | Process samples by chromosome, and then merge to single '.VCF'
somatic | minSTRAND | --min-strands2 0" | Minimum number of strands on which variant observed
somatic | posVALID | --validation 1" | If set to 1, outputs all compared positions even if non-variant