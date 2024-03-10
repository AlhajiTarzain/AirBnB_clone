#!/usr/bin/python
""" city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """classfields for city """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
