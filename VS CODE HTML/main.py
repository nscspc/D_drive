tle=input("enter the title of the reminder : ")
msg=input("enter the message to be displayed in the reminder : ")
tm=float(input("after how much time you want the reminder : "))

from time import time
from plyer import notification

if __name__=="__main__":
    t=time()+tm
    var=True
    while var:
        if t<=time():
            notification.notify(
                title=tle,
                message=msg,
                timeout=1
            )
            var=False
