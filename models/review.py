#!/usr/bin/python
""" class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """classfields Review """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)

