def next_number(num):
    if 1 <= num <= 9:
        return num
    else:
        total = 0
        while num > 0:
            total += num % 10
            num //= 10
    return total


number = int(input())
sequence = [next_number(int(str(number)[: i + 1])) for i in range(len(str(number)))]
print(sequence)
