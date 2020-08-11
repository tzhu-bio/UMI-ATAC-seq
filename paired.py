import os,re
import gzip
import argparse, sys
from Bio.SeqIO.QualityIO import FastqGeneralIterator
parser = argparse.ArgumentParser(description='Paired the read1 and read2 file.')
parser.add_argument('umi_fr1', action = 'store', nargs = '?', type = str, default = sys.stdin, help = 'Input new FASTQ read1 produced by remove_me.py ')
parser.add_argument('fr2', action = 'store', nargs = '?', type = str, default = sys.stdin, help = 'Input FASTQ read2 produced by umi_tools_extract.py')
parser.add_argument('outfile',action = 'store', nargs = '?',type = str, default = sys.stdout,help = 'Output file name')
args = parser.parse_args()
r1_lst=[]
f1 = gzip.open(args.umi_fr1,"rt",encoding='utf-8')
f2 = gzip.open(args.fr2,"rt",encoding='utf-8')
sample_name_1 = os.path.basename(args.umi_fr1)
sample_name_2 = os.path.basename(args.fr2)
print('Paired '+sample_name_1+' and '+sample_name_2+' ...')
f3 = gzip.open(args.outfile,'wt')
for (title,sequence,quantily) in FastqGeneralIterator(f1):
    r1_lst.append(title.strip().split(' ')[0])
for (title,sequence,quantily) in FastqGeneralIterator(f2):
    r2_name=title.strip().split(' ')[0]
    if r2_name in r1_lst:
        f3.write('@'+title+'\n'+sequence+'\n'+'+'+'\n'+quantily+'\n')
print('Done!')
f1.close()
f2.close()
f3.close()
