#გადმოგეცემათ რიცხვებით სავსე სია და თქვენ უნდა დააბრუნოთ ამ სიის ელემენტების საშუალო არითმეტიკული
def average(list):
    jami = 0
    length = len(list)
    for i in list:
        jami += i
    result = jami / length
    return result
print(average([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))
