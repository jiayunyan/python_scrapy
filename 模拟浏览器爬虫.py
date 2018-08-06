import urllib.request
import urllib.error
import re
url="http://blog.csdn.net/"
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
data=opener.open(url).read().decode("utf-8","ignore")
pat='<h3  class="csdn-tracking-statistics" data-mod="popu_430" data-poputype="feed"  data-feed-show="false"  data-dsm="post"><a href="(http://blog.csdn.net/.*?)"  target="_blank">'
result=re.compile(pat).findall(data)
print(result)
for i in range(0,len(result)):
    thisurl=result[i]
    file="F:/csdn/"+str(i)+".html"
    urllib.request.urlretrieve(thisurl, file)
    print("第" + str(i) + "成功")
