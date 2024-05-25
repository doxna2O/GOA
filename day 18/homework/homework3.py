#მომხმარებელს შემოატანინეთ სიტყვა. თქვენი დავალებაა, რომ ლუწ ინდექსებზე მყოფი 
#ასოები გარდაქმნათ uppercase-ად, ხოლო კენტ ინდექსებზე მყოფები lowecase-ად, 
#საბოლოოდ კი დაბეჭდოთ შედეგი.

def modify_word(word):
    changed_word = ''
    for i in range(len(word)):
        if i % 2 == 0:
            changed_word = changed_word + word[i].upper()
        else:
            changed_word = changed_word + word[i].lower()
    return changed_word
result1 = input("enter ur word: ")
result = modify_word(result1)
print(result)