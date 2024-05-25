#2) `შექმენით ფუნქცია, სახელად find_index, რომელსაც გადაეცემა სთრინგი და საპოვნელი ასო. თქვენი დავალებაა, რომ გადაცემულ სთრინგში არსებული ასოს ინდექსი დააბრუნოთ.
def find_index(string, chr):
    result = []
    for i in range(len(string)):
        if chr == string[i]:
            result.append(i)
    return result
print(find_index("nikoloz", "z"))