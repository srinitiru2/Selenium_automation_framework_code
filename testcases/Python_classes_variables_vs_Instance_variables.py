class RateOfInterest():
    # class variables. These are available to all objects
    interest = .04

    def __init__(self, name, loan):
        # Instance variables
        self.name = name
        self.loan = loan

    def calc_interest(self):
        print("Total interest for : ", self.loan * self.interest)


# Creating object of the class
p1 = RateOfInterest("Srinivas", 100000)
p1.calc_interest()

p2 = RateOfInterest("Joe", 100000)
# instance variable.  It is specific to this object p2
RateOfInterest.interest = .07
p2.calc_interest()
