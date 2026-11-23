students = []
while True:
    print("\n------ student management ------")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Exit")

    choice = input("Your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = float(input("Enter grade: "))
        student = {
            "name": name,
            "grade": grade
        }
        students.append(student)
        
        print("student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            for student in students:
                print(student["name"], "-", student["grade"])

    elif choice == "3":
        print("Exitint program...")
        break

    else:
        print("Invalid choice!")
