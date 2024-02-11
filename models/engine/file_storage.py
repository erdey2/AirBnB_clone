#!/usr/bin/python3
"""File storage class."""
import json


class FileStorage:
    """File storage class."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dict __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects."""
        classname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(classname, obj.id)] = obj

    def save(self):
        """serialize __objects."""
        odict = FileStorage.__objects
        objdict = {obj:odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(objdict, f)

    def reload(self):
        """deserialize the json file."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for obj in objdict.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return
