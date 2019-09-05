import requests
import datetime

def UrlsAutoPush():
    # 读取 urls.txt 中需要推送的链接
    urls = {'file': open('urls.txt', 'rb')}
    # 将 urls 推送至百度，并接收百度返回的结果
    baiduResult = requests.post("http://data.zz.baidu.com/urls?site=https://www.diostudio.wang&token=IXUROgLSmZjHZm6P", files=urls)

    result = {
            "surplusQuantity" : baiduResult.text[10:17], # 今日剩余推送数量
            "successQuantity" : baiduResult.text[28:30]  # 本次成功推送数量,这里去几位数根据你的url数量自己调整就可以了
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