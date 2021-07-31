import string
alpha_list = list(string.ascii_lowercase)
while True:
    try:
        text = input()
        arr = []
        result_list = []
        for i in range(len(alpha_list)):
            if alpha_list[i] in text:
                arr.append(alpha_list[i])
            else:
                if len(arr)!=0:
                    ans = arr[0]+":"+arr[len(arr)-1]
                    result_list.append(ans)
                    arr = []
        if len(arr) != 0:
            ans = arr[0] + ":" + arr[len(arr) - 1]
            result_list.append(ans)
        if len(result_list)>1:
            print(result_list[0], end="")
            for i in range(1,len(result_list)):
                print(", "+result_list[i], end="")
            print()
        elif len(result_list) == 1:
            print(result_list[0])
        else:
            print()
    except EOFError:
        break