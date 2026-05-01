students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        age = input("Enter age: ")
        marks = input("Enter marks: ")

        student = {
            "name": name,
            "age": age,
            "marks": marks
        }

        students.append(student)
        print("✅ Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("❌ No students found")
        else:
            print("\n--- Student List ---")
            for s in students:
                print(f"Name: {s['name']}, Age: {s['age']}, Marks: {s['marks']}")

    elif choice == "3":
        search = input("Enter name to search: ")
        found = False

        for s in students:
            if s["name"] == search:
                print("✅ Found:", s)
                found = True

        if not found:
            print("❌ Student not found")

    elif choice == "4":
        delete_name = input("Enter name to delete: ")
        for s in students:
            if s["name"] == delete_name:
                students.remove(s)
                print("🗑️ Student deleted")
                break
        else:
            print("❌ Student not found")

    elif choice == "5":
        print("👋 Exiting program...")
        break

    else:
        print("❌ Invalid choice, try again")
