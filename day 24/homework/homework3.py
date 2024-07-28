#3. მომხმარებელს შემოატანინეთ დადებითი მთელი რიცხვი. შემდეგ გამოიყენეთ ციკლი, სიაში დაამატეთ ყველა ამ რიცხვის გამყოფი და დაბეჭდეთ ეს სია.
def num(number):
    list = []
    for i in range(1, number + 1):
        if number % i == 0:
            list.append(i)
    return list
print(num(24))