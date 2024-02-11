#!/usr/bin/python3
""" Review module """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class is a subclass of the BaseModel class """
    place_id = ""
    user_id = ""
    text = ""
