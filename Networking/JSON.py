import json

print('=='*10)
print('Example 1:')
data = '''
{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])

print(info)

print('=='*10)
print('Example 2:')

data = ''' 
[
    { 
        "id" : "001",
        "x" : "2",
        "name" : "Chuck"
    } ,
    { 
        "id" : "009",
        "x" : "7",
        "name" : "Bangladesh"
    }
  ]'''

info = json.loads(data)
print('User count:', len(info))

for user in info:
    print('')
    print('Name:', user["name"])
    print('Id:', user["id"])
    print('Attribute:', user["x"])

print(info)
