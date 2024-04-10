def find(collection,value):
    
    for index in range(len(collection)):
        if collection[index] == value:
            return index
print(find(["mini", "nika", "fio"], "mini"))