def f(n):
    s=set()
    for d in range(2,int(n**0.5)+1):
        if n%d==0:
            s.add(d)
            s.add(n//d)
    return s

k=0
for n in range( 700000,800000):
    s=f(n)
    s= [i for i in s if i%10==7 and i!=7]
    if s:
        print(n,min(s))
        k+=1
        if k==5:
            break