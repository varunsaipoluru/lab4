import functools
def sum_even(l, u):
	mylist = []
	for i in range(l,u):
		if i % 2 ==0:
			mylist.append(i)
	return functools.reduce(add,mylist)

def add(x,y):
	return x+y

print(sum_even(100, 500))
