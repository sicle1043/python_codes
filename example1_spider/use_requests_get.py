import requests
# import re
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) \
#       AppleWebKit/537.36 (KHTML, like Gecko) \
#          Chrome/52.2.2743.116 Safari/537.36'
# }
# r = requests.get("https://www.zhihu.com/explore", headers=headers)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
# titles = re.findall(pattern, r.text)
# print(titles)
r = requests.get("https://www.github.com/favicon.ico")
with open('favicon.ico', 'wb') as f:
    f.write(r.content)
# s3.bytecdn.cn/aweme/resource/web/static/image/index
