# buildFile Module (Multi-Python)
Assist in generating the '.YAML' and 'Snakefile' for a pipeline. 

## Modules:
See individual files for expanded explanations of their purpose and the manner in which they accomplish it.
* buildHeader.py = Creates YAML and Snake file, added generic parameters to both.
* buildSample.py = Adds the sample parameter to the YAML file. 

Calling the Script ~ python path/to/buildFile.py type sampleFILE chrTYPE yamlFILE jsonFILE snakeFILE
```
python buildFile.py pair sampleFILEpair.txt hncbi config.yaml config.json Snakefile
python buildFile.py single sampleFILEsingle.txt hncbi config.yaml config.json Snakefile
python buildFile.py csv sampleFILEcsv.txt hncbi config.yaml config.json Snakefile
```    

### buildHeader.py
Contain functions to assist in creation and population of both the YAML and Snakefile. The resulting
files are to be used as the core documents for a prospective pipeline. 
```
buildHeader(chrTYPE, yamlFILE, jsonFILE, snakeFILE)
```
**chrTYPE**
 * Human: NCBI ~ 'hncbi'
 * Human: UCS ~ 'hucs'
 * Mouse: NCBI ~ 'mncbi'
 * Mouse: UCS ~ 'mucs'

### buildSample.py
Contains functions to assit in opening, parsing, and outputting to the YAML file the user's desired
samples, as dervied from a sample file. The following describes file formatting for input files for 
functions in buildSample.py.
```
buildSample(type, sampleFILE, yamlFILE)
```

**sampleFILEpair.txt** - Sample-pairs should be formatted in a .TXT file as seen below. They can be space or table delimited. 
The number of spaces or tabs used does not matter as we are using a Python fuction called "split()" which handles "whitespace".
This format is used when processing tumor-normal sample pairs.
 * type = 'pair'
```
Pfeiffer2 Pfeiffer2T
Pfeiffer3 Pfeiffer3T
```

**sampleFILEsingles.txt** - Samples which are separated by line should be formatted as seen below. A single word is read 
from each line, so the spacing on the line should not matter. Include one sample name per line.
 * type = 'single'
```
Pfeiffer2
Pfeiffer3
Pfeiffer4
```
    
**sampleFILEcsv.txt** - Samples which are CSV delimited should be formatted as seen below. There should not be any white 
space inbetween the sample names as the regex function is only looking for a ",".
 * type = 'csv'
```
Pfeiffer2,Pfeiffer3,Pfeiffer4
```

