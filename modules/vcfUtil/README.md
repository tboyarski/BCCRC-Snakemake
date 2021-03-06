# vcfUtil Module

## Logging:
Will be stored in: "log/vcfUtil"

## Modules:
* getVcfTable: Produce a variant table from a '.VCF' file.
* mergeVCF: Merge chromosomal '.VCF' files into a single genomic '.VCF' file.
* sortVCF: Sort a '.VCF' file based on sequence provided.
* **vcfUtil_INCLUDE: Master file which includes both modules above.**

## Control Flags:
None

## Global Directories:
Module | Argument | Default Value | Description
:--------: | :--------: | :--------: | :--------
None | bamDIR | bam | Directory to conatin the processed, symlinked, and name-normalized '.bam' and '.BAI' files.
None | inputDIR | input | Directory to contain all files prior to starting pipeline (Reference and input files).
None | fastqDIR | fastq | Directory to contain the processed '.fastq' files.
None | metricsDIR | metrics | Directory to contain the processed '.metrics' files.
None | mpileupDIR | mpileup | Directory to contain the processed '.mpileup' files.
All | outputDIR | output | Directory to contain all file generated by the pipeline.

## Global Parameters:
Module | Argument | Default Value | Description
:--------: | :--------: | :--------: | :--------
All | shellCallFile | shellCalls.txt | File to which a copy of all shell calls is printed.
All | offCluster | False | Adds input redirection to end of shell calls as to capture STDERR when not on cluster.
None | fastqKEEP | False | Flag of 'True' or 'False' on retaining '.fastq' files after they are used in the pipeline.
None | inputPartList | inputPartList.txt | List containing the parts which comprise each sample.
None | refFILE | *Varies* | Absolute path to genomic reference file.
None | supportRefFILE | *Varies* | Absolute path to supporting genomic references files.
None | chrLIST | *Varies* | Full chromosomal list parse from one of the supporting genomic reference files.

## Module Specific Software:
Module | Argument | Default Value | Description
:--------: | :--------: | :--------: | :--------
getVcfTable | vcfUtil_javaProg | java -Xmx2G | Program path and memory request.
getVcfTable | vcfUtil_snpSiftProg | -jar ~/share/usr/anaconda/4.3.0/envs/CentOS5-APR28-2/share/snpeff-4.1l-0/SnpSift.jar | Program path.
getVcfTable | vcfUtil_vcfEffOnePerLineProg | ~/share/usr/anaconda/4.3.0/envs/CentOS5-APR28-2/share/snpeff-4.1l-0/scripts/vcfEffOnePerLine.pl | Program Path
sortVCF | vcfUtil_picardProg | picard | Program path.

## Module Specific Paramters:
Module | Argument | Default Value | Description
:--------: | :--------: | :--------: | :--------
vcfSORT | vcfSORTValStringency | VALIDATION_STRINGENCY=LENIENT | Validation stringency for all SAM files read by this program.
vcfSORT | vcfSORTMaxRec | MAX_RECORDS_IN_RAM=5000000 | Specify the number of records stored in RAM before spilling to disk. 
vcfSORT | vcfSORTSeqDict | ~/share/references/genomes/gsc/GRCh37-lite.dict | Path to sorting reference dictionary.
All | vcfUtilDIR | vcfUtilDIR | Directory to store the log files.
getVcfTable |  snpSiftExtractFieldOpts | **Not Used** | Sometimes this is set to  -e \".\", not sure why.
getVcfTable | vcfFields | CHROM POS ID REF ALT QUAL FILTER | Fields to be used for SnpSift; Will end up as column headers.
getVcfTable | vcfInfoFields | **Not Used** | Not sure yet.
getVcfTable | vcfGenIDs | GT GQ SDP DP RD AD FREQ PVAL RBQ ABQ RDF RDR ADF ADR | Not sure yet.
getVcfTable | vcfGenFields | **Not Used** | Not sure yet.
getVcfTable | effFields | ['\"EFF[*].EFFECT\"', '\"EFF[*].IMPACT\"', '\"EFF[*].FUNCLASS\"', '\"EFF[*].CODON\"', '\"EFF[*].AA\"', '\"EFF[*].GENE\"', '\"EFF[*].BIOTYPE\"', '\"EFF[*].CODING\"', '\"EFF[*].TRID\"', '\"EFF[*].RANK\"'] | Fields to be used for SnpSift; Wil end up as column headers. Applicable only to older versions of SnpSift. Newer versions will utilize 'ANN' instead of 'EFF'.
getVcfTable | extractFieldOpts | **Not Used** | Not sure yet.
getVcfTable | OnePerLineFLAG | False | Pre-processing flag to enable use of 'SnpEff/vcfEffOnePerLine.pl'.
sam2BAM | Sam2BamARGS | -bS | Program arguments for Samtools whne converting to a '.SAM' file.
