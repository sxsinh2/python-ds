import datetime



var_input = input("enter your goal with the deadline separated by colon. \n")
input_list = var_input.split(":")
dict_input = {"goal": input_list[0], "deadline": input_list[1]}
deadline_str = dict_input["deadline"]
print(deadline_str)
deadline_date=datetime.datetime.strptime(deadline_str,"%d.%m.%Y")
timedelta=deadline_date-datetime.datetime.today()
print(timedelta)