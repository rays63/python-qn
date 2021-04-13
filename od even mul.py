data = int(input("Enter a number:"))
total1 = []
modu = data % 2
while data != 0:
    if modu == 0:
        mul = data * 2
        total1.append(mul)
    else:
        mul = data * 4
        total1.append(mul)

    data = int(input("enter any number:"))

print(total1)
