"""
Name: Logan Roman
Lab time: 2:00 Thurs
"""

def calculate_car_wash_price(service_choice1, service_choice2):
    services = {'Air freshener': 1, 'Rain repellent': 2, 'Tire shine': 2, 'Wax': 3, 'Vacuum': 5}
    base_wash = 10
    total = 0
   
   #type your code here
    print("ZyCar Wash")
    print(f"Base car wash - ${base_wash}")
    total += base_wash
    if service_choice1!="-":
        print(f"{service_choice1} - ${services.get(service_choice1)}")
        total += services.get(service_choice1)
    if service_choice2!="-":
        print(f"{service_choice2} - ${services.get(service_choice2)}")
        total += services.get(service_choice2)
    print("-----\nTotal price: $%d" %(total))

    
if __name__ == '__main__':
    # Get user input for service choices
    service_choice1 = input("Enter first service choice: ")
    service_choice2 = input("Enter second service choice: ")

    # Call the function to calculate car wash price
    calculate_car_wash_price(service_choice1, service_choice2)
