# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(len(arr)):
        min = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for n in range(i+1, len(arr)):
            if arr[min] > arr[n]:
                min = n
                
        # TO-DO: swap 
        stash = arr[i]
        arr[i] = arr[min]
        arr[min] = stash

    return arr
             
# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    for i in range(len(arr)-1,0,-1):

      #Loop over i in range
       for n in range(i):

           #Compare n with number to right
           if arr[n] > arr[n+1]:

               #swap is number to right is bigger
               stash = arr[n]
               arr[n] = arr[n+1]
               arr[n+1] = stash

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr