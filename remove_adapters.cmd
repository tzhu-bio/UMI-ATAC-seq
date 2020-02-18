~/umi_atac_seq_data$ mkdir custom_adapters
~/umi_atac_seq_data$ echo -e '>Prefix/1\nCTGTCTCTTATACACATCTCCGAGCCCACGAGAC\n>Prefix/1_rc\nGTCTCGTGGGCTCGGAGATGTGTATAAGAGACAG\n>Prefix/2\nACACTCTTTCCCTACACGACGCTCTTCCGATCT\n>Prefix/2_rc\nAGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT'> custom_adapters/umi_atac.fa
~/umi_atac_seq_data$ trimmomatic PE -threads 15 -phred33 reads1.fastq reads2.fastq reads1.paired.fastq reads1.unpaired.fastq reads2.paired.fastq reads2.unpaired.fastq ILLUMINACLIP:~/umi_atac_seq_data/adapters/umi_atac.fa:2:30:10:8:TRUE SLIDINGWINDOW:4:15 MINLEN:30
