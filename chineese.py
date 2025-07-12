a=int(input())
b=list(map(int,input().split()))
c=list(map(int,input().split()))
d=int(input())
e=[]
f=[]
for i in range(a):
    for j in range(a):
        if(b[i]+c[j]==d):
            e.append(b[i])
            f.append(c[j])
        elif(b[i]+c[j]>d):
            amnt=((abs(b[i]+c[j])-5) * (100))
        else:
            amnt=0
print(amnt)