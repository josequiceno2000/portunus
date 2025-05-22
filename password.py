import random

def get_password_details():
    letter_cnt =  int(input("How many letters would you like in your password?\n> "))
    symbol_cnt =  int(input("How many symbols would you like?\n> "))
    number_cnt =  int(input("Finally, how many numbers?\n> "))
    return [letter_cnt, symbol_cnt, number_cnt]

def construct_password(letter_cnt: int, symbol_cnt: int, number_cnt: int):
    alphabet = "abcdefjhijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbols = "!#$%&()*+"
    numbers = "1234567890"
    
    password = set()

    while len(password) < letter_cnt:
        password.add(random.choice(alphabet))
    
    while len(password) < letter_cnt + symbol_cnt:
        password.add(random.choice(symbols))

    while len(password) < letter_cnt + symbol_cnt + number_cnt:
        password.add(random.choice(numbers))
    
    return "".join(password)