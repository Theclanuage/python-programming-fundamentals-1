   #1:Variables and datatypes # type: ignore


# Declare variables
name = "Thecla"
age = 21
is_AI_student = True

# Print the output
print(f"Hello, my name is {name}. I am {age} years old and AI student status is {is_AI_student}.")

  # 2:Control structures
# Ask the user to enter a number
number = int(input("Enter a number: "))

# Check conditions
if number < 0:
    print("Invalid input – negative numbers not allowed.")
elif number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

     #3:Loops and functions.
 # Create a list of 9 student names
students = ["Monicah", "Irwine", "Benedict", "Gloria",
            "Faith", "Teddy", "Sandra", "Drina", "Ryan"]

# Use a for loop to print each name in uppercase with index number
for index, name in enumerate(students, start=1):
    print(f"{index}. {name.upper()}")
 # List of student names
students = ["Monicah", "Irwine", "Benedict", "Gloria",
            "Faith", "Teddy", "Sandra", "Drina", "Ryan"]

# For loop to print each name in uppercase with index number
for i in range(len(students)):
    print(f"{i + 1}. {students[i].upper()}")

    #4:Functions .
def area_of_circle(radius):
    from math import pi
    return pi * radius ** 2
# Radius = 4
result = area_of_circle(4)
print(round(result, 2))  # Output: 50.27

def area_of_circle(radius):
    from math import pi
    if radius <= 0:
        return "Invalid input – radius must be greater than 0."
    return pi * radius ** 2
# Valid radius
print(round(area_of_circle(4), 2))  # Output: 50.27

# Invalid radius
print(area_of_circle(-3))            # Output: Invalid input – radius must be greater than 0.

def area_of_circle(radius):
    from math import pi
    if radius <= 0:
        return "Invalid input – radius must be greater than 0."
    return round(pi * radius ** 2, 2)

# Fixed radius
radius = 4
area = area_of_circle(radius)
print(f"Radius {radius}: Area = {area}")