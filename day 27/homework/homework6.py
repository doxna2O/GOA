#6. შექმენით ფუნქცია, რომელსაც გადაეცემა სია. თქვენი დავალებაა, რომ დააბრუნოთ ამ სიაში არსებული დუპლიკატები.
def duplicates(list):
    list1 = []
    for i in list:
        x = list.count(i)
        if x > 1:
            list1.append(i)
    return list1
print(duplicates([1,1,2,3,4,5,4,5,6,7,8,9]))