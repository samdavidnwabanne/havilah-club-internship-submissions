# Day 11 — Introduction to Python
# Task: Complete exercises on variables, data types, operators, and basic input/output.
# Submit this .py file with all working programs.

# ── Exercise 1: Variables and Data Types ─────────────────────────────────────
# Create variables of 4 different types: string, integer, float, and boolean.
# Print all of them with descriptive labels.

# TODO: your code here
student_name = "Kamsi"            # str
student_age = 22                  # int
student_cgpa = 4.5                # float
is_enrolled = True                # bool

print("Student Information")
print("Name:", student_name)
print("Age:", student_age)
print("CGPA:", student_cgpa)
print("Enrolled:", is_enrolled)

print("Data Types")
print("Type of student_name:", type(student_name))
print("Type of student_age:", type(student_age))
print("Type of student_cgpa:", type(student_cgpa))
print("Type of is_enrolled:", type(is_enrolled))


# ── Exercise 2: Basic Calculator ────────────────────────────────────────────
# Ask the user to enter two numbers and convert the inputs to numbers.
# Print the sum, difference, product, quotient, and remainder with clear labels.

# TODO: your code here
print("\n Calculator")

# input() always returns a string, so we convert to float
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

print("Sum:", first_number + second_number)
print("Difference:", first_number - second_number)
print("Product:", first_number * second_number)
print("Quotient:", first_number / second_number)
print("Remainder:", first_number % second_number)


# ── Exercise 3: Temperature Converter ────────────────────────────────────────
# Ask the user to enter a temperature in Celsius, then print the Fahrenheit equivalent.
# Then ask for a temperature in Fahrenheit and convert it to Kelvin. Accept decimal values.

# TODO: your code here
print("\n Temperature Converter")

# Celsius to Fahrenheit: F = (C x 9/5) + 32
celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit_result = (celsius * 9 / 5) + 32
print(celsius, "°C is equal to", fahrenheit_result, "°F")

# Fahrenheit to Kelvin: K = (F - 32) x 5/9 + 273.15
fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
kelvin_result = (fahrenheit - 32) * 5 / 9 + 273.15
print(fahrenheit, "°F is equal to", kelvin_result, "K")


# ── Exercise 4: Robot Sensor Monitor ────────────────────────────────────────────
# Ask for the Robot Name, Robot ID, Sensor Name, Sensor Reading, and Operating Limit.
# Calculate the difference between the operating limit and the reading, then print a report.

# TODO: your code here
print("\n Robot Sensor Monitor")

robot_name = input("Enter the Robot Name: ")
robot_id = input("Enter the Robot ID: ")      # kept as text, since IDs are not used in calculations
sensor_name = input("Enter the Sensor Name: ")
sensor_reading = float(input("Enter the Sensor Reading: "))
operating_limit = float(input("Enter the Operating Limit: "))

# Difference between the limit and the current reading
difference = operating_limit - sensor_reading

print("\n SENSOR REPORT")
print(f"Robot Name      : {robot_name}")
print(f"Robot ID        : {robot_id}")
print(f"Sensor Name     : {sensor_name}")
print(f"Sensor Reading  : {sensor_reading}")
print(f"Operating Limit : {operating_limit}")
print(f"Difference      : {difference}")

# Status check using if/else
if difference >= 0:
    print("Status          : Within operating limit")
else:
    print("Status          : LIMIT EXCEEDED")
print("")