---
title: 百度主动推送（Python）
date: 2018-09-01 10:09:26
tags: [百度主动推送, Python]
---
之前做过一个用 ***C#*** 写的百度站长主动推送程序，并设置了任务计划，具体内容点 **[这里](https://www.diostudio.wang/2014/05/26/Urls-Auto-Push-Service-by-CSharp/)** ，现在在学习 ***Python*** ，所以又写了一个基于 ***Python*** 的百度站长主动推送程序，供大家参考，代码如下：

	import requests
	import datetime
	
	def UrlsAutoPush():
	    # 读取 urls.txt 中需要推送的链接
	    urls = {'file': open('urls.txt', 'rb')}
	    # 将 urls 推送至百度，并接收百度返回的结果
	    baiduResult = requests.post("http://data.zz.baidu.com/urls?site=www.diostudio.wang&token=IXUROgLSmZjHZm6P", files=urls)
	
	    result = {
	            "surplusQuantity" : baiduResult.text[10:17], # 今日剩余推送数量
	            "successQuantity" : baiduResult.text[28:29]  # 本次成功推送数量,这里去几位数根据你的url数量自己调整就可以了
	        }
	
	    return result
	
	def FeedBack():
	    resultFile = open("result.txt", "a")
	    result = UrlsAutoPush()
	    # 判断最高位是否大于0，无论成功还是失败都写入日志
	    if int(result["successQuantity"]) > 0:
	        resultFile.write(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "\tSurplus URLs Quantities : " + result["surplusQuantity"] + "\tSuccess URLs Quantities : " + result["successQuantity"] + "\n")
	    else:
	        resultFile.write(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "COME TO NOTHING!!!\n")
	
	    resultFile.close()
	
	if __name__ == "__main__":
	    FeedBack()

这里没有设置任务计划，因为不知道什么原因在我的电脑、公司的电脑上设置之后都无法运行，等有时间在看看怎么解决。

----------

<div align="center">
    ![自媒平台.jpg](https://i.loli.net/2019/07/29/5d3ea08e5052e51593.jpg)
</div>

