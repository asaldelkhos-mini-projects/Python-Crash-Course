#exercise from book example's
squares = [value**2 for value in range(1, 11)]
print(squares)

#exercise 4-10

print(f"Three first items in your list are:{squares[:3]}")
print(f"Three items from the middle of the list are:{squares[4:7]}")
print(f"Three last items in the list are:{squares[-3:]}")
