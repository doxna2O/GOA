#დავალება1) შექმენით სია პროგრამირების ენების შესახებ, შეიტანეთ 5 პროგრამირების
# ენა. დაპრინტეთ  ჯერ მთლიანი სია, შემდეგ კი ბოლო ელემენტი.
print("1) davaleba")

languages = ["html", "css", "javascript", "python", "php"]
print(languages)
print(languages[4])

print("2) davaleba")

#დავალება2) შექმენით სია, სადაც გექნებათ შეტანილი string, integer, float,
# boolean. საბოლოოდ ყველა ელემენტი ცალ-ცალკე გამოიტანეთ.
datatypes = ["Wood", 8, 1.5, True]
print(datatypes[0])
print(datatypes[1])
print(datatypes[2])
print(datatypes[3])

print("3) davaleba")

#დავალება3) შექმენით სია, სადაც გექნებათ 0-იდან 20-ის ჩათვლით 4-ის ჯერადები და პრინტით გამოიტანეთ უდიდესი.

numbers = []

for i in range(0,20):
    if i % 4 == 0 and True:
        numbers.append(i)

print(numbers)
print(numbers[4])

print("4) davaleba")

#დავალება4) შექმენით სია სადაც შეტანილი გექნებათ 30-იდან 50-ის ჩათვლით კენტი რიცხვები. შემდეგ დაპტინტეთ სამი უმცირესი ელემენტის ჯამი.
numbers1 = []
for i in range(29,50,2):
    numbers1.append(i)
print(numbers1)
print(numbers1[0] + numbers1[1] + numbers1[2])

#დავალება5) დაპრინტეთ სამის ჯერადები დავალება 4-ის სიიდან.

numbers2 = []
for i in numbers1:
    if i % 3 == 0 and True:
        numbers2.append(i)
print(numbers2)