# name = "nikoloz dokhnadze"
# name_list = name.split(" ")
# new_list = " ".join(name)

# print(name_list)
# print(new_list)


#შექმენით ფუნქცია რომელსაც მისცემთ list ტიპის არგუმენტს, შეართეთ და შექმენით
# რაიმე წინადადება, შემდეგ კი გამოიტანეთ ტერმინალში
def list_func(list):
    join_func = " ".join(list)

    return join_func
print(list_func(["Best", "Academy", "Is", "Goal", "Oriented", "Academy"]))