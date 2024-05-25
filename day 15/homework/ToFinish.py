#დავალება: შექმენით ოთხი მათემატიკური ფუნქცია, თითოეულს გადაეცით ორი არგუმენტი
#და სახელის შესაბამისად მოახდინეთ მუშაობა. ოპერაციები: +, -, *, /.
def add(num1, num2):
    print(num1 + num2)

def subtract(num1, num2):
    print(num1 - num2)

def multiply(num1, num2):
    print(num1 * num2)

def divide(num1, num2):
    print(num1 / num2)


add(5,2)
subtract(6,2)
multiply(10,2)
divide(15,3)

#დავალება2: შექმენით ფუნქცია, რომელსაც გადასცემთ მართკუთხედის სიგრძესა და 
#სიმაღლეს, გამოითვლით მის ფართობს.
def area(w,h):
    print(w * h)

area(7,5)

#დავალება3: შექმენით ფუნქცია, რომელსაც გადასცემთ მართკუთხედის ოთხ გვერდს,
# გამოითვლით მის პერიმეტრს.
def perimeter(side1,side2):
    print(2 * (side1 + side2))

perimeter(10,5)

#დავალება4: შექმენით ფუნქცია, რომელიც მიიღებს არგუმენტად სიას და დაბეჭდეთ
# სიის რიცხვების ჯამი, არ გამოიყენოთ sum.
def my_sum_func(numbers_list): 
    sum = 0
    
    for i in numbers_list:
        sum = sum + i
    
    print(sum)

my_sum_func([1,2,3,4,5])


#დავალება5: შექმენით ფუნქცია, რომელიც დაბეჭდავს კონკრეტული სიიდან მინიმალურ და 
#მაქსიმალურ რიცხვებს, არ გამოიყენოთ min და max. გამოიყენეთ def, for, if/else,
# indexing, print.
def max_min(nums):
    min = nums[0]
    max = nums[0]
    for i in nums:
        if min > i:
            min = i
        if max < i:
            max = i
    print(min,max)

max_min([1,2,3,4,5])