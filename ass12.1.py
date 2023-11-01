# Write a program to store n values into the list and print first and last value.

n=int(input())
l=[]
for i in range(n):
    x=int(input())
    l.append(x)
print(l)
print(l[0])
print(l[n-1])
