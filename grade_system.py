# grade_system.py


def get_grade(mark: float) -> str:
    #Grading 
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


def gradecall():
    try:
        user_input = input("Enter your mark): ")
        mark = float(user_input)

        # Check for valid mark boundary
        if mark < 0 or mark > 100:
            print("Error: Mark must be a number between 0 and 100.")
            return

        grade = get_grade(mark)

        print(f"Mark: {mark} -> Grade: {grade}")

    except Exception as e:
        print("Error: Invalid input. Please enter a valid numerical mark."+e)

gradecall()