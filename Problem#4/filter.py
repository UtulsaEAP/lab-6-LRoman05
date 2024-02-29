"""
Name: Logan Roman
Lab time: 2:00 Thurs
"""

def process_and_print(input_string):
      # Split into separate strings

    # Convert strings to integers and filter out negative values
  input_data = [int(str(input_string).split()[i]) for i in range(0,len(str(input_string).split()))]
  filter_data= []
  for i in range(0,len(input_data)):
    if(input_data[i]<0):
      filter_data.append(input_data[i])
    # Sort integers in reverse order
  filter_data = sorted(filter_data)

    # Print sorted integers
  output_data = ""
  for i in range(len(filter_data)-1,-1,-1):
      output_data+=str(filter_data[i])+" "
  print(output_data)
         

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function to process and print the result
    process_and_print(user_input)
