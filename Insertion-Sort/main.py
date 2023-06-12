def insertion_sort(arr):
    for i in range(1, len(arr)):
        value = arr[i]
        sort = i - 1
        while sort >= 0 and arr[sort] > value:
            arr[sort + 1] = arr[sort]
            sort = sort - 1
        arr[sort + 1] = value
    return arr
