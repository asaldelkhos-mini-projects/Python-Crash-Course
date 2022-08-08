# testing sth for myself

def pet_info(name, type ='dog'):
    print(f"\nI have a {type}")
    print(f"my {type}'s name is {name}")

name = input("What is your dog's name? ")
pet_info(name)

pet_info(name, type='cat')
