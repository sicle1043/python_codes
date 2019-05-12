import pymongo
from bson.objectid import ObjectId
client = pymongo.MongoClient(host='localhost', port=27017)
# client = pymongo.MongoClient('mongodb"//localhost:27017')
db = client.test
# db = client['test']
collection = db.students
# collection = db['students']

result = collection.find_one({'name': 'zhuleyuan'})
print(type(result))
print(result)
result = collection.find_one({'_id': ObjectId('5cbbe27a6a69d331c4c4c44a')})
print(result)
results = collection.find({'age': 20})
print(results)
for result in results:
    print(result)


# 插入数据
# student1 = {
#     'id': '417190116',
#     'name': 'zhuleyuan',
#     'age': 20,
#     'gender': 'man'
# }
# student2 = {
#     'id': '417190114',
#     'name': 'huangbinfeng',
#     'age': 21,
#     'gender': 'man'
# }
# student3 = {
#     'id': '417190108',
#     'name': 'xiaobinqi',
#     'age': 20,
#     'gender': 'man'
# }
# result = collection.insert_one(student1)
# print(result)
# print(result.inserted_id)
# result = collection.insert_many([student2, student3])
# print(result)
# print(result.inserted_ids)
