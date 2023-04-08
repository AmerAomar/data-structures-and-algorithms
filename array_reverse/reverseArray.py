def reverseArray(array):
    new_array = []
    for x in range(len(array)):
        new_array.append(array[len(array)-1 -x])
    return new_array