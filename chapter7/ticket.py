#exercise 7-5

age = input("How old are you?")
age = int(age)
if age <= 3:
    print("free")
elif age > 3 and age <= 12:
    print("$10")
elif age > 12:
    print("$15")
