def square_sum(l, u):
	sum = 0 
	for i in range(l, u):
		if i % 2 ==0:
			sum += (2 * i) * (2 * i)
	
	return sum

print(square_sum(1,10))
