# 1
#check in the IDLE the function input ()
n = int(input)

# 2
# create a function that returns zero or the number entered by the user
def func_zero(n);
    return(int(n))

# 3
# create another function that returns the value passed by parameter multiplied by itself
def func_mult(n):
    return n*n

# 4
# Now create the main function that calls the function from step 3 with the result of the function from step 2.
# and print the result
def main():
    return(func_mult(func_zero))

# 5
# create the sintax to call the main function
if __name__ == "__main__": main()


