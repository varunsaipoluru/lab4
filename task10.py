probability=1.0
cs=23
for i in range(cs):
	probability=(probability*(365-i))/365
	print("probability after excluding", i ,"student",  (probability))
"""print(probability)"""
