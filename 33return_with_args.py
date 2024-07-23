def palindrome():
    string = input("enter a string :")
    rev_string = string[::-1]
    if string == rev_string:
        print("palindrome")
        return None        
  
    else:
        print("not palindrome")
        return None        
ok = palindrome()
print(ok)



