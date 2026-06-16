def fib(n):
    if (n<=1):
        return n
    oneback = fib(n-1)
    twoback = fib(n-2)
    return (oneback + twoback)

number = input('Enter a number\n')
number = int(number)
for i in range(number + 1):
    print(fib(i), end=" ")