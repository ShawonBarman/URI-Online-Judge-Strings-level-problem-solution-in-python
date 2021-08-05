n = int(input())
while n != 0:
    n -= 1
    rajesh, sheldon = input().split()
    if (rajesh == "pedra" and sheldon == "pedra") or (rajesh == "papel" and sheldon == "papel") or (rajesh == "tesoura" and sheldon == "tesoura") or (rajesh == "lagarto" and sheldon == "lagarto") or (rajesh == "spock" and sheldon == "spock"):
        print("empate")
    elif (rajesh == "tesoura" and sheldon == "papel") or (rajesh == "papel" and sheldon == "pedra") or (rajesh == "pedra" and sheldon == "lagarto") or (rajesh == "lagarto" and sheldon == "spock") or (rajesh == "spock" and sheldon == "tesoura") or (rajesh == "tesoura" and sheldon == "lagarto") or (rajesh == "lagarto" and sheldon == "papel") or (rajesh == "papel" and sheldon == "spock") or (rajesh == "spock" and sheldon == "pedra") or (rajesh == "pedra" and sheldon == "tesoura"):
        print("rajesh")
    else:
        print("sheldon")