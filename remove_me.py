import os,re
import gzip
import argparse, sys
from Bio.SeqIO.QualityIO import FastqGeneralIterator
parser = argparse.ArgumentParser(description='remove ME sequences from FASTQ read1.')
parser.add_argument('infile', action = 'store', nargs = '?', type = str, default = sys.stdin, help = 'Input FASTQ read1 processed by umi tools extract')
parser.add_argument('outfile',action = 'store', nargs = '?',type = argparse.FileType('wb'), default = sys.stdout,help = 'Output file name')
args = parser.parse_args()
me_1 = re.compile("AGATG")
me_7 = re.compile("GTATA")
me_15 = re.compile("GACAG")
file_in = gzip.open(args.infile, "rt",encoding='utf-8')
UMI_out = gzip.open(args.outfile,'wt')
print('Removing ME sequences in ' + os.path.basename(args.infile)+'...')
for (title,sequence,quantily) in FastqGeneralIterator(file_in):
    me_1_pos = me_1.search(sequence)
    me_7_pos = me_7.search(sequence)
    me_15_pos = me_15.search(sequence)
    if me_1_pos and me_7_pos and (me_7_pos.start() - me_1_pos.start() == 6):
        UMI_out.write('@'+title+'\n'+sequence[(me_1_pos.start()+19):]+'\n'+'+'+'\n'+quantily[(me_1_pos.start()+19):]+'\n')
    elif me_1_pos and me_15_pos and (me_15_pos.start() - me_1_pos.start() == 14):
        UMI_out.write('@'+title+'\n'+sequence[(me_1_pos.start()+19):]+'\n'+'+'+'\n'+quantily[(me_1_pos.start()+19):]+'\n')
    elif me_15_pos and me_7_pos and (me_15_pos.start() - me_7_pos.start() == 8):
        UMI_out.write('@'+title+'\n'+sequence[(me_15_pos.start()+5):]+'\n'+'+'+'\n'+quantily[(me_15_pos.start()+5):]+'\n')
UMI_out.close()
print('Done!')
