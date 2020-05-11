for _ in range(int(input())):
    n = int(input())
    temp = list(map(int, input().split()))
    c = 0
    for i in range(n-1):
        temp2 = list(map(int, input().split()))
        if c==0:
            for j in range(n-1):
                if temp[j]==1 and (temp[j+1]==1 or temp2[j]==1):
                    c=1
        temp = temp2
    if c:
        print('UNSAFE')
    else:
        print('SAFE')
