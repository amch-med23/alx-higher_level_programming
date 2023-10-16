#!/usr/bin/python3
""" Defines a base model calss. """
import json #implementing json
import csv #implementing csv
import turtle #implementing turtle


class Base:
    """ This calss represent the base model
        This is the base for all the calsses in this project

        Attributes:
            __nb_object typecatedas: (int): Instantiated bases
    """
    __nb_object = 0

    def __init__(self, id=None):
        """Initiation
            Args:
                id (int): the identity of the base
        """
        if id is None:
            Base.__nb_object += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

        @staticmethod
        def to_json_string(list_dictionaries):
            """ Returns JSON serialization of the passed list of
                dictionaries.
                Args:
                    list_dictionaries (list): A list of dictionaries
            """
            if list_dictionaries is None or list_dictionaries == []:
                return "[]"
            return json.dumps(list_dictionaries)
        
        @classmethod
        def save_to_file(cls, list_objs):
            """ Write JSON serialization of a list of objects to a file
                
                Args:
                    list_objs (list): A list of inherited Base instances.
            """
            filename = cls.__name__ + ".json"
            with open(filename, 'w', encoding="utf-8") as f:
                if list_objs is None:
                    f.write("[]")
                else:
                    list_dicts = [o.to_dictionary() for o in list_objs]
                    f.write(Base.to_json_string(list_dicts))
        
        @staticmethod
        def from_json_string(json_string):
            """ Return the deserialzed content of the JSON file
                
                Args:
                    json_string (str): A josn string represantings a list of
                    dics.
                Returns:
                        if sjon_string is None empty - an empty list.
                        Otherwise - the python list represanted by the json_str
            """
            if json_string is None or json_string == "[]":
                return []
            return json.loads(json_string)
        
        @classmethod
        def create(cls, **dictionary):
            """ Return a class instantiated from a dictionary of attributes
                
                Args:
                    **dicionary (dict): key/value pairs of attributes 
                    to initialize.
            """
            if dictionary and dictionary != {}:
                if cls.__name__ == "Rectangle":
                    new = cls(1, 1)
                else:
                    new = cls(1)
                new.update(**dictionary)
                return new

        @classmethod
        def load_from_file(cls):
            """ returns a list of classes instantiated from a JSON file"""
            filename = str(cls.__name__) + ".json"
            try:
                with open(filenmae, 'r', encoding="utf-8") as f:
                    list_dicts = Base.from_json_string(f.read())
                    return [cls.create(**d) for d in list_dicts]
            except IOError:
                return []

        @classmethod
        def save_to_file_csv(cls, list_objs):
            """ write CSV serialization of a list of objects to a file.
                
                Args:
                    list_object (list): A list of inherited Base instances.
            """
            filename = cls.__name__ + ".csv"
            with open(filename, 'w', newline="") as csvfile:
                if list_objs is None or list_objs == []:
                    csvfile.write("[]")
                else:
                    if cls.__name__ == "Rectangle":
                        fieldnames = ["id", "width", "height", "x", "y"]
                    else:
                        fieldnames = ["id", "size", "x", "y"]
                    writer = csv.DictWriter(csvfilw, fieldnames=fieldnames)
                    for obj in list_objs:
                        writer.writerow(obj.to_dictionary())

        @classmethod
        def load_from_file_csv(cls):
            """ Return a list of classes instantiated from CSV file.
                
                Reads from `<cls.__name__>`.csv 

                Returns:
                        if the file does not exist - an empty list
                        Otherwise - a list of instantiated classes.
            """
            filename = cls.__name__ + ".csv"
            try:
                with open(filename, 'r', newline="") as csvfile:
                        if cls.__name__ = "Rectangle":
                            fieldnames = ["id", "width", "height", "x", "y"]
                        else:
                            fieldnames = ["id", "size", "x", "y"]
                        list_dics = csv.DictReader(csvfile, fieldnames=fieldnames)
                        list_dics = [dict([k, int(v)] for k, v in d.items())
                                for d in list_dicts]
                        return [cls.create(**d) for d in list_dicts]
            except IOError:
                return []

        @classmethod
        def draw(list_rectangles, list_squares):
            """ Draws a square and a rectangle using the 
            turtle module

            Args:
                list_rectangles (list): A list of rectangle objects to draw.
                list_squares (list): A list of Squre objects to draw.
            """
            turt = turtle.Turtle()
            turt.screen.bgcolor("#b7312c")
            turt.pensize(3)
            turt.shape("turtle")

            turt.color("#ffffff")
            for rect in list_rectangles:
                turt.showturtle()
                turt.up()
                turt.goto(rect.x, rect.y)
                turt.down()
                for i in range(2):
                    turt.forward(rect.width)
                    turt.left(90)
                    turt.forward(rec.height)
                    turt.left(90)
                turt.hideturtle()

            turt.color("#b5e3d8")
            for sq in list_squares:
                turt.showturtle()
                turt.up()
                turt.goto(sq.x, sq.y)
                turt.down()
                for i in range(2):
                    turt.forward(sq.width)
                    turt.left(90) # this turns 90 degree to left
                    turt.forward(sq.height)
                    turt.left(90)
                turt.hideturtle()

            turtle.exitonclick()


