#!/usr/bin/python3
"""the BaseModel module."""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """the BaseModel class of the AirBnB project."""
    def __init__(self, *args, **kwargs):
        """Initialize the object."""
        tformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, tformat)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """print the string representation of the object."""
        return "{}".format(self.__dict__)

    def save(self):
        """update the date and time."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns the dictionary representation of the object."""
        rdict = self.__dict__.copy()
        rdict['created_at'] = self.created_at.isoformat()
        rdict['updated_at'] = self.updated_at.isoformat()
        rdict['__class__'] = self.__class__.__name__
        return rdict
