class Department:
    """Class representing a department in the hospital."""
    
    def __init__(self, name: str)->None:
        """
        Initialize a new Department instance.

        Args:
            name (str): The name of the department.
        """
        self.name = name
        self.patients = []
        self.staff = []

    def add_patient(self, patient:str)->None:
        """
        Add a patient to the department's patient list.

        Args:
            patient (Patient): The patient object to be added.
        """
        self.patients.append(patient)

    def add_staff(self, staff_member:str)->None:
        """
        Add a staff member to the department's staff list.

        Args:
            staff_member (Staff): The staff object to be added.
        """
        self.staff.append(staff_member)