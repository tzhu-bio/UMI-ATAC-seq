from Bio.SeqIO.QualityIO import FastqGeneralIterator
import os,re
import gzip
def extract_umi(f_in,f_out_name):
    me_1 = re.compile("AGATG")
    me_7 = re.compile("GTATA")
    me_15 = re.compile("GACAG")
    file_in = gzip.open(f_in, "rt",encoding='utf-8')
    UMI_out=open(os.path.dirname(f_in)+'/'+f_out_name,'w')
    for (title,sequence,quantily) in FastqGeneralIterator(file_in):
        me_1_pos = me_1.search(sequence)
        me_7_pos = me_7.search(sequence)
        me_15_pos = me_15.search(sequence)
        if me_1_pos and me_7_pos and (me_7_pos.start() - me_1_pos.start() == 6):
            UMI_out.write('@'+title.strip().split(' ')[0]+'_UMI:'+sequence[:6]+' '+title.strip().split(' ')[1]+'\n'+sequence[(me_1_pos.start()+19):]+'\n'+'+'+'\n'+quantily[(me_1_pos.start()+19):]+'\n')
        elif me_1_pos and me_15_pos and (me_15_pos.start() - me_1_pos.start() == 14):
            UMI_out.write('@'+title.strip().split(' ')[0]+'_UMI:'+sequence[:6]+' '+title.strip().split(' ')[1]+'\n'+sequence[(me_1_pos.start()+19):]+'\n'+'+'+'\n'+quantily[(me_1_pos.start()+19):]+'\n')
        elif me_15_pos and me_7_pos and (me_15_pos.start() - me_7_pos.start() == 8):
            UMI_out.write('@'+title.strip().split(' ')[0]+'_UMI:'+sequence[:6]+' '+title.strip().split(' ')[1]+'\n'+sequence[(me_15_pos.start()+5):]+'\n'+'+'+'\n'+quantily[(me_15_pos.start()+5):]+'\n')
    UMI_out.close()
