def binary_search(arr, key):
    """
    Binary search algorithm to search for the key in a sorted array.
    Returns the index of the array's element that is equal to the value of the search key,
    or -1 if the element is not in the array.
    """
    begin = 0
    end = len(arr) - 1
    
    while begin <= end:
        mid = (begin + end) // 2
        
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            begin = mid + 1
        else:
            end = mid - 1
    
    return -1


