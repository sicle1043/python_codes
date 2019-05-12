import requests
from pyquery import PyQuery as pq

url = ''
headers = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36\
         (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
html = requests.get(url, headers=headers).text
doc = pq(html)
items = doc('.blacktab').items()
with open('course.txt', 'a', encoding='utf-8') as file:
    file.write('\n'.join(items))
