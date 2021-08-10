# Python datetime :-
'''
a date in python is not a datatype of its own , but we can
import a module named datetime to work with dates
as date objects .

'''
import datetime
x=datetime.datetime.now( )# the date contains year, month, hour,day , minute, microsecond.
print(x,'\n')

# to print only year :-
print(x.year)
    #or
print(datetime.datetime.now().year,'\n')


# strftime( )
'''
the strftime( ) function is used to convert date and time
objects to their string representation .

'''
print(x.strftime("%a"))# %a is used for short version of days .
print(x.strftime("%A"))# %A is used for days .

print(x.strftime("%B"))# %B is used for months .
print(x.strftime("%b"))# %b is used for short version of months .

print(x.strftime("%d"))# %d is used to print only date .

print(x.strftime("%m"))# %m is used to print no. of month (01 - 12).
print(x.strftime("%M"))# %M is used to print no. of minute (00 - 59).

print(x.strftime("%w"))# w% is used to print no. of weekday ( 0 - 6 ) , 0 is Sunday .
print(x.strftime("%W"))# %W is used to print no. of week in the year ( Sunday is taken as the first day of the week )(00 - 53) .

print(x.strftime("%y"))# %y is used to print only the year without century .
print(x.strftime("%Y"))# %Y is used to print year with century .

print(x.strftime("%H"))# %H is used to print no. of hour from 00 - 23. 

print(x.strftime("%I"))# %I is used to print no. of hour from 00 - 12.

print(x.strftime("%p"))# %p is used to print print meridian ( AM & PM ) .

print(x.strftime("%f"))# %f is used t print microsecond.

print(x.strftime("%z"))# UTC offset :- +0100
print(x.strftime("%Z"))# %Z is used to print timezone .( CST )

print(x.strftime("%j"))# %j is used to print day number in the year.

print(x.strftime("%U"))# to print week no. of the year ( sunday is taken as the first day of the week ) ( 00 - 53 ). 
print(x.strftime("%u"))# to print weekday(monday is taken as 1 and sunday is taken as 7).

print(x.strftime("%c"))# to print local version of date and time.

print(x.strftime("%x"))# to print local verion of date.
print(x.strftime("%X"))# to print local version of time.

print(x.strftime("%%"))# to print a '%' character.

print(x.strftime("%G"))# to print full year.

print(x.strftime("%V"))# to print weeknumber ( 00 - 53 )

print(x.strftime("%S"),"\n")# to print no. of second ( 00 - 59 )


# Creating date objects :-
'''
to create a date , we can use the datetime( ) class(constructor)
of the datetime module.

the datetime( ) class requires three parameters to create
a date : year, month, day .

'''
import datetime
x=datetime.datetime(2021,1,1)
print(x)

'''
the datetime can also take parameters for time and
timezone(hour,minute,second,microsecond,tzone),but they
are optional and has a default value 0,None(None for timezone) .

'''
