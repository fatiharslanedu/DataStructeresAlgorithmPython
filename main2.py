# write your code here

def split(string: str) -> list:
    return [x for x in string]


def reformat(string: list) -> list:
    list1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    k = 0
    for i in range(3):
        for j in range(3):
            list1[i][j] = string[k]
            k += 1

    return list1


def check(string: list):
    result = list()
    start_point = 0
    # check rows
    for i in range(3):
        if string[i].count('X') == 3:
            result.append('X wins')
        if string[i].count('O') == 3:
            result.append('O wins')
    # check cols
    for i in range(3):
        for j in range(start_point, start_point + 7, 3):
            print(string[j])

def main():
    string = split(input("Enter cells: "))
    string = reformat(string)
    print(check(string))

    print("---------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(string[i][j], end=" ")
        print("|", end="\n")
    print("---------")


if __name__ == "__main__":
    main()
