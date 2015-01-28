fp1 = open("3d.txt","r")
fp = open("3d_gsh.txt","w")
for line in fp1:
    #print(line[31])#»úºÅ
    #print(line[33])#ÇòºÅ
    #line=fp1.readline()
    #print(line)
    line1=line[0:35]
    print(line1)
    
    fp.write(line1+'\n')   
        
                
fp.close()
fp1.close()
print ("ok!")
