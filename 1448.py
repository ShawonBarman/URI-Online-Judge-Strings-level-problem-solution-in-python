t = int(input())
for x in range(t):
    if x > 0:
        print("")
    message = input().upper()
    team1 = team2 = 0
    team1_msg = input().upper()
    team2_msg = input().upper()

    for i in range(len(message)):
        if team1_msg[i] == message[i]:
            team1 += 1
        if team2_msg[i] == message[i]:
            team2 += 1
    print("Instancia {}".format(x + 1))
    if team1 == team2:
        print("empate")
    elif team1 > team2:
        print("time 1")
    else:
        print("time 2")