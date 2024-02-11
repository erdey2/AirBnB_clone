#!/usr/bin/python3
""" City module """
from models.base_model import BaseModel


class City(BaseModel):
    """ City class is a subclass of the BaseModel class """
    state_id = ""
    name = ""
