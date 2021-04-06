#Define the function fib
def fib(n):
#Return 1 when n is 0 or 1
    if(n == 0):
        return 1

    elif(n == 1):
        return 1

#Recursive call to generate fibonacci numbers
    else:
        return fib(n-1) + fib(n-2)

#main
#prompting user to enter the number
x = input("Please enter the number you want a sequence from:\n")
    if(x != int):
        print("Error, incorrect input")
#Generate fibonacci number for n = 1
    else:
        print("Fibonacci number for n = " + x )
        for  in range(x):
            print(fib(i))

#Generate fibonacci number for n = 5
x = 5
print("Fibonacci number for n = 5")
for i in range(x):
    print(fib(i))

#Generate fibonacci number for n = 10
x = 10
print("Fibonacci number for n = 10")
for i in range(x):
    print(fib(i))

#Generate fibonacci number for n = 20
x = 20
print("Fibonacci number for n = 20")
for i in range(x):
    print(fib(i))

#Generate fibonacci number for n = 30
x = 30
print("Fibonacci number for n = 30")
for i in range(x):
    print(fib(i))

#Generate fibonacci number for n = 35
x = 35
print("Fibonacci number for n = 35")
for i in range(x):
    print(fib(i))

#Generate fibonacci number for n = 40
x = 40
print("Fibonacci number for n = 40")
for i in range(x):
    print(fib(i))