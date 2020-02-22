import pysam
import os,re
def rm_umi_dup(bam_file,bam_out_folder):
    umi_type = {6:"A1",13:"A5",20:"A6",25:"A7"}
    sample_name = re.sub(".bam","",os.path.basename(bam_file))
    print(sample_name+' is running...')
    umi_id_dict={}
    path_out = "%s/%s_rm_umidup.bam"%(bam_out_folder,sample_name)
    infile = pysam.AlignmentFile(bam_file, "rb")
    outfile = pysam.AlignmentFile(path_out, "wb", template=infile)
    for read in infile:
        umi = read.qname.split(':')[7]
        if len(umi) in umi_type:
            umi_id = "_".join([umi,read.reference_name,str(read.pos),str(read.tlen)])
            if umi_id not in umi_id_dict:
                umi_id_dict[umi_id] = 1
                outfile.write(read)
            else:
                umi_id_dict[umi_id] += 1
    print('Done')


