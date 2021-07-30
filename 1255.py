n = int(input())
while n != 0:
    n -= 1
    text = input().lower()
    maxi = 0
    i = 0
    alpha = 'a'
    while True:
        if alpha in text:
            maxi = text.count(alpha)
            break
        alpha = chr(ord(alpha) + 1)
        i += 1
    dic = {}
    alpha = 'a'
    for i in range(26):
        x = text.count(alpha)
        if x >= maxi:
            maxi = x
            dic.update({
                alpha: maxi
            })
        alpha = chr(ord(alpha) + 1)
    ans = ""
    for letter, value in dic.items():
        if value == maxi:
            ans += letter
    ans_string = "".join(sorted(ans))
    print(ans_string)