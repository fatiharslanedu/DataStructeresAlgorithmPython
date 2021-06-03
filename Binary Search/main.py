def binary_search_iterative(data, target): #todo: this take O(logn)
    low = 0
    high = len(data) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

data = [1, 3, 5, 8, 11, 13, 15]
target = 3
print(binary_search_iterative(data, target))

def binary_search_recursive(data, target, low, high):
    if low > high:
        return False
    mid = (low + high) // 2
    if data[mid] == target:
        return True
    elif target < data[mid]:
        return binary_search_recursive(data, target, low, mid - 1)
    else:
        return binary_search_recursive(data, target, mid + 1, high)
    

data = [1, 3, 5, 8, 11, 13, 15]
target = 12
print(binary_search_recursive(data,target, 0, len(data) - 1))