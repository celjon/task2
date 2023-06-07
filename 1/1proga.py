def palindrome(str):
    str = str.lower().replace(" ", "")
    return str == str[::-1]

# Пример использования функции
input_str = input("Ввод: ")
if palindrome(input_str):
    print("палиндром")
else:
    print("не палиндром")
