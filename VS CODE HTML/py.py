import time
from plyer import notification

if __name__=="__main__":
    while True:
        notification.notify(
            title="Please Drink Water Now ! !",
            message="To prevent dehydration, you need to get plenty of water from drink and food every day. Health experts commonly recommend about 2 liters, or half a gallon a day.",
            app_icon="E:\Downloads\Iconsmind-Outline-Glass-Water.ico",
            timeout=2
        )
        time.sleep(4)
