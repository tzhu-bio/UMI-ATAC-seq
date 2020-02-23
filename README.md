# UMI-ATAC-dedup

This pipeline is for UMI-ATAC-seq raw data processing,including extract the UMI information from raw fastq read1 file,rename the fastq read2 header,remove sequencing adapters and PCR deduplicates with UMIs.

## Dependencies
UMI-ATAC-dedup is mainly tested  in Python 3 and shell commands.  It requires the Python modules  `gzip` ,`Bio.SeqIO.QualityIO module`and `pysam`.It also requires the software `trimmomatic`.
## workflow

![image]( https://github.com/tzhu-bio/UMI-ATAC-seq/blob/master/workflow.jpg)
##  Programs

### extract_umi.py
This program extracts UMIs from Illumina sequence reads and adds them to the fastq read1 header. It also remove the ME sequence (AGATGTGTATAAGAGACAG) and the sequence before it . It reads and writes in FASTQ format . This step uses the raw fastq read1 file (.gz).
**Usage**:extract_umi(`fastq_read1`,`output_file_name`)

### rename_fastq_read2_header.py

This program adds the UMIs to fastq read2 header. 
**Usage**: rename_fastq_read2_header(`fastq read1 path`,`fatsq read2 path`,`output path`). 
The input and output are gzip file format (`.gz`).

### remove adapters.cmd
This step is performed on shell commands. Due to the design of UMI-ATAC-seq library, we need to customize a adapters combination file.
### rm_dup.py

This program removes PCR duplicates with mapping coordinates.You can also use softwares(eg,`Picard`,`samtools`) to do this. 
**Usage**: rm_dup(`input bam file`,`output path`)

### rm_umi_dup.py
This program removes PCR duplicates with mapping coordinates and UMIs. The reads have the identical mapping coordinates but have differnet umi, we consider the reads are from identical Tn5 insertion events rather than PCR duplicates. 
**Usage**: rm_umi_dup(`input bam file`,`output path`)

## Publication




