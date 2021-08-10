car=["Mercedes-Benz","Toyota"," Ferrari","Nissan Rogue"]
user_car=input("which car do you have : ").title()
'''if(user_car[0].islower):
    user_car[0].upper()
'''
print(user_car)
y=[]
user_car.strip()
for c in car:
    y.append(c.strip())

for a in y:
    y.append(a.split("-"))
    print(y)

print(y)

if user_car in y:
    print("your car is in top 10 cars")
else:
    print("your car is not in top 10 cars")

