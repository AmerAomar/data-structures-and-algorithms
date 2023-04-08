def insertShiftArray(array: list, value: object):   
    middle = (len(array) + 1) // 2        # Calculate the middle index using ceil division
    
    array.append(None)                    # Append a None value to the end of the array
    
    for i in range(len(array) - 1, middle, -1):    # Shift the values in the array to the right of the middle by one position
        array[i] = array[i - 1]

    array[middle] = value  # Insert the new value at the middle

    return array
