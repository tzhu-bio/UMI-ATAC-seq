use strict;
use warnings;

my $kmer="AGATGTGTATAAGAGACAG";
my @kmer;
for(my $i=0;$i<=length($kmer)-5;$i++){
  push @kmer,substr($kmer,$i,5);
  #print "",substr($kmer,$i,5),"\n";
}

my $rdir="~/umi_atac_seq/raw_data"; #input your raw fastq pathway
my $wdir="~/umi_atac_seq/temp/result/"; # output umi information pathway
if(! -e $rdir){
 print "error! readdir doesn't exist\n";
}
if(! -e $wdir){
 mkdir $wdir;
}

my $rfile=$rdir."11A2_S2_L008_R1_001.fastq.gz"; # read your raw fastq file
my $wfile=$wdir."11A2_S2_L008_R1_001.fastq.gz"; # write umi information to file
my $logfile=$wdir."11A2_S2_L008_R1_001.fastq.gz.log"; 
open R,"gunzip -c  $rfile  |";
open W,">$wfile";
open LOG,">$logfile";

my @me_end_all;
while(<R>){
  if(($. % 1000000)==1){
    print "current line:\t$.\n";
  }
 
  if(($. % 4) == 1){
    my $flag = $_;my $seq = <R>;my $str = <R>;my $qual=<R>;
    my $seq_s=substr($seq,0,60);
    #print LOG"$.\t$seq_s\n";

    my @me_end=();
    for(my $i=0;$i<=14;$i+=1){
      if($seq_s =~ m/$kmer[$i]/g ){
        my $me_endi=pos($seq_s)-4-$i+18;
        push @me_end,$me_endi;
        #print LOG"$i\t",$me_endi,"\t",substr($seq_s,0,$me_endi),"\t\t";
      }
      pos($seq_s)=0;
    }

    my $end=0;    
    if(scalar(@me_end)>=1){
      my %me_endh;
      for(@me_end){
        $me_endh{$_}++;
      }
      my @end=sort{$me_endh{$b}<=>$me_endh{$a}} keys %me_endh;
      $end=$end[0];
      push @me_end_all,$end;
      #print LOG"$end\t$me_endh{$end}\t",substr($seq_s,0,$end),"\n";
    }else{
      push @me_end_all,$end;
      print LOG"$.\t$seq_s\n";
    }

    my $umi=substr($seq,0,6);
    my ($flag_head,$flag_tail)=split(/ /,$flag,2);
    my $flag_new=$flag_head."_UMI:".$umi." ".$flag_tail; 
    my $seq_new=substr($seq,$end);
    my $qual_new=substr($qual,$end);
    print W $flag_new;
    print W $seq_new;
    #print W substr($seq,0,$end),"\n";
    print W $str;
    print W $qual_new;
    #print W substr($qual,0,$end),"\n";
 
  }
}


my %me_end_allh;
for(@me_end_all){
  $me_end_allh{$_}++;
}
for my $key(sort{$a<=>$b} keys %me_end_allh){
 print "$key\t$me_end_allh{$key}\n";
}


close R;
close W;
