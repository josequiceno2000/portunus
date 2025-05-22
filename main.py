from intro import opening
from password import get_password_details, construct_password

def main():
    opening()
    letter_cnt, symbol_cnt, number_cnt = get_password_details()
    password = construct_password(letter_cnt, symbol_cnt, number_cnt)
    print(f"\nYour password is: {password}")

if __name__ == "__main__":
    main()