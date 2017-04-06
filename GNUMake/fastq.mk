# This module is used to rxtract fastq files from bam files. 
# Multiple different approaches for extracting fastq from bams are provided.
# Each has their own trade-offs, please cread carefully as to which extraction method you should use.

# OPTIONS -- DEFAULT = BIOBAMBAM (Line 30)

#	EXTRACT_TOOL = BEDTOOLS (BEDTOOLS/PICARD/HYDRA).
#	BEDTOOLS 	- least amount of memory, but low since it requires a  name sort. This is most reliant method and will
#				work across all file sizes.
#	HYDRA 		- memory intensive, but fast. Use for maller .bam files like WTSS. 
#				**DO NOT USE FOR WGSS** (Memory size incompatibility issues)
#	PICARD		- An intermediate processing tool, between HYDRA and BEDTOOLS with respect to speed and file size.
#	
#	Author: TBoyarski -- tim.boyarski@gmail.com -- tboyarski@bccrc.ca

# If not already set, create and intialize variable.
FASTQ_DIR ?= fastq						#Set pathing variable
LOGDIR ?= log/$(FASTQ_DIR).$(NOW)				#Create a log directory; Named using current date

# Import a data-set of variables.
include ~share/modules/Makefile.inc				

# If not already set, create and intialize variable.
SAMPLE_FILE ?= samples.txt					#Simple 1-col data file with input-file-prefixes
SAMPLES ?= $(shell cat $(SAMPLE_FILE))				#Shell command variable to output  input-file-prefixes
VPATH ?= gsc_bam						#Set pathing variable

# Chosing of DEFAULT 
EXTRACT_TOOL ?= BIOBAMBAM

# Max memory in RAM before creating a temporary output file
SAM_TOOLS_SORT_MAX_MEM ?= 4000*1000*1000			#Max memory set at 4GB

#Makefile commands to assist in proper dataflow
.SECONDARY:
.DELETE_ON_ERROR:
.PHONY: fastq							#Set fastq to be explcitly interpretted as a rule and not a file

# Under influence of .PHONY command, may be called as a rule, and is not a file.
# For each input-file-prefix, aka sample, in SAMPLES, create an associated #.fastq.gz file at the appropriate directory
fastq: $(foreach sample,$(SAMPLES),$(FASTQ_DIR)/$(FASTQ_DIR/$(sample).1.fastq.gz $(FASTQ_DIR)/$(sample).2.fastq.gz)

########################################################## SAMTOOL PACKAGE CALLS #####################################################################

## PICARD
# Calling the PICARD module of SAMTOOLS. Directing all output to STD_ERR (2>) located in a specialized directory (LOGDIR).
# Inlcudes the required calls for interacting with the SGE (cluster), all shell commands provided as fifth argument in "..."
# Using SAMTOOLS to output the .bam files "view", piping it back into SAMTOOLS for sorting "sort".
# With sorted output files as .fastq, use a 
ifeq ($(EXTRACT_TOOL),PICARD)									#If Picard tool selected in shell call
$(FASTQ_DIR)/%.1.fastq.gz $(FASTQ_DIR)/%.2.fastq.gz : $(VPATH)/%.bam				#fast.gz files reliant on existance of .bam files
	$(call LSCRIPT_PARALLEL_MEM_DRMMA,4,4G,5G,\						#Provide arguments for the SGE (cluster) call
	"$(SAMTOOLS) view -bF 512 $< 2> $(LOGDIR)/$@.vendor_failed_reads.log |\			#Pass .bam files to SAMTOOLS, output to STD_ERR
												#Name vendor_failed after the fastq filename
	$(SAMTOOLS) sort -no -m $(SAMETOOLS_SORT_MAX_MEM) - $@.namesort\			#Call SAMTOOLS and provide args, "-" is pipelined input
	2> $(LOGDIR)/$@.samtools.namesort.log | \						#Output of previous line to STD_ERR
	$(call SAM_TO_FASTQ_MEM, 10G) I=/dev/stdin FASTQ=>(gzip > $(FASTQ_DIR)/$*.1.fastq.gz)\  #FASTQ argument is front-end-read .fastq file; compressing result
	SECOND_END_FASTQ=>(gzip > $(FASTQ_DIR)/$*.2.fastq.gz)")					#SECOND_END_FASTQ is back-end-read .fastq file; compressing result
endif

## BEDTOOLS
# Calling the BEDTOOLS module of SAMTOOLS. Directing all outputs to STD_ERR (2>) location in a specialized directory (LOGDIR)
# Inlcudes the required calls for interacting with the SGE (cluster), all shell commands provided as fifth argument in "..."
# Using SAMTOOLS to output the .bam files "view", piping it back into SAMTOOLS for sorting "sort",
ifeq ($(EXTRACT_TOOL),BEDTOOLS)
$(FASTQ_DIR)/%.1.fastq.gz $(FASTQ_DIR)/%.2.fastq.gz : $(VPATH)/%.bam				#fast.gz files reliant on existance of .bam files
	$(call LSCRIPT_PARALLEL_MEM_DRMMA,2,4G,5G,\						#Provide arguments for the SGE (cluster) call
	"$(SAMTOOLS) view -bF 512 $< 2> $(LOGDIR)/$@.vendor_failed_reads.log |\			#Pass .bam files to SAMTOOLS, output to STD_ERR
												#Name vendor_failed after the fastq filename
	$(SAMTOOLS) sort -no -m $(SAMETOOLS_SORT_MAX_MEM) - $@.namesort\			#Call SAMTOOLS and provide args, "-" is pipelined input
	2> $(LOGDIR)/$@.samtools.namesort.log | \						##UNKNOWN - Not in original -- Output of previous line to STD_ERR
	$(BAM_TO_FASTQ) -i /dev/stdin -fq >(gzip > $(FASTQ_DIR)/$*.1.fastq.gz)\   		# -fq argument is front-end-read .fastq file; compressing result
	-fq2 >(gzip > $(FASTQ_DIR)/$*.2.fastq.gz)")						# -fq2 argument is back-end-read .fastq file; compressing result
endif



######################################################### FASTQ to FASTQ.GZ COMPRESSION #############################################################

#Compress the .fastq output files into .fastq.gz, then remove the uncompressed .fastq files (rm $<).
# Uses short-circuiting conditional shell operator "&&", will not attempt to remove unless compression is successful.
$(FASTQ_DIR)/%.fastq.gz : $(FASTQ_DIR)/%.fastq
	$(call LSCRIPT_MEM_DRMAA,500M,1G,"gzip -c $< > $@ && rm $<")				#Call to SGE (cluster); 3rd argument is shell command
												



