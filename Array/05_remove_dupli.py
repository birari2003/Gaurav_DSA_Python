li = list(map(int, input().split()))
new_li = []
for i in li:
    if i not in new_li:
        new_li.append(i)
print(new_li)