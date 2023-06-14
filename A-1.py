total = 0

with open('data.txt', 'r') as file:
    for line in file:
        try:
            number=int(line)
        except ValueError as e:
            continue
        total += int(line)

print("合計:", total)
