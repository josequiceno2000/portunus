def opening():
    print("Welcome to Portunus: the Ultimate Password Generator!")
    return int(input("How many letters would you like in your password?\n> "))

def main():
    letter_count = opening()
    print(letter_count)

if __name__ == "__main__":
    main()