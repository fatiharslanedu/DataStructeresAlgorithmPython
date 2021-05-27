

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

def main():
    arrayAdvanceGame()


if __name__ == '__main__':
    main()
