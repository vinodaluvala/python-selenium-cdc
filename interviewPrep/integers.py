# Find a prime of a given number
num = int(input("Enter a number greater than 2:"))
flag = False
if num ==1:
    print("num is not a prime number")
elif num>1:
    for i in range(2, num):
        if num%i ==0:
            flag = True
            break
if flag:
    print(f"{num} is not a prime")
else:
    print(f"{num} is a prime")

#Find the prime numbers in a given range
lower = 1
upper = 100
for num in range(lower, upper+1):
    if num>1:
        for i in range(2, num):
            if num%i==0:
                break
        else:
            print(num)
    else:
        print("no print numbers")

# find the prime numbers from the given list of numbers
num = [2, 5, 7, 7, 8, 34, 55, 11]
