with open("No_sort_stuff.txt")as f:
    no_sort=f.read()
no_sort=no_sort.split(",")
no_sort=[int(item) for item in no_sort]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        current_value = arr[i]
        j = i - 1
        while j >= 0:
            if current_value < arr[j]:
                arr[j+1] = arr[j]
                arr[j] = current_value
                j = j - 1
            else:
                break
    return arr

print(insertion_sort(no_sort))

#Как и в сортировке выбором представляем последовательность как две части: первая включает отсортированные элменты, вторая — неотсортированные. Алгоритм сортировки вставками последовательно помещает каждый элемент из неотсортированной части на правильную позицию отсортированной части.