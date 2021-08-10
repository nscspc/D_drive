# Deleting object properties :-
'''
using del operator

syntax :
    del object.attribute

'''
class student:
    marks=50
    def mf(self):
        self.rno=1

s=student()
s.mf()
print(s.rno)
print(s.marks)

del s.rno

print()
#print(s.rno)#it returns a attribute error for rno.

s.mf()
print(s.rno)
