#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """ A parent class (BaseModel) for our AirBnB project"""
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel,
        Args:
            *args (any): Unused.
            **kwargs (dict): key /value pairs of attributes. 
        """

        dt_format = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], dt_format)
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(kwargs["updated_at"], dt_format)
                else:
                    self.__dict__[key] = kwargs[key]
        
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)


    def __str__(self):
        """Returns official string representation"""

        return "[{}] [{}] [{}]".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """update the public instance attribute updated_at"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all key values of __dict__"""

        my_dict = self.__dict__.copy()
        my_dict["__classs__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
