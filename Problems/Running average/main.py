number = input()
avg_list = []
for i in range(len(number) - 1):
    x = (int(number[i]) + int(number[i + 1])) / 2
    avg_list.append(x)
print(avg_list)
