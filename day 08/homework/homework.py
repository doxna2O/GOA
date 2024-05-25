name = input("შეიყვანეთ სახელი: ")
password = input("შეიყვანეთ პაროლი: ")
repeat_password = input("გაიმეორეთ პაროლი: ")

if password == repeat_password:
    print(f"{name} წარმატებით გაიარეთ რეგისტრაცია:)")
else:
    print("პაროლი არ დაემთხვა")