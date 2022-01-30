with open("No_sort_stuff.txt")as f:
	no_sort=f.read()
no_sort=no_sort.split(",")
no_sort=[int(item) for item in no_sort]

def bubble_sort(ar):
	n=len(ar)
	for i in range(n):
		for j in range(n-i-1):
			if ar[j]>ar[j+1]:
				ar[j],ar[j+1]=ar[j+1],ar[j]
	return ar
sort=bubble_sort(no_sort)
print(sort)
#Сортировка пузырьком проходит по массиву несколько раз. На каждом этапе алгоритм сравнивает два соседних элемента и, если левый элемент больше правого — меняет их местами.
