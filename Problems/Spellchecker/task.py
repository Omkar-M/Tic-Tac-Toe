dictionary = {'all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain'}

sent = input()
sent_set = list(sent.split())
lists1 = []
lists = [x for x in sent_set if x not in dictionary]
print('\n'.join(lists))
if lists == lists1:
    print('OK')
