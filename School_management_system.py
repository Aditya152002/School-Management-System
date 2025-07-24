import json, sys

class Student:
  def __init__(self, name, roll_number, marks):
    self.name = name
    self.roll_number = roll_number
    self.marks = marks

class StudentManagementSystem:
  def __init__(self, filename="students.json"):
    self.filename = filename
    self.students = self.load_students()

  def load_students(self):
    try:
      with open(self.filename, 'r') as f:
        student_data = json.load(f)
        return [Student(s['name'], s['roll_number'], s['marks']) for s in student_data]
    except FileNotFoundError:
      return []
    except json.JSONDecodeError:
      print("Error: Could not decode JSON from file.")
      return []

  def save_students(self):
    student_data = [{'name': s.name, 'roll_number': s.roll_number, 'marks': s.marks} for s in self.students]
    try:
      with open(self.filename, 'w') as f:
        json.dump(student_data, f, indent=4)
    except IOError as e:
      print(f"Error: Could not save data to file: {e}")

  def add_student(self, name, roll_number, marks):
    try:
      marks = int(marks)
      new_student = Student(name, roll_number, marks)
      self.students.append(new_student)
      self.save_students()
      print("Student added successfully.")
    except ValueError:
      print("Error: Invalid input for marks. Please enter a number.")

  def view_students(self):
    if not self.students:
      print("No students in the system.")
    else:
      print("Student List:")
      for student in self.students:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, Marks: {student.marks}")

  def search_student(self, roll_number):
    for student in self.students:
      if student.roll_number == roll_number:
        print(f"Student Found: Name: {student.name}, Roll Number: {student.roll_number}, Marks: {student.marks}")
        return
    print("Student not found.")

  def delete_student(self, roll_number):
    initial_count = len(self.students)
    self.students = [student for student in self.students if student.roll_number != roll_number]
    if len(self.students) < initial_count:
      self.save_students()
      print("Student deleted successfully.")
    else:
      print("Student not found.")

sms = StudentManagementSystem()

while True:
  try:
    print("\nStudent Management System Menu:")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
      name = input("Enter student name: ")
      roll_number = input("Enter student roll number: ")
      marks = input("Enter student marks: ")
      sms.add_student(name, roll_number, marks)
    elif choice == '2':
      sms.view_students()
    elif choice == '3':
      roll_number = input("Enter roll number to search: ")
      sms.search_student(roll_number)
    elif choice == '4':
      roll_number = input("Enter roll number to delete: ")
      sms.delete_student(roll_number)
    elif choice == '5':
      print("Exiting Student Management System.")
      sys.exit()
    else:
      print("Invalid choice. Please try again.")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")
