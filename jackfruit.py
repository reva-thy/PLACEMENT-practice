arr=list(map(int,input().split()))
n=arr[0]
d=arr[1]
a=list(map(int,input().split()))
for i in range(0,n):
    for j in range(0,n-i-1):
        if a[j]<a[j+1]:
            temp=a[j+1]
            a[j+1]=a[j]
            a[j]=temp
sum=0
for i in range(d):
    sum=sum+a[i]
print(sum)