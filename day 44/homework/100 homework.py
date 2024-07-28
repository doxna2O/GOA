# Day 44
# Python Syntax

# Write a Python script that prints "Hello, World!"
print("Hello, World!")
# Create a script that takes user input and prints it.
print(input("Enter your name: "))
# Write a script that uses both single-line and multi-line comments.
#halo
"""
halo
"""
# Write a script that demonstrates indentation in Python.
def random_func():
    for i in range(1): 
        print(i)       
# Write a script that shows how to break lines in Python.
numz = ("1 line"
        "2 line")
# Python Comments

# Add comments to explain each line of a given script.
#for ციკლი გადაუვლის იმ არგუმენტს რომელიც ჩაწერილია შიგნით იმდენჯერაც რა რიცხვი წერია rangeში
for i in range(1):
    print(1+2)
# Write a script and use comments to explain a function's purpose.
#აქ გვაქვს ნაჩვენები ფუნქცია რომელიც თვლის ყველაზე მეტად დაწერილ რიცხვის რაოდენობას
def repeater(list):
    count1 = 0
    for i in list:
        count = list.count(i)
        if count1 < count:
            count1 = count
    return count1
print(repeater([1, 1, 1, 1, 3, 4, 5, 6]))

# Add a block comment to describe the script's overall functionality.
#აქ გვაქვს ნაჩვენები ფუნქცია რომელიც თვლის ყველაზე მეტად დაწერილ რიცხვის რაოდენობას
def repeater(list):
    count1 = 0
    for i in list:
        count = list.count(i)
        if count1 < count:
            count1 = count
    return count1
print(repeater([1, 1, 1, 1, 3, 4, 5, 6]))
# Use comments to disable a part of the script and re-enable it.
def repeater(list):
    count1 = 0
    for i in list:
        count = list.count(i)
        if count1 < count:
            count1 = count
    return count1
print(repeater([1, 1, 1, 1, 3, 4, 5, 6]))
# Write a script with intentional errors and comment on why they occur.
#აქ გვაქვს ნაჩვენები ფუნქცია რომელიც თვლის ყველაზე მეტად დაწერილ რიცხვის რაოდენობას
# def repeater(list):
#     #აქ ცოუნტს არააქვს ინდენტაცია ამიტომაც ერორს წერ
# count1 = 0
#     #ორი წერტილი აკლია
#     for i in list
#         count = list.count(i)
#         if count1 < count:
#             count1 = count
#     return count1
# print(repeater([1, 1, 1, 1, 3, 4, 5, 6]))
# Python Variables

# Create and initialize multiple variables of different data types.
var1 = 1
var2 = 'wats ip'
var3 = 2.0
type(var1)
type(var2)
type(var3)
# Swap the values of two variables.
a = 5
b = 10
a = b
b = a
# Create a script that takes user input to assign values to variables.
var = input("enter a value: ")
# Write a script that uses both global and local variables.
gay = "gay"
def function_4():
    sigma = "sigma"
    print(sigma)
# Demonstrate variable naming conventions in Python.
giorgi = ""


# Create variables of types: integer, float, string, and boolean.
num1 = 1
num2 = 1.0
num3 = "nika"
num4 = True
# Demonstrate the use of type() function to check variable types.
var1 = 1
var2 = 'wats ip'
var3 = 2.0
type(var1)
type(var2)
type(var3)

# Python Numbers

# Write a script to perform arithmetic operations.
a = 10
b = 5

mimateba = a + b
minus = a - b
multiply = a * b
divide = a / b

print("Sum: ", mimateba)
print("Difference: ", minus)
print("Product: ", multiply)
print("Quotient: ", divide)
# Create a script that generates a random number.
import random


random_number = random.randint(1, 100)
print("Random Number: ", random_number)
# Write a script that calculates the square root of a number.
import math

num = 16
square_root = math.sqrt(num)

print("Square Root of", num, ":", square_root)
# Demonstrate the use of math functions like ceil() and floor().


num = 4.7

ceil_result = math.ceil(num)
floor_result = math.floor(num)

print("Ceil of", num, ":", ceil_result)
print("Floor of", num, ":", floor_result)
# Write a script to find the greatest common divisor (GCD) of two numbers.

num1 = 48
num2 = 18

gcd_result = math.gcd(num1, num2)

print("GCD of", num1, "and", num2, ":", gcd_result)
# Python Casting

# Write a script to convert integers to floats and vice versa.
int_num = 10
float_num = float(int_num)
print("Integer to Float: ", float_num)

float_num = 10.5
int_num = int(float_num)
print("Float to Integer: ", int_num)

# Create a script to convert strings to integers and floats.
str_num = "100"
int_num = int(str_num)
print("String to Integer: ", int_num)

str_num = "100.5"
float_num = float(str_num)
print("String to Float: ", float_num)

# Demonstrate casting between lists and tuples.
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)
print("List to Tuple: ", my_tuple)

my_tuple = (1, 2, 3, 4)
my_list = list(my_tuple)
print("Tuple to List: ", my_list)

# Write a script to handle casting errors.
str_num = "abc"

try:
    int_num = int(str_num)
    print("String to Integer: ", int_num)
except ValueError:
    print("Error: Cannot convert string to integer")

try:
    float_num = float(str_num)
    print("String to Float: ", float_num)
except ValueError:
    print("Error: Cannot convert string to float")

# Create a script to convert a string representing a number to an integer.
str_num = "123"
int_num = int(str_num)
print("String to Integer: ", int_num)

# Python Booleans
# Write a script to demonstrate the use of boolean values.
a = True
b = False
print("Boolean a: ", a)
print("Boolean b: ", b)

# Create a script to perform logical operations (and, or, not).
a = True
b = False

and_result = a and b
or_result = a or b
not_result = not a

print("a and b: ", and_result)
print("a or b: ", or_result)
print("not a: ", not_result)

# Demonstrate the use of comparison operators to return boolean values.
a = 10
b = 20

print("a == b: ", a == b)
print("a != b: ", a != b)
print("a < b: ", a < b)
print("a > b: ", a > b)
print("a <= b: ", a <= b)
print("a >= b: ", a >= b)

# Write a script that uses if-else statements based on boolean values.

is_raining = True

if is_raining:
    print("Take an umbrella.")
else:
    print("No need for an umbrella.")

# Create a script that returns a boolean result from a function.
def is_even(number):
    return number % 2 == 0

print("Is 4 even? ", is_even(4))
print("Is 7 even? ", is_even(7))


# Python Operators

# Write a script that demonstrates arithmetic operators.
a = 10
b = 5

sum_result = a + b
difference = a - b
product = a * b
quotient = a / b
modulus = a % b
exponent = a ** b

print("Sum: ", sum_result)
print("Difference: ", difference)
print("Product: ", product)
print("Quotient: ", quotient)
print("Modulus: ", modulus)
print("Exponent: ", exponent)

# Create a script to use assignment operators.
# Assignment operators
a = 10

a += 5
print("a += 5: ", a)

a -= 3
print("a -= 3: ", a)

a *= 2
print("a *= 2: ", a)

a /= 4
print("a /= 4: ", a)

a %= 3
print("a %= 3: ", a)

a **= 2
print("a **= 2: ", a)

# Write a script to show the use of comparison operators.
a = 10
b = 20

print("a == b: ", a == b)
print("a != b: ", a != b)
print("a < b: ", a < b)
print("a > b: ", a > b)
print("a <= b: ", a <= b)
print("a >= b: ", a >= b)

# Demonstrate the use of logical operators in a script.
a = True
b = False

and_result = a and b
or_result = a or b
not_result = not a

print("a and b: ", and_result)
print("a or b: ", or_result)
print("not a: ", not_result)

# Create a script to use identity operators (is, is not).
# Identity operators
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("a is b: ", a is b)  # False, because they are different objects
print("a is c: ", a is c)  # True, because they refer to the same object
print("a is not b: ", a is not b)  # True, because they are different objects
print("a is not c: ", a is not c)  # False, because they refer to the same object


# Python Lists

# Write a script to create and print a list.
my_list = [1, 2, 3, 4, 5]
print("List: ", my_list)

# Create a script to add and remove elements from a list.
my_list = [1, 2, 3, 4, 5]

my_list.append(6)
print("After append: ", my_list)

my_list.insert(0, 0)
print("After insert: ", my_list)

my_list.remove(3)
print("After remove: ", my_list)

removed_element = my_list.pop()
print("After pop: ", my_list)
print("Removed element: ", removed_element)

# Write a script to sort a list.
my_list = [5, 2, 9, 1, 5, 6]
my_list.sort()
print("Sorted list: ", my_list)

# Demonstrate the use of list comprehension.
squares = [x**2 for x in range(10)]
print("Squares: ", squares)

# Create a script to find the length of a list.
my_list = [1, 2, 3, 4, 5]
length = len(my_list)
print("Length of list: ", length)


# Python If...Else

# Write a script that uses an if statement to check a condition.
a = 10
if a > 5:
    print("a is greater than 5")

# Create a script that uses an if-else statement.
a = 10
if a > 5:
    print("a is greater than 5")
else:
    print("a is not greater than 5")

# Write a script that uses an if-elif-else statement.
a = 10
if a > 10:
    print("a is greater than 10")
elif a == 10:
    print("a is equal to 10")
else:
    print("a is less than 10")

# Demonstrate nested if statements.
a = 10
b = 5
if a > 5:
    if b < 10:
        print("a is greater than 5 and b is less than 10")

# Write a script that uses the ternary operator.

a = 10
result = "a is greater than 5" if a > 5 else "a is not greater than 5"
print(result)


# Python While Loops

# Write a script to demonstrate a while loop.
i = 1
while i <= 5:
    print(i)
    i += 1

# Create a script that uses a while loop with a break statement.
i = 1
while i <= 5:
    if i == 3:
        break
    print(i)
    i += 1

# Write a script that uses a while loop with a continue statement.
i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1

# Demonstrate an infinite loop and how to stop it.
i = 0
while True:
    print(i)
    i += 1
    if i > 10:  # Stop condition for demonstration
        break

# Create a script that uses a while loop to iterate over a list.
my_list = [1, 2, 3, 4, 5]
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

# Python For Loops

# Write a script to demonstrate a for loop.
for i in range(5):
    print(i)

# Create a script that uses a for loop to iterate over a list.
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)

# Write a script that uses a for loop with the range() function.
for i in range(1, 6):
    print(i)

# Demonstrate nested for loops.
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

# Create a script that uses a for loop with an else clause.
for i in range(5):
    print(i)
else:
    print("Loop finished")

# Python Functions

# Write a script to define and call a function.
def greet():
    print("Hello, World!")

greet()

# Create a script that uses a function with parameters.
def greet(name):
    print("Hello, " + name + "!")

greet("Alice")

# Write a script that uses a function with a return value.  
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)


# Demonstrate the use of default parameters in a function.
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Alice")


# Create a script that uses a function with keyword arguments.
def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

greet(first_name="Alice", last_name="Smith")
greet(last_name="Doe", first_name="John")


# Python Operator
# Write a program that uses all basic arithmetic operators (+, -, *, /, %, //, **) with two numbers.
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Floor Division:", a // b)
print("Exponentiation:", a ** b)


# Create a script to demonstrate the use of assignment operators (=, +=, -=, *=, /=, %=, //=, **=).
a = 10

a += 5
print("a += 5:", a)

a -= 3
print("a -= 3:", a)

a *= 2
print("a *= 2:", a)

a /= 4
print("a /= 4:", a)

a %= 3
print("a %= 3:", a)

a //= 2
print("a //= 2:", a)

a **= 2
print("a **= 2:", a)

# Write a program to compare two numbers using comparison operators (==, !=, >, <, >=, <=).
a = 10
b = 20

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# Demonstrate the use of logical operators (and, or, not) in a simple condition.
a = True
b = False

print("a and b:", a and b)
print("a or b:", a or b)
print("not a:", not a)


# Create a script that shows the use of bitwise operators (&, |, ^, ~, <<, >>).
a = True
b = False

print("a and b:", a and b)
print("a or b:", a or b)
print("not a:", not a)

# Write a program that checks if a number is within a specified range using comparison and logical operators.
a = 5  # 0b0101
b = 3  # 0b0011

print("a & b:", a & b)  # AND
print("a | b:", a | b)  # OR
print("a ^ b:", a ^ b)  # XOR
print("~a:", ~a)        # NOT
print("a << 1:", a << 1) # Left Shift
print("a >> 1:", a >> 1) # Right Shift



# Use identity operators (is, is not) to compare objects and variables.
num = 15
start = 10
end = 20

if start <= num <= end:
    print(f"{num} is within the range")
else:
    print(f"{num} is not within the range")


# Write a program that uses membership operators (in, not in) to check if a value exists in a list.
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("a is b:", a is b)
print("a is c:", a is c)
print("a is not b:", a is not b)
print("a is not c:", a is not c)


# Demonstrate the use of operator precedence by creating a complex expression.
my_list = [1, 2, 3, 4, 5]
value = 3

print(f"{value} in my_list:", value in my_list)
print(f"{value} not in my_list:", value not in my_list)


# Write a program that takes two user inputs and performs all the basic arithmetic operations on them.
result = (2 + 3) * (5 ** 2) / 4 - 1
print("Result:", result)


# Create a script that swaps the values of two variables without using a third variable.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Floor Division:", a // b)
print("Exponentiation:", a ** b)


# Python Lists

# Create a list of five numbers and print the list.
a = 10
b = 20

a, b = b, a
print("a:", a)
print("b:", b)


# Write a program to access elements from a list using positive and negative indexing.
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)


# Create a script to add, remove, and update elements in a list.
my_list = [1, 2, 3, 4, 5]

print("First element:", my_list[0])
print("Last element:", my_list[-1])

# Write a program that concatenates two lists.
my_list = [1, 2, 3, 4, 5]

# Add elements
my_list.append(6)
print("After append:", my_list)

my_list.insert(2, 2.5)
print("After insert:", my_list)

# Remove elements
my_list.remove(2)
print("After remove:", my_list)

my_list.pop()
print("After pop:", my_list)

# Update elements
my_list[0] = 0
print("After update:", my_list)

# Create a script that finds the length of a list using the len() function.
list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined_list = list1 + list2
print("Combined List:", combined_list)


# 1. Write a program that checks if a specified element is present in a list.
def check_element(my_list, element):
    return element in my_list

my_list = [1, 2, 3, 4, 5]
element = 3
print("Is element present:", check_element(my_list, element))  # Output: True

# 2. Create a script to slice a list and print the sliced list.
def slice_list(my_list, start, end):
    return my_list[start:end]

sliced_list = slice_list(my_list, 1, 4)
print("Sliced list:", sliced_list)  # Output: [2, 3, 4]

# 3. Write a program that sorts a list in ascending and descending order.
def sort_list(my_list):
    ascending = sorted(my_list)
    descending = sorted(my_list, reverse=True)
    return ascending, descending

sorted_asc, sorted_desc = sort_list([5, 2, 9, 1, 5, 6])
print("Ascending:", sorted_asc)  # Output: [1, 2, 5, 5, 6, 9]
print("Descending:", sorted_desc)  # Output: [9, 6, 5, 5, 2, 1]

# 4. Create a script that demonstrates the use of list comprehension.
squares = [x**2 for x in range(10)]
print("List comprehension squares:", squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 5. Write a program to find the maximum and minimum values in a list.
def find_max_min(my_list):
    return max(my_list), min(my_list)

max_val, min_val = find_max_min([5, 2, 9, 1, 5, 6])
print("Maximum value:", max_val)  # Output: 9
print("Minimum value:", min_val)  # Output: 1

# 6. Create a script that reverses the elements of a list.
def reverse_list(my_list):
    return my_list[::-1]

reversed_list = reverse_list([1, 2, 3, 4, 5])
print("Reversed list:", reversed_list)  # Output: [5, 4, 3, 2, 1]

# Python While Loops

# 1. Write a program that prints numbers from 1 to 10 using a while loop.
i = 1
while i <= 10:
    print(i, end=' ')  # Output: 1 2 3 4 5 6 7 8 9 10
    i += 1
print()

# 2. Create a script that calculates the sum of the first 10 natural numbers using a while loop.
sum = 0
i = 1
while i <= 10:
    sum += i
    i += 1
print("Sum of first 10 natural numbers:", sum)  # Output: 55

# 3. Write a program that prints the multiplication table of a given number using a while loop.
def multiplication_table(number):
    i = 1
    while i <= 10:
        print(f"{number} * {i} = {number * i}")
        i += 1

multiplication_table(5)

# 4. Create a script that finds the factorial of a number using a while loop.
def factorial(number):
    result = 1
    while number > 1:
        result *= number
        number -= 1
    return result

print("Factorial of 5:", factorial(5))  # Output: 120

# 5. Write a program that prints all even numbers between 1 and 50 using a while loop.
i = 1
while i <= 50:
    if i % 2 == 0:
        print(i, end=' ')  # Output: 2 4 6 8 ... 48 50
    i += 1
print()

# 6. Create a script that reverses a given number using a while loop.
def reverse_number(number):
    reversed_num = 0
    while number > 0:
        digit = number % 10
        reversed_num = reversed_num * 10 + digit
        number //= 10
    return reversed_num

print("Reversed number of 12345:", reverse_number(12345))  # Output: 54321

# 7. Write a program that calculates the sum of digits of a number using a while loop.
def sum_of_digits(number):
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

print("Sum of digits of 12345:", sum_of_digits(12345))  # Output: 15

# 8. Create a script that finds the greatest common divisor (GCD) of two numbers using a while loop.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print("GCD of 48 and 18:", gcd(48, 18))  # Output: 6

# 9. Write a program that prints the Fibonacci sequence up to a specified number using a while loop.
def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=' ')
        a, b = b, a + b

fibonacci(50)  # Output: 0 1 1 2 3 5 8 13 21 34
print()

# 10. Create a script that prints numbers from 1 to 100, but skips numbers divisible by 5, using a while loop.
i = 1
while i <= 100:
    if i % 5 != 0:
        print(i, end=' ')  # Output: 1 2 3 4 6 7 8 9 11 ... 98 99
    i += 1
print()
# Python For Loops

# 1. Write a program that prints each element of a list using a for loop.
my_list = [1, 2, 3, 4, 5]
print("Elements of the list:")
for element in my_list:
    print(element)

# 2. Create a script that prints numbers from 1 to 10 using a for loop.
print("Numbers from 1 to 10:")
for i in range(1, 11):
    print(i, end=' ')
print()

# 3. Write a program that calculates the sum of elements in a list using a for loop.
def sum_of_elements(my_list):
    total = 0
    for number in my_list:
        total += number
    return total

print("Sum of elements:", sum_of_elements([1, 2, 3, 4, 5]))

# 4. Create a script that prints the multiplication table of a given number using a for loop.
def multiplication_table(number):
    print(f"Multiplication table for {number}:")
    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")

multiplication_table(5)

# 5. Write a program that prints all even numbers between 1 and 50 using a for loop.
print("Even numbers between 1 and 50:")
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=' ')
print()

# 6. Create a script that prints the Fibonacci sequence up to a specified number using a for loop.
def fibonacci_sequence(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=' ')
        a, b = b, a + b
    print()

fibonacci_sequence(50)

# 7. Write a program that iterates over a dictionary and prints each key-value pair.
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Key-value pairs in the dictionary:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# 8. Create a script that finds the maximum and minimum values in a list using a for loop.
def find_max_min(my_list):
    max_val = my_list[0]
    min_val = my_list[0]
    for number in my_list:
        if number > max_val:
            max_val = number
        if number < min_val:
            min_val = number
    return max_val, min_val

max_val, min_val = find_max_min([5, 2, 9, 1, 5, 6])
print("Maximum value:", max_val)
print("Minimum value:", min_val)

# 9. Write a program that prints each character of a string using a for loop.
my_string = "hello"
print("Characters in the string:")
for char in my_string:
    print(char)

# 10. Create a script that prints the reverse of a list using a for loop.
def reverse_list(my_list):
    reversed_list = []
    for element in my_list:
        reversed_list.insert(0, element)
    return reversed_list

print("Reversed list:", reverse_list([1, 2, 3, 4, 5]))

# 11. Write a program that uses nested for loops to print a pattern, such as a triangle of stars.
print("Triangle of stars:")
for i in range(1, 6):
    for j in range(i):
        print('*', end='')
    print()

# Python Functions

# 1. Write a function that takes two numbers as arguments and returns their sum.
def add_numbers(a, b):
    return a + b

print("Sum of 5 and 3:", add_numbers(5, 3))

# 2. Create a function that checks if a given number is prime.
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

print("Is 7 prime?", is_prime(7))

# 3. Write a function that calculates the factorial of a number.
def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

print("Factorial of 5:", factorial(5))

# 4. Create a function that returns the largest number in a list.
def largest_number(my_list):
    return max(my_list)

print("Largest number in the list:", largest_number([5, 2, 9, 1, 5, 6]))

# 5. Write a function that returns the nth Fibonacci number.
def nth_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print("The 5th Fibonacci number:", nth_fibonacci(5))

# 6. Create a function that checks if a given string is a palindrome.
def is_palindrome(s):
    return s == s[::-1]

print("Is 'radar' a palindrome?", is_palindrome('radar'))

# 7. Write a function that takes a list and an element as arguments and returns the index of the element in the list.
def find_index(my_list, element):
    return my_list.index(element) if element in my_list else -1

print("Index of 3 in the list:", find_index([1, 2, 3, 4, 5], 3))

# 8. Create a function that takes a list of numbers and returns a new list with the squares of those numbers.
def square_numbers(my_list):
    return [x**2 for x in my_list]

print("Squares of the list:", square_numbers([1, 2, 3, 4, 5]))

# 9. Write a function that takes a string and returns the number of vowels in the string.
def count_vowels(s):
    vowels = 'aeiou'
    return sum(1 for char in s if char in vowels)

print("Number of vowels in 'hello':", count_vowels('hello'))

# 10. Create a function that merges two dictionaries.
def merge_dicts(dict1, dict2):
    result = dict1.copy()  # Copy dict1 to avoid modifying the original
    result.update(dict2)   # Merge dict2 into result
    return result

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
print("Merged dictionary:", merge_dicts(dict1, dict2))

# 11. Write a function that takes a variable number of arguments and returns their sum.
def sum_all(*args):
    return sum(args)

print("Sum of 1, 2, 3, 4:", sum_all(1, 2, 3, 4))
