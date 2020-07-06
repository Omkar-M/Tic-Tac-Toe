ht = int(input())
space = [' ' for x in range(ht - 1)]

i = 1
while ht > 0:
    calc = "#" * i
    print(''.join(space) + calc)
    ht -= 1
    i += 2
    if ' ' in space:
        space.remove(' ')
