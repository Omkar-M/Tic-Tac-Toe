seq = input().split()
x = input()
count = 0
con = True
lists = []
i = 0
for y in seq:
    if y == x:
        lists.insert(i, str(count))
        con = False
        i += 1
    count += 1
print(' '.join(lists))
if con:
    print('not found')
