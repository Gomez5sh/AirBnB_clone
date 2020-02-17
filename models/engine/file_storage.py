#!/usr/bin/python3
""" Convert the dictionary representation to a JSON string """
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """ serializes instances to a JSON file and deserializes
    JSON file to instances """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return (self.__objects)

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        ser_dict = {}
        all_dict = FileStorage.__objects
        with open(FileStorage.__file_path, 'w') as f:
            for value in all_dict.values():
                key = "{}.{}".format(value.__class__.__name__, value.id)
                ser_dict[key] = value.to_dict()
            json.dump(ser_dict, f)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists, otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised) """
        # from models.base_model import BaseModel
        # Validate if file exists
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as f:
                des_json = json.load(f)
            for key in des_json.keys():
                # search "__class__": "BaseModel"
                inst_dict = des_json[key]
                inst_class = inst_dict['__class__']
                if "BaseModel" in inst_dict['__class__']:
                    self.__objects[key] = BaseModel(des_json[key])
