import gzip
# input your fastq read1 file 
f1 = gzip.open("/public/home/tzhu/umi_raw_data/test/C019_fastq_read1.gz", "rt",encoding='utf-8')
# input your fastq read2 file
f2 =gzip.open('/public/home/tzhu/umi_raw_data/C019_fastq_read2.gz',"rt",encoding='utf-8')
f3=open('/public/home/tzhu/umi_raw_data/C019_fq_r2_test','w') #file you want to write the result
x=0
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
    f3.write(umi[i]+ ' ' +lst_read2[x]+'\n'+lst_read2_line[y+1]+lst_read2_line[y+2]+lst_read2_line[y+3])
    x+=1
    y+=4
f3.close()
