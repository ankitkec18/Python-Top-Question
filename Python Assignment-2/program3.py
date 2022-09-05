def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
num=int(input("Enter any Number: "))
ans=fact(num)
print("Factorial is : ",ans);