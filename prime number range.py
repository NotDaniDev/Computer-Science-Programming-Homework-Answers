def isPrime(n):
    if n > 1:
        for i in range(2, int(n/2)):
            if n%i == 0:
                return False
        return True
    return False
r1 = int(input('Enter first value of range: '))
r2 = int(input('Enter last value of range: '))

list = []

print("The Prime Numbers in the range are: ")
for n in range(r1, r2 + 1):
    if isPrime(n) == True:
        list.append(n)
    else:
        n += 1

print(list)