import json
person = {
    'name': 'max',
    'age': 10,
    'phone':['2222', '4444']
}
result = json.dumps(person)
print(result)
print(type(result))

person = [12, 34,56, 78, 90]

result = json.dumps(person)
print(result)
print(type(result))

result = json.loads(result)
print(result)
print(type(result))
