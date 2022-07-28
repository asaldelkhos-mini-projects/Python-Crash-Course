#exercize 5-6

age = 12

if age < 2:
    person = 'a baby'
elif age >= 2 and age < 4:
    person = 'a toddler'
elif age >=4 and age <13:
    person = 'a kid'
elif age >=13 and age < 20:
    person = 'a teenager'
elif age >= 20 and age < 65:
    person = 'an adult'
else:
    person = 'an elder'
# USING JUST IF IS OK, IF AND ELIF ALO IS OK, IF/ELIF/ELSE IS OK TOO
print(f"the person is {person}")
