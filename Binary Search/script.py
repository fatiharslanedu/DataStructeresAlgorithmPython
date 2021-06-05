def binary_search_iterative(data, target):  # todo: O(logn)
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

def binary_search_recursive(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_recursive(data, target, low, mid - 1)
        else:
            return binary_search_recursive(data, target, mid + 1, high)


def find_closest_num(A, target):
    min_diff = float("inf")
    low = 0
    high = len(A) - 1
    closest_num = None
    
    # Edge case for empty list of list with only one element:
    if len(A) == 0:
        return None
    if len(A) == 1:
        return A[0]
    
    while low <= high:
        mid = (low + high) // 2
        
        # Ensure you do not read beyond the bounds of the list.
        if mid + 1 < len(A):
            min_diff_right = abs(A[mid + 1] - target)
        if mid > 0:
            min_diff_left = abs(A[mid - 1] - target)
            
        # Check if the absolute value between left and right elements
        # are right elements are smaller than any senior element.
        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = A[mid - 1]
            
        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = A[mid + 1]
            
        # Move the mid-point appropriately as is done via binary search.
        if A[mid] < target:
            low = mid + 1
        elif A[mid] > target:
            high = mid - 1
            if high < 0:
                return A[mid]
            
        # If the element itself is the target, the closest number
        # to it is itself. Return the number.
        else:
            return A[mid]
    return closest_num
            
    
def main():    
    data = [1, 3, 5, 7, 11, 15]
    target = 1
    # print(binary_search_iterative(data, target))
    
    data1 = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
    target1 = 37
    # print(binary_search_recursive(data1, target1, 0, len(data1) - 1))

    A1 = [1, 2, 4, 5, 6, 6, 8, 9]
    A2 = [2, 5, 6, 7, 8, 8, 9]
    
    print(find_closest_num(A1, 11))
    print(find_closest_num(A2, 4))


if __name__ == '__main__':
    main()