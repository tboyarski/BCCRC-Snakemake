# varScan Module (Multi-Snakemake)
This directory contains the varScan module. It is a multi-module system focusing on variant identification.

## Modules:
See invidual files for expanded explanations of their purpose and the manner in which they accomplish it.
* mpileup2vcf_SingleUNSPLIT: Generate single '.VCF' file from single '.mpileup' file.
* mpileup2vcf_SingleSPLIT: Generate single chromosomal '.VCF' files from single chromosomal '.mpileup' files.
* mpileup2vcf_PairUNSPLIT: Generate single '.VCF' file from a pair of tumor-normal '.mpileup' file.
* mpileup2vcf_SingleSPLIT: Generate single chromosomal '.VCF' files from a pair of tumor-normal chromosomal '.mpileup' files.
* mpileup2copycall_PairUNSPLIT: Infer somatic copy number changes using data from matched tumor-normal pairs.
* mpileup2copynum_PairUNSPLIT: Call variants and identify their somatic status
* mpileup2cns_SingleUNSPLIT: Generate concensus calls from a '.mpileup' file.
* **varScan_INCLUDE: Master file which includes the submodules above.**

## Regression Testing:
Most recently on: **June 21st, 2017**

### SPLIT vs UNSPLIT
Even though SPLIT and UNSPLIT write to different directories, the YAML configuration parameter varScanChrSplit forces users
to chose between SPLIT and UNSPLIT. Consequently, only one of them can be run at a time, as such, this required 2 workspaces.

### Pair vs Single
Even though Pair and Single produce different outputs, the way the Snakemake file and YAML file are created by buildPipe.py,
users are forced to chose between Pair or Single workspaces. Consequently, only one of them can be run at a time, as such, this
required 2 workspaces.

**Directory Prefix = /genesis/extscratch/clc/projects/tboyarski/RegressionTest/3-varScan/varScan-**

Please refer the the contained "RegTestREADME" directory for more information about each of the following directories:

    1 = 1-
    = 2-
    = 3-
    = 4-
    = 5-
  29     1 = 1-bwa_biobambam_biobambam
  30     2 = 2-star_samtools_samtools
  31     3 = 3-RemainingModules




Module | Directory Tested Within
:--------: | :--------
mpileup2cns_SingleUNSPLIT | varScan-5-RemainingModules
mpileup2copycall_PairUNSPLIT | varScan-5-RemainingModules
mpileup2copynum_PairUNSPLIT | varScan-5-RemainingModules
mpileup2vcf_PairSPLIT | varScan-1-PairSPLIT
mpileup2vcf_PairUNSPLIT | varScan-2-PairUNSPLIT
mpileup2vcf_SingleSPLIT | varScan-3-SingleSPLIT
mpileup2vcf_SingleUNSPLIT | varScan-4-SingleUNSPLIT

## Logging:
Will be stored in: "log/varScan"

## Global Directories:
* outputDIR = Directory to contain all file generated by the pipeline

## Global Paramters:
Module | Argument | Default Value | Description
:--------: | :--------: | :--------: | :--------
All | offCluster | False | Adds input redirection to end of shell calls as to capture STDERR when not on cluster.
All | shellCallFile | shellCalls.txt | File to which a copy of all shell calls is printed.
mpileup2MERGE, somTumorNormalMERGE | chrLIST | ['chr1', ... 'chrY'] OR ['1', ... 'Y'] | List of organism (Human or Mouse) and format (NCBI or UCS) specific chromosomes

## Module Specific Paramters:
Module |Argument | Default Value | Description
:--------: | :--------: | :--------: | :--------
mpileup2vcf_SingleSPLIT, mpileup2vcf_PairUNSPLIT | varScan_varScanProg | varscan | Version of varScan to be used.
mpileup2vcf_PairSPLIT, ,mpileup2vcf_PairUNSPLIT | varScan_varScanProg | varscan | Version of varScan to be used.
*SPLIT, *UNSPLIT | mpileupDIR | mpileup | Directory provides '.pileup' files to be processed.
*SPLIT, *UNSPLIT, *MERGE | varScanSplitDIR | varScanSplit | Directory to store chromosomal '.VCF' file prior to their merge.
*MERGE | varScanDIR | varScan | Log directory and core directory to store files.
*SPLIT, *UNSPLIT | minCOV | --min-coverage 20 | Minimum read depth at a position to make a call.
*SPLIT, *UNSPLIT | minREAD | --min-reads2 10 | Minimum supporting reads at a position to call variants.
*SPLIT, *UNSPLIT | minQUAL | --min-avg-qual 20 | Minimum base quality at a position to count a read.
*SPLIT, *UNSPLIT | minFREQ | --min-var-freq 0.01 | Minimum variant allele frequency threshold.
*SPLIT, *UNSPLIT | pVALUE | --p-value 0.05 | Default p-value threshold for calling variants.
*SPLIT, *UNSPLIT | strandFILT | --strand-filter 0 | Ignore variants with >90% support on one strand.
*SPLIT, *UNSPLIT | outVCF | --output-vcf 1 | If set to 1, outputs in VCF format.
*SPLIT | varScanChrSplit | True | Process samples by chromosome, and then merge to single '.VCF'.
mpileup2vcf_PairSPLIT, ,mpileup2vcf_PairUNSPLIT | minSTRAND | --min-strands2 0 | Minimum number of strands on which variant observed.
mpileup2vcf_PairSPLIT, ,mpileup2vcf_PairUNSPLIT | posVALID | --validation 0 | If set to 1, outputs all compared positions even if non-variant.
mpileup2copynum_PairUNSPLIT | mapQSkip | -q 1 | Skip alignments with mapQ smaller than the INT.

## WARNINGS:
```
Not resetting normal file because...
```
This is becuase the two mpileup files provided to varScan have different levels of coverage at different points. 
In the makefile example, process substitution is used to compute both the tumor and the normal mpileup files in 
a single call to generate a single file. The single file in this case is already adjusted, whereas, when submitting
two separate files, the adjustments are made later and are subsequently reported.
Change varScan somatic calls to accept a single file (--mpileup 1) to avoid this message.
This was not done as the coding for inline process substitution is not easily understood, preferred the clarify of 
generating two separate files and providing them together.
Concerns may exist for moments disk usage overhead, by not piping the output directly this increases the footprint
of the Snakerun. However, it also drastically reduces the memory footprint as an entire chromosome or sample is no
longer needed to be stored in memory.

varScank.mk did not use the '-bh -F 512' flag when calculating indels for single samples, or when calcualting any tumor-normal pairs.
The snakemake equivalents all use the same code, so they all will use the '-bh -F 512' flags.