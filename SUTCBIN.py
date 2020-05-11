n = int(input())
#input()
a = list(map(int, input().split()))
ignore = []
s = set(a)
for e in a:
    if e not in ignore:
        print(a.count(e)+e, end=" ")
        ignore.append(e)
    if len(ignore)==len(s):
        break
