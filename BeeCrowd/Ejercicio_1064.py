count = 0
total = 0

for _ in range(6):
    num = float(input())
    if num > 0:
        count += 1
        total += num

print(f"{count} valores positivos")
print(f"{total / count:.1f}")
