#!/bin/bash
rm -rf output/
rm -rf log/
rm -rf .snakemake/
rm Snakefile
rm input/config.yaml
rm input/config.json
m dag.svg
python buildPipe.py
