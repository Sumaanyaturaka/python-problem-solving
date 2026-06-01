num=int(input("Enter a number:"))
print("The reversed number is: ",end="")
while num>0:
    r=num%10
    print(r,end="")
    num=num//10