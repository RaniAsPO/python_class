# creating classes and subclasses - my solution
import pathlib

class Person:
    """Class representing a person."""
    def __init__(self, first_name, last_name, id_number, sex, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number
        self.sex = sex
        self.date_of_birth = date_of_birth

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
        

class Researcher(Person):
    """Class representing a researcher, inheriting from Person."""
    def __init__(self, first_name, last_name, id_number, sex, date_of_birth, position, title):
        super().__init__(first_name, last_name, id_number, sex, date_of_birth)
        self.position = position
        self.title = title

    def get_full_name(self):
        full_name = super().get_full_name()
        print(f"Hello, my name is {self.title} {full_name}.")

class participant(Person):
    """"Class representing a participant, inheriting from Person."""
    def __init__(self, first_name, last_name, id_number, sex, date_of_birth, weight, dominant_hand):
        super().__init__(first_name, last_name, id_number, sex, date_of_birth)
        self.weight = weight
        self.dominant_hand = dominant_hand

    def read_text(self):
        """Read a text file and print its content."""
        # Construct the file path dynamically using the participant's id_number
        file_path = pathlib.Path(__file__).parent / "data" / f"{self.id_number}" / f"{self.id_number}.txt"
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            print(f"File not found: {file_path}")

#suggested solution
from datetime import datetime
from pathlib import Path


class Person:
    """
    Base class representing people.
    """

    def __init__(self, **kwargs):
        """
        Extracts person attributes from the provided keyword arguments.
        """
        self.first_name: str = kwargs.get("first_name", "")
        self.last_name: str = kwargs.get("last_name", "")
        self.id_number: str = kwargs.get("id_number", "")
        self.sex: str = kwargs.get("sex", "")
        self.date_of_birth: datetime.date = kwargs.get("date_of_birth")

    def get_full_name(self) -> str:
        """
        Returns the full name of the person in the format of "first last".

        Returns
        -------
        str
            Full name
        """
        return f"{self.first_name} {self.last_name}"


class Researcher(Person):
    """
    Represents a researcher in the lab.
    """

    def __init__(self, **kwargs):
        """
        Extract researcher attributes from the provided keyword arguments.
        """
        super().__init__(**kwargs)
        self.title: str = kwargs.get("title", "")
        self.position: str = kwargs.get("position", "")

    def get_full_name(self) -> str:
        """
        Returns the full name of the researcher, including their title.

        Returns
        -------
        str
            Researcher name and title
        """
        full_name = super().get_full_name()
        # Introducting Python's ternary expressions:
        return f"{self.title} {full_name}" if self.title else full_name


def Participant(Person):
    """
    Represents a participant in some experiment.
    """
    TEXT_PATH_TEMPLATE: str = "data/{id_number}.txt"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.weight: float = kwargs.get("weight")
        self.dominant_hand: str = kwargs.get("dominant_hand", "")

    def read_text(self) -> str:
        """
        Reads the participant's textual data from a predefined location.

        Returns
        -------
        str
            Participants textual data
        """
        path = self.TEXT_PATH_TEMPLATE.format(id_number=self.id_number)
        with open(path, "r") as text_file:
            return text_file.read()