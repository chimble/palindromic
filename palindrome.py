#NormalModeBOYZ
newstring = ''
string_gnirts = ''
def compare_elements(a, b):
    if a == b:
        return True
    else:
        return False

def is_palindrome(newstring):
    newstring = stringer(newstring)
    for character in newstring:
        if character == newstring[-1:]:
            newstring = newstring[1:-1]
            if len(newstring) <=1:
                return True
            continue
        else:
            return False

# def is_palindrome(newstring):
#     newstring = stringer(newstring)
#     if len(newstring) == 0:
#         print("is palindrome")
#         return True
#     else:
#         if compare_elements(newstring[0], newstring[-1:]):
#             newstring = newstring[1:-1]
#             return is_palindrome(newstring)
#         else:
#             print("is not palindrome")
#             return False
def main():

    string_gnirts = input("give me word/sentence please ")
    #string_gnirts = stringer(string_gnirts)
    print(is_palindrome(string_gnirts))

def stringer(string_gnirts):
    newstring = ''
    for character in string_gnirts:
        if character.isalpha() == True:
            newstring += character.lower()
            string_gnirts = string_gnirts[1:]
        else:
            string_gnirts = string_gnirts[1:]
    return newstring


if __name__ == "__main__":
    main()

#string_to_test[1:-1]
# is_palindrome(newstring)
