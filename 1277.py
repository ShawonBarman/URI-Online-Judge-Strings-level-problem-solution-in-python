n = int(input())
while n != 0:
    n -= 1
    num = int(input())
    names = list(map(str, input().split()))[:num]
    attendance = list(map(str, input().split()))[:num]
    ans = ""
    for i in range(num):
        name = names[i]
        total_present = attendance[i].count("P")
        report = attendance[i].count("M")
        x = len(attendance[i]) - report
        avg = int((total_present/x) * 100)

        if avg < 75:
            ans = ans + " " + name
    print(ans.strip())