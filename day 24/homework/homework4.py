#მომხმარებელს შემოატანინეთ სიტყვა და შემდეგ განიხილეთ ამ სიტყვის ყველა ასო. lowercase გადააკეთეთ uppercase-ად, ხოლო uppercase კი lowercase-ად.
def word(word):
    shecvlili = ""
    for i in word:
        if i.islower():
            shecvlili += i.upper()
        else:
            shecvlili += i.lower()
    return shecvlili
print(word("nikOloZI"))