from lxml import etree

html = etree.parse('./text.html', etree.HTMLParser())  # 初始化的方法2：直接读取HTML文件
result = html.xpath('//*')   # 选取所有节点
print("结果一", result)
result = html.xpath('//li')  # 选取指定名称节点
print("结果二", result)
print("结果3", result[0])
result = html.xpath('//li/a')  # 选取子节点
print("结果4", result)
# result = html.xpath('//a[@href="link4.html"]/../@class')
result = html.xpath('//a[@href="link4.html"]/parent::*/@class')  # 第二种方式获取父节点
print("结果5", result)
result = html.xpath('//li[@class="item-0"]/a/text()')
print("结果6", result)
result = html.xpath('//li[@class="item-0"]//text()')  # 此方式会获取li节点内部的换行符
print("结果7", result)

# 以下换html文本
text = '''
<li class="li li-first" name="item"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li")]/a/text()')
print(result)
result = html.xpath('//li[contains(@class, "li")and @name="item"]/a/text()')
print(result)
