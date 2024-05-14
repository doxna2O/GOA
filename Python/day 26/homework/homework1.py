#1) მომხმარებელს შემოატანინეთ მისი სახელი, შემდეგ დაბეჭდეთ lower, upper, capitalize ვარიანტებად.
def name(name):
    uppercase = name.upper()
    lowercase = name.lower()
    capitalize = name.capitalize()
    return uppercase, lowercase, capitalize
print(name(input("Enter your name: ")))