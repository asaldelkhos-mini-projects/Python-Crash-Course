#exercise 7-3

num = input("Hi Dear User, tell me a number \nand a tell you if it is multiples of Ten or not.")
num = int(num)

if num % 10 == 0:
    print(f"\n{num} is multiples of TEN")
else:
    print(f"\n{num} ISN'T multiples of TEN")    
