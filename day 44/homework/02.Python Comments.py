#Add comments to explain each line of a given script.
#for ციკლი გადაუვლის იმ არგუმენტს რომელიც ჩაწერილია შიგნით იმდენჯერაც რა რიცხვი წერია rangeში
for i in range(1):
    print(1+2)
#Write a script and use comments to explain a function's purpose.
#აქ გვაქვს ნაჩვენები ფუნქცია რომელიც 
def repeater(list):
    count1 = 0
    for i in list:
        count = list.count(i)
        if count1 < count:
            count1 = count
    return count1
print(repeater([1, 1, 1, 1, 3, 4, 5, 6]))