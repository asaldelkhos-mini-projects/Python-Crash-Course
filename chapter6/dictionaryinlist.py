
info1 = {
    'first_name' : 'jim',
    'last_name' : 'halpert',
    'job' : 'sale man'
}
info2 = {
    'first_name' : 'pam',
    'last_name' : 'vizly',
    'job' : 'resptionist'
}
info3 = {
    'first_name' : 'dwit',
    'last_name' : 'shrot',
    'job' : 'sale man'
}

people = [info1, info2, info3]

for person in people:
    for info in person.values():
        print(info)
    print('\n')    
