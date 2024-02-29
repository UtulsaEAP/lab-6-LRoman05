"""
Name: Logan Roman
Lab time: 2:00 Thurs
"""

def process_input(input_string):
      # Split into separate strings
  main_list = str(input_string).split()

    # Convert strings to floats
  for i in range(0,len(main_list)):
     main_list[i]=float(main_list[i])

    # Get max and average
  max_value = max(main_list)
  average_value = sum(main_list)/len(main_list)
  return max_value, average_value

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function and get the results
    max_value, average_value = process_input(user_input)

    print(f'Max Value: {max_value:.2f}')
    print(f'Average Value: {average_value:.2f}')
