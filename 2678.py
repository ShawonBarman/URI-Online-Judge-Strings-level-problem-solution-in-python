while True:
    try:
        num = input().upper()
        ans = ''
        list_num = '0123456789*#'
        for digit in num:
            if digit in list_num:
                ans += digit
            elif digit == 'A' or digit == 'B' or digit == 'C':
                ans += '2'
            elif digit == 'D' or digit == 'E' or digit == 'F':
                ans += '3'
            elif digit == 'G' or digit == 'H' or digit == 'I':
                ans += '4'
            elif digit == 'J' or digit == 'K' or digit == 'L':
                ans += '5'
            elif digit == 'M' or digit == 'N' or digit == 'O':
                ans += '6'
            elif digit == 'P' or digit == 'Q' or digit == 'R' or digit == 'S':
                ans += '7'
            elif digit == 'T' or digit == 'U' or digit == 'V':
                ans += '8'
            elif digit == 'X' or digit == 'Y' or digit == 'W' or digit == 'Z':
                ans += '9'
        print(ans)
    except EOFError:
        break