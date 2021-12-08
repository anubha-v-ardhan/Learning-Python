to_units = 24 * 60 * 60   # we don't define data type in Python
                            # note the variable naming convention
                            # we cannot use reserved words as variable names (search python reserved words)

name_of_unit = "seconds"

print(f"20 days are {20 * to_units} {name_of_unit}")