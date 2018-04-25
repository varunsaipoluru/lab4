import collections

text='htjsdjnkjhsghhksgkh'
count=collections.Counter(text)

print(count.most_common())
# [('c', 5), ('b', 4), ('a', 2)]

print(''.join(letter*freq for letter,freq in count.most_common()))
