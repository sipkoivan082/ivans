a=open('24_28765.txt').readline()
n=180

s=a.replace('BC','B1C').split('1')

lst=[]

for i in range(len(s)-n):
    f=s[i:i+n+1]
    s=''.join(f)
    lst.append(len(s))
print(max(lst))