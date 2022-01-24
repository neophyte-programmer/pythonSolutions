# Initialising Variables
college = None
college_answer = None
james_college = None
program_start = True

print("2021 MSU Undergraduate Tuition Calculator.\n")

# Placing program in a loop until answer is no
while program_start:
    level = input("Enter Level as freshman, sophomore, junior, senior: ").lower()

    # Verification Loop
    while not ((level == "freshman") or (level == "sophomore") or (level == "junior") or (level == "senior")):
        print("Invalid input. Try again.")
        level = input("Enter Level as freshman, sophomore, junior, senior: ").lower()
        if (level == "freshman") or (level == "sophomore") or (level == "junior") or (level == "senior"):
            break
    if (level == "junior") or (level == "senior"):
        college = input("Enter college as business, engineering, health, sciences, or none: ").lower()

    elif (level == "freshman") or (level == "sophomore"):
        college_answer = input("Are you admitted to the College of Engineering (yes/no): ").lower()

    if (college == "business") or (college == "engineering") or (college == "health") or (college == "sciences")\
            or (college_answer == "yes"):
        pass
    else:
        james_college = input("Are you in the James Madison College (yes/no): ").lower()

    school_credits = input("Credits: ")
    verify_credit = school_credits.isdigit()
    if verify_credit == True:
        credit_int = int(school_credits)

    # print(verify_credit)
    # Verification Loop for Letter
    while verify_credit == False:
        print("Invalid input. Try again.")
        school_credits = input("Credits: ")
        verify_credit = school_credits.isdigit()
        if verify_credit == True:
            credit_int = int(school_credits)
        if verify_credit == True:
            break

    # Verification Loop for 0
    while credit_int <= 0:
        print("Invalid input. Try again.")
        school_credits = input("Credits: ")
        verify_credit = school_credits.isdigit()
        if verify_credit == True:
            credit_int = int(school_credits)
        if credit_int > 0:
            break

# Calculations
    # Variables and Constants
    tuition_fee = 0

    regular_freshman = 0
    regular_sophomore = 0
    regular_junior = 0
    regular_senior = 0

    # be = business and engineering
    be_freshman = 0
    be_sophomore = 0
    be_junior = 0
    be_senior = 0

    all_undergrad_tax = 21
    radio_tax = 3   # all students
    news_tax = 5    # 6+ credits
    james_college_tax = 7.5     # students in james madison

    if credit_int <= 11:
        regular_freshman = 482
        regular_sophomore = 494
        regular_junior = 555
        regular_senior = 555

        be_freshman = 482
        be_sophomore = 494
        be_junior = 573
        be_senior = 573

    elif 12 <= credit_int <= 18:
        regular_freshman = 7230
        regular_sophomore = 7410
        regular_junior = 8325
        regular_senior = 8325

        be_freshman = 7230
        be_sophomore = 7410
        be_junior = 8595
        be_senior = 8595

    else:
        difference = credit_int - 18
        regular_freshman = 7230 + (difference * 482)
        regular_sophomore = 7410 + (difference * 494)
        regular_junior = 8325 + (difference * 555)
        regular_senior = 8325 + (difference * 555)

        be_freshman = 7230 + (difference * 482)
        be_sophomore = 7410 + (difference * 494)
        be_junior = 8595 + (difference * 573)
        be_senior = 8595 + (difference * 573)

    # Calculation for Freshman
    if level == "freshman":
        if college == "business" or college == "engineering":
            if credit_int <= 4:
                tuition_fee = be_freshman + radio_tax
                if college_answer == "yes":
                    tuition_fee += 402
            else:
                tuition_fee = be_freshman + all_undergrad_tax + radio_tax
                if credit_int >= 6:
                    tuition_fee += news_tax
                if college_answer == "yes":
                    tuition_fee += 670

        elif college == "health" or college == "sciences":
            if credit_int <= 4:
                tuition_fee = regular_freshman + radio_tax
            else:
                tuition_fee = regular_freshman + all_undergrad_tax + radio_tax
                if credit_int >= 6:
                    tuition_fee += news_tax
        elif james_college == "yes":
            if credit_int <= 4:
                tuition_fee = regular_freshman + radio_tax + james_college_tax
            else:
                tuition_fee = regular_freshman + all_undergrad_tax + radio_tax + james_college_tax
                if credit_int >= 6:
                    tuition_fee += news_tax
        else:
            if credit_int <= 4:
                tuition_fee = regular_freshman + radio_tax
            else:
                tuition_fee = regular_freshman + all_undergrad_tax + radio_tax
                if credit_int >= 6:
                    tuition_fee += news_tax

    # Calculation for Sophomore
    elif level == "sophomore":
        if college == "business" or college == "engineering":
            if credit_int <= 4:
                tuition_fee = be_sophomore + radio_tax
                if college_answer == "yes":
                    tuition_fee += 402
            else:
                tuition_fee = be_sophomore + all_undergrad_tax + radio_tax
                if credit_int >= 6:
                    tuition_fee += news_tax
                if college_answer == "yes":
                    tuition_fee += 670

        elif college == "health" or college == "sciences":
            if credit_int <= 4:
                tuition_fee = regular_sophomore + radio_tax
                if college_answer == "yes":
                    tuition_fee += 402
            else:
                tuition_fee = regular_sophomore + all_undergrad_tax + radio_tax
                if college_answer == "yes":
                    tuition_fee += 670
                if credit_int >= 6:
                    tuition_fee += news_tax

        elif james_college == "yes":
            if credit_int <= 4:
                tuition_fee = regular_sophomore + radio_tax + james_college_tax
                if college_answer == "yes":
                    tuition_fee += 402
            else:
                tuition_fee = regular_sophomore + all_undergrad_tax + radio_tax + james_college_tax
                if credit_int >= 6:
                    tuition_fee += news_tax
                    if college_answer == "yes":
                        tuition_fee += 670
        else:
            if credit_int <= 4:
                tuition_fee = regular_sophomore + radio_tax
                if college_answer == "yes":
                    tuition_fee += 402
            else:
                tuition_fee = regular_sophomore + all_undergrad_tax + radio_tax
                if credit_int >= 6:
                    tuition_fee += news_tax
                    if college_answer == "yes":
                        tuition_fee += 670

    # Calculation for Junior
    elif level == "junior":
        if college == "business" or college == "engineering":
            if credit_int <= 4:
                tuition_fee = be_junior + radio_tax
                if college_answer == "yes":
                    tuition_fee += 402
                if college == "business":
                    tuition_fee += 113
            else:
                tuition_fee = be_junior + all_undergrad_tax + radio_tax
                if credit_int >= 6:
                    tuition_fee += news_tax
                if college_answer == "yes":
                    tuition_fee += 670
                if college == "business":
                    tuition_fee += 226

        elif college == "health" or college == "sciences":
            if credit_int <= 4:
                tuition_fee = regular_junior + radio_tax + 50
                if college_answer == "yes":
                    tuition_fee += 402
            else:
                tuition_fee = regular_junior + all_undergrad_tax + radio_tax + 100
                if college_answer == "yes":
                    tuition_fee += 670
                if credit_int >= 6:
                    tuition_fee += news_tax

        elif james_college == "yes":
            if credit_int <= 4:
                tuition_fee = regular_junior + radio_tax + james_college_tax
                if college_answer == "yes":
                    tuition_fee += 402
            else:
                tuition_fee = regular_junior + all_undergrad_tax + radio_tax + james_college_tax
                if credit_int >= 6:
                    tuition_fee += news_tax
                    if college_answer == "yes":
                        tuition_fee += 670
        else:
            if credit_int <= 4:
                tuition_fee = regular_junior + radio_tax
                if college_answer == "yes":
                    tuition_fee += 402
            else:
                tuition_fee = regular_junior + all_undergrad_tax + radio_tax
                if credit_int >= 6:
                    tuition_fee += news_tax
                    if college_answer == "yes":
                        tuition_fee += 670
    # Calculation for Senior
    elif level == "senior":
        if college == "business" or college == "engineering":
            if credit_int <= 4:
                tuition_fee = be_senior + radio_tax
                if college_answer == "yes":
                    tuition_fee += 402
                if college == "business":
                    tuition_fee += 113
            else:
                tuition_fee = be_senior + all_undergrad_tax + radio_tax
                if credit_int >= 6:
                    tuition_fee += news_tax
                if college_answer == "yes":
                    tuition_fee += 670
                if college == "business":
                    tuition_fee += 226

        elif college == "health" or college == "sciences":
            if credit_int <= 4:
                tuition_fee = regular_senior + radio_tax + 50
                if college_answer == "yes":
                    tuition_fee += 402
            else:
                tuition_fee = regular_senior + all_undergrad_tax + radio_tax + 100
                if college_answer == "yes":
                    tuition_fee += 670
                if credit_int >= 6:
                    tuition_fee += news_tax

        elif james_college == "yes":
            if credit_int <= 4:
                tuition_fee = regular_senior + radio_tax + james_college_tax
                if college_answer == "yes":
                    tuition_fee += 402
            else:
                tuition_fee = regular_senior + all_undergrad_tax + radio_tax + james_college_tax
                if credit_int >= 6:
                    tuition_fee += news_tax
                    if college_answer == "yes":
                        tuition_fee += 670
        else:
            if credit_int <= 4:
                tuition_fee = regular_senior + radio_tax
                if college_answer == "yes":
                    tuition_fee += 402
            else:
                tuition_fee = regular_senior + all_undergrad_tax + radio_tax
                if credit_int >= 6:
                    tuition_fee += news_tax
                    if college_answer == "yes":
                        tuition_fee += 670

    # Print tuition fees with correct formatting
    print("Tuition is ${:,.2f}.".format(tuition_fee))

    # Restart Program
    user_continue = input("Do you want to do another calculation (yes/no): ").lower()
    if user_continue == "yes":
        program_start = True
    else:
        program_start = False
