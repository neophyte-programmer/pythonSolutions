import math

print("Welcome to Horizons car rentals.")
print("At the prompts, please enter the following: ")
print("\tCustomer's classification code (a character: BD, D, W) ")
print("\tNumber of days the vehicle was rented (int)")
print("\tOdometer reading at the start of the rental period (int)")
print("\tOdometer reading at the end of the rental period (int)")

user_start = input("Would you like to continue (A/B)? ")


while user_start == "A":
    customer_code = input("Customer code (BD, D, W): ")
    while not(customer_code == "BD" or customer_code == "D" or customer_code == "W"):
        print("Wrong input")
        customer_code = input("Customer code (BD, D, W): ")
        if customer_code == "BD" or customer_code == "D" or customer_code == "W":
            break

    rental_days = int(input("Number of days: "))
    o_start = int(input("Odometer reading at the start: "))
    o_end = int(input("Odometer reading at the end: "))

    # Actual logic
    amount_due = 0
    miles_driven = (o_end - o_start) / 10
    base_charge = 0
    mileage_charge = 0
    avg_daily = miles_driven / rental_days
    weeks = (rental_days / 7)

    if customer_code == "BD":
        base_charge = 40.00 * rental_days
        mileage_charge = 0.25 * miles_driven

    elif customer_code == "D":
        base_charge = 60.00 * rental_days
        if avg_daily <= 100:
            mileage_charge = 0
        else:
            mileage_charge = 0.25 * (avg_daily - 100)
    
    elif customer_code == "W":
        base_charge = 190.00 * weeks





    print("\nCustomer summary: ")
    print("\tclassification code:", customer_code)
    print("\trental period (days):", rental_days)
    print("\todometer reading at start:", o_start)
    print("\todometer reading at end:", o_end)
    print("\tamount due:", amount_due)

    user_start = input("Would you like to continue (A/B)? ")

else:
    print("Thank you for your loyalty.")

