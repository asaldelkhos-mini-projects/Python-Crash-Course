filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    pi_string += line.strip()    
