# STRETCH: implement Linear Search				
def linear_search(data, thing):
    for i in data:
        if i == thing:
            return i
        else:
            x = 'Thing not found'
    return x


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(data, thing):
    middle = (int(len(data) / 2))
    if len(data) == 1:
        if thing != data[middle]:
            print(f'{thing} not found')
            
    if thing == data[middle]:
        print(f'Found {thing}')
        

    if thing < data[middle]:
        s = slice(int(middle))
        data = data[s]
        binary_search_recursive(data, thing)
    elif thing > data[middle]:
        s = slice(int(middle), int(len(data)))
        data = data[s]
        binary_search_recursive(data, thing)

print(binary_search_recursive([2, 3, 4, 6, 8, 9], 4))
