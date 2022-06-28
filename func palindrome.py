string = input('Введите строку: ')
def palindrome():
    a = string.replace(' ', '')
    if a[::1] == a[::-1]:
        print('Эта строка - палиндром.')
    else:
        print('Эта строка не является палиндромом.')

palindrome()