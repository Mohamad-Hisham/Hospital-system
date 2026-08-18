"""Module defining the base Person class for the hospital system."""


class Person:
    """Base class representing a person within the hospital system.

    Attributes:
        name (str): The person's full name.
        age (int): The person's age in years.
    """

    def __init__(self, name: str, age: int) -> None:
        """Initialize a Person instance.

        Args:
            name (str): The person's full name.
            age (int): The person's age in years.
        """
        self.name: str = name
        self.age: int = age

    def view_info(self) -> str:
        """Return a formatted string with the person's basic information.

        Returns:
            str: A string containing the person's name and age.
        """
        return f"Name: {self.name}, Age: {self.age}"