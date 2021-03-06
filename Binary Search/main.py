import bisect


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

def find_fixed_point_linear(A):
    for i in range(len(A)):
        if A[i] == i:
            return A[i]
        
    return None


def find_fixed_point(A):
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = (low + high) // 2
        if A[mid] < mid:
            low = mid + 1
        elif A[mid] > mid:
            high = mid - 1
        else:
            return A[mid]
    return None


def find_highest_number(A):
    # initalize the value for binary search...
    low = 0
    high = len(A) - 1

    # if we want to find bitonic sequence, array must be 3 elements.
    if len(A) < 3:
        return None
    
    while low <= high:
        mid = (low + high) // 2
        
        # define a variable like a boss
        # check if the value is not out of index. 
        mid_left = A[mid - 1] if mid - 1 > 0 else float("-inf")
        # check the right is not out of bound.
        mid_right = A[mid + 1] if mid + 1 < high else float("inf")
        
        if mid_left < A[mid] and mid_right > A[mid]:
            low = mid + 1
        elif mid_left > A[mid] and mid_right < A[mid]:
            high = mid - 1
        elif mid_left < A[mid] and mid_right < A[mid]:
            return A[mid]
    
    return None
        
def find(A, target):
    low = 0
    high = len(A) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if target < A[mid]:
            high = mid - 1
        elif target > A[mid]:
            low = mid + 1
        else: #todo: if A[mid] == target...
            if mid - 1 < 0:
                return mid
            if A[mid - 1] != target:
                return mid
            high = mid - 1
    return None        

def integer_square_root(k: int) -> int:
    low = 0
    high = k
    
    while low <= high:
        mid = (low + high) // 2
        mid_squared = mid * mid
        #todo: sequence like k is equal to 5 => 1, 4
        if mid_squared <= k:
            low = mid + 1
        else:
            high = mid - 1
    return low - 1
      
        
        
def main():
    
    data = [1, 3, 5, 8, 11, 13, 15]
    target = 12
    print(binary_search_recursive(data,target, 0, len(data) - 1))

    data = [1, 3, 5, 8, 11, 13, 15]
    target = 3
    print(binary_search_iterative(data, target))
    
    data = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    target = 108
    print(find(data, target))
    
    print("Bisect Left")
    A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    print(bisect.bisect_left(A, 108))
    print(bisect.bisect_left(A, 285))
    print("Bisect Right")
    print(bisect.bisect_right(A, -10))
    print(bisect.bisect_right(A, 285))
    print("Insort Left and Right")
    print(A)
    bisect.insort_left(A, 108)
    print(A)
    bisect.insort_right(A, 108)
    print(A)
    print("\nInteger Square Root\n")
    print(integer_square_root(300))

if __name__ == '__main__':
    main()