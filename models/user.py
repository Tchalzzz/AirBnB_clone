#!/usr/bin/python3

from models.base_model import BaseModel


class User(BaseModel):
    """class to manage the user objects"""

    first_name = ""
    last_name = ""
    email_id = ""
    password = ""
    tel_number = ""
