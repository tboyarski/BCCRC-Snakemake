# Pipeline Exploration
This repository has been developed for the purpose of tracking the exploration of 
biological pipelines by leveraging the build-automation software tools. The project 
began with a preliminary assessment of the build-automation landscape. Three tools 
were considered reasonable with respect to the scope of requirements as established
for the LCR. The three tools were: Snakemake, BigDataScript, and Nextflow.
    
## POC/  ~Proof of Concept
This directory was used during the initial evaluation of the three languages being 
considered. The POC diretory contains sub-directories for Snakemake and BigDataScript
only. This is due to the early elimination of Nextflow during the evaluation process.


### Snakemake
The language can be considered an extended version of GNUMake. It offers the core
functionality of GNUMake, but provides an additional level of syntactic sugar, as 
well as additional functionality and a bit more code clarity. The ability to 
seemlessly integrate Conda environents, and scripts (Python, R) into rules was a 
significant advantage over other languages considered. Many additional rule specifc
features offered needed granularity. Combined with the flexibility provided by wrappers,
workflows, and reproducible archiving; Snakemake is the preffered choice, as such, a 
dedicated root directory has been created to support pipeline development.
* Status: **Chosen**
* Root-Directory: **Yes**
* http://snakemake.readthedocs.io/en/latest/

### BigDataScript
A langauge very similar to Java and C, it was easily read. It both provided features
not offered, and lacked featured offered by Snakemake. Notably it had very impressive
innate logging functionality. The CLI help assist was also deemed exceptionally useful,
however, it's shortcomings were also significant. The supporting community was limited 
to a handful of individuals, as such, support was limited. Furthermore, it lacked some
features offered by Snakemake, like Conda support.
* Status: **Rejected -- Lack of certain functionality**
* Root-Directory: **No**
* http://pcingola.github.io/BigDataScript/bigDataScript_manual.html

### Nextflow
This language was deemed excessively complex for the needs of our department. The DSL
provided an exceptional number of features; however, many of these features would not
necessarily be used, and the syntactic learning curve was very significant.
* Status: **Rejected -- Excessive complexity and learning curve**
* Root-Directory: **No**
* https://www.nextflow.io/docs/latest/index.html
