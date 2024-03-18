"""
1. Multiple inheritance - A class can inherit attributes and methods
    from more than one class
2. Method Resolution Order (MRO) - Search is done first in current class, then the search continues
into parent classes in depth-first, left-right fashion without searching the same class twice

"""
class black:
    def black_colour(self):
        print("I am from black")


    def blackkkk_colour(self):
        print("I am from blackkkkk")



class white:
    def white_colour(self):
        print("I am from white")


    def whiteeeee_colour(self):
        print("I am from whiteeeeee")


class blackAndWhite(black, white):
    def red(self):
        print("I am from black and white")


p1 = blackAndWhite()
p1.whiteeeee_colour()
#This method is not in the child class. So, it will serch in the black class then white ( from left to right)
p1.black_colour()