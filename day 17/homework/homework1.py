#1) შექმენით ფუნქცია, რომელშიც გააერთიანებთ იმ ფუნქციებს რაც დღეს ვისწავლეთ (lower(), upper(), capitalize(), find())
def mix(low,up,cap,find):
    first = low.lower()
    second = up.upper()
    third = cap.capitalize()
    fourth = find.find("love")

    return first, second, third, fourth

print(mix("HELLO MY FRIEND","hello my fella","my name is nick","when love is in the air"))