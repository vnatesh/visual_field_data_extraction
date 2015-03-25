#!/usr/bin/env python
import re
import string
import time
import os
import fnmatch

start=time.time()



all_vfs=os.listdir('/Users/vikasnatesh/Documents/vf_ois')
vf_list=fnmatch.filter(all_vfs,'*.txt')

for i in vf_list:
    with open(i,'r') as file1, open('/Users/vikasnatesh/Documents/output.txt','a') as file2:
        
# read out all text from the file

        lines=file1.read()

# create primary pattern matching through regular expressions

        ID_pattern=re.compile(r'ID:\s*\d+',re.I)


        fixloss_pattern=re.compile(r'Fixation\s\Losses:\s*\S*',re.I)


        falsepos_pattern1=re.compile(r'false\s\pos\s\errors:\s*\d+\s*\W*\%',re.I)
        falsepos_pattern2=re.compile(r'false\s\pos\s\errors:\s*\d+\/\d+',re.I)


        falseneg_pattern1=re.compile(r'false\s\NEG\s\errors:\s*\d+\s*\W*\%',re.I)
        falseneg_pattern2=re.compile(r'false\s\NEG\s\errors:\s*\d+\/\d+',re.I)


        strat_pattern1=re.compile(r'strategy:\s*sita-standard',re.I)
        strat_pattern2=re.compile(r'strategy:\s*sita standard',re.I)
        strat_pattern3=re.compile(r'strategy:\s*sita-swap',re.I)
        strat_pattern4=re.compile(r'strategy:\s*sita swap',re.I)
        strat_pattern5=re.compile(r'strategy:\s*sita-fast',re.I)
        strat_pattern6=re.compile(r'strategy:\s*sita fast',re.I)
        strat_pattern7=re.compile(r'strategy:\s*two-zone',re.I)
        strat_pattern8=re.compile(r'strategy:\s*two zone',re.I)
        strat_pattern9=re.compile(r'strategy:\s*top',re.I)
        strat_pattern10=re.compile(r'strategy:\s*fastpac',re.I)
        strat_pattern11=re.compile(r'strategy:\s*dynamic',re.I)
        strat_pattern12=re.compile(r'strategy:\s*kinetic',re.I)
        strat_pattern13=re.compile(r'strategy:\s*suprathreshold',re.I)
        strat_pattern14=re.compile(r'strategy:\s*full\s*threshold',re.I)


        PSD_pattern1=re.compile(r'PSD\s*\S+\s*\S*',re.I)
        PSD_pattern2=re.compile(r'PSD',re.I)
        PSD_pattern3=re.compile(r'db',re.I)
        PSD_pattern4=re.compile(r'p<',re.I)
        PSD_pattern5=re.compile(r'\n',re.I)


 
        MD_pattern=re.compile(r'MD\s*\S*\d+',re.I)






        
        a=re.findall(strat_pattern1,lines)+re.findall(strat_pattern2,lines)+re.findall(strat_pattern3,lines)+re.findall(strat_pattern4,lines)+re.findall(strat_pattern5,lines)+re.findall(strat_pattern6,lines)+re.findall(strat_pattern7,lines)+re.findall(strat_pattern8,lines)+re.findall(strat_pattern9,lines)+re.findall(strat_pattern10,lines)+re.findall(strat_pattern11,lines)+re.findall(strat_pattern12,lines)+re.findall(strat_pattern13,lines)+re.findall(strat_pattern14,lines)
        b=re.findall(falsepos_pattern1,lines)+re.findall(falsepos_pattern2,lines)
        c=re.findall(fixloss_pattern,lines)
        d=re.findall(ID_pattern,lines)
        e=re.findall(falseneg_pattern1,lines)+re.findall(falseneg_pattern2,lines)
        f=re.findall(MD_pattern,lines)

        psd1=''.join(re.findall(PSD_pattern1,lines))
        psd2=''.join(re.split(PSD_pattern2,psd1)).strip()
        psd3=re.split(PSD_pattern3,psd2)
        

# create secondary patterns to isolate the specific text and exclude headers

        a_pattern=re.compile(r'strategy:',re.I)
        a=''.join(re.split(a_pattern,''.join(a))).strip()

        b_pattern=re.compile(r'false\s\pos\s\errors:',re.I)
        b=''.join(re.split(b_pattern,''.join(b))).strip()

        c_pattern=re.compile(r'Fixation\s\Losses:',re.I)
        c=''.join(re.split(c_pattern,''.join(c))).strip()

        d_pattern=re.compile(r'ID:',re.I)
        d=''.join(re.split(d_pattern,''.join(d))).strip()

        e_pattern=re.compile(r'false\s\NEG\s\errors:',re.I)
        e=''.join(re.split(e_pattern,''.join(e))).strip()

        f_pattern=re.compile(r'MD',re.I)
        f=''.join(re.split(f_pattern,''.join(f))).strip()



        if a=='TOP':
            psd4=re.split(PSD_pattern5,psd3[0])
            h=''
        else:
            psd4=re.split(PSD_pattern4,''.join(psd3))
            try:
                if '%' in psd4[1]:
                    h=re.split(PSD_pattern5,psd4[1])[0].strip()
##                    h=psd4[1]
                else: h=''
            except IndexError: h=''

        g=re.split(PSD_pattern5,psd4[0])[0].strip()

 #       g=psd4[0].strip()

        
# write out parsing output into "output.txt" file

        file2.write(d +'\t'+a+'\t'+c+'\t'+b+'\t'+e+'\t'+f+'\t'+g+'\t'+h+'\n')
        file1.close()    
        file2.close()



end=time.time()
print end-start
