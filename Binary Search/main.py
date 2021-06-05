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
    

def find_closest_num(A, target):
    min_diff = float('inf')
    low = 0
    high = len(A) - 1
    closest_num = None
    
    if len(A) == 0:
        return None
    if len(A) == 1:
        return A[0]
    
    while low <= high:
        mid = (low + high) // 2
        
        if mid + 1 < len(A):
            min_diff_right = abs(A[mid + 1] - target)
        if mid > 0:
            min_diff_left = abs(A[mid - 1] - target)
            
        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = A[mid - 1]
            
        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = A[mid + 1]
            
        if A[mid] < target:
            low = mid + 1
        elif A[mid] > target:
            high = mid - 1
            if high < 0:
                return A[mid]
        else:
            return A[mid]
        
    return closest_num


def main():
    
    data = [1, 3, 5, 8, 11, 13, 15]
    target = 12
    print(binary_search_recursive(data,target, 0, len(data) - 1))

    data = [1, 3, 5, 8, 11, 13, 15]
    target = 3
    print(binary_search_iterative(data, target))


if __name__ == '__main__':
    main()