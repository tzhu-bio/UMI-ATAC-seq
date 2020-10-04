import os,re
import time
import gzip
import argparse, sys
from joblib import Parallel, delayed
from fuzzysearch import find_near_matches
from Bio.SeqIO.QualityIO import FastqGeneralIterator
parser = argparse.ArgumentParser(description='remove ME sequences from FASTQ read1.')
parser.add_argument('infile', action = 'store', nargs = '?', type = str, default = sys.stdin, help = 'Input FASTQ read1 processed by umi tools extract')
parser.add_argument('outfile',action = 'store', nargs = '?',type = argparse.FileType('wb'), default = sys.stdout,help = 'Output file name')
args = parser.parse_args()
time_start=time.time()
def match(title,sequence,quantily):
    fuzzy_match=find_near_matches("AGATGTGTATAAGAGACAG", sequence, max_deletions=1, max_insertions=0,max_substitutions=4)
    if fuzzy_match:
        pos_start=str(fuzzy_match[0]).split(',')[0].split('=')[1]
        a=('@'+title+'\n'+sequence[(int(pos_start)+19):]+'\n'+'+'+'\n'+quantily[(int(pos_start)+19):]+'\n')
        all_lst.append(a)
        return a
    return None
if __name__ == '__main__':
    file_in = gzip.open(args.infile, "rt",encoding='utf-8')
    UMI_out = gzip.open(args.outfile,'wt')
    print('Removing ME sequences in ' + os.path.basename(args.infile)+'...')
    all_lst=[]
    all_lst=Parallel(n_jobs= 10)(delayed(match)(title,sequence,quantily) for title,sequence,quantily in FastqGeneralIterator(file_in))
    for line in all_lst:
        if line:
            UMI_out.write(line)
    UMI_out.close()
    file_in.close()
time_end=time.time()
print('Totally cost',float((time_end-time_start)/60),'min')

