n = int(input())
while n != 0:
    n -= 1
    word = input()
    x = int(len(word)/2)
    first_part = word[:x]
    last_part = word[x:]
    first_part = first_part[::-1]
    last_part =  last_part[::-1]
    print(first_part+last_part)