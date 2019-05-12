counts = dict()
names = ['啊', '哦', '额', '啊', '啊', '哦', '阿']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)
