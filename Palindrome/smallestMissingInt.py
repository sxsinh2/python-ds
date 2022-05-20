def get_different_number(arr):
    sorted_arr = sorted(arr)
    for i in range(0, len(sorted_arr) - 1):
        if sorted_arr[i + 1] - sorted_arr[i] > 1:
            retval = sorted_arr[i] + 1
            print(retval)
            return retval


get_different_number([0,1,2,3,4,5,9,10,13])