print('Enter username and password')
count=0
for count in range(3):
    username = input('Enter username: ')
    password = input('Enter password: ')
    if password=='asd' and username=='qwe':
        print('Access granted')
        break
    else:
        print('Access denied. Try again.')
        count += 1