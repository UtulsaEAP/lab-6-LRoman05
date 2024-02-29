"""
Name: Logan Roman
Lab time: 2:00 Thurs
"""

def check_palindrome(user_input):
 #type your code here
    mod_input = user_input.split()
    sans_input =""
    is_palindrome = True
    for i in range(0,len(mod_input)):
        sans_input+=str(mod_input[i])
    for i in range(0,len(sans_input)//2):
        if sans_input[i] != sans_input[-i-1]:
            is_palindrome = False
    if (is_palindrome == True):
        print("palindrome: "+user_input )
    else:
        print("not a palindrome: "+user_input)

if __name__ == "__main__":
    user_input = input()
    check_palindrome(user_input)
