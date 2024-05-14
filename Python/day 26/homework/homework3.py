#3) def keyword'ის გამოყენებით შექმენით len()'ის მსგავსი ფუნქცია ( ფუნქცია რომელიც გამოიტანს რამდენი ელემენტია list'ში).
def manual_len(list):
    length = 0
    for i in list:
        length += 1
    return length
print(manual_len([1,2,3,4,5,6,7,8,9,10]))