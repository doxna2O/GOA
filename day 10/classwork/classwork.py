#num = int (input("Please enter number: "))
#print (num % 3 == 0 or num % 5 == 0)

name = input("enter your name: ")

if name == "doxna":
    print("Hello owner")
elif name == "nini":
    print("Hello admin")
elif name == "sergo":
    print("Hello moderator")
else:
    print("Hello user")


age = int(input("Enter Your age: "))

if age >= 1 and age < 13:
    print("you are a kid")
elif age >= 13 and age < 18:
    print("you are a teenager")
elif age >= 18 and age <= 55:
    print("you are an adult")
elif age > 55 and age <= 80:
    print("you are an elder")
else:
    print("you are not alive")


shopping_list = ["Apple", "Cloth", "Wood"]
print(shopping_list[0])

movies = ["matrix", "breaking bad", "you"]
print(movies)
print(f"my favorite movie is '{movies[2]}'")