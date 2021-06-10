

def find_uppercase_letter():

    def find_uppercase_iterative(stri: str):
        for i in range(len(stri)):
            if stri[i].isupper():
                return stri[i]
        return "No uppercase character found"

    str_1 = "lucidProgramming"
    str_2 = "LucidProgramming"
    str_3 = "lucidprogramming"
    print("Iterative approach")
    print(find_uppercase_iterative(str_1))
    print(find_uppercase_iterative(str_2))
    print(find_uppercase_iterative(str_3))

    def find_uppercase_recursive(stri: str, idx=0):
        if stri[idx].isupper():
            return stri[idx]
        if idx == len(stri) - 1:
            return "No uppercase character found"
        return find_uppercase_recursive(stri, idx + 1)

    print("Recursive approach")
    print(find_uppercase_recursive(str_1))
    print(find_uppercase_recursive(str_2))
    print(find_uppercase_recursive(str_3))


def calculate_str_length():

    def calculate_str_len_recurseive(input_str):
        if input_str == "":
            return 0
        return 1 + calculate_str_len_recurseive(input_str[1:])

    input_str = "LucidProgramming"
    print(calculate_str_len_recurseive(input_str))


def main():
    calculate_str_length()


if __name__ == "__main__":
    main()
