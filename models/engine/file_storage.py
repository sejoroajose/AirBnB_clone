#!/usr/bin/python3
import json
from os.path import exists

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, 'w') as f:
            temp_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(temp_dict, f)

    def reload(self):
        if exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                temp_dict = json.load(f)
                for obj_dict in temp_dict.values():
                    class_name = obj_dict['__class__']
                    del obj_dict['__class__']
                    if class_name == 'BaseModel':
                        from models.base_model import BaseModel
                        obj = BaseModel(**obj_dict)
                    self.new(obj)
