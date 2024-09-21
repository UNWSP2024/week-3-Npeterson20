# Programming Excersize 3-13

# The Fast Freight Shipping Company charges the following rates:

# Weight    	Price Per Pound
# 2 pounds or less   	$1.50
# Over 2 pounds but not more than 6 pounds  	$3.00
# Over 6 pounds but not more than 10 pounds	$4.00
# Over 10 pounds	$4.75
# Write a program which calculates the shipping charge and displays the total.

def weight_conversion(weight):
    # Calculate the shipping charge.
    shippingCost = 0.0
    ######################
    # WRITE YOUR CODE HERE
    # Start of the program
weight = float(input("Enter the package weight in pounds: "))

if weight <= 2:
    rate = 1.50
elif 2 < weight <= 6:
    rate = 3.00
elif 6 < weight <= 10:
    rate = 4.00
else:
    rate = 4.75

shipping_charge = rate * weight
print(f"The shipping charge is: ${shipping_charge:.2f}")
# End of the program

    
    return shippingCost

#### This piece of the code has been done for you,
#### you only need to worry about the actual shipping 
#### charge logic in the weight_conversion function
if __name__ == '__main__':
    # Local variables
    weight = 0.0
    shippingCost = 0.0
    # Get package weight from the user.
    weight = float(input('Enter the weight of the package: '))
    # Display the shipping charge.
    shippingCost = weight_conversion(weight)
    print ('Shipping charge: $', format(shippingCost, '.2f'))
