#2)შექმენით ფუნქცია რომელიც სიაში ლუწ ინდექსებზე მდგომ რიცხვთა ჯამს დააბრუნებს,
# შესატანი მონაცემები: [1,2,3,4,5] ---- გამოსატანი მონაცემები (შედეგი):  9
def odd_nums(list):
    result = 0
    
    for i in range(len(list)):
        if i % 2 == 0:
            result = result + list[i]
    print(result)
odd_nums([1,2,3,4,5])