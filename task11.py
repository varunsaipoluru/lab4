from collections import OrderedDict
def remove_duplicates():
	print(list(OrderedDict.fromkeys('1,2,3,4,5,6,6,3,2,1,5,6,4,3,2')))
remove_duplicates()
