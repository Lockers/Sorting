# TO-DO: Complete the selection_sort() function below 

def selection_sort( arr ):
    # loop through n-1 elements

    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 

        for k in range(cur_index, len(arr)):
            if arr[k] < arr[smallest_index]:
                smallest_index = k
        
        # TO-DO: swap
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
    
    return arr

# TO-DO:  implement the Bubble Sort function below

def bubble_sort( arr ):
    # Set Number of iterations to take away from loop length
    iterations = 0

    # Set if swapped or not for while loop
    swapped = True

    # While swapped is true keep looping over list and look for swaps
    while(swapped):

        # Set swapped to False so loop ends if no swaps are found
        swapped = False

        # Loop over list to look for swaps, swap them if there are and set Swapped to True
        for j in range(len(arr) - iterations - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # Each iteration add 1 so can take away from length of list so dont need so many passes as biggest numbers end up at end sorted        
        iterations += 1            
    return arr

array = [9, 5, 4, 3, 2, 100, 200]
print(array)
bubble_sort(array)
print(array)



# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr