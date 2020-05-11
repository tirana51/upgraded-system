for _ in range(int(input())):
    r,c = map(int, input().split())
    x,y = map(int, input().split())
    r,c = r-1,c-1
    print(max(x,r-x,y,c-y))
