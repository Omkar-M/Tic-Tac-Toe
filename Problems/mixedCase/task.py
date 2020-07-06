words = input().split()
print("".join([words[0]] + [word.capitalize() for word in words[1:]]))
