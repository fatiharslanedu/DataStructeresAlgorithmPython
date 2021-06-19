'''
111221 is read of as "three 1s, two 2s, then one 1" or 312211
'''


def next_number(s):
    result = []
    i = 0
    count = 1
    s = [int(x) for x in s]
    print(s)
    while i < len(s):  # todo: better than edu. O(n)
        if i == len(s) - 1:
            result.append(count)
            result.append(s[i])
        elif s[i] == s[i + 1]:
            count += 1
        elif s[i] != s[i + 1]:
            result.append(count)
            result.append(s[i])
            count = 1
        i += 1
    result = [str(x) for x in result]
    return ''.join(result)


def spreadsheet_encode_column(col_str):
    upper = len(col_str) - 1
    num = 0
    for i in col_str:
        num += 26**upper * (ord(i) - ord('A') + 1)
        upper -= 1
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


def is_anagram(s1: str, s2: str) -> bool:
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
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


def is_perm_1(str1: str, str2: str):
    str1, str2 = str1.lower(), str2.lower()

    if len(str1) != len(str2):
        return False

    str1 = ''.join(sorted(str1))
    str2 = ''.join(sorted(str2))

    n = len(str1)

    for i in range(n):
        if str1[i] != str1[i]:
            return False

    return True


def is_perm_2(str1: str, str2: str):
    str1, str2 = str1.lower(), str2.lower()
    d = dict()

    for i in str1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    for i in str2:
        if i in d:
            d[i] -= 1
        else:
            return False

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


def main():
    # todo: 1
    # print(next_number('13112221'))
    # todo: 2
    # print(spreadsheet_encode_column("ZZ"))
    # todo 3
    '''
    s = "was it a cat I saw?"
    s = ''.join([i for i in s if i.isalnum()]).replace(' ', '').lower()
    print(s == s[::-1])
    s = "was it a cat I saw?"
    print(is_palindrome(s))
    '''
    # todo 4
    '''
    s1 = "William Shakespeare"
    s2 = "I am a weakish speller"
    print(is_anagram(s1, s2))
    '''
    # todo 5
    is_permutation_1 = "google"
    is_permutation_2 = "ooggle"

    not_permutation_1 = "not"
    not_permutation_2 = "top"
    print(is_perm_1(is_permutation_1, is_permutation_2))
    print(is_perm_1(not_permutation_1, not_permutation_2))

    print(is_perm_2(is_permutation_1, is_permutation_2))
    print(is_perm_2(not_permutation_1, not_permutation_2))


if __name__ == "__main__":
    main()
