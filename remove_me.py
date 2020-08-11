import os,re
import gzip
import argparse, sys
from fuzzysearch import find_near_matches
from Bio.SeqIO.QualityIO import FastqGeneralIterator
file_in = gzip.open('/public/home/tzhu/umi_raw_data/C019_umitools_processed.1_40000.fastq.gz', "rt",encoding='utf-8')
UMI_out = gzip.open('/public/home/tzhu/umi_raw_data/test_8_11.fastq.gz','wt')
#print('Removing ME sequences in ' + os.path.basename(args.infile)+'...')
#m=re.compile('AGATG')
for (title,sequence,quantily) in FastqGeneralIterator(file_in):
    fuzzy_match=find_near_matches("AGATGTGTATAAGAGACAG", sequence, max_deletions=1, max_insertions=0,max_substitutions=4)
    if fuzzy_match:
        #pos_start=str(fuzzy_match[0])[12]
        #print(fuzzy_match[0])
        pos_start=str(fuzzy_match[0]).split(',')[0].split('=')[1]
        #b=list(filter(str.isdigit,a))
        print(pos_start)
        UMI_out.write('@'+title+'\n'+sequence[(int(pos_start)+19):]+'\n'+'+'+'\n'+quantily[(int(pos_start)+19):]+'\n')
    else:
        continue
    #me_pos = re.compile(m).search(sequence)
    #UMI_out.write('@'+title+'\n'+sequence[(me_pos.start()+19):]+'\n'+'+'+'\n'+quantily[(me_pos+19):]+'\n')
UMI_out.close()
