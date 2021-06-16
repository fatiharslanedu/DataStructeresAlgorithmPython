
def find_uppercase_letter():

    def find_uppercase_iterative(input_str):
        for i in range(len(input_str)):
            if input_str[i].isupper():
                return input_str[i]
        return "No uppercase character found"

    str_1 = "lucidProgramming"
    str_2 = "LucidProgramming"
    str_3 = "lucidprogramming"
    print("Iterative approach")
    print(find_uppercase_iterative(str_1))
    print(find_uppercase_iterative(str_2))
    print(find_uppercase_iterative(str_3))

    def find_uppercase_recursive(input_str: str, idx=0):
        if input_str[idx].isupper():
            return input_str[idx]
        if idx == len(input_str) - 1:
            return "No uppercase character found"
        return find_uppercase_recursive(input_str, idx + 1)

    print("Recursive approach")
    print(find_uppercase_recursive(str_1))
    print(find_uppercase_recursive(str_2))
    print(find_uppercase_recursive(str_3))


def calc_string_length():

    def calc_string_length_recursive(input_str: str):
        if input_str == '':
            return 0
        return 1 + calc_string_length_recursive(input_str[1:])

    input_str = "LucidProgramming"
    print(calc_string_length_recursive(input_str))

def count_consanants_strings():
    vowels = "aeiou"
    def recurcive_count_consanants(input_str: str):
        if input_str == '':
            return 0
        if input_str[0].lower() not in vowels and input_str[0].isalpha():
            return 1 + recurcive_count_consanants(input_str[1:])
        else:
            return recurcive_count_consanants(input_str[1:])
    print(recurcive_count_consanants('Lucid programming'))

def main():
    count_consanants_strings()


if __name__ == "__main__":
    main()
