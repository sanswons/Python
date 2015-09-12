class Parent():
    def __init__(self,last_name,eye_color):
        print("Parent constructor called")
        self.last_name=last_name
        self.eye_color=eye_color

    def show_info(self):
        print("Last Name -"+self.last_name)
        print("Eye color -"+self.eye_color)

#cyrus=Parent("Cyrus","Blue")
#print(cyrus.last_name)
#cyrus.show_info()

class Child(Parent):
    def __init__(self,last_name,eye_color,no_of_toys):
        print("Child constructor called")
        Parent.__init__(self, last_name, eye_color)
        self.no_of_toys=no_of_toys
    def show_info(self):
        print("Last Name -"+self.last_name)
        print("Eye color -"+self.eye_color)
        print("No of toys -"+str(self.no_of_toys))


mc=Child("Cyrus","Blue",5)
mc.show_info()
