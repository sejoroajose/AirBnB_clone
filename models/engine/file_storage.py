#!/usr/bin/python3
import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        with open(self.__file_path, 'w') as f:
            temp = {}
            for key, val in self.__objects.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, val in obj_dict.items():
                    cls_name = val["__class__"]
                    # Delayed import to avoid circular import issues
                    if cls_name == "BaseModel":
                        from models.base_model import BaseModel
                        cls = BaseModel
                    elif cls_name == "User":
                        from models.user import User
                        cls = User
                    else:
                        cls = None
                    if cls:
                        self.__objects[key] = cls(**val)
        except FileNotFoundError:
            pass
