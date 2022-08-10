def build_profile(first, last, **user_info):
    user_info['firs_name'] = first
    user_info['last_name'] = last_name
    return user_info

user_profile = build_profile('Asal', 'Delkhosh',
                            location = 'Mashhad',
                            age = 21,
                            field = 'computer science')
print(user_profile)
