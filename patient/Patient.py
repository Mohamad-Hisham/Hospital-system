from person import Person


class Patient(Person):
    """Class for hospital patients, inheriting from Person."""

    def __init__(
        self,
        name: str,
        age: int,
        patient_id: str,
        ailment: str
    ) -> None:
        """
        Initialize a Patient instance.

        Args:
            name (str): The patient's name.
            age (int): The patient's age.
            patient_id (str): The patient's unique ID.
            ailment (str): The patient's ailment.
        """

        super().__init__(name, age)

        self.patient_id = patient_id
        self.ailment = ailment

    def view_record(self) -> str:
        """Return the patient's information."""

        return (
            f"Patient ID: {self.patient_id}, "
            f"Name: {self.name}, "
            f"Age: {self.age}, "
            f"Ailment: {self.ailment}"
        )