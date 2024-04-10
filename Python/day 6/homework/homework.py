#false or false = false
#everything after that true
print("1)")
print(5 > 4 or 6 > 10)
print(6 < 3 or 8 > 10)
print(1 > 7 or 4 < 10)
print(5 < 4 or 7 < 1)
print(5 > 4 or 5 > 23)

#true and true = true
#everything after that false
print("2)")
print(8 < 3 and 30 < 23)
print(9 > 6 and 10 < 18)
print(6 < 2 and 3 < 16)
print(4 < 8 and 8 < 46)
print(9 > 3 and 9 > 13)

#აქ მაქ შედარების შედარება
print("3)")
first = True and False #false
second = False or True #true
print(first or second)

#აქ მაქ შედარების შედარება
print("4)")
comparison = 10 < 9
comparison2 = 5 > 4
print(comparison and comparison2)

#აქ მაქ შედარების შედარება და 3 ცვლადია ვიდრე პირდაპირ დაპრინტვა
print("5)")
comparison3 = 30 > 20
comparison4 = 10 < 60
anwser = comparison3 and comparison4
print(anwser)


print("მექანიკური გარდაქმნა)")
# აქ მაქ ცვლადები და როდესაც type ფუნქციას ვიყენებ გამოაქვს მონაცემის ტიპს
# შემდეგ დავპრინტე და გამოიყვანა3 სხვადასხვა მონაცემთა ტიპი
print("1)")
new_word = "Python"
new_number = 42
new_float = 3.14
new_boolean = 7 > 2

print(type(new_word))
print(type(new_number))
print(type(new_float))
print(type(new_boolean))

#აქ მე მაქ გამოყენებული input() რათა ჩავწეროთ პასუხი. შემდეგ დაპრინტავს პასუხს წინადადების სახით
print("2)")
name = input("თქვენი სახელი ჩაწერეთ: ")
number = input("თქვენი ჯგუფის ნომერი ჩაწერეთ: ")
print("მოგესალმებით " + name + ". Welcome to Group " + number)

print("3)")
divide = 25 / 5
print(divide)
print(type(divide))
#დაწერა რომ იყო float მონაცემთა ტიპი

#აქ მიზანი იყო რათა 2024 გამოგვეყვანა
print("4)")
num1 = "20"
num2 = "24"
print(num1 + num2)

#აქ უნდა გადაგვეყვანა float(ათწილადი) integer-ში(მთელი რიცხვი) 
print("5)")
float1 = 4.23
float2 = 6.2
float3 = 2.14
float4 = 7.01
float5 = 9.24
print(int(float1))
print(int(float2))
print(int(float3))
print(int(float4))
print(int(float5))