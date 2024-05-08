li = [1,5,7,-1]
k = 6
count = 0
for i in li:
    li.remove(i)
    for j in li:
        if (i+j)==k:
            count += 1
print(count)

