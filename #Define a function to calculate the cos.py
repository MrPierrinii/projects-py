# Define a function to calculate the cost of house cleaning
def calculate_house_cleaning_cost(num_rooms, num_bathrooms, senior_discount=False):
    base_cost = 100 # base cost for cleaning a house
    cost_per_room = 25 # additional cost per room
    cost_per_bathroom = 20 # additional cost per bathroom
    total_cost = base_cost + (num_rooms * cost_per_room) + (num_bathrooms * cost_per_bathroom)
    if senior_discount:
        total_cost *= 0.9 # apply 10% discount for seniors
    return total_cost

# Define a function to calculate the cost of yard service
def calculate_yard_service_cost(square_footage, linear_footage, num_shrubs, senior_discount=False):
    cost_per_square_foot = 0.25 # cost per square foot for mowing
    cost_per_linear_foot = 0.10 # cost per linear foot for edging
    cost_per_shrub = 5 # cost per shrub for pruning
    total_cost = (square_footage * cost_per_square_foot) + (linear_footage * cost_per_linear_foot) + (num_shrubs * cost_per_shrub)
    if senior_discount:
        total_cost *= 0.9 # apply 10% discount for seniors
    return total_cost

# Define a function to calculate the discount
def calculate_discount():
    is_senior = input("Are you a senior? (Y/N)").lower() == 'y'
    if is_senior:
        return 0.1 # apply 10% discount for seniors
    else:
        return 0

# Define the main function to prompt the user for the service and calculate the cost
def main():
    # Prompt the user for the type of service they want
    service_choice = input("What service do you want? (house cleaning/yard service)").lower()
    # Keep prompting until the user enters a valid choice
    while service_choice not in ['house cleaning', 'yard service']:
        service_choice = input("Invalid choice. What service do you want? (house cleaning/yard service)").lower()

    # If the user chose house cleaning
    if service_choice == 'house cleaning':
        # Prompt the user for the number of rooms and bathrooms
        num_rooms = int(input("How many rooms do you have?"))
        num_bathrooms = int(input("How many bathrooms do you have?"))
        # Calculate the senior discount, if applicable
        senior_discount = calculate_discount()
        # Calculate the total cost of the service
        total_cost = calculate_house_cleaning_cost(num_rooms, num_bathrooms, senior_discount)
    # If the user chose yard service
    elif service_choice == 'yard service':
        # Prompt the user for the square footage, linear footage, and number of shrubs
        square_footage = int(input("What is the square footage of your yard?"))
        linear_footage = int(input("What is the linear footage of your yard's edges?"))
        num_shrubs = int(input("How many shrubs do you have?"))
        # Calculate the senior discount, if applicable
        senior_discount = calculate_discount()
        # Calculate the total cost of the service
        total_cost = calculate_yard_service_cost(square_footage, linear_footage, num_shrubs, senior_discount)

    # Print the total cost of the service
    print("The total cost of the {} service is ${:.2f}".format(service_choice, total_cost))

# Call the main function
if __name__ == '__main__':
    main()
