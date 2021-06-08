from enum import Enum

class Tag(Enum):
    family = 1,
    private = 2,
    work = 3

    @classmethod
    def has_member(cls, data):
        return data in Tag._member_names_