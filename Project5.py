#1-10 table 12 rows

#step-1: setting values
max_value = 1
no_of_repetitions = 1

#step 2: creating iterations using nested while
while max_value <= 10:
    print("Table of",max_value)
    while no_of_repetitions <= 12:
        value = max_value * no_of_repetitions
        print(max_value,"*",no_of_repetitions,"=",value)
        no_of_repetitions += 1
    print("")
    no_of_repetitions = 1
    max_value += 1