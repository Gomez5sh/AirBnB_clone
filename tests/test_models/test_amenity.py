#!/usr/bin/python3


"""Unittest User"""


import unittest
import os
from models.user import User
from models.base_model import BaseModel


class test_Amenity(unittest.TestCase):
        @classmethod
        def setup(self):
            self.Amenity = Amenity()
            self.Amenity.name = "Yggdrasil"

        @classmethod
        def tearDown(self):
            del self.Amenity
            try:
                os.remove("file.json")
            except FileNotFoundError:
                pass

        def test_to_dict(self):
            self.assertEqual("to_dict" in dir(self.Amenity), True)

        def test_functions(self):
            self.assertIsNotNone(Amenity.__dict__)

        def save_test(self):
            self.Amenity.save()
            self.assertNotEqual(self.Amenity.created_at,
                                self.Amenity.updated_at)

        def test_subclass(self):
            self.assertTrue(issubclass(self.Amenity.__class__.BaseModel), True)

        def test_attributes(self):
            self.assertTrue("name" in self.Amenity.__dict__)
            self.assertTrue("created_at" in self.Amenity.__dict__)
            self.assertTrue("updated_at" in self.Amenity.__dict__)
            self.assertTrue("id" in self.Amenity.__dict__)

        def test_strings(self):
            self.assertEqual(type(self.Amenity.name), str)

if __name__ = "__main__":
    unittest.main()
