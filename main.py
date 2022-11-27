A = int(input("Enter a number: "))
isprime = True
B = A - 1
while(B != 1):
    if A%B == 0:
        isprime = False
    B = B-1
if isprime == True :
    print(A, "is a prime number")
else:
    print(A, "is not a prime number")

