products = input().split()
d={}
for i in products:
    if d.get(i):
        d[i]+=1
    else:
        d[i]=1
maxi = max(d.values())
for i,j in sorted(d.items(),reverse=True):
    if j == maxi:
        print(i)
        break
