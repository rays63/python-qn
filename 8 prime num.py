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

if len(prim_num) >= 8:
    num = prim_num.index(cl_num)
    if even_input == 8:
        print(prim_num[num - 3: num + 5])
    elif even_input == 6:
        i = prim_num.index(cl_num)
        total = prim_num[i - 2: i + 6]
        print(total)
    elif even_input == 4:
        i = prim_num.index(cl_num)
        total = prim_num[i - 1: i + 7]
        print(total)
    elif even_input == 2:
        i = prim_num.index(cl_num)
        total = prim_num[i : i + 8]
        print(total)
    else:
        num = prim_num.index(cl_num)
        total = prim_num[num - 4:num + 4]
        print(total)
else:
    print('enter a valid even number')