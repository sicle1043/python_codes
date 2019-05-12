vocabularies = {
    'set': 'different list',
    'dictionary': 'key and value',
    'tuple': 'unchange',
    'list': 'just a list',
}

for value, key in vocabularies.items():
    print(value.title() + ':' + key)

print('*****************')

for vocabulary in sorted(vocabularies.keys()):
    print(vocabulary)
