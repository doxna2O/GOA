##დავალება: შექმენით ოთხი მათემატიკური ფუნქცია, თითოეულს გადაეცით ორი არგუმენტი
## და სახელის შესაბამისად მოახდინეთ მუშაობა. ოპერაციები: +, -, *, /
# def print_8(name,count):
#     for i in range(count):
#         print(name)


# print_8("nika",10)

# print_8("doxna",3)

# print_8("luka",5)


# def lights_on(color,minutes):
#     print("lights are on. color is ",color,"and it will run for",minutes,"minutes")

# lights_on("red", 20)

# lights_on("red",30)

# lights_on("blue",10)

# def intro():
#     hello = input("enter your name: ")

#     print("hello how are you today",hello)
# intro()

# def add(num1,num2):
#     print(num1 + num2)

# add(20,5)

# def multiply(num1,num2):
#     print(num1 * num2)

# multiply(4,7)

#1 davaleba
def add(num1,num2):
    print(num1 + num2)
add(10,4)
def subtraction(num1,num2):
    print(num1 - num2)
subtraction(16,8)
def multiply(num1,num2):
    print(num1 * num2)
multiply(2,7)
def division(num1,num2):
    print(num1 / num2)
division(20,5)
    

#meore
def area(area1,area2):
    print(area1 * area2)

area(20,5)

#mesame
def perimeter(perimeter1,perimeter2):
    print(2 * (perimeter1 + perimeter2))

perimeter(10,5)

#me 4

def list(numbers):
    list_sum = 0
    for num in numbers:
        list_sum += num
    print(list_sum)


my_list = [1, 2, 3, 4, 5]
list(my_list)