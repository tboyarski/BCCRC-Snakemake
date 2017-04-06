# vim: set ft=make : # Run VarScan on tumour-normal matched pairs
# Detect point mutations
# OPTIONS:
# 	SPLIT_CHR: Splits the variant calling per chromosome. Speeds up variant calling (false).
# 	MAX_READ_DEPTH: Set the maximum read depth at each position for samtools (1000000)
# 	MAPPING_QUAL: Set the minimum read mapping quality to consider for variant calling (20)
# 	TARGETS_BED_FILE: Sets the target regions to call variants (bed file format)
#	STRAND_FILTER: Sets the strand filter (false)
#	VAR_FREQ: Sets the variant allele frequency (0.01)
##### MAKE INCLUDES #####

# If not already set, create and initialize variable.
LOGDIR ?= log/varScan.$(NOW)					#Create a log directory; Named using current date

# Import a data-set of variables.
include ~/share/modules/Makefile.inc
include ~/share/modules/vcftools.mk
include ~/share/modules/table.mk

# If not already set, create and initialize variable.
SAMPLE_FILE ?= samples.txt					#Simple 1-col data file with input-file-prefixes
SAMPLES ?= $(shell cat $(SAMPLE_FILE))				#Shell command variable to output input-file-prefixes
SAMPLE_PAIR_FILE ?= sample_pairs.txt				#Simple 2-col data file with input-file-prefixes
TUMOR_SAMPLES ?= $(shell cut -f 1 $(SAMPLE_PAIR_FILE))		#Shell command to extract col-1 as a list.   E.g. Tumor1\n...\nTumorN
NORMAL_SAMPLES ?= $(shell cut -f 2 $(SAMPLE_PAIR_FILE))		#Shell command to extract col-1 as a list.   E.g. Normal1\n...\nNormalN

# Create a list of variables using words in a file, set them equal to words in a different file.
# Foreach TumorSampleName in $(TUMOR_SAMPLES), set normal_loopup.TumorSampleNameNumberN := NormalSampleNameNumberN
$(foreach i,$(shell seq 1 $(words $(TUMOR_SAMPLES))),$(eval normal_lookup.$(word $i,$(TUMOR_SAMPLES)) := $(word $i,$(NORMAL_SAMPLES))))
# RESULT:
#   normal.lookup.Tumor1 := Normal1
#   ..
#   normal.lookup.Tumorn := Normaln


# Create a list of variables using words in a file, set them equal to works in a different file.
# Foreach NormalSampleName in $(NORMAL_SAMPLES), set tumor_lookup.NormalSampleNameNumberN := TumorSampleNameNumberN
$(foreach i,$(shell seq 1 $(words $(TUMOR_SAMPLES))),$(eval tumor_lookup.$(word $i,$(NORMAL_SAMPLES)) := $(word $i,$(TUMOR_SAMPLES))))
# RESULT:
#   tumor.lookup.Normal1 := Tumor1
#   ..
#   tumor.lookup.Normaln := Tumorn


# If not already set, create and initialize variable.
SPLIT_CHR ?= false	    # GNU Make Variable; Set true to splits the variant calling per chromosome (May be faster if true) 
VAR_FREQ ?= 0.01	    # varScan ALL; Set the minimum allele variance frequency
MIN_COVERAGE ?= 20	    # varScan ALL; Set the minimum read depth
MIN_VARIANT_READS ?= 10	# varScan ALL; Set the minimum varient read count threshold
SOMATIC_PVAL ?= 0.05	#**NOT USED**; Set the pValue threshold for calling variants
SOMATIC_PVALUE ?= 0.05	# varScan ALL; Set the pValue threshold for calling variants
MIN_AVG_QUAL ?= 20	    # varScan ALL; Set the minimum base quality at a position to cound as a read
MIN_STRANDS2 ?= 0	    # SOMATIC    ; Set value for strans on which allele was observed

# For 3 different varScan Calls: mpileup2snp, mpileup2indel, and somatic
# If not already set, create variable for varScan arguments when making accepting a .pileup and outputting a .vcf. 
VARSCAN_MPILEUP2SNP_OPTS ?= --min-coverage $(MIN_COVERAGE) --min-reads2 $(MIN_VARIANT_READS) --p-value 0.05 --min-avg-qual 20 --min-var-freq $(VAR_FREQ) --output-vcf 1 
VARSCAN_MPILEUP2INDEL_OPTS ?= --min-coverage $(MIN_COVERAGE) --min-reads2 $(MIN_VARIANT_READS) --p-value 0.05 --min-avg-qual 20 --min-var-freq $(VAR_FREQ) --output-vcf 1 
VARSCAN_SOMATIC_OPTS ?= --min-var-freq $(VAR_FREQ) --min-coverage $(MIN_COVERAGE) --min-strands2 $(MIN_STRANDS2) --somatic-p-value $(SOMATIC_PVALUE) --min-avg-qual $(MIN_AVG_QUAL) --min-reads2 $(MIN_VARIANT_READS) --output-vcf

# If not already set, create and initialize variable. 
STRAND_FILTER ?= false
ifeq ($(STRAND_FILTER),false)
VARSCAN_MPILEUP2SNP_OPTS += --strand-filter 0		#Concatenate to end of SNP_OPTS argument variable
VARSCAN_MPILEUP2INDEL_OPTS += --strand-filter 0		#Concatenate to end of INDEL_OPTS argument variable
VARSCAN_SOMATIC_OPTS += --strand-filter 0		#Concatenate to end of SOMATIC_OPTS argument variable
endif

# If not already set, create and intialize variable.
VALIDATION_FLAG ?= false
ifeq ($(VALIDATION_FLAG),true)
VARSCAN_SOMATIC_OPTS += --validation 1			#Set every single position that is compared to be output to the output file.
endif


# If not already set, create and intialize variable.
MAX_READ_DEPTH ?= 10000000					#SAMTOOLS mpileup; Set max read depth to 10G
MAPPING_QUAL ?= 20						#SAMTOOLS mpileup; Set minimum mapping quality for alignment to be used.	
MPILEUP_OPTS ?= -A -B -q $(MAPPING_QUAL) -d $(MAX_READ_DEPTH)	#SAMTOOLS mpileup; If not already set, create variable for mpileup arguments.
ifdef TARGETS_BED_FILE						
MPILEUP_OPTS += -l $(TARGETS_BED_FILE)				#SAMTOOLS mpileup; Can define the directory location of BED or position list file, in varScan.mk call 
endif

ALL_VCF_FIELDS = *** OMITTED FOR TIM's SIMPLICITY

# samtools bitwise flag to be used in samtools view -F 
SAMTOOLS_FILTER_BITFLAG ?= 512

.DELETE_ON_ERROR:

.SECONDARY: $(foreach sample,$(SAMPLES),$(foreach chr,$(CHROMOSOMES),varScan/vcf/$(sample).$(chr).varScan.indels.vcf)) 
	        $(foreach sample,$(SAMPLES),$(foreach chr,$(CHROMOSOMES),varScan/vcf/$(sample).$(chr).varScan.snps.vcf))

.PHONY: single_snvs.vcf single_snvs_tables single_indels.vcf single_indels.tables pair_variants.vcf pair_variants.tables 

single_snvs.vcf : \
	$(foreach sample,$(SAMPLES),varScan/vcf/$(sample).varScan.snps.snpEff_canonical$(VARSCAN_ANNOTATE_SUFFIX)vcf)

single_snvs.tables : \
	$(foreach sample,$(SAMPLES),varScan/tables/$(sample).varScan.snps.snpEff_canonical$(VARSCAN_ANNOTATE_SUFFIX)txt) \
	varScan/tables/all.single_samples.varScan.snps.snpEff_canonical$(VARSCAN_ANNOTATE_SUFFIX)txt

single_indels.vcf : \
	$(foreach sample,$(SAMPLES),varScan/vcf/$(sample).varScan.indels.snpEff_canonical.indels_annotated.vcf)

single_indels.tables : \
	$(foreach sample,$(SAMPLES),varScan/tables/$(sample).varScan.indels.snpEff_canonical.indels_annotated.txt) \
	varScan/tables/all.single_samples.varScan.indels.snpEff_canonical.indels_annotated.txt

# do not specify the *.indels.vcf target as it is automatically generated by the snps.vcf target already
pair_variants.vcf : $(foreach tumor,$(TUMOR_SAMPLES),varScan/vcf/$(tumor)_$(normal_lookup.$(tumor)).varScan.snps.snpEff_canonical.snps_annotated.cosmic_annotated.vcf)
pair_variants.tables : $(foreach tumor,$(TUMOR_SAMPLES),varScan/tables/$(tumor)_$(normal_lookup.$(tumor)).varScan.snps.snpEff_canonical.snps_annotated.cosmic_annotated.txt) varScan/tables/all.paired_samples.varScan.snps.snpEff_canonical.snps_annotated.cosmic_annotated.txt varScan/tables/all.paired_samples.varScan.indels.snpEff_canonical.indels_annotated.txt

pair_variants.noncanon.vcf : $(foreach tumor,$(TUMOR_SAMPLES),varScan/vcf/$(tumor)_$(normal_lookup.$(tumor)).varScan.snps.snpEff.snps_annotated.cosmic_annotated.vcf)
pair_variants.noncanon.tables : $(foreach tumor,$(TUMOR_SAMPLES),varScan/tables/$(tumor)_$(normal_lookup.$(tumor)).varScan.snps.snpEff.snps_annotated.cosmic_annotated.txt) varScan/tables/all.paired_samples.varScan.snps.snpEff.snps_annotated.cosmic_annotated.txt varScan/tables/all.paired_samples.varScan.indels.snpEff.indels_annotated.txt

copycalls : $(foreach tumor,$(TUMOR_SAMPLES),varScan/copycall/$(tumor)_$(normal_lookup.$(tumor)).copycall)

mpileup/%.mpileup : bam/%.bam
	$(call LSCRIPT_MEM_DRMAA,2G,4G,"$(SAMTOOLS) mpileup $(MPILEUP_OPTS) -f $(REF_FASTA) $< > $@")

#----------
# Single Test Sample Rules for SNVs
#----------
# Check if splitting by chromosome.
ifeq ($(SPLIT_CHR),true)
	# Define a function which allows samtools to be called at a chromosomal granularity.
	define varScan-single-snv-chr
		varScan/vcf/$(1).$(2).varScan.snps.vcf : bam/$(1).bam
			$$(call LSCRIPT_PARALLEL_MEM_DRMAA,2,2G,4G,"$$(SAMTOOLS) view -bh -F $$(SAMTOOLS_FILTER_BITFLAG) $$< $(2) | $$(SAMTOOLS) mpileup $$(MPILEUP_OPTS) -f $$(REF_FASTA) - | $$(VARSCAN) mpileup2snp $$(VARSCAN_MPILEUP2SNP_OPTS) > $$@")
	endef

	$(foreach sample,$(SAMPLES),\
		$(foreach chr,$(CHROMOSOMES),\
		$(eval $(call varScan-single-snv-chr,$(sample),$(chr)))))

	$(foreach sample,$(SAMPLES),\
		$(eval $(call catVcf,varScan/vcf/$(sample).varScan.snps.vcf,$(foreach chr,$(CHROMOSOMES),varScan/vcf/$(sample).$(chr).varScan.snps.vcf))))

else
	# No splitting by chromosome.
	varScan/vcf/%.varScan.snps.vcf : bam/%.bam
		$(call LSCRIPT_PARALLEL_MEM_DRMAA,2,1G,2G,"$(SAMTOOLS) view -bh -F $(SAMTOOLS_FILTER_BITFLAG) $< | $(SAMTOOLS) mpileup $(MPILEUP_OPTS) -f $(REF_FASTA) - | $(VARSCAN) mpileup2snp $(VARSCAN_MPILEUP2SNP_OPTS) > $@")
endif

$(foreach sample,$(SAMPLES),\
	$(eval $(call getVariantTable,varScan/tables/$(sample).varScan.snps.snpEff_canonical$(VARSCAN_ANNOTATE_SUFFIX)txt,varScan/vcf/$(sample).varScan.snps.snpEff_canonical$(VARSCAN_ANNOTATE_SUFFIX)vcf,$(ALL_VCF_FIELDS) $(EFF_FIELDS),$(sample),false)))




#---------
# Single test sample rules for indels
#---------
ifeq ($(SPLIT_CHR),true)
define varScan-single-indel-chr
varScan/vcf/$(1).$(2).varScan.indels.vcf : bam/$(1).bam
	$$(call LSCRIPT_PARALLEL_MEM_DRMAA,2,1G,2G,"\
		$$(SAMTOOLS) mpileup $$(MPILEUP_OPTS) \
		-f $$(REF_FASTA) \
		-r $(2) $$< \
		| $$(VARSCAN) mpileup2indel $$(VARSCAN_MPILEUP2INDEL_OPTS) \
		> $$@")
endef
$(foreach sample,$(SAMPLES),\
	$(foreach chr,$(CHROMOSOMES),$(eval $(call varScan-single-indel-chr,$(sample),$(chr)))))

$(foreach sample,$(SAMPLES),\
	$(eval $(call catVcf,varScan/vcf/$(sample).varScan.indels.vcf,$(foreach chr,$(CHROMOSOMES),varScan/vcf/$(sample).$(chr).varScan.indels.vcf))))

else # no splitting by chr
varScan/vcf/%.varScan.indels.vcf : bam/%.bam
	$(call LSCRIPT_PARALLEL_MEM_DRMAA,2,1G,2G,"$(SAMTOOLS) mpileup $(MPILEUP_OPTS) -f $(REF_FASTA) $< | $(VARSCAN) mpileup2indel $(VARSCAN_MPILEUP2INDEL_OPTS) > $@")
endif

$(foreach sample,$(SAMPLES),$(eval $(call getVariantTable,varScan/tables/$(sample).varScan.indels.snpEff_canonical.indels_annotated.txt,varScan/vcf/$(sample).varScan.indels.snpEff_canonical.indels_annotated.vcf,$(ALL_VCF_FIELDS) $(EFF_FIELDS),$(sample),false)))

$(eval $(call mergeTables,\
	varScan/tables/all.single_samples.varScan.snps.snpEff_canonical$(VARSCAN_ANNOTATE_SUFFIX)txt,\
	$(foreach sample,$(SAMPLES),varScan/tables/$(sample).varScan.snps.snpEff_canonical$(VARSCAN_ANNOTATE_SUFFIX)txt)))

$(eval $(call mergeTables,varScan/tables/all.single_samples.varScan.indels.snpEff_canonical.indels_annotated.txt,$(foreach sample,$(SAMPLES),varScan/tables/$(sample).varScan.indels.snpEff_canonical.indels_annotated.txt)))

varScan/cns/%.varScan.mpileup2cns : bam/%.bam
	$(call LSCRIPT_PARALLEL_MEM_DRMAA,2,1G,2G,"$(SAMTOOLS) mpileup $(MPILEUP_OPTS) -f $(REF_FASTA) -r 12 $< | $(VARSCAN) mpileup2cns > $@")

#----------
# Test-control paired sample rules for snvs and indels
#----------
# The varscan somatic function returns both snvs and indels at the same time.
# The varscan somatic function has takes a 2-sample normal-tumour pileup. This 
# is suggested in http://varscan.sourceforge.net/support-faq.html#error-resetting-file
# to eliminate the resetting file error. Careful of the order; Normal then Tumour

ifeq ($(SPLIT_CHR),true) # splitting by chr
define varScan-somatic-tumor-normal-chr
varScan/chr_vcf/$(1)_$(2).$(3).varScan.snps.vcf varScan/chr_vcf/$(1)_$(2).$(3).varScan.indels.vcf : bam/$(1).bam bam/$(2).bam
	$$(call LSCRIPT_PARALLEL_MEM_DRMAA,2,1.5G,3G,"$$(VARSCAN) somatic <($$(SAMTOOLS) mpileup $$(MPILEUP_OPTS) -r $(3) -f $$(REF_FASTA) $$(word 2,$$^) $$<) --mpileup 1 --output-indel varScan/chr_vcf/$(1)_$(2).$(3).varScan.indels.vcf --output-snp varScan/chr_vcf/$(1)_$(2).$(3).varScan.snps.vcf $$(VARSCAN_SOMATIC_OPTS) &> $$(LOG)")
endef
$(foreach chr,$(CHROMOSOMES),\
	$(foreach tumor,$(TUMOR_SAMPLES),$(eval $(call varScan-somatic-tumor-normal-chr,$(tumor),$(normal_lookup.$(tumor)),$(chr)))))

# convert the per-chr vcf files into tables
$(foreach tumor,$(TUMOR_SAMPLES),\
	$(foreach chr,$(CHROMOSOMES),$(eval $(call getVariantTable,varScan/tables/$(tumor)_$(normal_lookup.$(tumor)).$(chr).varScan.snps.snpEff_canonical.snps_annotated.cosmic_annotated.txt,varScan/chr_vcf/$(tumor)_$(normal_lookup.$(tumor)).$(chr).varScan.snps.snpEff_canonical.snps_annotated.cosmic_annotated.vcf,$(ALL_VCF_PAIRED_FIELDS) $(EFF_FIELDS),$(tumor)_$(normal_lookup.$(tumor)),false))))

$(foreach tumor,$(TUMOR_SAMPLES),\
	$(foreach chr,$(CHROMOSOMES),$(eval $(call getVariantTable,varScan/tables/$(tumor)_$(normal_lookup.$(tumor)).$(chr).varScan.indels.snpEff_canonical.indels_annotated.txt,varScan/chr_vcf/$(tumor)_$(normal_lookup.$(tumor)).$(chr).varScan.indels.snpEff_canonical.indels_annotated.vcf,$(ALL_VCF_PAIRED_FIELDS) $(EFF_FIELDS),$(tumor)_$(normal_lookup.$(tumor)),false))))

# merge the per-chr table files into one table per-sample
$(foreach tumor,$(TUMOR_SAMPLES),$(eval $(call mergeTables,varScan/tables/$(tumor)_$(normal_lookup.$(tumor)).varScan.snps.snpEff_canonical.snps_annotated.cosmic_annotated.txt,$(foreach chr,$(CHROMOSOMES),varScan/tables/$(tumor)_$(normal_lookup.$(tumor)).$(chr).varScan.snps.snpEff_canonical.snps_annotated.cosmic_annotated.txt))))
$(foreach tumor,$(TUMOR_SAMPLES),$(eval $(call mergeTables,varScan/tables/$(tumor)_$(normal_lookup.$(tumor)).varScan.indels.snpEff_canonical.indels_annotated.txt,$(foreach chr,$(CHROMOSOMES),varScan/tables/$(tumor)_$(normal_lookup.$(tumor)).$(chr).varScan.indels.snpEff_canonical.indels_annotated.txt))))

# merge the sample-pair tables to one big summary table
$(eval $(call mergeTables,varScan/tables/all.paired_samples.varScan.snps.snpEff_canonical.snps_annotated.cosmic_annotated.txt,$(foreach tumor,$(TUMOR_SAMPLES),$(foreach chr,$(CHROMOSOMES),varScan/tables/$(tumor)_$(normal_lookup.$(tumor)).$(chr).varScan.snps.snpEff_canonical.snps_annotated.cosmic_annotated.txt))))
$(eval $(call mergeTables,varScan/tables/all.paired_samples.varScan.indels.snpEff_canonical.indels_annotated.txt,$(foreach tumor,$(TUMOR_SAMPLES),$(foreach chr,$(CHROMOSOMES),varScan/tables/$(tumor)_$(normal_lookup.$(tumor)).$(chr).varScan.indels.snpEff_canonical.indels_annotated.txt))))

else # no splitting by chr

define varScan-somatic-tumor-normal
varScan/vcf/$(1)_$(2).varScan.snps.vcf varScan/vcf/$(1)_$(2).varScan.indels.vcf : bam/$(1).bam bam/$(2).bam
	$$(call LSCRIPT_PARALLEL_MEM_DRMAA,2,1.5G,3G,"$$(VARSCAN) somatic <($$(SAMTOOLS) mpileup $$(MPILEUP_OPTS) -f $$(REF_FASTA) $$(word 2,$$^) $$<) --mpileup 1 --output-indel varScan/vcf/$(1)_$(2).varScan.indels.vcf --output-snp varScan/vcf/$(1)_$(2).varScan.snps.vcf $$(VARSCAN_SOMATIC_OPTS) &> $$(LOG)")
endef
$(foreach tumor,$(TUMOR_SAMPLES),$(eval $(call varScan-somatic-tumor-normal,$(tumor),$(normal_lookup.$(tumor)))))

# convert the vcf into a table per sample-pair
$(foreach tumor,$(TUMOR_SAMPLES),$(eval $(call getVariantTable,varScan/tables/$(tumor)_$(normal_lookup.$(tumor)).varScan.snps.snpEff_canonical.snps_annotated.cosmic_annotated.txt,varScan/vcf/$(tumor)_$(normal_lookup.$(tumor)).varScan.snps.snpEff_canonical.snps_annotated.cosmic_annotated.vcf,$(ALL_VCF_PAIRED_FIELDS) $(EFF_FIELDS),$(tumor)_$(normal_lookup.$(tumor)),false)))
$(foreach tumor,$(TUMOR_SAMPLES),$(eval $(call getVariantTable,varScan/tables/$(tumor)_$(normal_lookup.$(tumor)).varScan.indels.snpEff_canonical.indels_annotated.txt,varScan/vcf/$(tumor)_$(normal_lookup.$(tumor)).varScan.indels.snpEff_canonical.indels_annotated.vcf,$(ALL_VCF_PAIRED_FIELDS) $(EFF_FIELDS),$(tumor)_$(normal_lookup.$(tumor)),false)))

$(eval $(call mergeTables,varScan/tables/all.paired_samples.varScan.snps.snpEff_canonical.snps_annotated.cosmic_annotated.txt,$(foreach tumor,$(TUMOR_SAMPLES),varScan/tables/$(tumor)_$(normal_lookup.$(tumor)).varScan.snps.snpEff_canonical.snps_annotated.cosmic_annotated.txt)))
$(eval $(call mergeTables,varScan/tables/all.paired_samples.varScan.indels.snpEff_canonical.indels_annotated.txt,$(foreach tumor,$(TUMOR_SAMPLES),varScan/tables/$(tumor)_$(normal_lookup.$(tumor)).varScan.indels.snpEff_canonical.indels_annotated.txt)))
endif

####
## Test-control paired sample rules for copy number
#####
define varScan-copynum-tumor-normal
varScan/copynum/$1_$2.copynumber :  $1.bam $2.bam
	$$(call LSCRIPT_MEM_DRMAA,9G,12G) $$(SAMTOOLS) mpileup -q 1 -f $$(REF_FASTA) $$(word 2,$$^) $$< | awk 'NF == 9 { print }' |  $$(VARSCAN) copynumber -mpileup 1 - $$(basename $$@) &> $$(LOG)
endef
$(foreach tumor,$(TUMOR_SAMPLES),$(eval $(call varScan-copynum-tumor-normal,$(tumor),$(normal_lookup.$(tumor)))))

varScan/copycall/%.copycall : varScan/copynum/%.copynumber
	$(call INIT_MEM,9G,12G) $(VARSCAN) copyCaller $< --output-file $@ &> $(LOG)
