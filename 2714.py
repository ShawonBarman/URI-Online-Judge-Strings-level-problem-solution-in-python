n = int(input())
while n != 0:
    n -= 1
    password = input()
    x = ""
    flag = 0
    for i in password:
        if i.isdigit() and i != '0':
            flag = 1
        if flag == 1:
            x += i
    if len(password) == 20 and password.startswith("RA") and (password.count('0') >= 0 and password.count('0') <= 17) and (len(x) >= 1 and len(x) <= 18):
        print(x)
    else:
        print("INVALID DATA")