# used to avoid repeating the same logic
calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days, custom_message):    # def used to define a function
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")
    print(custom_message)


days_to_units(20, "Awesome!")
days_to_units(35, "Looks good!")
days_to_units(40, "aha")
days_to_units(110, "Awesome!")

# days_to_units() => this will give error now