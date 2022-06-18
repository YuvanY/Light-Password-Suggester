import random

while True:
    try:
        LEN_LIST = int(input("What should be the length Sir ?: "))

        DIGITS = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        random.shuffle(DIGITS)

        LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
        random.shuffle(LOCASE_CHARACTERS)

        UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
        random.shuffle(UPCASE_CHARACTERS)

        SYMBOLS = ['@', '#', '$', '*']
        random.shuffle(SYMBOLS)

        COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
        random.shuffle(COMBINED_LIST)

        rand_digit = random.choice(DIGITS)
        rand_uppper = random.choice(UPCASE_CHARACTERS)
        rand_lower = random.choice(LOCASE_CHARACTERS)
        rand_symbol = random.choice(SYMBOLS)
        password = rand_digit + rand_uppper + rand_lower + rand_symbol


        for _ in range(LEN_LIST - 4):
            password += random.choice(COMBINED_LIST)


        print(password)
    
    except:
        print("Error: Length of the password must be in numbers!")
        continue

    

    ask_quit = input("\nWill I exit or you need more password(y/n): ").strip().lower()
    if ask_quit == "y":
        break
    elif ask_quit == "n":
        continue

    ask_quit = input("Will I exit or you need more password(y/n): ").strip().lower()
    if ask_quit == "y":
        break
    elif ask_quit == "n":
        continue
    elif ask_quit != 'n' or ask_quit != 'y':
        while ask_quit != 'n' or ask_quit != 'y':
            print('Please answer in y/n ')
            ask_quit = input("Will I exit or you need more password(y/n): ").strip().lower()

            