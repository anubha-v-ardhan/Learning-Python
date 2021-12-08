# Variable scope means where the variable used in function is defined
#   Global Scope: variables available from within any scope (calculation_to_units, _name_of_unit)
#                   (can be from completely different file too)
#   Local Scope: variables created inside funtion (num_of_days, custom_message)
#                   (only available inside funtion)

calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days, custom_message):    # def used to define a function
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")
    print(custom_message)


def scope_check():
    print(name_of_unit)
    # print(num_of_days) => This will give error num_of_days not defined as its local scope


def variable_inside_function():
    my_var = "variable inside function"
    print(my_var)


days_to_units(20, "Awesome!")
days_to_units(35, "Looks good!")
days_to_units(40, "aha")
days_to_units(110, "Awesome!") 

scope_check(20)
variable_inside_function()