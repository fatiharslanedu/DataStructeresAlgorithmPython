def next_number(s):
    result = []
    i = 0

    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            i += 1
            count += 1
        result.append(str(count) + s[i])
        i += 1
    return "".join(result)


def spreadsheet_encode_column(col_str):
    num = 0
    upper = len(col_str) - 1
    for i in col_str:
        num += 26**upper * (ord(i) - ord('A') + 1)
        upper -= upper
    return num


def is_palindrome(s: str):
    i = 0
    j = len(s) - 1
    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1

        if s[i].lower() != s[j].lower():
            return False

        i += 1
        j -= 1
    return True


def is_anagram(s1: str, s2: str):
    ht = dict()

    if len(s1) != len(s2):
        return False

    for i in s1:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1

    for i in s2:
        if i in ht:
            ht[i] -= 1
        else:
            ht[i] = 1

    for i in ht:
        if ht[i] != 0:
            return False
    return True


def is_palin_perm(input_str: str):
    input_str = input_str.replace(" ", "").lower()

    d = dict()

    for i in input_str:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    odd_count = 0

    for k, v in d.items():
        if v % 2 != 0 and odd_count == 0:
            odd_count += 1
        elif v % 2 != 0 and odd_count != 0:
            return False
    return True

# Time Complexity: O(n log n)
# Space Complexity: O(1)


def is_perm_1(str_1: str, str_2: str):
    str_1 = str_1.lower()
    str_2 = str_2.lower()

    if len(str_1) != len(str_2):
        return False

    str_1 = "".join(sorted(str_1))
    str_2 = "".join(sorted(str_2))

    n = len(str_1)

    for i in range(n):
        if str_1[i] != str_2[i]:
            return False
    return True


def is_perm_2(str_1: str, str_2: str):
    str_1 = str_1.lower()
    str_2 = str_2.lower()

    d = dict()

    for i in str_1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    for i in str_2:
        if i in d:
            d[i] -= 1
        else:
            return False
    print(d)
    return all(value == 0 for value in d.values())


def is_unique(input_str: str):
    input_str = input_str.lower()
    d = dict()
    for i in input_str:
        if i in d:
            return False
        else:
            d[i] = 1

    return True


def is_unique_2(input_str: str):
    return len(set(input_str)) == len(input_str)


def is_unique_3(input_str: str):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in input_str:
        if i in alpha:
            alpha = alpha.replace(i, "")
        else:
            return False
    return True

def int_to_str(input_int):
    
    if input_int < 0:
        is_negative = True
        input_int *= -1
    else:
        is_negative = False
        
    output_str = []
    if input_int == 0:
        output_str.append('0')
    else:
        while input_int > 0:
            output_str.append(chr(ord('0') + input_int % 10))
            input_int //= 10
        output_str = output_str[::-1]
    
    output_str = ''.join(output_str)
    
    if is_negative:
        return '-' + output_str
    else:
        return output_str
    
    
def main():
    # todo 1
    '''
    s = "1"
    print(s)
    n = 4
    for i in range(n - 1):
        s = next_number(s)
        print(s)
    '''
    # todo 2
    '''
    print(ord("A") - ord("A") + 1)
    print(ord("Z") - ord("A") + 1)
    print(spreadsheet_encode_column("ZZ"))
    '''
    # todo 3
    '''
    s = "was it a cat I saw?"
    s = ''.join([i for i in s if i.isalnum()]).replace(' ', ' ').lower()
    print(s == s[::-1])    
    s = "Was it a cat I saw?"
    print(is_palindrome(s))
    '''
    # todo 4 Anagram
    '''
    s1 = "fairy tales"
    s2 = "rail safety"
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    print(sorted(s1) == sorted(s2))
    print(is_anagram(s1, s2))
    '''
    # todo 5
    '''
    palin_perm = "Tact Coa"
    not_palin_perm = "This is not a palindrome permutation"
    print(is_palin_perm(palin_perm))
    print(is_palin_perm(not_palin_perm))
    is_permutation_1 = "google"
    is_permutation_2 = "ooggle"

    not_permutation_1 = "not"
    not_permutation_2 = "top"
    print(is_perm_1(is_permutation_1, is_permutation_2))
    print(is_perm_1(not_permutation_1, not_permutation_2))

    print(is_perm_2(is_permutation_1, is_permutation_2))
    print(is_perm_2(not_permutation_1, not_permutation_2))
    '''
    # todo 6 is Unique
    '''
    string = "abCDefGh"
    string2 = "nonunique"
    print(is_unique(string))
    print(is_unique(string2))
    print(is_unique_3(string))
    '''
    # todo 7 int to str
    input_int = 123
    print(input_int)
    print(type(input_int))

    output_str = int_to_str(input_int)
    print(output_str)
    print(type(output_str))

if __name__ == "__main__":
    main()
