import random

def opening():
    print("Welcome to Portunus: the Ultimate Password Generator!")

def get_password_details():
    letter_cnt =  int(input("How many letters would you like in your password?\n> "))
    symbol_cnt =  int(input("How many symbols would you like?\n> "))
    number_cnt =  int(input("Finally, how many numbers?\n> "))
    return [letter_cnt, symbol_cnt, number_cnt]

def construct_password(letter_cnt: int, symbol_cnt: int, number_cnt: int):
    alphabet = "abcdefjhijklmnopqrstuvwxyz"
    numbers = "1234567890"
    symbols = "!#$%&()*+"



def main():
    opening()
    letter_cnt, symbol_cnt, number_cnt = get_password_details()
    # password = construct_password()
    print(letter_cnt, symbol_cnt, number_cnt)

if __name__ == "__main__":
    main()