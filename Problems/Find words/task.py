sent = input().split()
lists = [str(x) for x in sent if str(x).endswith('s')]
print('_'.join(lists))
