#  Method 1

def merge(arr1, arr2):
    arr1_size = len(arr1)
    arr2_size = len(arr2)
    if arr1_size == 0:
        return arr2
    if arr2_size == 0:
        return arr1
    # third array for returning sorted elements
    arr3 = [0] * (arr1_size + arr2_size)
    i, j, k = 0, 0, 0
    # looping over the both the arrays
    while(i < arr1_size and j < arr2_size):
        # if first array element is smaller
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            i += 1
        # if second array element is smaller
        else:
            arr3[k] = arr2[j]
            j += 1
        k += 1
    # executes copying if remaining elements are from array 1
    while i < arr1_size:
        arr3[k] = arr1[i]
        i += 1
        k += 1
    # executes copying if remaining elements are from array 2
    while j < arr2_size:
        arr3[k] = arr2[j]
        k += 1
        j += 1

    return arr3

#  Method 2

def merge_mod(arr1, arr2):
    arr1_size = len(arr1)
    arr2_size = len(arr2)
    if arr1_size == 0:
        return
    if arr2_size == 0:
        return
    # looping from back of second array
    for i in range(arr2_size - 1, -1, -1):
        # setting pointer for first array
        j = arr1_size - 2
        # saving the last element
        last = arr1[arr1_size - 1]
        # looping over the first array and shifting the elements
        while j >= 0 and arr2[i] < arr1[j]:
            arr1[j + 1] = arr1[j]
            j -= 1
        # now, the position is found, then just putting elements in appropriate positions
        if j != arr1_size - 2 and last > arr2[i]:
            arr1[j + 1] = arr2[i]
            # everytime last will change, as arr1 is modified
            arr2[i] = last



# main driver function

if __name__ == '__main__':
    assert merge([1, 5, 9, 10, 15, 20], [2, 3, 8, 13]) == [1, 2, 3, 5, 8, 9, 10, 13, 15, 20]
    assert merge([], [2, 3, 8, 13]) == [2, 3, 8, 13]
    assert merge([1, 5, 9, 10, 15, 20], []) == [1, 5, 9, 10, 15, 20]
    assert merge([1, 5, 9, 9, 10, 15, 20, 20, 20], [2, 3, 8, 8, 10, 10, 13, 13]) == [1, 2, 3, 5, 8, 8, 9, 9, 10, 10, 10, 13, 13, 15, 20, 20, 20]
