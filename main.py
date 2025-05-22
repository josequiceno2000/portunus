def opening():
    print("Welcome to Portunus: the Ultimate Password Generator!")

def get_password_details():
    letter_count =  int(input("How many letters would you like in your password?\n> "))
    symbol_count =  int(input("How many symbols would you like?\n> "))
    number_count =  int(input("Finally, how many numbers?\n> "))
    return {
        "letters": letter_count, 
        "symbols": symbol_count,
        "numbers": number_count,
        }

def main():
    opening()
    password_details = get_password_details()
    print(password_details)

if __name__ == "__main__":
    main()