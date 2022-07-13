'''
项目:代码实例
文件名:图片转字符画
制作人:"黄涛"
date:2022/2/26
'''
import requests
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print(r.status_code)
print(r.json())
