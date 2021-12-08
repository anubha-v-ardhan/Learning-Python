to_units = 24 * 60 * 60   # we don't define data type in Python
                            # note the variable naming convention
                            # we cannot use reserved words as variable names (search python reserved words)

name_of_unit = "seconds"

print(f"20 days are {20 * to_units} {name_of_unit}")
print(f"30 days are {30 * to_units} {name_of_unit}")
print(f"45 days are {45 * to_units} {name_of_unit}")
print(f"110 days are {110 * to_units} {name_of_unit}")