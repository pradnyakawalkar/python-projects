import csv
import os

FILE_NAME = "students.csv"

students = []


# ======================
# Calculate Percentage
# ======================

def calculate_result(student):
    total = sum(student["marks"])
    percentage = total / 5

    student["total"] = total
    student["percentage"] = percentage

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B+"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    student["grade"] = grade


# ======================
# Load Data from CSV
# ======================

def load_data():

    if not os.path.exists(FILE_NAME):
        return

    with open(FILE_NAME, "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            student = {
                "name": row["Name"],
                "roll": int(row["RollNo"]),
                "marks": [
                    float(row["Mark1"]),
                    float(row["Mark2"]),
                    float(row["Mark3"]),
                    float(row["Mark4"]),
                    float(row["Mark5"])
                ]
            }

            calculate_result(student)

            students.append(student)


# ======================
# Save Data to CSV
# ======================

def save_data():

    with open(FILE_NAME, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Name",
            "RollNo",
            "Mark1",
            "Mark2",
            "Mark3",
            "Mark4",
            "Mark5"
        ])

        for s in students:

            writer.writerow([
                s["name"],
                s["roll"],
                s["marks"][0],
                s["marks"][1],
                s["marks"][2],
                s["marks"][3],
                s["marks"][4]
            ])


# ======================
# Assign Rank
# ======================

def assign_rank():

    students.sort(
        key=lambda x: x["percentage"],
        reverse=True
    )

    for i, s in enumerate(students, start=1):
        s["rank"] = i


# ======================
# Add Student
# ======================

def add_student():

    name = input("\nEnter Name       : ")

    roll = int(input("Enter Roll No    : "))

    print("Enter 5 Subject Marks")

    marks = []

    for i in range(5):
        marks.append(
            int(input(f"Subject {i+1}: "))
        )

    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }

    calculate_result(student)

    students.append(student)

    save_data()

    print("\n=== Record Added Successfully ===")

    print(
        f"Name: {name} | "
        f"Roll: {roll} | "
        f"%: {student['percentage']:.2f} | "
        f"Grade: {student['grade']}"
    )


# ======================
# View All Students
# ======================

def view_all():

    if len(students) == 0:
        print("\nNo Records Found")
        return

    assign_rank()

    print("\n" + "=" * 90)

    print(
        f"{'Rank':<6}"
        f"{'Roll':<8}"
        f"{'Name':<20}"
        f"{'Total':<10}"
        f"{'%':<10}"
        f"{'Grade':<10}"
    )

    print("=" * 90)

    for s in students:

        print(
            f"{s['rank']:<6}"
            f"{s['roll']:<8}"
            f"{s['name']:<20}"
            f"{s['total']:<10}"
            f"{s['percentage']:<10.2f}"
            f"{s['grade']:<10}"
        )


# ======================
# Search Student
# ======================

def search_student():

    roll = int(input("Enter Roll No: "))

    for s in students:

        if s["roll"] == roll:

            print("\nStudent Found")

            print("Name       :", s["name"])
            print("Roll No    :", s["roll"])
            print("Marks      :", s["marks"])
            print("Percentage :", round(s["percentage"], 2))
            print("Grade      :", s["grade"])

            return

    print("Student Not Found")


# ======================
# Update Student
# ======================

def update_student():

    roll = int(input("Enter Roll No: "))

    for s in students:

        if s["roll"] == roll:

            print("Enter New Marks")

            marks = []

            for i in range(5):
                marks.append(
                    int(input(f"Subject {i+1}: "))
                )

            s["marks"] = marks

            calculate_result(s)

            save_data()

            print("Record Updated Successfully")

            return

    print("Student Not Found")


# ======================
# Delete Student
# ======================

def delete_student():

    roll = int(input("Enter Roll No: "))

    for s in students:

        if s["roll"] == roll:

            students.remove(s)

            save_data()

            print("Record Deleted Successfully")

            return

    print("Student Not Found")


# ======================
# Sort By Percentage
# ======================

def sort_by_percentage():

    assign_rank()

    print("\nStudents Sorted By Percentage")

    view_all()


# ======================
# Class Report
# ======================

def class_report():

    if len(students) == 0:
        print("No Records Found")
        return

    assign_rank()

    topper = students[0]

    avg = sum(
        s["percentage"] for s in students
    ) / len(students)

    pass_count = len([
        s for s in students
        if s["percentage"] >= 40
    ])

    fail_count = len(students) - pass_count

    print("\n====== CLASS REPORT ======")

    print(
        f"Topper       : "
        f"{topper['name']} "
        f"({topper['percentage']:.2f}%)"
    )

    print(
        f"Average %    : "
        f"{avg:.2f}"
    )

    print(
        f"Pass Count   : "
        f"{pass_count}"
    )

    print(
        f"Fail Count   : "
        f"{fail_count}"
    )


# ======================
# Main Program
# ======================

load_data()

while True:

    print("\n====== STUDENT MANAGEMENT SYSTEM ======")
    print("1. Add Student")
    print("2. View All")
    print("3. Search")
    print("4. Update")
    print("5. Delete")
    print("6. Sort By Percentage")
    print("7. Class Report")
    print("8. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_all()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        sort_by_percentage()

    elif choice == "7":
        class_report()

    elif choice == "8":
        save_data()
        print("Data Saved Successfully")
        break
    else:
        print("Invalid Choice")