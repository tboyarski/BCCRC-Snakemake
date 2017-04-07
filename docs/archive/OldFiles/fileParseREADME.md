#fileParse Module (Python)
Allows the parsing of input files to return python collections of the input.

## Calling the Script
E.g. python path/to/fileParse.py type inputFILE yamlFILE
```
python fileParse/fileParse.py hash SamplePairs.txt MyYaml.yaml
python fileParse/fileParse.py line SampleSingleLines.txt MyYaml.yaml
python fileParse/fileParse.py csv SampleSingleCSV.txt MyYaml.yaml
```    


## Input file formatting and setup
The following describes how the input files for fileParse.py are to be setup.

###SamplePairs.txt
Sample-pairs should be formatted in a .TXT file as seen below. They can be space or table delimited. 
The number of spaces or tabs used does not matter as we are using a Python fuction called "split()"
which handles "whitespace".
```
1G 1B
2G  2B
3G    3B
4G  4B
5G 5B
```

###SampleSingleCST.txt
Samples which are CSV delimited should be formatted as seen below. There should not be any white 
space inbetween the sample names as the regex function is only looking for a ",".
```
1G,2G,3G,4G,5G,6G  
```

###SampleSingleLines.txt
Samples which are separated by line should be formatted as seen below. A single word is read 
from each line, so the spacing on the line should not matter. Include one sample name per line.
```
Pfeiffer2
Pfeiffer3
```
