n=int(input())
f_sum=0
for i in range(1,n):
    if(n%i==0):
        f_sum+=i
if f_sum==n:
    print("True")
else:
    print("False")