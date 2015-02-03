# -*- coding: cp936 -*-
fp1 = open("www.txt",'r')
fp = open("3d_xlj.txt","w")
for line in fp1 :
    #print(line[31])#机号
    #print(line[33])#球号
    #line=fp1.readline()
    #print(line)
   
    line1=line[0:25]
    print(line1)
    
    fp.write(line1+'\n')   
        
                
fp.close()
fp1.close()
print ("ok!")
