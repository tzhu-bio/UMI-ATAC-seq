import gzip
import os,re
def rename_fastq_read2_header(umi_fastq_read1,fastq_read2,umi_fastq_read2_folder):
    f1 = gzip.open(umi_fastq_read1,"rt",encoding='utf-8')
    f2 = gzip.open(fastq_read2,"rt",encoding='utf-8')
    sample_name = re.sub(".gz","",os.path.basename(fastq_read2))
    path_out = "%s/%s_umi_read2"%(umi_fastq_read2_folder,sample_name)
    f3 = gzip.open(path_out,'wb') #file you want to write the result
    y=0
    umi=[]
    lst_read2_line=[]
    lst_read2=[]
    for line in f1:
        if line.startswith('@'):
            l1_umi=line.strip().split(' ')[0]
            umi.append(l1_umi) 
    for line in f2:
        lst_read2_line.append(line)
        if line.startswith('@'):
            l2=line.strip().split(' ')[1]
            lst_read2.append(l2)
    for i in range(len(umi)):        
        f3.write(umi[i].encode()+ ' '.encode() +lst_read2[i].encode()+'\n'.encode()+lst_read2_line[y+1].encode()+lst_read2_line[y+2].encode()+lst_read2_line[y+3].encode())
        y+=4
    f3.close()
    print('Done')
