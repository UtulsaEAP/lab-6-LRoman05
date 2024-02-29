"""
Name: Logan Roman
Lab time: 2:00 Thurs
"""

def filter_and_print_range(input_list, min_val, max_val):
    #write your code here
    extra_list = []
    for i in range(0,len(input_list)):
        if (min_val<=input_list[i]<=max_val):
            extra_list.append(input_list[i])
    out_string =""
    for i in range(0,len(extra_list)):
        out_string+=str(extra_list[i])+","
    print(out_string)

if (__name__ == '__main__'):
    # Get input for the list of integers
    user_input = input("Enter a space-separated string of numbers: ")
    integer_list = [int(user_input.split()[i])for i in range(0,len(user_input.split()))]

    # Get input for the range (min and max values)
    user_input = input("Enter the min and max values separated by a space: ")
    min_val, max_val = int(user_input.split()[0]),int(user_input.split()[1])

    # Call the function to filter and print the numbers in the given range
    filter_and_print_range(integer_list,min_val,max_val)
   
