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

# time comp: O(n)
# space comp: O(1)
def find_fixed_point_linear(A):  # todo: naive approach
    for i in range(len(A)):
        if A[i] == i:
            return A[i]
    return None

# time comp: O(logn)
# space comp: 0(1)
# * check the point is equal the index number, if it is return the number.
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
    low = 0
    high = len(A) - 1
    
    # Require at least 3 elements for a bitonic sequence.
    if len(A) < 3:
        return None
    
    while low <= high:
        mid = (low + high) // 2
        
        mid_left = A[mid - 1] if mid - 1 > 0 else float("-inf")
        mid_right = A[mid + 1] if mid + 1 < len(A) else float("inf")
        
        
        if mid_left < A[mid] and mid_right > A[mid]:
            low = mid + 1
        elif mid_left > A[mid] and mid_right < A[mid]:
            high = mid - 1
        elif mid_left < A[mid] and mid_right < A[mid]:
            return A[mid]
        
    return None
    
    
        

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
    
    A1 = [-10, -5, 0, 3, 7] #todo: fixed point is 3
    A2 = [0, 2, 5, 8, 17] #todo: fixed point is 0
    A3 = [-10, -5, 3, 4, 7, 9] #todo: fixed point is None
    
    print("Linear approach")
    print(A1)
    print(find_fixed_point_linear(A1))
    print(A2)
    print(find_fixed_point_linear(A2))
    print(A3)
    print(find_fixed_point_linear(A3))
    
    print("Binary search Approach")
    print(A1)
    print(find_fixed_point(A1))
    print(A2)
    print(find_fixed_point(A2))
    print(A3)
    print(find_fixed_point(A3))
    
    print("Find highest number")
    A = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    print(find_highest_number(A))
    A = [1, 6, 5, 4, 3, 2, 1]
    print(find_highest_number(A))
    A = [1, 2, 3, 4, 5]
    print(find_highest_number(A))
    A = [5, 4, 3, 2, 1]
    print(find_highest_number(A))
    

if __name__ == '__main__':
    main()
