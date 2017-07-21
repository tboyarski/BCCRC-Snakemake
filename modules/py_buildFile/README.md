# buildFile Module (Multi-Python)
Assist in generating the YAML, JSON and Snakefile for a pipeline. This scripting module is utilized by 
the startHERE module to help automate the process of setting up a new Snakemake project pipeline workspace.

## Modules:
See individual files for expanded explanations of their purpose and the manner in which they accomplish it.
* buildFile.py = Validates, reporting, and calling of 'buildHeader.py' and 'buildSample.py' scripts.
* buildHeader.py = Builds the headers for the YAML, JSON, and Snakemake files.
* buildSample.py = Inserts the sample data into the YAML file. 

Calling the Script ~ python path/to/buildFile.py type sampleFILE chrTYPE yamlFILE jsonFILE snakeFILE
```
python buildFile.py pair sampleFILEpair.txt hncbi config.yaml config.json Snakefile
python buildFile.py single sampleFILEsingle.txt hncbi config.yaml config.json Snakefile
python buildFile.py csv sampleFILEcsv.txt hncbi config.yaml config.json Snakefile
```    

### buildHeader.py
Contain functions to assist in creation and population of both the YAML and Snakefile. The resulting
files are to be used as the core documents for a prospective pipeline. The refFILE argument provided 
is used to identify the list of chromosomes to be used for this pipeline.
```
buildHeader(refFILE, yamlFILE, jsonFILE, snakeFILE)
```

### buildSample.py
Contains functions to assit in opening, parsing, and outputting to the YAML file the user's desired
samples, as dervied from a sample file. The following describes file formatting for input files for 
functions in buildSample.py.
```
buildSample(type, sampleFILE, yamlFILE)
```


**sampleFILEpair.txt** - Sample-pairs should be formatted by 2-column line as seen below. They can be space or tab separated. 
The number of spaces or tabs used does not matter as we are using a Python fuction called "split()" which handles "whitespace".
This format is used when processing tumor-normal sample pairs.
 * type = 'pair'
```i
tumor normal
Pfeiffer2T Pfeiffer2N
Pfeiffer3T Pfeiffer3N
```

**sampleFILEsingles.txt** - Samples which are separated by line should be formatted as seen below. A single word is read 
from each line, so the spacing on the line should not matter. Include one sample name per line.
 * type = 'single'
```
Pfeiffer2
Pfeiffer3
Pfeiffer4
```
