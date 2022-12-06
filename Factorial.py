number = int(input('Enter an integer: '))
factorial = 1
if number<0:
    print('There is not a factorial for negative number')
else:
    for i in range(1,number+1):
        factorial = factorial * i
    print(f'Factorial of {number} is {factorial}')