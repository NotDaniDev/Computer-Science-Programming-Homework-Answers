Mcard = {}
Gcard = {}
names = []
marks = []
grade = []
num = int(input("please input the number of students in your class: "))
names = [str(i) for i in
         input("please input all the names separating each with a comma and then a space: ").split(", ")]
if len(names) != num:
    print("number of names inputted dont match the number of names you've given")
else:
    for i in range(0, num):
        iMarks = int(input("please input the overall percentage of student {}: ".format(names[i])))
        if iMarks > 100:
            print("invalid input please restart")
            break
        elif iMarks < 0:
            print("invalid input please restart")
            break
        else:
            if iMarks in range(71, 101):
                grade.append("A*")
            elif iMarks in range(60, 71):
                grade.append("A")
            elif iMarks in range(45, 60):
                grade.append("B")
            elif iMarks in range(33, 45):
                grade.append("C")
            else:
                grade.append("Fail")

            marks.append(iMarks)
            Mcard.update({names[i]: marks[i]})
            Gcard.update({names[i]: grade[i]})

    print("-------------------------------------------")
    print("The overall percentage for each student is:")
    for x, y in Mcard.items():
        print("{}: {}".format(x, y))

    print("The overall grade for each student is:")
    for x, y in Gcard.items():
        print("{}: {}".format(x, y))

    print("-------------------------------------------")
    print("the average percentage of the entire class is: ")
    print(f'{round(sum(marks) / num)}%')