# input() # input is a function provided by python itself
# input("Hey user, enter a number of days and I will convert it to hours!\n")

# IMPORTANT
# note that input() always returns String value

name_of_unit = "hours"
calculation_to_units = 24


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}" # return in a function 


user_input = input("enter a number of days and I will convert it to hours!\n")
user_input_number = int(user_input)                 # casting String [given by input()] to int
calculated_value = days_to_units(user_input_number)
print(calculated_value)
