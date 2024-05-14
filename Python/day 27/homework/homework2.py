#2. შექმენით ფუნქცია, რომელსაც გადაეცემა სახელების სია. ლუწ ინდექსებზე მყოფი სახელები გადაიყვანეთ uppercase-ში, ხოლო კენტ ინდექსებზე მყოფნი კი lowercase-ში.
def names(list):
    list1 = []
    for i in range(len(list)):
        if i % 2:
            up = list[i].upper()
            list1.append(up)
        else:
            low = list[i].lower()
            list1.append(low)
    return list1
print(names(["nika", "lizi", "luka", "gio", "dato"]))