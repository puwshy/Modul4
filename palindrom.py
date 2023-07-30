
vvod = input("Введите строку для проверки:")

def check_palindrome(stroka):
    reversed_str = stroka[::-1]
    if reversed_str == stroka:
        print('True')
    else:
        print('False')
       
check_palindrome(vvod)



