def initials(initial):
    split1 = initial.split(" ")
    firstname = split1[0]
    lastname = split1[1]

    result = firstname[0] + "." + lastname[0]

    print(result)
initials("Nikoloz Dokhnadze")

#an

firstname = input("Please enter your firstname: ").capitalize()
lastname = input("Please enter lastname: ").capitalize()

result = firstname[0] + '.' + lastname[0]

print(result)