a=int(input())
b=int(input())
c=int(input())
if(a>b>c):
    print(b)
elif(b>a>c):
    print(a)
elif(c>b>a):
    print(b)
elif(a>c>b):
    print(c)
elif(b>c>a):
    print(c)
else:
    print(a)

