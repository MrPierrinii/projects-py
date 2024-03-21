# Assignment Week #4 
# The program computes the cost of house cleaning based on the number of rooms and type of cleaning selected.
#Also, prompts the user for the number of rooms in the house and whether the cleaning should be a light cleaning or a more complete one.
# Then, it calculates the cost of cleaning the house based on the user's inputs and outputs the final cost.

# Define the cutoffs for small, medium, and large number of rooms
SMALL_HOUSE = 1   # houses with 1 or fewer rooms are considered small
MEDIUM_HOUSE = 3  # houses with 2 or 3 rooms are considered medium

# Define the prices for each house size
SMALL_HOUSE_PRICE = 50    # $50 for a small house
MEDIUM_HOUSE_PRICE = 100  # $100 for a medium house
LARGE_HOUSE_PRICE = 150   # $150 for a large house

# Define the prices for each type of cleaning
FLOOR_PRICE = 25      # $25 surcharge for floors
WINDOW_PRICE = 15     # $15 surcharge for windows
BATHROOM_PRICE = 30   # $30 surcharge for bathrooms
DUSTING_PRICE = 20    # $20 surcharge for dusting

# Define a function that computes the cost of cleaning a house based on its size and the type of cleaning
def compute_cost(num_rooms, cleaning_type):
    if num_rooms <= SMALL_HOUSE:
        house_size = "small"
        cost = SMALL_HOUSE_PRICE
    elif num_rooms <= MEDIUM_HOUSE:
        house_size = "medium"
        cost = MEDIUM_HOUSE_PRICE
    else:
        house_size = "large"
        cost = LARGE_HOUSE_PRICE

    if cleaning_type == 1:
        cleaning_name = "floors"
        cleaning_price = FLOOR_PRICE
    elif cleaning_type == 2:
        cleaning_name = "windows"
        cleaning_price = WINDOW_PRICE
    elif cleaning_type == 3:
        cleaning_name = "bathrooms"
        cleaning_price = BATHROOM_PRICE
    else:
        cleaning_name = "dusting"
        cleaning_price = DUSTING_PRICE

    total_cost = cost + cleaning_price  # compute the total cost
    return total_cost   # return the total cost

# Prompt the user for the number of rooms in the house
num_rooms = int(input("Enter the number of rooms in the house: "))

# Prompt the user for the type of cleaning
print("Types of cleaning:")
print("1. Floors ($25)")
print("2. Windows ($15)")
print("3. Bathrooms ($30)")
print("4. Dusting ($20)")
cleaning_type = int(input("Enter the type of cleaning (1-4): "))

# Compute the cost of cleaning the house using the function
total_cost = compute_cost(num_rooms, cleaning_type)

# Output the cost of house cleaning based on the number of rooms and the type of cleaning
print("The cost of cleaning a", house_size, "house with", num_rooms, "rooms and", cleaning_name, "is $", total_cost)
