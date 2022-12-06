x = input("input the amount: ")
list = x.split(".")
try:
    r = int(list[0])
    x = float(x)
    p = (x - r) * 100
    print("{} rupees and {} paisa or {} total paisa".format(r, round(p), round(x * 100)))
except:
    print("invalid syntax")