l=sorted(list(map(int,input().split())))
l1=sorted(set(l))
l=sorted(l1,key=lambda i:l.count(i),reverse=True)
print(*l)
