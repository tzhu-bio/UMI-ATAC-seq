import pysam
import os,re
def rm_dup_bam(bam_file,bam_out_folder):
    umi_type = {6:"A1",13:"A5",20:"A6",25:"A7"}
    sample_name = re.sub(".bam","",os.path.basename(bam_file))
    print(sample_name+ ' is running')
    rmdup_dic={}
    path_out = "%s/%s_rm_dup.bam"%(bam_out_folder,sample_name)
    infile = pysam.AlignmentFile(bam_file, "rb")
    outfile = pysam.AlignmentFile(path_out, "wb", template=infile)
    for read in infile:
        umi = read.qname.split(':')[7]
        if len(umi) in umi_type:
            seq_id = "_".join([read.reference_name,str(read.pos),str(read.tlen)])
            if seq_id not in rmdup_dic:
                rmdup_dic[seq_id] =  1
                outfile.write(read)
            else:
                rmdup_dic[seq_id] +=  1
    print('Done!')
    

