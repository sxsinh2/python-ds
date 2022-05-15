"""from helper import *

user_input = ""
while user_input != "exit":
    user_input = input("pass number of days and conversion unit\n")
    days_and_unit = user_input.split(":")
    print(f"{days_and_unit} days and conversation unit ")
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(f"{days_and_unit_dictionary} dict ")
    days_to_hrs(days_and_unit_dictionary)
"""


import openpyxl as o
inv_file=o.load_workbook("inventory.xlsx")
product_list=inv_file["Sheet1"]
print(product_list)
product_per_supplier