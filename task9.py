
def is_anagram(l1,l2):
	l1=list(l1)
	l1.sort()
	l2=list(l2)
	l2.sort()
	return (l1==l2)
print (is_anagram("ear","are"))
