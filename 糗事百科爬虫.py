import re
import urllib.request
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
for i in range(1,3):
    url="https://www.qiushibaike.com/8hr/page/"+str(i)
    pagedata=urllib.request.urlopen(url).read().decode("utf-8","ignore")
    pat='<div class="content">.*?<span>(.*?)</span>.*?</div>'
    datalist=re.compile(pat,re.S).findall(pagedata)
    for j in range(0,len(datalist)):
        print("第"+str(i)+"页第"+str(j)+"个段子内容是：")
        print(datalist[j])


