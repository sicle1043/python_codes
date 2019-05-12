from urllib import request, parse
# data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')
# response = urllib.request.urlopen('https://httpbin.org/get', timeout=1)
# print(response.read())
# print(type(response))
# print(response.read().decode('utf-8'))
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))
url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0(compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'Germey'
}
data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
