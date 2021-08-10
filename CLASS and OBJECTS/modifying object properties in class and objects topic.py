# modifying object propreties :-

class person:
    def mf(self):
        self.name='a'
        self.age=20

p1=person()
p1.mf()
print(p1.name,p1.age)
print()

p1.age=1
print(p1.name,p1.age)
