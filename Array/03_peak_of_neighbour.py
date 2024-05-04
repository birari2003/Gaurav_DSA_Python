arr = list(map(int, input().split()))
for i in range(0, len(arr)):
    if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
        print(f"The element is {arr[i]} and its index is {i}")
