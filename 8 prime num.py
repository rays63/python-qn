even_input = int(input("Enter even number range: "))
upper = even_input + 30
prim_num = []
# upper = int(input("Enter upper range: "))

for num in range(even_input - even_input, upper):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            prim_num.append(num)


def closest(lst, K):
    return lst[min(range(len(lst)), key=lambda i: abs(lst[i] - K))]


cl_num = closest(prim_num, even_input)
print(cl_num)

if len(prim_num) >= 8:
    num = prim_num.index(cl_num)
    if even_input == 8:
        print(prim_num[num - 3: num + 5])
    elif even_input == 6:
        print(prim_num[num - 2: num + 6])
    elif even_input == 4:
        print(prim_num[num - 1: num + 7])
    elif even_input == 2:
        print(prim_num[num : num + 8])
    else:
        print(prim_num[num - 4: num + 4])
else:
    print('enter a valid even number')
