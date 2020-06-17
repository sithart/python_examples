import html
import os
import re
import requests

url = 'https://program-think.blogspot.com/'
# 爬虫参数
proxies = {
    "http": "127.0.0.1:10809",
    "https": "127.0.0.1:10809"
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
pdir = r'F:\py\pa\\'  # 爬虫工作路径
a = re.compile(r"<a href='https://program-think.blogspot.com/(.*)</a>")  # 匹配规则


def mkdir(path):  # 创建文件夹函数
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        return False


def pa(url1, dir1):
    print()
    y = []
    r = requests.get(url=url1, headers=headers, proxies=proxies)
    title = re.findall(a, r.text.split(r"<div class='sidebar section' id='sidebar'>")[0])  # 排除不相关内容
    for z in title:
        if z[:7] != 'search/':  # 排除不相关内容
            y.append('https://program-think.blogspot.com/' + requests.utils.unquote(html.unescape(z)))
    for z in y:
        x = z.split("'>")
        print(x)
        mkdir(pdir + str(dir1))  # 创建本地目录，存放爬取到的文件
        ldir = pdir + str(dir1) + '\\' + x[1].replace('/', '') + '.html'  # 去掉文件名中的/
        ldir = ldir.replace(" ", "")  # 去掉文件名中的空格
        if not os.path.exists(ldir):  # 判断文件是否已存在，以达到断点续爬的效果
            res = requests.get(x[0], headers=headers, proxies=proxies)
            with open(ldir, "w", encoding='utf-8') as txt:
                txt.write(res.text)


def eveP(p):
    url1 = 'https://program-think.blogspot.com/search/label/IT.信息安全'  # 爬取该分类下所有文章
    pa(url1, p)  # url1为指定分类，url则是爬取全站
    old = []
    while True:
        try:
            r = requests.get(url=url1, headers=headers, proxies=proxies)
            old = re.findall("href='(.*)id='Blog1_blog-pager-older-link'", r.text)  # 查找下一页
            url1 = old[0][:-2]
            p += 1  # 把每一页文章放到不同的文件夹里，注释掉本句即放到同个文件夹下
            pa(url1, p)  # 调用爬虫
        except:
            print('爬完了')
            exit(0)


if __name__ == '__main__':
    eveP(1)
