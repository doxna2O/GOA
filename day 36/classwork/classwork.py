# dictionary
person = {
# key value
    "name": "davit",
    "surname": "Grdzelishvili",
    "age": "20",
    "arr": [1,2,3,5,6]
}
# შეგვიძლია შეუცვალოთ მნიშვნელობები
person ['name'] = "George"
# update შეუძლია შეცვალოდ და დაამატოს ახალი ათიემები თავისი Value ბით
person.update({"name": "Daviti"})
person.update({"car" : "Aston Martin"})

print(person)
# გვიბურნებს value
print(person["name"] , "/ arr method")
# გვიბურნებს value
print(person.get('name') , '/ get method')
#
print(person.values() , "valuesssss")
#
# გვიბრუნებს key
x = person.keys()
print(person.keys())
#
#
# აბრუნებს წყვილ tuples
print(person.items() , "items ")
#
# გვიბრუნებს key
print(person["arr"][0])
print(len(person))
x = person["arr"]
print(x)
# item ის დამატება
person['food'] = "mtsavadi"
person.pop("car")
person.popitem()
del person['name']
# del person
person.clear()
print(person)