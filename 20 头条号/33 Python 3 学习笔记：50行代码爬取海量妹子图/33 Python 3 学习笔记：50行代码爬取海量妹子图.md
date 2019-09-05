> 人生苦短，我用 Python

# 环境

- Python
- selenium
- requests
- ChromeDriver
- Chrome 浏览器

首先，下载并安装好 Python 之后（一定要加入系统环境变量 Path 中），然后将 ChromeDriver 放入其 Scripts 目录中，这里需要注意的是，ChromeDriver 的版本一定要和你的 Chrome 浏览的大版本号一致，例如我的 Chrome 浏览器的版本号是 76.0.3809.132，所以我下载的 ChromeDriver 的版本是 76.0.3809.126。

然后，使用 pip 工具安装 selenium 和 requests 两个库就行了，不会的可以看我之前的文章。

最后，就可以愉快的下图了。

# 效果

测试程序的时候，最多下了两千张，当然最后都删了，要不我怕无法推送到 github 上。

![效果图.jpg](https://i.loli.net/2019/08/31/lXcsBQrdGSFzI8a.jpg)

# 代码

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

# 初始 url
access = r'http://www.win4000.com/meinv185222.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'
}


def main():
    is_continue = True
    # 图片计数器
    image_count = 0
    # 设置浏览器对象，并获取网页内容
    browser = webdriver.Chrome(chrome_options=webdriver.ChromeOptions().add_argument('--headless'))
    browser.get(url=access)
    # 判断是否继续执行
    while is_continue:
        try:
            # 延时等待
            wait = WebDriverWait(browser, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="pic-meinv"]/a/img')))
            # 获取图片地址
            url = browser.find_element_by_xpath('//*[@id="pic-meinv"]/a/img').get_attribute('url')
            # 下载图片
            image = requests.get(url=url, headers=headers).content
            with open(r'E:\Python-Study-Notes\MeiNvSpider' + url[32:], 'wb') as file:
                file.write(image)
        except TimeoutError:
            print('time out')
        finally:
            browser.find_element_by_xpath('//*[@id="pic-meinv"]/a/img').click()

        image_count += 1
        # 设置想要下载的图片的数量
        if image_count < 20:
            is_continue = True
        else:
            is_continue = False

    browser.close()


if __name__ == '__main__':
    main()

```

最开始我只用了 requests 写的一百来行才能下图，而且特别麻烦，有的时候还会被服务器断开连接，后来学了 selenium 基本用法，将代码缩减到了50行。然后，测试下载了两千张，没有被服务器强制断开连接，就是需要花些时间。



------

因头条号文章修改次数有限，而本文一直在持续修改充实的路上，故请各位看官移步个人博客，谢谢！

https://www.diostudio.wang