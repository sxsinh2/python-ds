list = [1, 4, 5, 13, 44, 55, 23, 22, 63, 12]
search_str = input("enter the num to search for. \n")
search_num = int(search_str)
sorted_list = sorted(list)
print(sorted_list)
list_len = len(sorted_list)
if sorted_list[0] == search_num:
    print("answer is 0")
elif sorted_list[-1] == search_num:
    print(f"answer is {list_len}")
else:
    lo = 1
    hi = list_len-1
    while lo < hi:
        mid = int((lo+hi) / 2)
        print(f"lo={lo} mid={mid} hi={hi}")
        if search_num == sorted_list[mid]:
            print(f"answer is {mid}")
            break
        elif search_num > sorted_list[mid]:
            lo = mid
        else:
            hi = mid







