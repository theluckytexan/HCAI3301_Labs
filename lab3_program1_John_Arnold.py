""" Rental Program: Old VHS and New VHS
Program outputs questions of how many new and used videos
then asks for how many nights and calculates total
background price assigned by management for and used
Try and except if user enters an input besides an integer."""

neWVhs_price = 3.00
olDVhs_price = 2.00

try:
    # Assign inputs from clerk
    neWVhs_total = int(input("Enter the number of New VHS videos: "))
    olDVhs_total = int(input("Enter the number of Classic VHS videos: "))
    totaLPer_night = int(input("Enter the number of nights rented: "))
    #adding in code for sale need total amount of VHS for algorithm
    totaL_Vhs = neWVhs_total + olDVhs_total


    # Calculate the total cost
    totaL_Cost = ((neWVhs_total * neWVhs_price) + (olDVhs_total * olDVhs_price)) * totaLPer_night

    #if total vhs is 10 or higher, or the cost is 50+ then total cost is 80%. else total cost is the same
    if totaL_Vhs >= 10 or totaL_Cost >= 50:
        totaL_Cost = totaL_Cost * 0.8
    else : totaL_Cost = totaL_Cost

    # Display Cost in dollars to Clerk
    print(f"The total rental cost is: ${totaL_Cost:.2f}")

except ValueError:
    # Incase of input that isn't and integer
    print("Invalid input. Please enter a whole number for the video counts.")

    #one problem I have with this is the cost cant be above 50 without having the total vhs above 10
    #I think I would need to add something into it to charge for candy then to test it with that.