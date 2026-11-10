
class InvalidMarksError(Exception):
    pass


while True:
    try:
        name = input("Enter student name: ")

        assert name.strip() != "", "Student name cannot be empty"

        marks = float(input("Enter student marks: "))

        if marks < 0 or marks > 100:
            raise InvalidMarksError("Marks must be between 0 and 100")

        with open("student_records.txt", "a") as file:
            file.write(name + " - " + str(marks) + "\n")

        print("Student record saved successfully!")

    except AssertionError as e:
        print("Error:", e)

    except ValueError:
        print("Error: Please enter numeric marks.")

    except InvalidMarksError as e:
        print("Error:", e)

    finally:
        print("Record processing completed.")

    choice = input("\nDo you want to enter another record? (yes/no): ")

    if choice.lower() != "yes":
        break

print("\nStudent Marks Management System closed.")
