# Write a program to print difference of maximum and minimum values using existing function.

n=int(input())
l=[]
for i in range(n):
    x=int(input())
    l.append(x)
print(max(l))
print(min(l))
c=max(l)-min(l)
print(c)
