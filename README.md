# UMI-ATAC-dedup

This pipeline is used for UMI-ATAC-seq raw data processing, including removing the sequencing adapters, extracting UMIs from the original FASTQ read1 file, removing ME sequences and using the UMIs to remove PCR duplicates.

## Dependencies
UMI-ATAC-dedup is mainly tested in Python 3. It requires the Python modules  `gzip`, `Bio.SeqIO.QualityIO module`and `pysam`. It also requires the software `UMI tools`,`trimmomatic`.

To install these packages with conda run:
+ #### `gzip`: conda install -c ostrokach gzip
+ #### `Bio.SeqIO.QualityIO module`: conda install -c anaconda biopython
+ #### `UMI tools`: conda install -c bioconda umi_tools 
+ #### `pysam`: conda install -c bioconda pysam
+ #### `trimmomatic`: conda install -c bioconda trimmomatic
## workflow

![image]( https://github.com/tzhu-bio/UMI-ATAC-seq/blob/master/workflow.png)
##  Programs
Run python program with the -h argument for detailed help on command-line parameters.

+ ### remove sequencing adapters
This step is performed by `trimmomatic`. Due to the design of UMI-ATAC-seq library, we need to remove sequencing adapters with `NexteraPE-PE` adapter file.

+ ### [umi_tools extract](https://umi-tools.readthedocs.io/en/latest/QUICK_START.html)
We use the `extract` function in `UMI tools` package.This program extracts UMIs from Illumina sequence reads and adds them to the FASTQ read1 header. We can set `--bc-pattern=NNNNNN`(Here we take the first six bases as UMI sequence). We can process the paired-end UMI-ATAC-seq data like this:

```
$ umi_tools extract --stdin=pair.1.fastq.gz --bc-pattern=NNNNNN --log=processed.log --stdout processed.1.fastq.gz
```
+ ### remove_me.py
This program removes the ME sequence (AGATGTGTATAAGAGACAG) and the sequence before it (both sequence and qualities) in FASTQ read1 file. It reads and writes in FASTQ format.  The input and output are gzip file format (`.gz`).


+ ### rm_dup.py
This program removes PCR duplicates with mapping coordinates. You can also use softwares(such as `Picard`,`samtools`) to do this. 

+ ### rm_umi_dup.py
This program removes PCR duplicates with mapping coordinates and UMIs. The reads have the identical mapping coordinates but have differnet UMIs, and we consider they come from different Tn5 insertion events rather than real PCR duplicates. 

## Publication




