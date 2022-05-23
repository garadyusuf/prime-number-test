# program that asks a user for a number and then tests whether its prime or not
# print out "The number is prime" or "The number is not prime"

num = int(input("Enter a number: "))

flag = False

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

if flag:
    print("This is not a prime number")
else:
    print("This is a prime number")