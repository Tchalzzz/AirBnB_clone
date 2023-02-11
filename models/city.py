#!/usr/bin/python3
""" This module create a city class"""


from models.base_model import BaseModel

class City(BaseModel):
    """this class stores the city objects"""

    state_id = ""
    name = ""