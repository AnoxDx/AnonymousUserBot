from enum import auto, Enum


class AutoName(Enum):
    def _generate_next_value_(self, *args):
        return self.lower()

    def __repr__(self):
        return f"main.core.enums.{self}"

class UserType(AutoName):

    OWNER = auto()

    SUDO = auto()

    OTHER = auto()

    ALL = auto()
