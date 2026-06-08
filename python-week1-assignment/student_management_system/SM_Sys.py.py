# TASK-1 - STUDENT MANAGEMENT SYSTEM

class Student:
    def __init__(self, student_id, name, age, course, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks


class StudentManager:
    def __init__(self):
        self.students = []

    def save_st(self):
        try:
            with open("student_management.txt", "w") as f:
                for student in self.students:
                    f.write(
                        f"{student.student_id},"
                        f"{student.name},"
                        f"{student.age},"
                        f"{student.course},"
                        f"{student.marks}\n"
                    )
        except FileNotFoundError:
            print("File Not Found!")

    def read_st(self):
        try:
            with open("student_management.txt", "r") as file:
                for line in file:
                    data = line.strip().split(",")

                    student = Student(
                        data[0],
                        data[1],
                        int(data[2]),
                        data[3],
                        float(data[4])
                    )
                    self.students.append(student)
        except FileNotFoundError:
            pass

    def add_st(self):
        student_id = input("Student ID: ")
        name = input("Name: ")
        age = int(input("Age: "))
        course = input("Course: ")
        marks = float(input("Marks: "))
        st = Student(student_id, name, age, course, marks)
        self.students.append(st)
        self.save_st()
        print("Student added successfully!")

    def display_st(self):
        while True:
            print("\n---------- Display Menu ----------")
            print("1. Display All")
            print("2. Display (Sorted by Marks)")
            print("3. Display (Sorted by Name)")
            print("4. Exit")
            choice = input("Enter choice (1-4): ")

            if choice == "1":
                for st in self.students:
                    print(
                        f"ID:{st.student_id} | "
                        f"Name:{st.name} | "
                        f"Age:{st.age} | "
                        f"Course:{st.course} | "
                        f"Marks:{st.marks}"
                    )
            elif choice == "2":
                sort_st = sorted(
                    self.students,
                    key=lambda student: student.marks,
                    reverse=True
                )
                for st in sort_st:
                    print(
                        f"ID:{st.student_id} | "
                        f"Name:{st.name} | "
                        f"Age:{st.age} | "
                        f"Course:{st.course} | "
                        f"Marks:{st.marks}"
                    )
            elif choice == "3":
                sort_st = sorted(
                    self.students,
                    key=lambda student: student.name
                )
                for st in sort_st:
                    print(
                        f"ID:{st.student_id} | "
                        f"Name:{st.name} | "
                        f"Age:{st.age} | "
                        f"Course:{st.course} | "
                        f"Marks:{st.marks}"
                    )
            elif choice == "4":
                break
            else:
                print("Invalid Choice!")

    def find_st(self):
        sid = input("Enter Student ID to Search: ")

        for i in self.students:
            if i.student_id == sid:
                print("\nStudent Found!")

                print(
                    f"ID:{i.student_id} | "
                    f"Name:{i.name} | "
                    f"Age:{i.age} | "
                    f"Course:{i.course} | "
                    f"Marks:{i.marks}"
                )
                return
        print("Student Not Found!")

    def upd_st(self):
        sid = input("Enter Student ID To Update: ")

        for i in self.students:
            if i.student_id == sid:
                print("Enter New Details")
                i.name = input("Name: ")
                i.age = int(input("Age: "))
                i.course = input("Course: ")
                i.marks = float(input("Marks: "))
                self.save_st()
                print("Updated Student Details Successfully!")
                return
        print("Student Not Found!")

    def delete_st(self):
        sid = input("Enter Student ID to Delete: ")

        for i in self.students:
            if i.student_id == sid:
                self.students.remove(i)

                self.save_st()

                print("Student Deleted Successfully!")
                return
        print("Student Not Found!")

manager = StudentManager()
manager.read_st()

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        manager.add_st()
    elif choice == "2":
        manager.display_st()
    elif choice == "3":
        manager.find_st()
    elif choice == "4":
        manager.upd_st()
    elif choice == "5":
        manager.delete_st()
    elif choice == "6":
        print("Exiting Menu...")
        break
    else:
        print("Invalid Choice!")