#!/usr/bin/python3

"""A module to help with IDs"""
import json
import csv
# import turtoo library function
from random import choice as random


class Base:
    """A simple class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns json strings
        """
        if list_dictionaries is None:
            list_dictionaries = []
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.
        Args:
            list_objs (list): a list of objects.
        """
        lst = []
        if list_objs is not None and len(list_objs) > 0:
            for obj in list_objs:
                lst.append(obj.to_dictionary())
        with open(cls.__name__ + ".json", 'w') as f:
            f.write(Base.to_json_string(lst))

    @staticmethod
    def from_json_string(json_string):
        """just another function"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        just function play with instances
        """
        if cls.__name__ == "Rectangle":
            tempo = cls(1, 1)
        if cls.__name__ == "Square":
            tempo = cls(1)
        tempo.update(**dictionary)
        return (tempo)

    @classmethod
    def load_from_file(cls):
        """
        load from file
        """
        fn = cls.__name__ + ".json"
        lst = []
        try:
            with open(fn, mode="r", encoding='utf-8') as myFile:
                lst = cls.from_json_string(myFile.read())
            for i, j in enumerate(lst):
                lst[i] = cls.create(**lst[i])
        except:
            pass
        return (lst)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        function serializes in csv
        """
        fn = cls.__name__ + ".csv"
        if fn == "Rectangle.csv":
            fields = ["id", "width", "height", "x", "y"]
        else:
            fields = ["id", "size", "x", "y"]
        with open(fn, mode="w", newline="") as myFile:
            if list_objs is None:
                writer = csv.writer(myFile)
                writer.writerow([[]])
            else:
                writer = csv.DictWriter(myFile, fieldnames=fields)
                writer.writeheader()
                for x in list_objs:
                    writer.writerow(x.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        function deserializes from csv
        """
        try:
            fn = cls.__name__ + ".csv"
            with open(fn, newline="") as myFile:
                reader = csv.DictReader(myFile)
                lst = []
                for x in reader:
                    for i, n in x.items():
                        x[i] = int(n)
                    lst.append(x)
                return ([cls.create(**objt) for objt in lst])
        except FileNotFoundError:
            return ([])
