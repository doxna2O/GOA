#3) შექმენით ფუნქცია რომელიც გამოითვლის კენტების და ლუწების ჯამს ცალცალკე,
#დააბრუნეთ სია სადაც იქნება ეს ჯამები ჩასმული,
# შესატანი მონაცემები [1,2,3,4,5] ---- გამოსატანი მონაცემები [6, 9]
def odd_even_sum(list):
    even_sum = 0
    odd_sum = 0
    for i in range(len(list)):
        if i % 2 == 0:
            odd_sum += list[i]
        else:
            even_sum += list[i]
    result = [even_sum, odd_sum]
    print(result)
odd_even_sum([1, 2, 3, 4, 5])
