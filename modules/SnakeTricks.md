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
        ## This function call without () is correct!!
        ## http://snakemake.readthedocs.io/en/latest/snakefiles/rules.html?highlight=Functions%20as%20Input%20Files#functions-as-input-files
```


## 4) Run versus Shell
I still cannot find a reason in which 'shell' can do something 'run' cannot. For consistency, as such, I always use 'run'. 
This was also done because the two directives require paramters to be called differently, so it's confusing to try to switch
between the two, I have settled on 'run'.

"Remember that Snakemake is a syntax extension of Python. In the run directive, there is plain Python code. In the shell directive there is a Python string, 
that gets formatted via the Python format minilanguage (see google). In this minilanguage, you can access Python dictionaries, and because quotes would 
interfere with the quotes of the string, they decided to omit them there." -- Johannes Koester

**Preferred = Run/Call**
Conditionals work as per Python, but now becuase we are using the Python call() function, we must toString/Stringify all the Snakemake
objects which contain out variables. As a result, the code is much more verbose, however, the control flow and error handing is much stronger.
```
run:  
        input output wildcards.sample params.firstPARAM config["varYAML"]
        call(str(input) + str(output) + wildcards.sample + str(log) + config["varYAML"], shell=True)
    
run:
    callString=config["annotate_picardProg"] + ' SortVcf ' + str(params.picardARGS)  \
    + ' I= ' + str(input) + ' O=' + str(output) + ' SEQUENCE_DICTIONARY=' + config["picardSortSeqDict"] \
    + ' 2> ' + str(log) + '/' + str(params.logNAME)
    call('echo "' + str(params.logNAME) + ':\n ' + callString + '\n" >> ' + config["shellCallFile"], shell=True)
    call(callString, shell=True)

run:
    ...
    # Check if config file set to have fastq files removed after use.
    if config["fastqKEEP"] == False:
        call('rm ' + str(input[0]) + ' ' + str(input[1]), shell=True)
```

**Avoided = Shell/Shell**
Conditionals in a shell directive are inferior as they are really more-so terniary operators. This can result in duplicate code 
if the shell call is multi-part. The part that always runs will have to be replicated in each section. See below.
```
shell:  
    "somecommand --group {wildcards.group}  < {input}  > {output}"
    
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

**Avoided = Run/Shell**
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


## 6) Failing v_mem requirement errors
When I failed v_mem requirements on the cluster I received a very obscure error. Nothing was ever really printed to the log files, they
were usually empty. This was the 'qacct' report on the error.
```
[tboyarski@login1 buildArea]$ qacct -j 6997551
qname        all.q
hostname     node0143
group        users
owner        tboyarski
project      default_project
department   defaultdepartment
jobname      snakejob.indel.1.sh
jobnumber    6997551
taskid       undefined
account      sge
priority     0
qsub_time    Sat May 13 13:05:29 2017
start_time   Sat May 13 13:05:40 2017
end_time     Sat May 13 13:05:51 2017
granted_pe   ncpus
slots        1
failed       100 : assumedly after job
exit_status  137
...
```


## 7) How to code a MERGE rule.
Johannes has an example here from which inferences can be made.
http://snakemake.readthedocs.io/en/latest/tutorial/advanced.html#step-2-config-files

This indicates that a driver command for the sample name is to be used in the input directive. This is becuase the wildcards are determined from the output names,
but the cases of merges, we often are using a different, more generic name. As such, the names of the indivdual files cannot be derived from the output file name.
Since it cannot be derived from the output name, it must be generated somehow. For the most part, the generation is different between 'single' and 'pair' sample
lists. The 'single' list can just be read from the config file as it's printed there. For the 'pair' list it must be generated using a key-value call via the 
"Pandas" package. Consider copying existing code to do this more easily.

In the case below, the unpack function is required in order to have the 'expand' command execute properly. Otherwise the function just returns a string, and then
Snakemake tries to interpret this string as the actual file name, which obvious won't exist. Instead of generating the file names using purely the config.yaml
and string contatentation, it was preferred to pass in the wild cards as a suffix and work from this. Please refer to code below from 'utils/tableMERGE'

```
# Generate list of required input files with respect to the sampleFORMAT type.
def getInputFileList(wildcards):
    # Process if single
    if config["sampleFORMAT"] == 'single' or config["sampleFORMAT"] == 'csv':
        return unpack(expand("{outputDIR}/{varTablesDIR}/{samples}.{fileSuffix}",
            outputDIR=config["outputDIR"], varTablesDIR=config["varTablesDIR"],
            samples=config["sample"], fileSuffix=wildcards.annotationSUFFIX))
    # Process if pair
    elif config["sampleFORMAT"] == 'pair':
        return unpack(expand("{outputDIR}/{varTablesDIR}/{sample[1][tumor]}_{sample[1][normal]}.{fileSuffix}",
            outputDIR=config["outputDIR"], varTablesDIR=config["varTablesDIR"],
            sample=pandas.read_table(config["sampleFILE"], " ").iterrows(), fileSuffix=wildcards.annotationSUFFIX))

rule tableMERGE:
    input:
        # Need to provide sample names, generation of list different for 'single' versus 'pair'
        getInputFileList
    output:
        expand("{outputDIR}/{varTablesDIR}/all.samples.{{annotationSUFFIX}}", outputDIR=config["outputDIR"], varTablesDIR=config["varTablesDIR"])
```

## 8) When naming jobs on the cluster, it cannot include '/'
This has to do with how the jobs are setup locally before they are submitted to the clsuter by Snakemake. If you include '/' it creates a directory to put the temp
files in and this messes things up. Just don't use the. It can easily be alleviated by adding extra wildcards such that the sample name, or whatever portion is to
be used in the job name, to pull any path associated '/' into a different wildcard which is not included in the job name.


