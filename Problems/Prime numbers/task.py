# prime_numbers = [x for x in range(2, 1000) for y in range(2, x) if x % y != 0]
# for x in prime_numbers:
#     for y in range(2, x):
#         if x % y == 0:
#             print(x)
#             prime_numbers.remove(x)
#             break
# lists = []
# for x in range(2,1000):
#     for y in range(2,x):
#         if any(x % y == 0):
#             continue
#         else:
#             lists.append(x)
# prime_numbers = lists

prime_numbers = [n for n in range(2, 1001) if all(n % i != 0 for i in range(2, n - 1))]
