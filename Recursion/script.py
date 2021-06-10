


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
    
    def find_uppercase_recursive(stri: str, idx = 0):
        if stri[idx].isupper():
            return stri[idx]
        if idx == len(stri) - 1:
            return "No uppercase character found"
        return find_uppercase_recursive(stri, idx + 1)
        
    print("Recursive approach")
    print(find_uppercase_recursive(str_1))
    print(find_uppercase_recursive(str_2))
    print(find_uppercase_recursive(str_3))



def main():
    find_uppercase_letter()


if __name__ == "__main__":
    main()