first_text = input()
second_text = input()
x = ""
y = ""
z = ""
for i in range(len(first_text)):
    if first_text[i].isdigit():
        if len(x) < 11:
            x += first_text[i]
        else:
            z += first_text[i]
    if first_text[i] == ".":
        z += "."
for i in range(len(second_text)):
    if second_text[i].isdigit():
        y += second_text[i]
    elif second_text[i] == ".":
        y += second_text[i]
if "." in y:
    a, b = y.split(".")
    c, d = z.split(".")
    sum1 = str(int(a) + int(c))
    sum2 = str(int(b[:2]) + int(d[:2]))
    sum = sum1 + "." + sum2[:2]
    print("cpf", x)
    print(sum)
else:
    c, d = z.split(".")
    sum1 = str(int(y) + int(c))
    sum = sum1 + "." + d[:2]
    print("cpf", x)
    print(sum)