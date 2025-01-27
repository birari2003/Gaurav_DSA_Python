arr = [1,-1,3,5,-3,3]
count = 0
for i in range(len(arr)):
    if arr[i] > 0:
        count += arr[i]
print(count)