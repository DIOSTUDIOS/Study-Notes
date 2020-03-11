---
title: Python爬虫 学习笔记 01
date: 2018-08-30 22:12:41
tags: [Python, 爬虫, Spider]
---

# 开发环境 #

- Windows 7 旗舰版 x64
- Python 3.7

# 所需模块 #

- requests
- re

# 福利放送 #

我们将以爬去[校花网](http://www.xiaohuar.com/)的美女图片为目标，来开展我们的学习活动。

# 学习目标 #

将[校花网女神百科](http://www.xiaohuar.com/nvshen/)频道中的图片下载到本地，

# 网站分析 #

根据我们的目标，就获得了第一个参数 —— 目标网站的URL：**http://www.xiaohuar.com/nvshen/**，代码如下：

    # 导入我们需要的模块
    import requests
    import re
    
    # 定义爬虫函数
    def NvShenSpider():
    	# 定义目标网站的URL
    	gateUrl = "http://www.xiaohuar.com/nvshen/"

我们在浏览器（我使用的是Chrome）中打开网站，按 **F12** 打开 *开发者工具* ，如下图所示：

[![1.jpg](https://i.loli.net/2018/08/30/5b87d9643c228.jpg)](https://i.loli.net/2018/08/30/5b87d9643c228.jpg)

我们随便选择一张图片，看一下该图片的url是什么，如上图中红框中的部分，将其复制到浏览器中打开验证一下是否是该链接，

    http://www.xiaohuar.com/d/file/20151120/fd265b38be88ad52a3de87b1582e5bfe.jpg

在浏览器中打开上面的链接之后，我们可以看到下面的页面，如下图所示：

[![2.jpg](https://i.loli.net/2018/08/30/5b87d964133ca.jpg)](https://i.loli.net/2018/08/30/5b87d964133ca.jpg)

证明我们的分析是正确的，我们只要抓去这个链接就可以将图片下载下来。因为，我们想要将网页中的图片全部下载下来，那我们再找几个图片看看它们的链接是不是都是上面那个格式的？

    http://www.xiaohuar.com/d/file/20150919/27b984dabaf5aca51794c23f91347bd5.jpg
    http://www.xiaohuar.com/d/file/20150901/94aa0bced3a6568687cac371333fd998.jpg
    http://www.xiaohuar.com/d/file/20150830/93e9275048eb68924658a8420e8a2597.jpg
    ......................./d/file/20150827/31bcf4c523862d92ed80888e10436c52.jpg
    http://www.xiaohuar.com/d/file/20150830/93e9275048eb68924658a8420e8a2597.jpg

通过比对我们可以看到大部分的链接都是如第一个链接一样，具有相同的格式，也有不一样的，我们只需要做一下处理，使它们具有相同个结构即可。

# 反馈给我们的内容 #

我们先爬取一下网站，看看它给我们返回的数据是什么？看看我们都需要做什么处理，代码如下：

```python
# 导入我们需要的模块
import requests
import re

# 定义爬虫函数
def NvShenSpider():
	# 定义目标网站的URL
	gateUrl = "http://www.xiaohuar.com/nvshen/"
	# 给网站发送一个request，并得到网站反馈的response
	response = requests.get(url=gateUrl)

	print(response.text)
	
if __name__ == "__main__":
	NvShenSpider()
	
	pass
```

# 有价值的信息 #

运行上面的代码，我们得到以下反馈结果（我将不需要的部分删除了），如下图所示：

[![3.jpg](https://i.loli.net/2018/08/30/5b87eb2f913d3.jpg)](https://i.loli.net/2018/08/30/5b87eb2f913d3.jpg)

我们可以看到，我们实际得到的数据大多数是没有 ***http://www.xiaohuar.com*** 这部分的（其中有一条是有的，那我们就需要针对这一条做一下特殊处理）。

# 将有价值得信息转换为更有价值得信息 #

现在我们就需要利用正则表达式将我们需要的部分提取出来，代码如下：

```python
# 导入我们需要的模块
import requests
import re

# 定义爬虫函数
def NvShenSpider():
	# 定义目标网站的URL
	gateUrl = "http://www.xiaohuar.com/nvshen/"
	# 给网站发送一个request，并得到网站反馈的response
	response = requests.get(url=gateUrl)

	# print(response.text)

	imagesUrls = re.findall(r'class="items".*?src="(.*?)"', response.text, re.S)

	print(imagesUrls)

if __name__ == "__main__":
	NvShenSpider()
	
	pass
```

经过上面代码的处理，我们已经得到了我们期望的部分，如下图所示：

[![4.jpg](https://i.loli.net/2018/08/30/5b87ecbc6b243.jpg)](https://i.loli.net/2018/08/30/5b87ecbc6b243.jpg)

从上图中我们看到这些链接格式不统一，我们只需要做一下简单的处理使它们统一就行了，代码如下：

```python
# 导入我们需要的模块
import requests
import re

# 定义爬虫函数
def NvShenSpider():
	# 定义目标网站的URL
	gateUrl = "http://www.xiaohuar.com/nvshen/"
	# 给网站发送一个request，并得到网站反馈的response
	response = requests.get(url=gateUrl)

	# print(response.text)

	imagesUrls = re.findall(r'class="items".*?src="(.*?)"', response.text, re.S)

	# print(imagesUrls)

	for i in range(0, 22):
		if imagesUrls[i][0:23] != "http://www.xiaohuar.com":
			imagesUrls[i] = "http://www.xiaohuar.com" + imagesUrls[i]
		else:
			continue

		i += 1

	print(imagesUrls)
	
if __name__ =="__main__":
	NvShenSpider()
	
	pass
```

运行一下，看看结果如何：

[![5.jpg](https://i.loli.net/2018/08/30/5b87f10fb14fb.jpg)](https://i.loli.net/2018/08/30/5b87f10fb14fb.jpg)

这些链接正是我们想要的

# 根据更有价值得信息爬去目标并保存 #

现在我们就可以根据上面得到的链接进行进一步爬取图片了，代码如下：

```python
# 导入我们需要的模块
import requests
import re

# 定义爬虫函数
def NvShenSpider():
	# 定义目标网站的URL
	gateUrl = "http://www.xiaohuar.com/nvshen/"
	# 给网站发送一个request，并得到网站反馈的response
	response = requests.get(url=gateUrl)

	# print(response.text)
	# 利用正则表达式匹配我们需要的字符串
	imagesUrls = re.findall(r'class="items".*?src="(.*?)"', response.text, re.S)

	# print(imagesUrls)
	# 将上一步得到的字符串进一步处理得到完整的图片url
	for i in range(0, 22):
		if imagesUrls[i][0:23] != "http://www.xiaohuar.com":
			imagesUrls[i] = "http://www.xiaohuar.com" + imagesUrls[i]
		else:
			continue

		i += 1

	# print(imagesUrls)
	# 根据上一步得到的url，进行图片爬取并保存
	for j in range(0, len(imagesUrls)):
		pictureRresponse = requests.get(url=imagesUrls[j])
		# 保存爬取到的图片到 D:\NvShenImages 文件夹
		with open(r"D:\NvShenImages\picture_" + str(j) + ".jpg", "wb") as file:
			file.write(pictureRresponse.content)

		j += 1
        
if __name__ =="__main__":
    NvShenSpider()
    
    pass
```

# 成果展示 #

[![6.jpg](https://i.loli.net/2018/08/30/5b87fa0bad8c7.jpg)](https://i.loli.net/2018/08/30/5b87fa0bad8c7.jpg)

上面就是我们爬取到的图片。
