with open("No_sort_stuff.txt")as f:
    no_sort=f.read()
no_sort=no_sort.split(",")
no_sort=[int(item) for item in no_sort]

def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    else:
        middle = int(len(arr) / 2)
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    if len(left) > 0:
        result += left
    if len(right) > 0:
        result += right
    return result

print(merge_sort(no_sort))

#Рекурсивный алгоритм, который работает по следующему принципу:
#Разделить массив на две равные части
#Отсортировать каждую половину
#Из двух отсортированных массивов получить один (операция слияния)
