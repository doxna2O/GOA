#შექმენით ფუნქცია სახელად manual_pop, რომელსაც გადაეცემა სია და ასევე შესაძლოა ინდექსი. როდესაც გადაეცემა ინდექსი, სიიდან უნდა ამოიშალოს ამ ინდექსზე მყოფი ელემენტი და დაბრუნდეს სია ამ სახით. თუ ფუნქციას არ გადაეცემა index, მაშინ default მნიშვნელობა უნდა იყოს სიის ბოლო ელემენტი - ზოგადად pop როგორც მუშაობს. ამ დავალებაში რათქმაუნდა pop არ უნდა გამოიყენოთ
def manual_pop(list, index1= -1):
    list1 = []
    for i in range(len(list)):
        if i != index1:
            list1.append(list[i])
    return list1
print(manual_pop([1,2,3,4,5,6,7,8,9,10], 5))