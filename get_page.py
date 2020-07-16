import requests
import re
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

x = range(0, 250, 25)

for i in x:
    i=25
    # 请求排行榜页面
    #排行榜每页25个电影，每页网站的网址是https://movie.douban.com/top250?start=0(25/50/75...)"
    html = requests.get("https://movie.douban.com/top250?start=" + str(i), headers=headers)
    # 防止请求过于频繁
    time.sleep(0.01)
    # 将获取的内容采用utf8解码
    cont = html.content.decode('utf8')
    # 使用正则表达式获取电影的详细页面链接,在每次循环中，每个cont包含25个电影的链接页面
    urlList = re.findall('<a href="https://movie.douban.com/subject/\d*?/" class="">', cont)
    # 排行榜每一页都有25个电影，于是匹配到了25个链接，逐个对访问进行请求
    for j in range(len(urlList)):
        # 获取标签中的url 去掉标签中的a href 和class
        url = urlList[j].replace('<a href="', "").replace('" class="">', "")
        # 将获取的内容采用utf8解码
        content = requests.get(url, headers=headers).content.decode('utf8')
        # 采用数字作为文件名 第i页里面的第j个电影
        film_name = i + j
        # 将每个电影页面的内容写入文件，共250个文件
        f=open('./data1/'+str(film_name) + ".txt", "w", encoding='utf8')
        f.write(content)
















