import math

print("Welcome to Horizons car rentals.")

print("\n\nAt the prompts, please enter the following: ")
print("\tCustomer's classification code (a character: BD, D, W) ")
print("\tNumber of days the vehicle was rented (int)")
print("\tOdometer reading at the start of the rental period (int)")
print("\tOdometer reading at the end of the rental period (int)")

PROMPT = '''\nWould you like to continue (A/B)? '''
n = input(PROMPT)

while n == 'A':
    Customer_code = '''Customer code (BD, D, W): '''
    c = input(Customer_code)
    while not(c == "BD" or c == "D" or c == "W"):
        print("Wrong input")
        Customer_code = '''Customer code (BD, D, W): '''
        c = input(Customer_code)
        if c == "BD" or c == "D" or c == "W":
            break

    n_str = int(input("Number of days: "))

    Odometer_start = '''Odometer reading at the start: '''
    o = input(Odometer_start)

    Odometer_end = '''Odometer reading at the end:   '''
    e = input(Odometer_end)

    miles_driven = (e - o) / 10

    mileage_charge = 0
    base_charge = 0
    avg_daily = (miles_driven * n_str) / n_str
    week = math.ceil(n_str / 7)
    avg_weekly = (miles_driven * week) / week

    if c == "BD":
        base_charge = 40.00 * n_str
        mileage_charge = 0.25 * miles_driven

    elif c == "D":
        base_charge = 60.00 * n_str

        if avg_daily <= 100:
            mileage_charge = 0
        else:
            mileage_charge = 0.25 * miles_driven
    elif c == "W":
        base_charge = 190.00 * week

        if avg_weekly <= 900:
            mileage_charge = 0
        elif avg_weekly > 900 and avg_weekly <= 1500:
            mileage_charge = 100.00



    print("\nCustomer summary:")
    print("\tclassification code:", c)
    print("\trental period (days):", n_str)
    print("\todometer reading at start:", o)
    print("\todometer reading at end:  ", e)

if n != 'A':
    print("Thank you for your loyalty.")
