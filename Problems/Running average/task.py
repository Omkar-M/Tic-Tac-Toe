numbers = input()
numbers_list = [int(i) for i in list(numbers)]
print([(numbers_list[i] + numbers_list[i + 1]) / 2 for i in range(len(numbers) - 1)])
