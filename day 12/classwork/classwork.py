shopping_list = ["apple", 5, "wood", True]
shopping_list.append(5.5)
shopping_list.pop(2)
print(shopping_list)
print(shopping_list[2])


#numbers =[1,2,3,4,5,6,7,8,9,10]
#for i in numbers:
#    if i % 2 != 0:
#        index = numbers.index(i)
#        numbers.pop(index)
#print(numbers)
numbers =[1,2,3,4,5,6,7,8,9,10]
even_numbers =[]
for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)
print(even_numbers)          




list = ["nikolozi", "lizi", "gio","emzari"]

print(list[1:3])

word = 'Apple'
print(word[1:4])


list1 = ["nikolozi", "lizi", "gio","emzari", "nini", "sergo"]

print(list1[-5: -2])