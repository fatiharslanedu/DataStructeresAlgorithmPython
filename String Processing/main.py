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

def main():
    # todo: 1
    # print(next_number('13112221'))
    # todo: 2
    print(spreadsheet_encode_column("ZZ"))
    # todo 3
    s = "was it a cat I saw?"
    s = ''.join([i for i in s if i.isalnum()]).replace(' ', '').lower()
    print(s == s[::-1])
    s = "was it a cat I saw?"
    print(is_palindrome(s))
    


if __name__ == "__main__":
    main()
