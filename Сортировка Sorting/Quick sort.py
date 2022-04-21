import random


a=[1,23,546,324,67,43,67,324,6,8,3,23,456,546,87,789,46,423,67,786,432,54,76,796]
min_ = []
max_ = []
mid_ = []
def sort(ar):
	if len(ar)<2:
		return(ar)
	min_ = []
	max_ = []
	mid_ = []
	c=random.choice(ar)		
	for i in ar:
		if i>c:
			max_.append(i)
		if i<c:
			min_.append(i)		
		if i==c:
			mid_.append(i)

	return(sort(min_)+mid_+sort(max_))

print(sort(a))