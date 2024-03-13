#!/usr/bin/python
""" defiens class state"""
from models.base_model import BaseModel


class State(BaseModel):
    """ classfiels for state"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
