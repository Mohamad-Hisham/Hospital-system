class Hospital:
    """Class for managing hospital operations."""

    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.departments = []

    def add_department(self, department):
        """Add a department to the hospital."""
        self.departments.append(department)
        print(f"Department '{department.name}' added to {self.name}.")

    def view_departments(self):
        """View all departments in the hospital."""
        print("All departments:")
        for department in self.departments:
            print(f"Department Name: {department.name}")
