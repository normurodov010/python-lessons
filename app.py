class Person:
    def __int__(self):
        pass
    def __init__(self, name):
        self.name = name
    def base_func(self):
        print("I'm base class func")


def out_of_class_func():
    print("I'm out of class function")