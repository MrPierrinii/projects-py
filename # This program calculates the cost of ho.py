# This program calculates the cost of house cleaning or yard service based on user input.
# If the user selects house cleaning, the program prompts for the number of rooms and bathrooms, and calculates the cost of cleaning the house.
# If the user selects yard service, the program prompts for the square footage, linear footage, and number of shrubs, and calculates the cost of yard service.
# The program also prompts the user to indicate whether they are a senior, and applies a discount if applicable.
# The output of the program is the total cost of the requested service.

# Define the cost of house cleaning for different house sizes
# Small house: up to 2 rooms and 1 bathroom - $100
# Medium house: up to 3 rooms and 2 bathrooms - $150
# Large house: 4 or more rooms or 3 or more bathrooms - $200 + $50 surcharge for complete cleaning

# Define a function to calculate the cost of house cleaning
def calculate_house_cleaning_cost(num_rooms, num_bathrooms, senior_discount=False):
    # Define the base cost for cleaning a house
    base_cost = 0
    # Define the cost per room and per bathroom
    cost_per_room = 25
    cost_per_bathroom = 20
    # Determine the base cost for different house sizes
    if num_rooms <= 2 and num_bathrooms == 1:
        base_cost = 100
    elif num_rooms <= 3 and num_bathrooms <= 2:
        base_cost = 150
    elif num_rooms >= 4 or num_bathrooms >= 3:
        base_cost = 200
    # Determine the surcharge for a more complete cleaning based on the number of rooms and bathrooms
    if num_rooms >= 4 or num_bathrooms >= 3:
        cleaning_surcharge = 50
    else:
        cleaning_surcharge = 0
    # Calculate the total cost of cleaning the house
    total_cost = base_cost + (num_rooms * cost_per_room) + (num_bathrooms * cost_per_bathroom) + cleaning_surcharge
    # Apply the senior discount, if applicable
    if senior_discount:
        total_cost *= 0.9 # apply 10% discount for seniors
    return total_cost

# Define a function to calculate the cost of yard service
def calculate_yard_service_cost(square_footage, linear_footage, num_shrubs, senior_discount=False):
    # Define the cost per square foot for mowing, the cost per linear foot for edging, and the cost per shrub for pruning
    cost_per_square_foot = 0.25
    cost_per_linear_foot = 0.10
    cost_per_shrub = 5
    # Calculate the total cost of yard service
    total_cost = (square_footage * cost_per_square_foot) + (linear_footage * cost_per_linear_foot) + (num_shrubs * cost_per_shrub)
    # Apply the senior discount, if applicable
    if senior_discount:
        total_cost *= 0.9 # apply 10% discount for seniors
    return total_cost

# Define a function to determine the discount for seniors
def calculate_discount():
    # Determine if the user is a senior
    is_senior = input("Are you a senior? (Y/N)").lower() == 'y'
    # Define the senior discount as a percentage
    senior_discount = 0.1 # 10% discount for seniors
    # Return the discount as either 0
