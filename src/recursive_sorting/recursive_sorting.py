# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    a = 0
    b = 0

    #Loop over merged array
    for i in range (0, elements):
        #If a is bigger or equal put but bth item or arrB IN MERGED_ARRAY
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        #If b is bigger or equal put ath item in Merged Array
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    length = len(arr)
    if length < 2:
        return arr

    #Find middle using length divided by 2
    middle = length // 2
    #left hand side is everything left of middle
    lhs = arr[:middle]
    #right hand side is everything right of middle
    rhs = arr[middle:]

    # Run Merge taking in lhs sort and right hand sort as args
    return merge(merge_sort(lhs), merge_sort(rhs))


print(merge_sort([3,7,9,0,3,6,7,2]))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
