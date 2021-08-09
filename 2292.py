n = int(input())
while n != 0:
    n -=  1
    p, c = input().split()
    ans = ''
    for light in p:
        if light == 'X':
            ans += '0'
        else:
            ans += '1'
    rev_ans = ans[::-1]
    res = bin(int(rev_ans, 2) + int(n))
    res = str(res)[:1:-1]
    ans = ''
    for i in range(len(p)):
        if res[i] == '1':
            ans += 'X'
        else:
            ans += '0'
    print(ans)

# wrong answer