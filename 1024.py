n = int(input())
while n != 0:
    n -= 1
    m = list(input())
    x = int(len(m)/2)
    for i in range(len(m)):
        if (m[i] >= "A" and m[i] <= "Z") or (m[i] >= "a" and m[i] <= "z"):
            m[i] = chr(ord(m[i]) + 3)
    m = m[::-1]
    new_part = ""
    for i in range(x, len(m)):
        if (ord(m[i]) >= 32 and ord(m[i]) <= 176):
            m[i] = chr(ord(m[i]) - 1)
    for i in range(len(m)):
        new_part += m[i]
    print(new_part)