# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost. 

# Start of the program

# Prices
HOT_DOG = 3.50
CHILI_DOG = 4.50
CHEESE = 0.50
PEPPERS = 0.75
GRILLED_ONIONS = 1.00
TAX_RATE = 0.07

# Select hot dog type
dog_choice = input("Enter type of hot dog (hotdog/chilidog): ").lower()
if dog_choice == "hotdog":
    dog_cost = HOT_DOG
elif dog_choice == "chilidog":
    dog_cost = CHILI_DOG
else:
    print("Invalid choice.")
    dog_cost = 0

# Select toppings
topping_cost = 0
if input("Do you want cheese? (yes/no): ").lower() == "yes":
    topping_cost += CHEESE
if input("Do you want peppers? (yes/no): ").lower() == "yes":
    topping_cost += PEPPERS
if input("Do you want grilled onions? (yes/no): ").lower() == "yes":
    topping_cost += GRILLED_ONIONS

# Calculate costs
subtotal = dog_cost + topping_cost
tax = subtotal * TAX_RATE
total = subtotal + tax

# Display results
print(f"Hot dog cost: ${dog_cost:.2f}")
print(f"Toppings cost: ${topping_cost:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total cost: ${total:.2f}")

# End of the program
