string = input('Enter first value/text: ')
string2 = input('Enter second value/text: ')
string3 = string+string2
if string3.isdigit():
    print(float(string)+float(string2))
else:
    print('Your output is: ',string3)
    