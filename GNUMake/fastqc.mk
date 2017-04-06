# vim: set ft=make :
# OPTIONS:
# 	NOGROUP_FLAG: Disable grouping of bases for reads >50bp. All reports will show data for every base in the read. (true/false)
# Run Fastqc on bam files

LOGDIR = log/fastqc.$(NOW)

SAMPLE_FILE ?= samples.txt
SAMPLES ?= $(shell cat $(SAMPLE_FILE))

BAM_DIR ?= bam
OUTPUT_DIR ?= fastqc

include ~/share/modules/Makefile.inc

FASTQC_OPTS ?= -o $(@D)

# Disable grouping of bases for reads >50bp. All reports will show data for every base in the read.
NOGROUP_FLAG ?= false
ifeq ($(NOGROUP_FLAG),true)
FASTQC_OPTS += --nogroup
endif

.PHONY: all
.SECONDARY: 

all : $(foreach sample,$(SAMPLES),$(OUTPUT_DIR)/$(sample)_fastqc.zip)

$(OUTPUT_DIR)/%_fastqc.zip : $(BAM_DIR)/%.bam
	$(call LSCRIPT_MEM_DRMAA,4G,6G,"$(PERL) $(FASTQC) $(FASTQC_OPTS) $<")
