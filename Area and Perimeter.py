print('This code will let you find area and perimeter of circle, triangle, square and rectangle')
option = str(input('Choose which polygon you want to find area and perimeter of: '))
if option == 'circle':
    radius = float(input('Enter radius of circle: '))
    pi = 3.141592653589793
    print('Area of the circle is: ',pi*(radius**2))
    print('Circumfrence/Perimeter of the circle is: ', (2*pi)*radius)
elif option == 'triangle':
    base = float(input('Enter base of the triangle: '))
    height = float(input('Enter height of the triangle: '))
    print('Area of the triangle is: ',0.5*base*height)
    print('To find the perimeter of the triangle input the following values')
    a = float(input('Enter the length of the left side of the triangle: '))
    b = float(input('Enter the length of the right side of the triangle: '))
    print('Perimeter of the triangle is: ',a+b+base)
elif option == 'square':
    side = float(input('Enter the length of a side: '))
    print('Area of the square is: ',side**2)
    print('Perimeter of the square is: ',side*4)
elif option == 'rectangle':
    length = float(input('Enter the length: '))
    breadth = float(input('Enter the breadth: '))
    print('Area of the rectangle is: ',length*breadth)
    print('Perimeter of the rectangle is: ',2*(length+breadth))
else:
    print('Please enter the value again it should be either circle, triangle, square or rectangle or the code would not function as desired')
