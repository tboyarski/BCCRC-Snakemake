# buildFile Module (Multi-Python)
Assist in generating the '.YAML' and 'Snakefile' for a pipeline. 

## Modules:
See individual files for expanded explanations of their purpose and the manner in which they accomplish it.
* buildHeader.py = Creates YAML and Snake file, added generic parameters to both.
* buildSample.py = Adds the sample parameter to the YAML file. 

Calling the Script ~ python path/to/buildFile.py type inputFILE yamlFILE snakeFILE
```
python buildFile.py hash SamplePairs.txt MyYaml.yaml Snakefile
python buildFile.py line SampleSingleLines.txt MyYaml.yaml Snakefile
python buildFile.py csv SampleSingleCSV.txt MyYaml.yaml Snakefile
```    

### buildHeader.py
Contain functions to assist in creation and population of both the YAML and Snakefile. The resulting
files are to be used as the core documents for a prospective pipeline. 

### buildSample.py
Contains functions to assit in opening, parsing, and outputting to the YAML file the user's desired
samples, as dervied from a sample file. The following describes file formatting for input files for 
functions in buildSample.py.

**SamplePairs.txt** - Sample-pairs should be formatted in a .TXT file as seen below. They can be space or table delimited. 
The number of spaces or tabs used does not matter as we are using a Python fuction called "split()"
which handles "whitespace".
```
1G 1B
2G  2B
3G    3B
4G  4B
5G 5B
```

**SampleSingleCST.txt** - Samples which are CSV delimited should be formatted as seen below. There should not be any white 
space inbetween the sample names as the regex function is only looking for a ",".
```
1G,2G,3G,4G,5G,6G  
```

**SampleSingleLines.txt** - Samples which are separated by line should be formatted as seen below. A single word is read 
from each line, so the spacing on the line should not matter. Include one sample name per line.
```
Pfeiffer2
Pfeiffer3
```
