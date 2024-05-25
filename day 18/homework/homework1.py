#მომხმარებელს შემოატანინეთ სახელი. თქვენი დავალებაა, რომ შეადაროთ სახელი მის
#lowercase ვარიანტთან == ოპერატორის გამოყენებით.
def lower(word):
    word1 = word.lower()

    if word == word1:
        print(word)
    else:
        print(word + "," + word1)
    
    return

lower(input("Enter your name: "))