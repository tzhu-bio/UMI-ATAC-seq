import os,re
import gzip
import argparse, sys
from fuzzysearch import find_near_matches
from Bio.SeqIO.QualityIO import FastqGeneralIterator
parser = argparse.ArgumentParser(description='remove ME sequences from FASTQ read1.')
parser.add_argument('infile', action = 'store', nargs = '?', type = str, default = sys.stdin, help = 'Input FASTQ read1 processed by umi tools extract')
parser.add_argument('outfile',action = 'store', nargs = '?',type = argparse.FileType('wb'), default = sys.stdout,help = 'Output file name')
args = parser.parse_args()
file_in = gzip.open(args.infile, "rt",encoding='utf-8')
UMI_out = gzip.open(args.outfile,'wt')
print('Removing ME sequences in ' + os.path.basename(args.infile)+'...')

for (title,sequence,quantily) in FastqGeneralIterator(file_in):
    fuzzy_match=find_near_matches("AGATGTGTATAAGAGACAG", sequence, max_deletions=1, max_insertions=0,max_substitutions=4)
    if fuzzy_match:
        pos_start=str(fuzzy_match[0]).split(',')[0].split('=')[1]
        UMI_out.write('@'+title+'\n'+sequence[(int(pos_start)+19):]+'\n'+'+'+'\n'+quantily[(int(pos_start)+19):]+'\n')
    else:
        continue
file_in.close()
UMI_out.close()

