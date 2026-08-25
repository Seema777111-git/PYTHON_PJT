# grade_system.py

user_input = input("Enter your mark (0-100): ")

# Error 1: No input
if user_input.strip() == "":
    print("Error: No input provided.")

# Error 2: Decimal number
elif "." in user_input:
    print("Error: Decimal numbers are not allowed. Please enter a whole number.")

else:
    try:
        mark = int(user_input)

        if mark < 0 or mark > 100:
            print(f"Mark: {mark} -> Error: Mark must be between 0 and 100")

        elif mark >= 90:
            print(f"Mark: {mark} -> Grade: A")

        elif mark >= 80:
            print(f"Mark: {mark} -> Grade: B")

        elif mark >= 70:
            print(f"Mark: {mark} -> Grade: C")

        elif mark >= 60:
            print(f"Mark: {mark} -> Grade: D")

        else:
            print(f"Mark: {mark} -> Grade: F")

    # Error 3: Alphabet or invalid input
    except ValueError:
        print("Error: Please enter a whole number, not alphabets or special characters.")