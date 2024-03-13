#!/usr/bin/python
""" format for a use class """
from models.base_model import BaseModel


class User(BaseModel):
    """ Shows user """
    first_name = ""
    last_name = ""
    email = ""
    password = ""

    def __init__(self, *args, **kwargs):
        """ user start """
        super().__init__(*args, **kwargs)
