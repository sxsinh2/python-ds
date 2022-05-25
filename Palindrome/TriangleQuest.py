inp_str = input()
try:
    inp = int(inp_str)
    print(inp)
    if inp < 1 or inp > 9:
        print("invalid")

    for i in range(inp):
        for j in range(1,i+1):
            print(i,end='')
        print('')
except ValueError:
    print("invalid")