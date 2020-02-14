#!/usr/bin/python3
""" Base module """
import uuid
from datetime import datetime


class BaseModel:
    """ class for all other classes to inherit from """
    def __init__(self, id='', created_at='', updated_at=''):
        """ Constructor """
        # Generate a random UUID
        self.id = str(uuid.uuid4())
        # assign with the current datetime when an instance is created
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ overriding the __str__ method that returns a custom
        string object """
        # Old-style: self.__class__.__name__
        class_name = type(self).__name__
        mssg = "[{0}] ({1}) {2}".format(class_name, self.id, self.__dict__)
        return (mssg)

    # Public instance methods
    def save(self):
        """ updates the public instance attribute updated_at with
        the current datetime """
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance."""
        # Define a dictionary and key __class__ that add to this dictionary
        # with the class name of the object
        tdic = {}
        tdic["__class__"] = type(self).__name__
        # loop over dict items and validate created_at and updated_at to
        # convert in ISO format
        for n, i in self.__dict__.items():
            if isinstance(i, datetime):
                tdic[n] = i.isoformat()
            else:
                tdic[n] = i
        return (tdic)
