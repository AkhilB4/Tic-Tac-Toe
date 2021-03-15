n = int(input())
victories = []
while n > 0:
    match = input()
    if 'win' in match:
        victories.append(match[: match.find('win') - 1])
    n -= 1
print(victories)
print(len(victories))
