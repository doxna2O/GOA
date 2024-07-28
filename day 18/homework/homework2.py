#მომხმარებელს შემოატანინეთ სიტყვა. for ციკლის გამოყენებით შეამოწმეთ მისი 
#თითოეული ასო და თუ რომელიმე იქნება lowercase, მაშინ მომხმარებელს 
#შემოატანინეთ სიტყვა თავიდან. ასევე დაბეჭდეთ თუ რამდენჯერ მოუწია 
#მომხმარებელს სიტყვის შემოტანა - counter.

def lowercase(word):
    word = input("enter a word: ")
    for i in range(len(word)):
        if word[i] != word[i].lower():
            pass
        else:
            print("THIS CONTAINS LOWERCASE LETTERS TRY AGAIN")
                

lowercase(input("enter a word: "))

#მეტი ვეგარ გავაკეთე