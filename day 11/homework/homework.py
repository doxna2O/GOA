#შექმენით სია სადაც გადასცემთ 10 ინტეგერს, შემდეგ გადაუარეთ ამ სიას და თითოეული
#მათგანი გაამრავლეთ/გაყეთ/დაუმატეთ/გამოაკელით ერთმანეთს. 
#(ექსპერიმენტებიც გააკეთეთ)
#ვამატებთ list სახელად numbers და შემდეგ result ის ცარიელ list ს ვქმნით
numbers = [3, 6, 2, 67, 7, 1, 9, 1, 25, 12]
result = []
#ვქმნით for ცვლადს სადაც range(len(numbes) - 1 ) რადგან 0 იდან იწყება index ები
# დაამიტომაც ვაკლებთ 1 რადგან 0 იდან 9 მდე არის ინდექსები და 10 რო დაგვეწერა არ
#იზავდა და len ს იმიტომ გვინდა რომ რამდენი ინდექსი გვაქ მაგის დასაზუსტებლად
for i in range(len(numbers) - 1):
    multiply = numbers[i] * numbers[i+1]
#აქ გვაქ if else რადგან შეიძლება ნული გვეწეროს list ში და რომ გაიყოს და ერორი 
#არ ამოგვიგდოს
    if numbers[i+1] != 0:
        division = numbers[i] / numbers[i+1]
    else:
        division = "It will be zero"
    add = numbers[i] + numbers[i+1]
    subtraction = numbers[i] - numbers[i+1]

    result.append((multiply, division, add, subtraction))
print(result)


#დავალება 2)

#შექმენით სია, სადაც გამოიტანთ სათითაოდ მნიშვნელობებს და ასევე ჩაანაცვლებთ სხვა მნიშვნელობებით.

list = ["car", "door", "apple", "orange"]

list[2] = "pear"
list[0] = "cat"
print(list[0])
print(list[1])
print(list[2])
print(list[3])



#დავალება 3)
#შექმენით სია და მომხმარებელს აარჩევინეთ სასურველი მნიშვნელობა
list2 = ["sky", "butterfly", "mountains", "waterfall", "grass"]
choose = int(input("რომელი ინდექსი გნებავთ?:"))
print(list2[choose])