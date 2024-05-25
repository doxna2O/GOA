#2)შექმენით ფუნქცია რომელსაც გადაეცემა list = ["name1" , "name2" , "name3"....]
#შემდეგ მომხმარებელს კითხეთ რომელი ინდექსის შეცვლა სურს და ამის მიხედვით 
#შეცვალეთ ის კონკრეტული ინდექსი თქვენი სასურველი სტრინგით და ბოლოს შეაერთეთ join() ფუნქციის მეშვეობით

def list_func(list):
    index = input("please enter index between 0" + "-" + str(len(list) - 1) )

    list[index] = "nika"

    result = " ".join(list)

    return result

print(list_func(["nika", "nini", "gio"]))