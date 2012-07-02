male = False
female = False

while not male and not female:
    print "What is your gender? (Male/Female)"

    gender = raw_input()
    
    if gender == "Male":
        male = True
    elif gender == "Female":
        female = True
    else:
        print "Please enter Male or Female"

if male or female:
    print "You entered a valid gender"
    if male:
        print "You are male"
    else:
        print "You are female"
