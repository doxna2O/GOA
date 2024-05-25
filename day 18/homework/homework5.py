#სიაში შეინახეთ თქვენი სახელი და გვარი. capitalize მეთოდის გამოყენებით მასივის 
#ყველა ელემენტზე მოახდინეთ მუშაობა და ბოლოს დაბეჭდეთ უკვე შეცვლილი სია.


def list_change(list):
    
    for i in range(len(list)):
        list[i] = list[i].capitalize()

    print(list )
list_change(["nikoloz", "dokhnadze"])