l = [1,2,3,4,5,6]
def cumulative_sum(l):
	n=[]
	for i in range (0, len(l)):
		sum=0
		for j in range (0, i+1):
			sum = sum + l[j]
		n.append(sum)	
	return n
print(cumulative_sum(l))

		
