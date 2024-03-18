class Employee:

    def __init__(self, fname, lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email

    def greet_person(self):
        print("hello, welcome to movie " + self.fname)


emp1 = Employee('srini', 'tiru', 'srinitiru@yahoo.com')
emp1.greet_person()
print(emp1.email)
