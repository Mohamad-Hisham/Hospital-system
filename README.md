# 🏥 Hospital Management System

A simple **Hospital Management System** built with Python using **Object-Oriented Programming (OOP)** principles.

The project demonstrates how classes, inheritance, encapsulation, packages, and object relationships can be used to model a real-world hospital system.

---

## 📌 About the Project

The system allows users to create and manage a hospital through a command-line interface.

A hospital contains multiple departments, and each department can contain:

- Patients
- Staff members

The application provides a menu that allows the user to add and view hospital data while performing basic input validation.

---

## ✨ Features

The system currently supports:

- Create a hospital
- Add departments
- Prevent duplicate department names
- Add patients to departments
- Add staff members to departments
- View all departments
- View patients grouped by department
- View staff grouped by department
- Search for departments by name
- Validate numeric input such as age, experience, and salary
- Handle non-existing departments
- Prevent adding patients or staff before creating a department
- Support default or custom staff salaries
- Exit the system safely

---

## 🧠 OOP Concepts Used

This project demonstrates several important Object-Oriented Programming concepts.

### Inheritance

`Patient` and `Staff` inherit common attributes and behavior from the `Person` class.

```text
            Person
           /      \
      Patient     Staff
```

### Composition

A `Hospital` contains multiple `Department` objects.

Each `Department` contains its own patients and staff.

```text
Hospital
│
├── Department
│   ├── Patients
│   └── Staff
│
├── Department
│   ├── Patients
│   └── Staff
│
└── Department
    ├── Patients
    └── Staff
```

### Encapsulation

Each class is responsible for managing its own data and related functionality.

---

## 📂 Project Structure

```text
Hospital-system/
│
├── main.py
│
├── person/
│   ├── __init__.py
│   └── person.py
│
├── patient/
│   ├── __init__.py
│   └── Patient.py
│
├── staff/
│   ├── __init__.py
│   └── Staff.py
│
├── department/
│   ├── __init__.py
│   └── department.py
│
├── hospital/
│   ├── __init__.py
│   └── hospital.py
│
├── .gitignore
├── README.md
└── LICENSE
```

---

## 🧩 Main Classes

### `Person`

The base class shared by patients and staff.

Main attributes include:

- Name
- Age

---

### `Patient`

Represents a patient inside the hospital.

A patient contains information such as:

- Patient ID
- Name
- Age
- Ailment

Patients are assigned to specific departments.

---

### `Staff`

Represents a hospital staff member.

Staff information includes:

- Name
- Age
- Position
- Department
- Shift
- Years of experience
- Base salary

The class also contains functionality such as:

- Viewing staff information
- Changing shifts
- Promoting staff
- Checking seniority
- Calculating bonuses

---

### `Department`

Represents one hospital department.

Each department maintains:

```python
patients = []
staff = []
```

Examples of departments could include:

- Cardiology
- Emergency
- Pediatrics
- Surgery
- Radiology

---

### `Hospital`

Represents the hospital itself.

The hospital contains:

- Hospital name
- Hospital location
- List of departments

---

## 🚀 Running the Project

### 1. Clone the repository

```bash
git clone https://github.com/Mohamad-Hisham/Hospital-system.git
```

### 2. Move into the project directory

```bash
cd Hospital-system
```

### 3. Run the application

```bash
python3 main.py
```

On some systems, you can use:

```bash
python main.py
```

---

## 💻 Example

When the application starts:

```text
========================================
       CREATE YOUR HOSPITAL
========================================

Enter hospital name: El Salam Hospital
Enter hospital location: Cairo

Hospital created successfully!
```

The main menu will then appear:

```text
========================================
       HOSPITAL MANAGEMENT SYSTEM
========================================
1. Add Department
2. Add Patient
3. Add Staff
4. View Departments
5. View Patients
6. View Staff
7. Exit

Enter your choice:
```

### Example Department

```text
Enter your choice: 1
Enter department name: Cardiology

Department added successfully!
```

### Example Patient

```text
Enter your choice: 2
Enter patient name: Ahmed Ali
Enter patient age: 25
Enter patient ID: P001
Enter patient ailment: Chest Pain
Enter department name: Cardiology

Patient added successfully!
```

### Example Staff Member

```text
Enter your choice: 3
Enter staff name: Dr. Omar Hassan
Enter staff age: 38
Enter staff position: Cardiologist
Enter department name: Cardiology
Enter staff shift: Morning
Enter years of experience: 10
Enter base salary: 12000

Staff member added successfully!
```

---

## 🛡️ Input Validation

The program handles several invalid cases.

For example, trying to add a patient before creating a department:

```text
Please add a department first.
```

Trying to use a department that does not exist:

```text
Department not found.
```

Entering invalid numeric data:

```text
Invalid age. Please enter a number.
```

Duplicate departments are also rejected.

```text
Department already exists.
```

---

## 🧪 Testing

The system was manually tested for:

- Valid department creation
- Duplicate departments
- Adding patients
- Adding staff
- Invalid menu choices
- Invalid ages
- Invalid salaries
- Invalid experience values
- Missing departments
- Empty hospital states
- Multiple departments
- Patients assigned to different departments
- Staff assigned to different departments
- Viewing stored information
- Safe application exit

---

## 🔮 Possible Future Improvements

Possible features that could be added later include:

- Doctor-specific classes
- Nurse-specific classes
- Patient appointment management
- Medical history
- Patient discharge system
- Staff removal and editing
- Patient removal and editing
- Department removal
- Login and authentication
- Database integration
- File-based data persistence
- Graphical User Interface
- Automated unit testing

---

## 🛠️ Technologies Used

- Python 3
- Object-Oriented Programming
- Git
- GitHub
- Linux / WSL

---

## 👨‍💻 Author

**Mohamad Hisham**

GitHub: `Mohamad-Hisham`

---

## 📄 License

This project is licensed under the terms provided in the `LICENSE` file.

---

⭐ This project was created as a practical implementation of Python Object-Oriented Programming concepts.