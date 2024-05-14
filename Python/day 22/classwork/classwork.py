#POP
# def manual_pop(list, changed_list):
#     list1= []
#     for index in range(0, len(list)):
#         if index != changed_list:
#             list1.append(list[index])

#     return list1

# names = ["luka", "lile", "nia"]
# print(manual_pop(names, 1))

#COUNTER
# def counter(list, item):
#     count = 0

#     for i in list:
#         if i == item:
#             count = count + 1
        
#     return count

# names = ["nika", "doxna", "nia","doxna"]
# print(counter(names, "doxna"))

# INDEX
def manual_index(list, changed_list):
    for i in range(len(list)):
        if list[i] == changed_list:
            return i

    return -1
names = ["nika",  "nia","doxna"]
print(manual_index(names, "doxna"))