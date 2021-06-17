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
    s = "was it a cat I saw?"
    s = ''.join([i for i in s if i.isalnum()]).replace(' ', ' ').lower()
    print(s == s[::-1])    
    s = "Was it a cat I saw?"
    print(is_palindrome(s))
    
    
if __name__ == "__main__":
    main()