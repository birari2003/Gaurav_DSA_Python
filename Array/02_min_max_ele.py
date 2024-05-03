li = list(map(int, input().split()))
min = li[0]
max = li[0]
for i in li:
    if i > max:
        max = i
    elif i < min:
        min = i
print(f"Minimum value is {min} and maximum value is {max}")
