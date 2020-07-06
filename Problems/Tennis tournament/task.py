n = int(input())
list_of_players = [input().split() for x in range(n)]
victories = [x[0] for x in list_of_players if x[1] == 'win']
print(victories)
print(len(victories))
