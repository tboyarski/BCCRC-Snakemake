# SnakeTricks: Tips and Tricks when writing in Snakemake

## 1) expand(...)
Parameters:
```
outputDIR: output
mpileDIR: mpile
wildcards.samples= ["Pfeiffer1", "Pfeiffer2"]
```
Output Call:
```
expand("{outputDIR}/{mpileDIR}/{samples}.mpileup", outputDIR=config["outputDIR"], mpileDIR=config["mpileDIR"], samples=wildcards.samples)
```
Output Result:
```
output/mpile/Pfeiffer1.mpileup, output/mpile/Pfeiffer2.mpileup
```


## 2) Inline conditionals
Sometimes you will want to place a condition or a function inside of the output or params directives. Typically this does not function as
intended, and you will often find variables not passing well to the function. The best option is to change your shell directive to a run
directive. That way you can put the conditionals in the run statement. The run statements behaves like a Python script, so conditionals 
are easy to code, do what one would expect, and there is no need to pass variables as they are all automatically passed to run for you. 
See Point 4 for a further discussion on this topic, code examples included!

## 3) External Input Functions which require access to wildcards.
The below code can be seen in "varScan/mpileup2snp" and "varScan/mpileup2indels". Both submoduls need to provide different input statements
depending on how a variable in the '.YAML' configuration file is set. Few things to note in this function call:
 * Input functions automatically pass the wildcard object as their first actual argument
 * External functions used to generate input calls must accept the wildcard object as the first formal parameter
 * External functions using the wildcard object, if named wildcards, would refer to its attributes via dot notation, I.E. wildcards.samples

```
def varScanSplit(wildcards):
   if config["varScanChrSplit"] == True:
       return expand("{outputDIR}/{mpileDIR}/{samples}.{chr}.mpileup", outputDIR=config["outputDIR"], mpileDIR=config["mpileDIR"], chr=config["chrLIST"], samples=wildcards.samples)
   elif config["varScanChrSplit"] == False:
       return expand("{outputDIR}/{mpileDIR}/{samples}.mpileup", outputDIR=config["outputDIR"], mpileDIR=config["mpileDIR"], samples=wildcards.samples)

 rule mpileup2snp:
     input:
         # Function to determine the inputs depending on if split chromosome or not, wildcards is implicitly passed as an agrument.
         varScanSplit
```

## 4) Run versus Shell
I still cannot say for sure which is definitively better, but I can at least demonstrate the differences and let you decide.
Here are two equivalent snippets of code, as used in the reBam/alignBAM module.

"Remember that Snakemake is a syntax extension of Python. In the run directive, there is plain Python code. In the shell directive there is a Python string, 
that gets formatted via the Python format minilanguage (see google). In this minilanguage, you can access Python dictionaries, and because quotes would 
interfere with the quotes of the string, they decided to omit them there." -- Johannes Koester

**Shell/Shell**
Conditionals in a shell directive are inferior as they are really more-so terniary operators. This can result in duplicate code 
if the shell call is multi-part. The part that always runs will have to be replicated in each section. See below.
```
shell:  
       ' {input} {output} {wildcards.sample} {params.firstPARAM} {log} ' + config["varYAML"]
    
shell:
    config["alignBAM_bwaProg"] + ' mem {input[2]} {input[0]} {input[1]}' \
    + ' 2> {log}/{params.logNAME}.bwa.stderr' \
    + ' | ' + config["alignBAM_samtoolsProg"] + ' view -bhS - > {output} ' \
    + ' 2> {log}/{params.logNAME}.sam.stderr'
    # Check if config file set to have fastq files removed after use.
    if config["fastqKEEP"] == False else 
    config["alignBAM_bwaProg"] + ' mem {input[2]} {input[0]} {input[1]}' \
    + ' 2> {log}/{params.logNAME}.bwa.stderr' \
    + ' | ' + config["alignBAM_samtoolsProg"] + ' view -bhS - > {output} ' \
    + ' 2> {log}/{params.logNAME}.sam.stderr'
    + ' && rm {input[0]} {input[1]}'
```

**Run/Shell**
Conditionals in a run directive can be used as one would expect normal Python code to function. However, in using the Snakemake 
shell() command, Snakemake will only accept 0 as an acceptable return value. We found this to be problematic in certian editting
scenarios, as with GREP, where when it doesnt find anything, it return a status of 1, but this gets rejected by Snakemake and it 
is interpretted as a failed read, when actually it isn't. Failure from GREP is error status 2. 
```
run:  
       shell(' {input} {output} {wildcards.sample} {params.firstPARAM} {log} ' + config["varYAML"])
    
run: 
    shell("bwa mem {input[2]} {input[0]} {input[1]} 2> {log}/{params.logNAME}.bwa.stderr | samtools view -bhS - > {output} " \
    "2> {log}/{params.logNAME}.sam.stderr")
    # Check if config file set to have fastq files removed after use.
    if config["fastqKEEP"] == False:
        shell("rm {input[0]} {input[1]}")
```

**Run/Call**
Conditionals work as per Python, but now becuase we are using the Python call() function, we must toString/Stringify all the Snakemake
objects which contain out variables. As a result, the code is much more verbose, however, the control flow and error handing is much stronger.
```
run:  
        input output wildcards.sample params.firstPARAM config["varYAML"]
        call(str(input) + str(output) + wildcards.sample + str(log) + config["varYAML"], shell=True)
    
run:
    call(config["alignBAM_bwaProg"] + ' mem ' + str(input[2]) + ' ' + str(input[0]) + ' ' + str(input[1]) \
    + ' 2> ' + str(log) + '/' + str(params.logNAME) + '.bwa.stderr' \
    + ' | ' + config["alignBAM_samtoolsProg"] + ' view -bhS - > ' + str(output) \
    + ' 2> ' + str(log) + '/' + str(params.logNAME) + '.samtools.stderr', shell=True) 
    # Check if config file set to have fastq files removed after use.
    if config["fastqKEEP"] == False:
        call('rm ' + str(input[0]) + ' ' + str(input[1]), shell=True)
```

## 5) Cyclical Dependencies
I cannot say for sure why this happens, only that it happens and you should watch out for it. Understanding exactly how the DAG generates a cyclical 
dependency is diffucult. There are a few examples, but none of them area meant to be concrete. Usually users are indicated to a cylical dependency 
when Snakemake throws an error and reports a "cyclical dependency has occurred". Typically, this is a result of inputs and outputs that are named
too similarily. Examples are given below to better elucidate:

**BAD**
```
input:
    expand("{outputDIR}/{vcfDIR}/{{sampletSTNM}}_{{samplenSTNM}}.{chrSTNM}.varScan.{{varTypeSTNM}}.vcf", outputDIR=config["outputDIR"], varScanDIR=config["varScanDIR"], chrSTNM=config["chrLIST"])
output:
    expand("{outputDIR}/{vcfDIR}/{{sampletSTNM}}_{{samplenSTNM}}.varScan.{{varTypeSTNM}}.vcf", outputDIR=config["outputDIR"], vcfDIR=config["vcfDIR"])
```
**GOOD**
```
input:
    expand("{outputDIR}/{vcfDIR}/{{sampletSTNM}}_{{samplenSTNM}}.{chrSTNM}.varScan.{{varTypeSTNM}}.vcf", outputDIR=config["outputDIR"], varScanDIR=config["varScanDIR"], chrSTNM=config["chrLIST"])
output:
    expand("{outputDIR}/{vcfDIR}/{{sampletSTNM}}__{{samplenSTNM}}.varScan.{{varTypeSTNM}}.vcf", outputDIR=config["outputDIR"], vcfDIR=config["vcfDIR"])
```

**GOOD**
```
input:
    expand("{outputDIR}/{varScanDIR}/{{sampletSTNM}}_{{samplenSTNM}}.{chrSTNM}.varScan.{{varTypeSTNM}}.vcf", outputDIR=config["outputDIR"], varScanDIR=config["varScanDIR"], chrSTNM=config["chrLIST"])
output:
    expand("{outputDIR}/{vcfDIR}/{{sampletSTNM}}_{{samplenSTNM}}.varScan.{{varTypeSTNM}}.vcf", outputDIR=config["outputDIR"], vcfDIR=config["vcfDIR"])
```