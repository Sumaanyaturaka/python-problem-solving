totalamt=int(input("Enter the total amount: "))
fivehund=totalamt//500
leftamt=totalamt%500
twohund=leftamt//200
leftamt=leftamt%200
hund=leftamt//100
print("The number of 500 notes is: ",fivehund)
print("The number of 200 notes is: ",twohund)
print("The number of 100 notes is: ",hund)