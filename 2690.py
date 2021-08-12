n = int(input())
while n != 0:
    n -= 1
    test = input()
    ans = ""
    for i in test:
        if i.isalpha():
            if i == 'G' or i == 'Q' or i == 'a' or i == 'k' or i == 'u':
                ans += '0'
            elif i == 'I' or i == 'S' or i == 'b' or i == 'l' or i == 'v':
                ans += '1'
            elif i == 'E' or i == 'O' or i == 'Y' or i == 'c' or i == 'm' or i == 'w':
                ans += '2'
            elif i == 'F' or i == 'P' or i == 'Z' or i == 'd' or i == 'n' or i == 'x':
                ans += '3'
            elif i == 'J' or i == 'T' or i == 'e' or i == 'o' or i == 'y':
                ans += '4'
            elif i == 'D' or i == 'N' or i == 'X' or i == 'f' or i == 'p' or i == 'z':
                ans += '5'
            elif i == 'A' or i == 'K' or i == 'U' or i == 'g' or i == 'q':
                ans += '6'
            elif i == 'C' or i == 'M' or i == 'W' or i == 'h' or i == 'r':
                ans += '7'
            elif i == 'B' or i == 'L' or i == 'V' or i == 'i' or i == 's':
                ans += '8'
            elif i == 'H' or i == 'R' or i == 'j' or i == 't':
                ans += '9'
        elif i.isdigit():
            ans += i

        if len(ans) == 12:
            break
    print(ans)