# start with users that need to be verified,
# and an empty list to hold confirmed users.

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# verify each user until there are no more unconfirmed users.
# move each user verified user into thr list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(unconfirmed_users)
    print(confirmed_users)
    print('\n')

    print(f"verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
    print(confirmed_users)
    print('\n')
