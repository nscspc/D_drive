# Add properties

class person:
    def __init__(self,fname,lname):
        self.fs=fname
        self.ls=lname

    def pn(self):
        print(self.fs,self.ls)

class student(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)

        self.graduationyear=year

x=student('a','b',0000)
print(x.graduationyear)
