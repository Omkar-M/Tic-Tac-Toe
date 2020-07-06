word = input().split('_')
lists = []
for x in word:
    x = x.lower().capitalize()
    lists.append(x)
print(''.join(lists))
