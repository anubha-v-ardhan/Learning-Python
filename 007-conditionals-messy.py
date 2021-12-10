# Validating a user input

name_of_unit = "hours"
calculation_to_units = 24


def days_to_units(num_of_days):
    condition_check = num_of_days > 0
    print(type(condition_check))            # Just showing the data type is boolean here

    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
    elif num_of_days == 0:
        return "You entered a zero, please enter a valid positive number!"
    else:                                       # We don't need below check after using isdigit() check in line 22
        return "You entered a negative value, so no conversion for you!"



user_input = input("enter a number of days and I will convert it to hours!\n")

if user_input.isdigit():        # isdigit() will be False for negative number and float too
    user_input_number = int(user_input)
    calculated_value = days_to_units(user_input_number)
    print(calculated_value)
else:
    print("Your input is not a number, don't ruin my program")


# FINAL CLEAN CODE OF THIS IS IN FILE 007-conditionals.py
