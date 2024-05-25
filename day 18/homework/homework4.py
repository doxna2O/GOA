#ცვლადში შეინახეთ თქვენი სახელი. თუ მისი სიგრძე აღემატება ხუთს, გარდაქმენით
#მთლიანი სიტყვა uppercase-ად, სხვა შემთხვევაში კი lowecase-ად. საბოლოოდ კი 
#დაბეჭდეთ გარდაქმნილი სახელი.


def modify_word(word):
    if len(word) < 5:
        modified_word = word.upper()
    else:
        modified_word = word.lower()
    print(modified_word)
modify_word("nika")