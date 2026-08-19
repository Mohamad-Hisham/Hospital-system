from hospital import Hospital
from department import Department
from patient import Patient
from staff import Staff


def display_menu() -> None:
    """Display the main menu."""

    print("\n========================================")
    print("       HOSPITAL MANAGEMENT SYSTEM")
    print("========================================")
    print("1. Add Department")
    print("2. Add Patient")
    print("3. Add Staff")
    print("4. View Departments")
    print("5. View Patients")
    print("6. View Staff")
    print("7. Exit")


def find_department(hospital: Hospital, department_name: str):
    """Find a department by its name."""

    for department in hospital.departments:
        if department.name.lower() == department_name.lower():
            return department

    return None

def find_patient_by_id(hospital: Hospital, patient_id: str):
    """Find a patient anywhere in the hospital by ID."""

    for department in hospital.departments:
        for patient in department.patients:
            if patient.patient_id.lower() == patient_id.lower():
                return patient

    return None


def add_department(hospital: Hospital) -> None:
    """Add a new department to the hospital."""

    department_name = input("Enter department name: ").strip()

    if not department_name:
        print("Department name cannot be empty.")
        return

    # Check if department already exists
    if find_department(hospital, department_name):
        print("Department already exists.")
        return

    department = Department(department_name)

    hospital.add_department(department)

    print("Department added successfully!")


def add_patient(hospital: Hospital) -> None:
    """Add a patient to a department."""

    if not hospital.departments:
        print("Please add a department first.")
        return

    name = input("Enter patient name: ").strip()

    try:
        age = int(input("Enter patient age: "))
    except ValueError:
        print("Invalid age. Please enter a number.")
        return

    patient_id = input("Enter patient ID: ").strip()

    if find_patient_by_id(hospital, patient_id):
        print("A patient with this ID already exists.")
        return

    ailment = input("Enter patient ailment: ").strip()

    department_name = input("Enter department name: ").strip()

    department = find_department(
        hospital,
        department_name
    )

    if department is None:
        print("Department not found.")
        return

    patient = Patient(
        name,
        age,
        patient_id,
        ailment
    )

    department.add_patient(patient)

    print("Patient added successfully!")


def add_staff(hospital: Hospital) -> None:
    """Add a staff member to a department."""

    if not hospital.departments:
        print("Please add a department first.")
        return

    name = input("Enter staff name: ").strip()

    try:
        age = int(input("Enter staff age: "))
    except ValueError:
        print("Invalid age. Please enter a number.")
        return

    position = input("Enter staff position: ").strip()

    department_name = input("Enter department name: ").strip()

    department = find_department(
        hospital,
        department_name
    )

    if department is None:
        print("Department not found.")
        return

    shift = input("Enter staff shift: ").strip()

    try:
        experience = int(
            input("Enter years of experience: ")
        )
    except ValueError:
        print("Invalid experience. Please enter a number.")
        return

    salary_input = input(
        "Enter base salary (press Enter for 7000): "
    ).strip()

    if salary_input == "":
        base_salary = 7000.0

    else:
        try:
            base_salary = float(salary_input)
        except ValueError:
            print("Invalid salary. Please enter a number.")
            return

    staff_member = Staff(
        name,
        age,
        position,
        department_name,
        shift,
        experience,
        base_salary
    )

    department.add_staff(staff_member)

    print("Staff member added successfully!")


def view_departments(hospital: Hospital) -> None:
    """Display all departments."""

    if not hospital.departments:
        print("No departments available.")
        return

    print("\nDepartments:\n")

    for department in hospital.departments:
        print(f"- {department.name}")


def view_patients(hospital: Hospital) -> None:
    """Display all patients grouped by department."""

    if not hospital.departments:
        print("No departments available.")
        return

    print("\nPatients:\n")

    patient_found = False

    for department in hospital.departments:

        if department.patients:
            patient_found = True

            print(f"{department.name}:")

            for patient in department.patients:
                print(
                    f"Patient ID: {patient.patient_id}, "
                    f"Name: {patient.name}, "
                    f"Age: {patient.age}, "
                    f"Ailment: {patient.ailment}"
                )

            print()

    if not patient_found:
        print("No patients available.")

    if not patient_found:
        print("No patients available.")


def view_staff(hospital: Hospital) -> None:
    """Display all staff grouped by department."""

    if not hospital.departments:
        print("No departments available.")
        return

    print("\nStaff:\n")

    staff_found = False

    for department in hospital.departments:

        if department.staff:

            staff_found = True

            print(f"{department.name}:")

            for staff_member in department.staff:
                print(staff_member.view_info())
                print()

    if not staff_found:
        print("No staff available.")


def main() -> None:
    """Run the Hospital Management System."""

    print("========================================")
    print("       CREATE YOUR HOSPITAL")
    print("========================================")

    hospital_name = input("Enter hospital name: ").strip()
    hospital_location = input("Enter hospital location: ").strip()

    hospital = Hospital(
        hospital_name,
        hospital_location
    )

    print("\nHospital created successfully!")

    while True:

        display_menu()

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_department(hospital)

        elif choice == "2":
            add_patient(hospital)

        elif choice == "3":
            add_staff(hospital)

        elif choice == "4":
            view_departments(hospital)

        elif choice == "5":
            view_patients(hospital)

        elif choice == "6":
            view_staff(hospital)

        elif choice == "7":
            print("\nExiting Hospital Management System...")
            print("Goodbye!")
            break

        else:
            print(
                "Invalid choice. "
                "Please enter a number from 1 to 7."
            )


if __name__ == "__main__":
    main()