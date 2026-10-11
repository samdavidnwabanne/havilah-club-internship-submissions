# Day 12: Python Logic & Functions

# Exercise 1: Grade Calculator
def calculate_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"


def run_grade_calculator():
    print("\n Grade Calculator")

    # Exercise 4: int() raises a ValueError if the user types text
    try:
        score = int(input("Enter your score (0-100): "))
    except ValueError:
        print("Please enter a valid whole number.")
        return

    if score < 0 or score > 100:
        print("Score must be between 0 and 100.")
    else:
        grade = calculate_grade(score)
        print(f"A score of {score} gets Grade {grade}")


# Exercise 2: Multiplication Table
def run_multiplication_table():
    print("\n Multiplication Table")

    # The while loop lets the user do another table until they quit
    while True:

        # Exercise 4: int() raises a ValueError if the user types text
        try:
            number = int(input("Enter a number: "))
        except ValueError:
            print("Please enter a valid whole number.")
            continue    # skip back to the start of the loop

        # The for loop prints the table from 1 to 12
        for multiplier in range(1, 13):
            result = number * multiplier
            print(number, "x", multiplier, "=", result)

        answer = input("Press Enter to do another, or type quit to stop: ")
        if answer.strip().lower() == "quit":
            break


# Exercise 3: Temperature Converter
def celsius_to_fahrenheit(celsius):
    # F = (C x 9/5) + 32
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def run_temperature_converter():
    print("\n Temperature Converter")

    # Exercise 4: float() raises a ValueError if the user types text
    try:
        celsius = float(input("Enter the temperature in Celsius: "))
    except ValueError:
        print("Please enter a valid number, for example 36.5")
        return

    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit}°F")


# Exercise 5: Python Utility Menu
while True:
    print("\n PYTHON UTILITY MENU")
    print("1. Grade Calculator")
    print("2. Multiplication Table")
    print("3. Temperature Converter")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        run_grade_calculator()
    elif choice == "2":
        run_multiplication_table()
    elif choice == "3":
        run_temperature_converter()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please pick a number from 1 to 4.")