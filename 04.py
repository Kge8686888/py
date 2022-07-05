import requests
from lxml import etree
import re


def all_ing():  # 每页的所有图片
    img_html = requests.get(lj_url)
    img_href = etree.HTML(img_html.content.decode("utf8"))
    href = img_href.xpath('//li/a/@href')
    print(href)
    for href in href:
        print(href)
        # 请求
        img_html = requests.get(url+href)
        img_html = etree.HTML(img_html.content.decode("utf8"))
        # xpath获取数据
        img_name = img_html.xpath('//h1/text()')[0]
        img = img_html.xpath('//div[@class="article"]//a/img/@src')[0]
        print(img_name)
        print(url + href)
        print(img)
        img_url = requests.get(img)
        suffix = img[-4:]
        try:
            with open('../img/'+img_name+suffix, mode="xb") as f:
                f.write(img_url.content)
        except FileExistsError as e:
            pass


def select():   # 选择哪页
    html = requests.get(lj_url)
    html = etree.HTML(html.content.decode("utf8"))
    ys = input("1. 本页\n2. 其它页\n3.所有页\n需要什么选项全部下载：")
    if ys == '1':
        all_ing()
    elif ys == '2':
        zys = html.xpath('//div[@class="pages"]/a/text()')[-2]
        href = html.xpath('//div[@class="pages"]/a/@href')[-1]
        jy = input(f"一共{zys}页需要第几页的图片全部下载：")
        # 正则替换
        strinfo = re.compile('2')
        img_href = strinfo.sub(f'{jy}', href)
        print(href)
        img_href = url + img_href
        img_html = requests.get(img_href)
        img_href = etree.HTML(img_html.content.decode("utf8"))
        href = img_href.xpath('//li/a/@href')
        # print(href)
        for href in href:
            # print(href)
            # 请求
            img_html = requests.get(url + href)
            img_html = etree.HTML(img_html.content.decode("utf8"))
            # xpath获取数据
            img_name = img_html.xpath('//h1/text()')[0]
            img = img_html.xpath('//li//a/img/@src')[0]
            print(img_name)
            print(url + href)
            print(img)
            img_url = requests.get(img)
            suffix = img[-4:]
            try:
                with open('../img/' + img_name + suffix, mode="xb") as f:
                    f.write(img_url.content)
            except FileExistsError as e:
                pass
    elif ys == '3':
        zys = html.xpath('//div[@class="pages"]/a/text()')[-2]
        href = html.xpath('//div[@class="pages"]/a/@href')[-1]
        print(f"一共{zys}页需要从哪里到那里的图片全部下载(回车结束！)：")
        a = int(input("从:"))
        b = int(input("到:"))
        for i in range(a+1, b+1):
            # 正则替换
            strinfo = re.compile('2')
            img_href = strinfo.sub(f'{i}', href)
            # print(img_href)
            img_href = url + img_href
            # print(img_href)
            img_html = requests.get(img_href)
            img_href = etree.HTML(img_html.content.decode("utf8"))
            img_href = img_href.xpath('//li/a/@href')
            print(img_href)
            for img_href in img_href:
                print(url+img_href)
                # 请求
                img_html = requests.get(url + img_href)
                img_html = etree.HTML(img_html.content.decode("utf8"))
                # xpath获取数据
                img_name = img_html.xpath('//h1/text()')[0]
                img = img_html.xpath('//div[@class="article"]//a/img/@src')[0]
                print(img_name)
                print(url + href)
                print(img)
                img_url = requests.get(img)
                suffix = img[-4:]
                try:
                    with open('../img/' + img_name + suffix, mode="xb") as f:
                        f.write(img_url.content)
                except FileExistsError as e:
                    pass




url = 'http://www.bizhi360.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}
proxies = {
    'http': '202.116.32.236:80'
}
html = requests.get(url, headers=headers)   # ,proxies=proxies)
html = etree.HTML(html.content.decode("utf8"))
# 菜单栏
cdl_name = html.xpath('//div[@class="tags"]//div[@class="container"]//a/text()')[0:]
# 菜单栏链接
cdl = html.xpath('//div[@class="container"]/a/@href')[0:-1]
# 设置空集
lj = []
# 循环放进空集
for cdl in cdl[1:]:
    lj.append(url+cdl)
# print(lj)

# 输出菜单栏
for i in range(1, len(cdl_name)):
    print(f"{i}.{cdl_name[i]}")

# 就收用户输入的选项
sr = input("bizhi360壁纸下载输入要下载的数字：")
# 判断选项
if sr == '1':
    lj_url = lj[0]
    print(lj_url)
    select()
elif sr == '2':
    lj_url = lj[1]
    print(lj_url)
    select()
elif sr == '3':
    lj_url = lj[2]
    print(lj_url)
    select()
elif sr == '4':
    lj_url = lj[3]
    print(lj_url)
elif sr == '5':
    lj_url = lj[4]
    print(lj_url)
    select()
elif sr == '6':
    lj_url = lj[5]
    print(lj_url)
    select()
elif sr == '7':
    lj_url = lj[6]
    print(lj_url)
    select()
elif sr == '8':
    lj_url = lj[7]
    print(lj_url)
    select()
elif sr == '9':
    lj_url = lj[8]
    print(lj_url)
    select()
elif sr == '10':
    lj_url = lj[9]
    print(lj_url)
    select()
elif sr == '11':
    lj_url = lj[10]
    print(lj_url)
    select()
elif sr == '12':
    lj_url = lj[11]
    print(lj_url)
    select()
elif sr == '13':
    lj_url = lj[12]
    print(lj_url)
    select()
elif sr == '14':
    lj_url = lj[13]
    print(lj_url)
    select()
elif sr == '15':
    lj_url = lj[14]
    print(lj_url)
    select()
elif sr == '16':
    lj_url = lj[15]
    print(lj_url)
    select()
