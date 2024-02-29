"""
Name: Logan Roman
Lab time: 2:00 Thurs
"""

def process_user_contacts(user_input):
    user_contacts = {'Emergency Services':911} #I assumed this should be the dictionary, but I needed a key and value to start.


    user_input = str(user_input).split()
    user_input = [str(user_input[i]).split(",")for i in range(0,len(user_input))]
    tokens = [user_input[i][1] for i in range(0,len(user_input))]
    user_input = [user_input[i][0] for i in range(0,len(user_input))]

    # Put word pairs into a dictionary
    for i in range(0,len(user_input)):
        user_contacts[user_input[i]]=tokens[i]
    
    # Get contact name from input, output contact's phone number
    contact_name = input("Enter the contact name: ")
    if contact_name in user_contacts:
        print(user_contacts[contact_name])
    else:
        print("Contact not found.")
    
   
if __name__ == '__main__':
    # Get input for word pairs
    user_input = input("Enter word pairs (name, phone number): ")

    # Call the function to process user contacts
    process_user_contacts(user_input)
