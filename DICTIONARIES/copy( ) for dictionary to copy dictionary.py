# new_dict = another_dict.copy( ) :- to copy one dictionary to another .
d={
    1:2,
    2:3,
    3:4,
    4:5
   }
print(d)
print()
nd=d.copy()
print(nd)
print()
#another way to copy dictionary :-
nd2=dict(nd)
print(nd2)
print()

nd3=nd2
print(nd3)
