
def days_to_hrs(days_and_unit_dictionary):
    try:
        user_input_num = int(days_and_unit_dictionary["days"])
        user_unit = days_and_unit_dictionary["unit"]
        mul_factor = 1
        if user_unit == "hours":
            mul_factor = 24
        elif user_unit == "min":
            mul_factor = 60*60
        elif user_unit == "sec":
            mul_factor = 60*60*60
        if user_input_num > 0:
            print(f"{user_input_num} days are {user_input_num * mul_factor} {user_unit}")
        else:
            print("negative num")

    except ValueError:
        print("not a valid num of days")