seq = input()
list_digit = [int(x) for x in seq]
length = len(list_digit)
cu_list = [sum(list_digit[0:x:1]) for x in range(1, length + 1)]
print(cu_list)
