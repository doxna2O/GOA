#გადმოგეცემათ სია რომელშიც იქნება დადებითი და უარყოფითი რიცხვებიც, თქვენ უნდა დააბრუნოთ ორი სია სადაც გაფილტრური იქნება უარყოფითი რიცხვები ცალკე და დადებითი რიცხვები ცალკე
def minus_plus(list):
    plus = []
    minus = []
    for i in list:
        if i < 0:
            minus.append(i)
        elif i > 0:
            plus.append(i)
    return plus, minus
print(minus_plus([1,-4,2,-7,4,6,-1,-3,4,8,-9,13,-15]))