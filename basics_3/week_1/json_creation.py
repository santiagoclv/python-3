import json

def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

dic_example = {'key1': {'c': True, 'a': 90, '5': 50}, 'key2':{'b': 3, 'c': "yes"}}

print(dic_example)
print(type(dic_example) is dict)
print(type(dic_example))
print(id(dic_example))
print('----Creating a JSON----')
dic_json = pretty(dic_example)
print(pretty(dic_json))
print(type(dic_json) is str)
print(type(dic_json))
print(id(dic_json))
print('----Creating an Object from json string----')
dic_example_prima = json.loads(dic_json)
print(type(dic_example_prima) is dict)
print(type(dic_example_prima))
print(id(dic_example_prima))

# Pretty easy to write it on a file.
