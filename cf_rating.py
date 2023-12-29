t = int(input())
n = []
r = []
cha = []
for i in range(t):
    ne,re = [int(x) for x in input().split()]
    n.append(ne)
    r.append(re)
    arr = list(map(int,input().split()))
    cha.append(arr)
for i in range(t):
    if sum(cha[i]) + 1500 == r[i]:
        print("Correct")
    else:
        print("Bug")
