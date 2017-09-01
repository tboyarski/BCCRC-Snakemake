# Modules Directory
This directory exists to separate and organize the modules from all other workflow related materials.
Each module is to be setup following a specific criteria, in doing so, the files can then be accessed 
in a repeatable manner. The structure begins by creating a directory named after the module you wish
to create. The directory should include only a single module, or a group of highly correlated modules.
The directory (E.g MyMod/) then must contain the following:

**BasicPipelineExample.svg is to be a visualize aid for when designing pipelines with this system**

### Python Modules
* **README.md** - (Markdown) ~ Describe what the module does.
* **MyMod.py** - (Python) ~ A function, or a group of highly correlated functions. The python script which is to 
be used when populating a pipeline is to be named the same as the directory in which it is contained. 
All subsequent functions can be included in the directory, but their purpose should be highly related to 
the main script. In the event of two or more scripts, the directory named script is to not contain any 
new functionality, but rather, it calls and collates the other modules in the directory in a single source. 
* **MyOther.py** - (Python) ~ Supporting module with specific functions.
* **MyNother.py** - (Python) ~ Supporting module with specific functions.

### Snakemake Modules
* **README.md** - (Markdown) ~ Describe what the module does.
* **MyMod.py** - (Python) ~ Auto-generating script to place module into a pipeline. 
* **MyMod_INCLUDE** - (Snakemake) ~ Contains the rules and funtionality of module. The Snakemake script is to
be referred to by various pipelines. The script is to be named the same as the directory in which it is
contained. All subsequent Snakefiles can be incldued in the directory, but their purpose should be highly
related to the main Snakefile. In the event of two or more Snakefiles, the directory named Snakefile is not 
to contain any new rules, but rather, it calls and collates the other modules in the directory in a single
source.
* **MoreSnake** - (Snakemake) ~ Supporting module with specific rules.
* **AnotherSnake** - (Snakemake) ~ Supporting module with specific rules.
