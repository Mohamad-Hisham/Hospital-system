from person import person

class Patient(Person):
    """Class for hospital patients, inheriting from Person."""

    def __init__(self, name: string, age: int, medical_record: string) -> None:
        """
            Add a patient to the system

            Parameters:
                name (string): The name of the patient
                age (int): The age of the patient
                medical_record (string): The medical record of the patient

            Returns:
                None
        """
        
        super().__init__(name, age)
        self.medical_record = medical_record

    def view_record(self):
        """View patient record."""
        
        return f"Patient Record: {self.medical_record}"
