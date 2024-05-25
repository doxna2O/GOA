#თქვენ გადმოგეცემათ მთელი რიცხვების სია. დავალებაა, რომ ყველაზე ხშირად განმეორებადი რიცხვის რაოდენობა დააბრუნოთ ამ სიიდან. ამ დავალების სია აიღეთ ქვემოთ მოცემული test case-იდან.
def repeater(list):
    count1 = 0
    for i in list:
        count = list.count(i)
        if count1 < count:
            count1 = count
    return count1
print(repeater([1, 1, 1, 1, 3, 4, 5, 6]))