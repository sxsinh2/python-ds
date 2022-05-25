# Enter your code here. Read input from STDIN. Print output to STDOUT
import re


def validate_credi_cards(c_num):

    str2 = c_num.replace("-", "")

    if len(str2) != 16 or re.search("^![4-6]", str2) or re.findall("\D", str2) or len(re.findall("-", c_num)) not in [0, 3]:
        return "Invalid"
    elif re.search(".*([0-9])\\1{3}.*", str2):
        print("repear")
        return "Invalid"
    else:
        print("in else")
        if len(re.findall("-", c_num)) == 3:
            for each_four in c_num.split("-"):
                print(f"in each_four {each_four}")
                if len(each_four) != 4:
                    return "Invalid"
            return "Valid"
        else:
            return "Valid"


numofinputs = input("enter the num of credit cards to validate \n")
inp_count = int(numofinputs)
for i in range(0, inp_count):
    testcc = input("enter the cc num")
    print(testcc)
    retval = validate_credi_cards(testcc)
    print(retval)
