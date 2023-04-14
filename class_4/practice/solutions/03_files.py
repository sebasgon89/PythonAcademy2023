# 1
#check in the IDLE the function input ()

### --> Read a string from standard input
# 2
# create a function that returns zero or the number entered by the user

def func2():
    val = input("ingrese un numero: ")
    if val.isdigit():
        return int(val)
    else:
        return 0

# 3
# create another function that returns the value passed by parameter multiplied by itself

def func3(param):
    return param * param

# 4
# Now create the main function that calls the function from step 3 with the result of the function from step 2.
# and print the result


def main():
    print (func3(func2())) # 1
    print (func3(func2())) # 2
    print (func3(func2())) # 3
    

# 5
# create the sintax to call the main function

if __name__ == "__main__":
    main()
