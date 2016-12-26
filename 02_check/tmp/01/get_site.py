# coding:utf-8
import urllib


# def get_html(url):
#     html_o = urllib.urlopen(url)
#     html_c = html_o

url = 'https://www.baidu.com/'
html_o = urllib.urlopen(url).info()
# html_o = urllib.urlopen(url).info()
# print dir(html_o)
print html_o
