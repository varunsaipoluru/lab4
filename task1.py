def nested_sum(t):
	sum = 0
	for element in t:
		if type(element) == list:
			sum = sum + nested_sum(element)
		else:
			sum = sum + element
	return sum 



t = [[4,2,4],[5,6,7],[5,6,7]]
print(nested_sum(t))
