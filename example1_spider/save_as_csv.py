import csv

with open('example1_spider/data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', 20])
    writer.writerow(['10002', 'Bob', 22])
    writer.writerow(['10003', 'Jordan', 21])
    # writer.writerows([['10001', 'Mike', 20],
    # ['10002', 'Bob', 22], ['10003', 'Jordan', 21]])
    # 多行写入用writerows

with open('example1_spider/data.csv', 'a', encoding='utf-8') as csvfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id': '10001', 'name': '德玛西亚之力', 'age': 20})
    writer.writerow({'id': '10002', 'name': '艾欧尼亚之心', 'age': 21})
    writer.writerow({'id': '10003', 'name': '诺克萨斯之手', 'age': 22})

with open('example1_spider/data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
