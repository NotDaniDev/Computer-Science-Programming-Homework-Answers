x = input("input the time you want to convert: ")
list = x.split(".")
try:
    m = int(list[0])
    x = float(x)
    s = (x - m) * 60
    print(f"the time is {m} minutes and {round(s)} seconds")
except:
    print("invalid input")