while True:
    try:
        password = input()
        for_upper = 0
        for_lower = 0
        for_number = 0
        flag = 0
        if len(password) >= 6 and len(password) <= 32:
            for letter in password:
                if letter.isupper():
                    for_upper += 1
                elif letter.islower():
                    for_lower += 1
                elif letter.isdigit():
                    for_number += 1
                else:
                    flag = 1
            if flag == 1:
                print("Senha invalida.")
            else:
                if (for_upper >= 1) and (for_lower >= 1) and (for_number >= 1):
                    print("Senha valida.")
                else:
                    print("Senha invalida.")
        else:
            print("Senha invalida.")
    except EOFError:
        break