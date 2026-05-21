students = []
def add_student():

    name = input("Enter student name: ")
    age = int(input("Enter age: "))

    mark1 = int(input("Enter mark 1: "))
    mark2 = int(input("Enter mark 2: "))
    mark3 = int(input("Enter mark 3: "))

    # Store marks as tuple
    marks = (mark1, mark2, mark3)

    # Store student as dictionary
    student = {
        "name": name,
        "age": age,
        "marks": marks
    }

    # Add student to list
    students.append(student)

    print(" Student added successfully")


# Function to display students
def display_students():

    if len(students) == 0:
        print("No student records found")
        return

    print("\n Student Records")

    # Using for loop
    for student in students:

        average = sum(student["marks"]) / len(student["marks"])

        print("---------------------------")
        print("Name :", student["name"])
        print("Age :", student["age"])
        print("Marks :", student["marks"])
        print("Average :", average)


# Function to find topper
def find_topper():

    if len(students) == 0:
        print("No student records found")
        return

    topper = students[0]
    highest_average = sum(topper["marks"]) / len(topper["marks"])

    for student in students:

        average = sum(student["marks"]) / len(student["marks"])

        if average > highest_average:
            highest_average = average
            topper = student

    print("\n Topper Details")
    print("Name :", topper["name"])
    print("Age :", topper["age"])
    print("Marks :", topper["marks"])
    print("Average :", highest_average)


# Main Menu using while loop
while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Find Topper")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        find_topper()

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print(" Invalid choice")