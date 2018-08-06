import re
import urllib.request
import urllib.error
import time
def use_proxy(url):
    #建立异常处理机制
    try:
        req=urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36')
        data = urllib.request.urlopen(req).read()
        return data
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
        #若为URLError异常，延时10秒执行
        time.sleep(10)
    except Exception as e:
        print("exception:"+str(e))
        #若为Exception异常，延时1秒执行
        time.sleep(1)


key="python"
for i in range(0,10):
    key=urllib.request.quote(key)
    thispageurl="http://weixin.sogou.com/weixin?type=2&query="+key+"&page="+str(i)
    thispagedata=use_proxy(thispageurl)
    print(len(str(thispagedata)))
    pat1='<a target="_blank" href="(.*?)"'
    rs1=re.compile(pat1,re.S).findall(str(thispagedata))
    if(len(rs1)==0):
        print("此次（"+str(i)+"页）没成功")
        continue
    for  j in range(0,len(rs1)):
        thisurl=rs1[j]
        thisurl=thisurl.replace("amp;","")
        file="F:/result/第"+str(i)+"页第"+str(j)+"篇文章.html"
        thisdata=use_proxy(thisurl)
        try:
            fh=open(file,"wb")
            fh.write(thisdata)
            fh.close()
            print("第"+str(i)+"页第"+str(j)+"篇文章成功")
        except Exception as e:
            print(e)
            print("第"+str(i)+"页第"+str(j)+"篇文章失败")

