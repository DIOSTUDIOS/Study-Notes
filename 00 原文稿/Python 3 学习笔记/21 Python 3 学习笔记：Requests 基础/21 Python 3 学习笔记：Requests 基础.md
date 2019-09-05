> 人生苦短，我用 Python

requests 作为一个第三方库，需要使用 pip 工具安装，然后使用 import 语句引入，

``` python
import requests
```

# GET 请求

## 基本实例

HTTP 中最常见的就是 GET 请求，使用 requests 中的 get() 方法就可以向服务器发送一个 GET 请求，

``` python
response = requests.get(url)
```

上面是一个最简单、常见的 GET 请求，其返回一个 Response 对象。

如果需要参数，则可以构造一个参数字典，如：

``` python
parameters = {
    some parameters
}

response = requests.get(url, params=parameters)
```

## 抓取网页

以猫眼的电影榜单为例，抓取前十名的电影名称，

``` python
import requests
import re

url = r'https://maoyan.com/board'

def get_file_name():
	response = requests.get(url=url)
	files = re.findall(r'<a href="/films/\d+" title=".*?" data-act="boarditem-click" data-val="{movieId:\d+}">(.*?)</a>', response.text, re.I)

	print(files)

if __name__ == '__main__':
	get_file_name()
```

这里使用正则表达式匹配电影名称，然后提取出来。

## 抓取文件

同样可以抓取网页中的图片、音频、视频等，还是以猫眼为例，抓取电影的海报图片，

``` python
import requests
import re

url = r'https://maoyan.com/board'


def get_file_name():
	response = requests.get(url=url)
	pattern = r'<a href="/films/\d+" title=".*?" data-act="boarditem-click" data-val="{movieId:\d+}">(.*?)</a>'
	files = re.findall(pattern=pattern, string=response.text, flags=re.I)

	return files


def get_file_image():
	i = 0
	files = get_file_name()

	response = requests.get(url=url)
	pattern = r'<img data-src="(.*?)@160w_220h_1e_1c" alt=".*?" class="board-img" />'
	imgs = re.findall(pattern=pattern, string=response.text, flags=re.I)

	for img_url in imgs:
		image = requests.get(url=img_url).content
		with open(files[i] + '.jpg', 'wb') as file:
			file.write(image)

		i = i + 1


if __name__ == '__main__':
	get_file_image()
```

同样使用正则表达式，提取海报的 url ，然后根据这些 url 向服务器发送请求，将返回的数据（二进制数据），保存图片文件。

## 添加 headers 信息

有些网站是禁止爬虫的，例如知乎，所以可以传递 headers 参数将爬虫伪装成浏览器。headers 参数是一个字典的形式，类似于url 参数，下面是一个火狐浏览器的 headers 信息，

``` python
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}
```

下面是一个 Chrome 的 headers 信息，

``` python
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
```

# POST 请求

POST 请求主要是用于提交表单数据，用的地方不是很多，因为我们的主要目的是在网上抓取数据。

# 响应

服务器返回的响应处理 text 和 centent 两个属性，还有很多其他属性，如状态码、响应头、Cookies等，

``` python
import requests


response = requests.get(url=r'https://maoyan.com/board')
print(response.status_code)
print(response.headers)
print(response.cookies)
print(response.url)
print(response.history)
```

