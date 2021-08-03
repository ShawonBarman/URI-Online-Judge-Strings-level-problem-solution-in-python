import string
alpha_list = list(string.ascii_lowercase)

n = int(input())
while n != 0:
    n -= 1
    text = input()
    count = 0
    for i in range(len(alpha_list)):
        if alpha_list[i] in text:
            count += 1
    if count == len(alpha_list):
        print("frase completa")
    elif count >= int(len(alpha_list)/2):
        print("frase quase completa")
    else:
        print("frase mal elaborada")