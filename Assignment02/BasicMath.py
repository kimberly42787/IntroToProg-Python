


# Clean up the script
    # Most of the line of code can be consolidated into one or two line of code

print(
        """ 
                        Please enter two numbers below and this program will 
                    calculate them to give you the sum, difference, product, and 
                            the quotient. Numbers can contain decimals. 
                                            Thank you!!
        """
    )

# Instead of writing two addition lines of code to convert the string to a float, you can nest the input 
# function in the the float function
f_number = float(input("Enter your first number: ")) 
s_number = float(input("Enter your first number: "))

# Within the print function, I can calculate the two numbers by putting in the operations inside the print function
print("\nThe sum of", f_number, "and ", s_number, "is ", (f_number + s_number))
print("\nThe difference between", f_number, "and", s_number, "is", (f_number - s_number))
print("\nThe product of", f_number, "and", s_number, "is", (f_number * s_number))
print("\nThe quotient of", f_number, "and", s_number, "is", (f_number / s_number))



























