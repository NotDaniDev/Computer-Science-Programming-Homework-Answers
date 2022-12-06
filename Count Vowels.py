vowelList = ["a", "e", "i", "o", "u"]
vowels = []

x = input("please input the word you want to check for vowels: ")
for v in vowelList:
    for i in x:
        if i == v:
            vowels.append(i)
print(f"there are {len(vowels)} vowels in your input")