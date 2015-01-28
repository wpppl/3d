

import urllib



#======3d

url="http://www.17500.cn/getData/3d.TXT"
a=urllib.urlopen(url)
f=a.read()
print(f)
       
fpi = open("3d.txt","w")

fpi.write(f)

fpi.close()
print ("ok!")
