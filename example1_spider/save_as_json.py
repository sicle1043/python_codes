import json
# json格式，必须用双引号
str = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
},{
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''
print(type(str))
data = json.loads(str)
print(data)
print(type(data))
print(data[0]['name'])
print(data[0].get('name'))
print(data[0].get('age'))  # 查无此键返回None
print(data[0].get('age', 404))  # 查无此键返回第二个参数

data0 = [{'name': 'bob', 'gender': 'male', 'birthday': '1992-10-18'}]
data1 = [{'name': '王伟', 'gender': '男', 'birthday': '1993-10-18'}]
with open('example1_spider/data.json', 'w') as file:
    file.write(json.dumps(data0, indent=2))
with open('example1_spider/data.json', 'a', encoding='utf-8') as file:
    file.write('\n' + json.dumps(data1, indent=2, ensure_ascii=False))
