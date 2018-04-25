def square_sum(l, u):
	sum = 0 
	for i in range(l, u):
		if   i % 2 ==0:
			sum = sum + i**2
	
	return sum

print(square_sum(1,10))
