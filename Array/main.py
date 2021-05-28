

def arrayAdvanceGame():
    A = [3, 2, 0, 0, 2, 0, 1]
    A1 = [3, 3, 1, 0, 2, 0, 1]

    def arrayAdvance(A):
        furthest_reached = 0
        last_idx = len(A) - 1
        i = 0
        while i <= furthest_reached and furthest_reached < last_idx:
            furthest_reached = max(furthest_reached, A[i] + i)
            i += 1

        return furthest_reached >= last_idx

    print(arrayAdvance(A1))


def arbitraryPrecisionIncrement(): #todo: done

    def func1(A):
        A[-1] += 1
        for i in reversed(range(1, len(A))):
            if A[i] != 10:
                break

            A[i] = 0
            A[i - 1] += 1
        if A[0] == 10:
            A[0] = 1
            A.append(0)

        return A
    
    A = [1, 4, 9]
    print(func1(A))
    
    
def twoSum():
    #? Time Complexity: O(n^2)
    #? Space Complexity: O(1)
    def sol1(A, target):
        for i in range(len(A)):
            for j in range(i, len(A)):
                if A[i] + A[j] == target:
                    print(A[i], A[j])
                    return True
        return False
    
    A = [-2, 1, 2, 4, 7, 11]
    print(sol1(A, 13))
    
    #? Time Complexity: O(n)
    #? Space Complexity: O(n)    
    def sol2(A, target):
        keep = {}
        for i in range(len(A)):
            if A[i] in keep:
                print(keep[A[i]], A[i])   
                keep[target - A[i]] = A[i]           
            else:
                keep[target - A[i]] = A[i]
        
        return keep
    A = [-2, 1, 2, 4, 7, 11]
    print(sol2(A, 13))
    
    #? Time Complexity: O(n)
    #? Space Complexity: O(1)
    def sol3(A, target):
        j = len(A) - 1
        i = 0
        while i < j:
            if A[i] + A[j] == target:
                print(A[i], A[j])
                return True
            elif A[i] + A[j] < target:
                i += 1
            else:
                j += 1
        return False
            
    A = [-2, 1, 2, 4, 7, 11]
    print(sol3(A, 13))       

def optimalTaskAssignment():
    
    def sol(A: list):
        A = sorted(A)
        hours = []
        j = len(A) - 1
        for i in range(len(A) // 2):
            hours.append(A[i] + A[j])
            j -= 1
        return hours
    
    def greedysol(A: list):
        A = sorted(A)
        for i in range(len(A) // 2):
            print(A[i], A[~i]) #! this start the end
    
    A = [6, 3, 2, 7, 5, 5]
    print(sol(A))
    print(greedysol(A))
    
def intersectSortedArray():
    A = [2, 3, 3, 5, 7, 8, 11, 9]
    B = [3, 3, 7, 15, 31, 8, 9]
    # print(set(A).intersection(B))
    
    def intersect_Sorted_Array(A: list, B: list):
        j = 0
        i = 0
        intersectArray = list()
        while i < len(A) and j < len(B):
           
            if A[i] == B[j]:
                if A[i] == B[j] and A[i] != A[i - 1]:
                    intersectArray.append(A[i])
                i += 1
                j += 1
                
            elif A[i] < B[j]:
                i += 1
            else:
                j += 1
                
        return intersectArray
                
            
            
    
    print(intersect_Sorted_Array(A,B))
                
        

def main():
    intersectSortedArray()

if __name__ == '__main__':
    main()
