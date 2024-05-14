#შექმენით ფუნქცია სახელად manual_count: ფუნქციას გადაეცემა სია და ასევე შესაძლოა ელემენტი. როდესაც ფუნქციას ელემენტიც გადაეცემა, თქვენ უნდა დაითვალოთ სიაში ამ ელემენტის რაოდენობა, არ გამოიყენოთ count. როდესაც არ გადაეცემა ელემენტი, მისთვის გამოიყენეთ default მნიშვნელობა და გაუტოლეთ საწყისი სიის საშუალო არითმეტიკულს, ოღონდ მთელი რიცხვის სახით (int(აქ საშუალოს კოდი)).
def manual_count(list, num=15):
    count = 0
    count2 = 0
    for i in list:
        count += 1
        if i == num:
            count2 += 1
    jami = 0
    length = len(list)
    for i in list:
        jami += i
    result = jami / length
    
    return count, int(result), count2
print(manual_count([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,15,16,17,17,18], 17))