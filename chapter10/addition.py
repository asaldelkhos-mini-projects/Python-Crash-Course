print("Give me two number, and I'll add them together")
print("Enter 'q' to quit")

first_number = input("First number: ")
if first_number == 'q':
    break
second_number = input("Second number: ")
if second_number == 'q':
    break

sum = int(first_number) + int(second_number)
print(sum)
