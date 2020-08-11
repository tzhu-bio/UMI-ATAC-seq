import gzip
import os,re
import argparse
parser = argparse.ArgumentParser(description='Extract UMIs from FASTQ read1 and add it to FASTQ read2.')
parser.add_argument('umi_fr1', action = 'store', nargs = '?', type = str, default = sys.stdin, help = 'Input new FASTQ read1 produced by extract_umi.py ')
parser.add_argument('fr2', action = 'store', nargs = '?', type = str, default = sys.stdin, help = 'Input FASTQ read2')
parser.add_argument('outfile',action = 'store', nargs = '?',type = argparse.FileType('wb'), default = sys.stdout,help = 'Output file name')
args = parser.parse_args()
f1 = gzip.open(args.umi_fr1,"rt",encoding='utf-8')
f2 = gzip.open(args.fr2,"rt",encoding='utf-8')
sample_name_1 = os.path.basename(args.umi_fr1)
sample_name_2 = os.path.basename(args.outfile)
print('Extract UMIs from '+sample_name_1+' and add it to '+sample_name_2+'.')
f3 = gzip.open(args.outfile,'wb')
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
