x = int(input('Enter start of the range: '))
y= int(input('Enter end of the range: '))
if x == 0:
    print('Zero is not a natural number')
elif y == 0:
    print('Zero is not a natural number')
else:
    sum = 0
    for i in range(x, y + 1, 1):
        sum = sum + i
    print(sum)