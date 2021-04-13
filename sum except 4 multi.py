data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
sum = [n for n in data if n%4]
total1 = 0
for i in sum:
    total1 += i
print(f"The sum is {total1}")
