#Yes i know list.extend() exists. It doesnt work on my machine. I have no clue why. I have no intention on figuring it out.
def combineList(a, b, pivot): 
	if(b == None or a == None):
		return []
	a.append(pivot)
	for i in b:
		a.append(i)
	return a

def partitionSort(l):

	if(len(l) == 0):
		return []
	
	left, right = [], []
	pivot = l[-1]
	l.pop(-1)

	for i in l:
		if(i < pivot):
			left.append(i)
		else:
			right.append(i)

	return combineList(partitionSort(left), partitionSort(right), pivot)


print(f'List: {partitionSort([0, 2, 1, 4, 5, 3, 6, 9, 8, 7])}')
