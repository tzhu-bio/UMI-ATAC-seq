import pysam
import os,re
import argparse, sys
parser = argparse.ArgumentParser(description='Removing PCR duplicates with mapping coordinates and UMIs.')
parser.add_argument('infile', action = 'store', nargs = '?', type = str, default = sys.stdin, help = 'Input mapping paired bam')
parser.add_argument('outfile',action = 'store', nargs = '?',type = argparse.FileType('w'), default = sys.stdout,help = 'Output file name')
args = parser.parse_args()
sample_name =os.path.basename(args.infile)
print(sample_name+ ' is running...')
umi_id_dic={}
in_file = pysam.AlignmentFile(args.infile, "rb")
out_file = pysam.AlignmentFile(args.outfile, "wb", template=in_file)
for read in in_file:
    umi=(read.qname.split('_')[1]).split(' ')[0]
    umi_id = "_".join([umi,read.reference_name,str(read.pos),str(read.tlen)])
    if umi_id not in umi_id_dic:
        umi_id_dic[umi_id] =  1
        out_file.write(read)
    else:
        umi_id_dic[umi_id] +=  1
print('Done!')


