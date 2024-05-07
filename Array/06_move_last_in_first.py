li = list(map(int, input().split()))
temp = []
temp.append(li[-1])
for i in li:
    temp.append(i)
temp.pop()
print(temp)


    