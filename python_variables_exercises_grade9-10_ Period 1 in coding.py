"""
PYTHON VARIABLES — EXERCISES (GRADE 9-10 / INTERMEDIATE)
==========================================================
Complete each exercise where you see:
    # YOUR CODE HERE

A few exercises use input(). If you'd rather not type input while
testing, you can temporarily replace input("...") with a fixed
string, e.g. name = "Alex"  instead of  name = input("Name: ")
"""


# ===========================================================
# EXERCISE 1: Ask, cast, and use
# ===========================================================
# 1. Use input() to ask the user for their age (it will come
#    back as a string).
# 2. Convert it to an integer.
# 3. Print how old they will be in 10 years.
#
# Example run:
#   Enter your age: 15
#   In 10 years you will be 25.

# YOUR CODE HERE


print("--- End of Exercise 1 ---\n")


# ===========================================================
# EXERCISE 2: Temperature converter
# ===========================================================
# 1. Ask the user to enter a temperature in Celsius (input()).
# 2. Convert it to a float.
# 3. Convert it to Fahrenheit using:  F = C * 9/5 + 32
# 4. Print the result rounded to 2 decimal places using an
#    f-string format specifier (:.2f).
#
# Example run:
#   Enter temperature in Celsius: 21
#   21.0C is 69.80F

# YOUR CODE HERE


print("--- End of Exercise 2 ---\n")


# ===========================================================
# EXERCISE 3: Find and fix the bug
# ===========================================================
# The three lines below will crash with a TypeError if you
# uncomment them, because they try to join a string and a
# number with +.
#
#   quantity = 4
#   report = "You ordered " + quantity + " items"
#   print(report)
#
# Below, write a CORRECTED version that produces the same
# message without crashing. Use either str() or an f-string.

quantity = 4

# YOUR CODE HERE


print("--- End of Exercise 3 ---\n")


# ===========================================================
# EXERCISE 4: Circle calculator with a constant
# ===========================================================
# 1. Define a constant called PI and set it to 3.14159.
# 2. Ask the user for a radius using input(), and convert it
#    to a float.
# 3. Calculate the area:      area = PI * radius ** 2
# 4. Calculate the circumference: circumference = 2 * PI * radius
# 5. Print both results, formatted to 2 decimal places.

# YOUR CODE HERE


print("--- End of Exercise 4 ---\n")


# ===========================================================
# EXERCISE 5: Bank account simulator (augmented assignment)
# ===========================================================
# 1. Create a variable called balance and set it to 200.
# 2. Print the starting balance.
# 3. Using += and -=, apply these changes IN ORDER and print
#    the balance after each one:
#       - deposit of 75
#       - withdrawal of 40
#       - withdrawal of 100
#       - deposit of 15
# 4. Print the final balance with a message, e.g.:
#    "Final balance: $150"

balance = 200

# YOUR CODE HERE


print("--- End of Exercise 5 ---\n")


# ===========================================================
# EXERCISE 6: Predict, then run (scope)
# ===========================================================
# Below is a function and some code that calls it. BEFORE you
# run this file, write your prediction as a comment: what will
# each print() statement output? Then run the file and check
# whether you were right.

total = 100

def add_bonus():
    total = total + 50   # NOTE: this line will actually cause an error!
    print("Inside function:", total)

# YOUR PREDICTION (write as a comment):
# print(total) before calling add_bonus() -> ?
# calling add_bonus() -> ?

# Try running just this exercise (comment out the others if needed)
# and read the error message Python gives you. In a comment below,
# explain in your own words why the error happens, and how using
# a DIFFERENT local variable name would fix it.

# YOUR EXPLANATION HERE:


print("--- End of Exercise 6 ---\n")


# ===========================================================
# BONUS CHALLENGE: Receipt generator
# ===========================================================
# 1. Ask the user for an item name (input()).
# 2. Ask the user for a price (input(), cast to float).
# 3. Ask the user for a quantity (input(), cast to int).
# 4. Calculate subtotal = price * quantity
# 5. Calculate tax using a constant TAX_RATE = 0.13
#    (tax = subtotal * TAX_RATE)
# 6. Calculate total = subtotal + tax
# 7. Print a neat receipt using f-strings and :.2f, e.g.:
#
#    Item: Notebook
#    Quantity: 3
#    Subtotal: $14.97
#    Tax: $1.95
#    Total: $16.92

TAX_RATE = 0.13

# YOUR CODE HERE


print("--- End of Bonus Challenge ---\n")
