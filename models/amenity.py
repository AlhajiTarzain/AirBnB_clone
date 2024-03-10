#!/usr/bin/python
""" class Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Classifieds for amenity """
    name = ""

    def __init__(self, *args, **kwargs):
        """initialises Amenity"""
        super().__init__(*args, **kwargs)

