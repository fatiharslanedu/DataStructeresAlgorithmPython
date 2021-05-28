

def arrayAdvanceGame():

    def arrayAdvance(A):
        furthest_reached = 0
        last_idx = len(A) - 1
        i = 0
        while i <= furthest_reached and furthest_reached < last_idx:
            furthest_reached = max(furthest_reached, A[i] + i)
            i += 1
        return furthest_reached >= last_idx

    arrayA = [3, 3, 1, 0, 2, 0, 1]
    print(arrayAdvance(arrayA))


def arbitraryPrecisionIncrement():
    A1 = [1, 4, 9]
    A2 = [9, 9, 9]
    # todo: quick solve
    # s = "".join(map(str, A))
    # print(int(s) + 1)

    def plus_one(A):
        A[-1] += 1
        for i in reversed(range(1, len(A))):
            if A[i] != 10:  # After adding not overflow just break
                break
            A[i] = 0
            A[i - 1] += 1
        if A[0] == 10:
            A[0] = 1
            A.append(0)

        return A

    print(plus_one(A2))


def twoSum():

    def sol1(A, target):
        l = []
        for i in range(len(A)):
            for j in range(i, len(A)):
                if A[i] + A[j] == target:
                    l.append([A[i], A[j]])
                    print("(" + str(A[i]) + "," + str(A[j]) + ")")
                    return True
        return False

    def sol2(A, target):
        keep = {}
        for i in range(len(A)):
            if A[i] in keep:
                print(keep[A[i]], A[i])
                return True
            else:
                keep[target - A[i]] = A[i]

    def sol3(A, target):
        i = 0
        j = len(A) - 1
        while i < j:
            if A[i] + A[j] == target:
                print(A[i], A[j])
                return True
            elif A[i] + A[j] < target:
                i += 1
            else:
                j -= 1
        return False

    array1 = [-2, 1, 2, 4, 7, 11]
    target = 13
    print(sol3(array1, target))


def intersectSortedArray():
    A = [2, 3, 3, 5, 7, 8, 11, 9]
    B = [3, 3, 7, 15, 31, 8, 9]
    # print(set(A).intersection(B))

    def intersect_Sorted_Array(A: list, B: list): #todo: not sorted array greedy approach.
        j = 0
        i = 0
        intersectArray = list()
        A = list(set(A))
        B = list(set(B))
        # print(A,B)
        aSize = len(A)
        bSize = len(B)
        while i < aSize:

            if i is aSize - 1 or j is bSize - 1:
                if i is aSize - 1:
                    i = 0
                    j += 1
                else:
                    j = 0
                    i += 1
            if i >= aSize or j >= bSize - 1:
                break
            if A[i] == B[j]:
                intersectArray.append(A[i])
                i += 1
                j += 1
            else:
                if A[i] > B[j]:
                    j += 1
                elif B[j] > A[i]:
                    i += 1

        return intersectArray

    print(intersect_Sorted_Array(A, B))


def main():
    intersectSortedArray()


if __name__ == '__main__':
    main()
