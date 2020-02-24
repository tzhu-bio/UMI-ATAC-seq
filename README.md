# UMI-ATAC-dedup

This pipeline is for UMI-ATAC-seq raw data processing, including extract the UMIs from raw FASTQ read1 file, rename the FASTQ read2 header, remove sequencing adapters and PCR deduplications with UMIs.

## Dependencies
UMI-ATAC-dedup is mainly tested  in Python 3 and shell commands. It requires the Python modules  `gzip`, `Bio.SeqIO.QualityIO module`and `pysam`. It also requires the software `trimmomatic`.

To install these packages with conda run:
#### `gzip`: conda install -c ostrokach gzip
#### `Bio.SeqIO.QualityIO module`: conda install -c anaconda biopython
#### `pysam`: conda install -c bioconda pysam
#### `trimmomatic`: conda install -c bioconda trimmomatic
## workflow

![image]( https://github.com/tzhu-bio/UMI-ATAC-seq/blob/master/workflow.jpg)
##  Programs
Run python program with the -h argument for detailed help on command-line parameters.
### extract_umi.py
This program extracts UMIs from Illumina sequence reads and adds them to the FASTQ read1 header. It also removes the ME sequence (AGATGTGTATAAGAGACAG) and the sequence before it (both sequence and qualities). It reads and writes in FASTQ format. This step uses the FASTQ read1 file (`.gz`).

### rename_fastq_read2_header.py

This program adds the UMIs to fastq read2 header. The input and output are gzip file format (`.gz`).

### remove adapters.cmd
This step is performed on shell commands. Due to the design of UMI-ATAC-seq library, we need to customize a adapters combination file.

### rm_dup.py
This program removes PCR duplicates with mapping coordinates. You can also use softwares(eg,`Picard`,`samtools`) to do this. 

### rm_umi_dup.py
This program removes PCR duplicates with mapping coordinates and UMIs. The reads have the identical mapping coordinates but have differnet UMIs, we consider they are from identical Tn5 insertion events rather than true PCR duplicates. 

## Publication




