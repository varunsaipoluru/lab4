l = [1,2,3,4,5,6,7,8]

def is_sorted(l):
	for i in range (0, len(l)):
		if i <= i+1:
			return "true"
		else:
			return "false"
print(is_sorted(l))

