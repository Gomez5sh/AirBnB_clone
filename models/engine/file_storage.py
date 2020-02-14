#!/usr/bin/python3
""" Convert the dictionary representation to a JSON string """
import json
import os
from .. base_model import BaseModel


class FileStorage:
    """ serializes instances to a JSON file and deserializes
    JSON file to instances """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return (type(self).__objects)

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(obj.type(self).__name__, obj.id)
        type(self).__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        ser_dict = {}
        all_dict = type(self).__objects
        with open(type(self).__file_path, 'w') as f:
            for value in all_dict.values():
                key = "{}.{}".format(value.type(self).__name__, value.id)
                ser_dict[key] = value.to_dict()
            json.dump(ser_dict, f)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists, otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised) """
        # Validate if file exists
        if os.path.isfile(type(self).__file_path):
            with open(type(self).__file_path, 'r') as f:
                des_json = json.load(f)
            for key in des_json.keys():
                # search "__class__": "BaseModel"
                if (des_json[key] == '__class__'):
                    type(self).__objects[key] = BaseModel(des_json[key])
