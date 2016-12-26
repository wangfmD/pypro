import json

testStr = '''
{
 "firstName":"John",
 "lastName" :"Smith",
 "adress":{
  "streetAddress":"21 2nd Street",
  "city":"New York",
  "state":"NY",
  "postalCode":10021
  },
 "phoneNumbers":[
  "212 555-1234",
  "646 555-4567"
  ]
}
'''

# Deserialize s (a str or unicode instance containing a JSON document) to a Python object.
obj = json.loads(testStr)

print("firstName:" + obj["firstName"])
print("city:" + obj["adress"]["city"])
print("phoneNumbers:" + str(obj["phoneNumbers"]))

# Serialize obj to a JSON formatted str.
str = json.dumps(obj,indent=2)
print(str)

# the output:
# firstName:John
# city:New York
# phoneNumbers:[u'212 555-1234', u'646 555-4567']
# {
#   "lastName": "Smith",
#   "phoneNumbers": [
#     "212 555-1234",
#     "646 555-4567"
#   ],
#   "adress": {
#     "postalCode": 10021,
#     "city": "New York",
#     "streetAddress": "21 2nd Street",
#     "state": "NY"
#   },
#   "firstName": "John"
# }
