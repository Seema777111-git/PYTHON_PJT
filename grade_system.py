# grade_system.py

try:
    mark = int(input("Enter your mark (0-100): "))

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

except ValueError:
    print("Error: Please enter a whole number.")
    