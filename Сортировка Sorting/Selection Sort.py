with open("No_sort_stuff.txt")as f:
    no_sort=f.read()
no_sort=no_sort.split(",")
no_sort=[int(item) for item in no_sort]

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort(no_sort))

#Алгоритм находит наименьшее число из неотсортированной части и помещает его в конец отсортированной.