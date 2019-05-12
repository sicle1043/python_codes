from urllib.parse import urlparse, unquote
a = 'https://www.baidu.com/s?tn=80035161_2_dg&wd=%E7%A5%9E%E8%B6%85'
result = urlparse(a)
print(type(result), result)
# query = 'tn=80035161_2_dg&wd=SLG'
# print(parse_qs(query))
url = 'https://www.baidu.com/s?tn=80035161_2_dg&wd=%E7%A5%9E%E8%B6%85'
print(unquote(url))
