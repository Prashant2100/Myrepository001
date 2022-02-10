a=int(input())
for mm in range(a):
    l=list(map(int,input().split()))
    a=l[0]
    b=l[1]
    print(a,b)
    k=[]
    for i in range(a+1):
        for t in range(a+1):
            j=[]
            if(i+t)==b:
                
                j.append(i)
                j.append(t)
                k.append(j)
    k.sort()
    print(mm)
        
