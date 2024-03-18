class ParentClass:
    def __init__(self):
        print("Parent class Instance")

    def parent_method(self):
        print("Parents money")


#child class
class ChildClass(ParentClass):
    # just enter 'pass' if you don't want to do anything here
    pass


# object of parent calss
# p1 = ParentClass()
# p1.parent_method()

# we are creating object of child class which is inheriting from parent
p2 = ChildClass()
p2.parent_method()
