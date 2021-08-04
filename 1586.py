def cal(x, y, flag):
    ans = 0
    p = 1
    if flag == 1:
        for i in range(x, y+1):
            ans += students[i] * p
            p += 1
    else:
        for i in range(y, x-1, -1):
            ans += students[i] * p
            p += 1
    return ans

def func(x, y):
    while x <= y:
        # using binary search
        mid = int((x + y) / 2)
        team_A = cal(0, mid, -1)
        team_B = cal(mid+1, n-1, 1)
        if team_A == team_B:
            return mid
        elif team_A > team_B:
            y = mid-1
        else:
            x = mid + 1
    return -1
while True:
    try:
        n = int(input())
        if n == 0:
            break
        students = []
        while n != 0:
            n -= 1
            name = input()
            sum = 0
            for x in name:
                sum += ord(x)
            students.append(sum)
        idx = func(0, len(students)-1)
        if idx == -1:
            print("Impossibilidade de empate.")
        else:
            print(students[idx])
    except EOFError:
        break

# Time limit exceeded