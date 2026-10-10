
# Student Marks Analyzer
# Project 3 - Beginner Python Project

students = []
SUBJECTS = ["Maths", "Science", "English"]
MAX_MARKS = len(SUBJECTS) * 100


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


def add_student():
    print("\n--- Add Student ---")

    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty!")
        return

    # Prevent duplicate student names
    if any(s["name"].lower() == name.lower() for s in students):
        print("A student with this name already exists!")
        return

    marks = {}

    for subject in SUBJECTS:
        while True:
            try:
                mark = float(input(f"Enter {subject} marks (0-100): "))

                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    student = {
        "name": name,
        "marks": marks
    }

    students.append(student)
    print(f"{name} added successfully!")


def get_results(student):
    total = sum(student["marks"].values())
    percentage = (total / MAX_MARKS) * 100
    grade = calculate_grade(percentage)

    return total, percentage, grade


def view_students():
    print("\n--- All Student Results ---")

    if not students:
        print("No student records available. Add a student first.")
        return

    print("-" * 75)
    print(
        f"{'Name':<15}{'Maths':>8}{'Science':>10}"
        f"{'English':>10}{'Total':>10}{'Percent':>10}{'Grade':>8}"
    )
    print("-" * 75)

    for student in students:
        total, percentage, grade = get_results(student)

        print(
            f"{student['name']:<15}"
            f"{student['marks']['Maths']:>8.1f}"
            f"{student['marks']['Science']:>10.1f}"
            f"{student['marks']['English']:>10.1f}"
            f"{total:>10.1f}"
            f"{percentage:>9.2f}%"
            f"{grade:>8}"
        )

    print("-" * 75)


def show_class_summary():
    print("\n--- Class Summary ---")

    if not students:
        print("No student records available.")
        return

    results = []

    for student in students:
        total, percentage, grade = get_results(student)

        results.append({
            "name": student["name"],
            "total": total,
            "percentage": percentage,
            "grade": grade
        })

    topper = max(results, key=lambda item: item["total"])
    lowest = min(results, key=lambda item: item["total"])

    class_average = sum(
        item["percentage"] for item in results
    ) / len(results)

    print(f"Total students: {len(students)}")
    print(f"Class average: {class_average:.2f}%")
    print(
        f"Class topper: {topper['name']} "
        f"({topper['total']:.1f}/{MAX_MARKS})"
    )
    print(
        f"Lowest-scoring student: {lowest['name']} "
        f"({lowest['total']:.1f}/{MAX_MARKS})"
    )


def main():
    while True:
        print("\n" + "=" * 35)
        print("      STUDENT MARKS ANALYZER")
        print("=" * 35)
        print("1. Add student")
        print("2. View all results")
        print("3. View class summary")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            show_class_summary()
        elif choice == "4":
            print("Thank you for using Student Marks Analyzer!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
