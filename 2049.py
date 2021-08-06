count = 1
while True:
    a = input()
    if a == '0':
        break
    if count > 1:
        print()
    numbers = input()
    print("Instancia", count)
    if a in numbers:
        print("verdadeira")
    else:
        print("falsa")
    count += 1