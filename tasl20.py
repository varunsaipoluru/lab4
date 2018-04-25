l = [(3, 'one'), (2, 'was'), (2, 'two'), (1, 'too'), (1, 'racehorse'), (1, 'a')]
l.sort(key=lambda x: x[1], reverse=True)
l.sort(key=lambda x: x[0])
print(l)
