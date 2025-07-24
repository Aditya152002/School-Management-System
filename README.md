# School-Management-System

### 📌 **Project Overview:**
This project is a **command-line based Student Management System** built using Python. It allows users to add, view, search, and delete student records with persistent storage in a JSON file.

---

### 🔷 **Features:**
1. **Add Student** – Inputs name, roll number, and marks, validates marks as integer, saves to file.
2. **View Students** – Displays all saved student records in a readable format.
3. **Search Student** – Finds a student by roll number.
4. **Delete Student** – Deletes student data by roll number.
5. **Exit** – Safely terminates the program.

---

### 🔷 **Technologies & Concepts Used:**
- **Python OOP:** Classes `Student` and `StudentManagementSystem`
- **File Handling:** Reading and writing JSON data for persistence.
- **Exception Handling:** For file errors, invalid inputs, and unexpected runtime issues.
- **CLI Menu-driven Application:** Interactive user input loop for multiple functionalities.

---

### 🔷 **File Structure:**
- `students.json` – JSON file storing student records as a list of dictionaries.

---

### 🔷 **How it works:**
1. On startup, loads existing students from `students.json`.
2. Displays a menu to perform CRUD operations.
3. Updates `students.json` after every add or delete operation to maintain data persistence.

---

### 🔷 **Usage Instructions:**
1. **Run the script:** `python student_management_system.py`
2. **Follow on-screen menu:**
   - Press 1 to add a student
   - Press 2 to view all students
   - Press 3 to search student by roll number
   - Press 4 to delete student by roll number
   - Press 5 to exit program

---
