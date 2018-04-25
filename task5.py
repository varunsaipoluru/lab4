l = ["big", "name", "happy", "hey", "give", "root", "doggy", "man", "sixer"]
def capitalize_nested(l):
	n= []
	for  str in l:
		n.append(str.upper())
	return n
		
print(capitalize_nested(l))
