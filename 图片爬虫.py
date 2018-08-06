import urllib.request
import re
for i in range(1,10):
    pageurl="http://www.58pic.com/tupian/haibao-0-0-"+str(i)+".html"
    data=urllib.request.urlopen(pageurl).read().decode("utf-8","ignore")
    pat='class="thumb-box" target="_blank"><img  src="(.*?).jpg'
    imglist=re.compile(pat).findall(data)
    for j in range(0,len(imglist)):
        thisimg=imglist[i]
        thisimgurl=thisimg+"_1024.jpg"
        file = "F:/图片/" + str(i) +str(j)+ ".jpg"
        urllib.request.urlretrieve(thisimgurl, file)
        print("第" + str(i) + "页第"+str(j)+"个成功")

