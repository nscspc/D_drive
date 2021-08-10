users = {} # Username : {first, last, age, gender, password, message}
                                            

def signup(username, password):
  first_name= input('Enter your first name : ')
  last_name= input('Enter your last name : ')
  age = int(input("Enter your age : "))
  gender = input("Select gender, (male, female, binary): ")

  users[username] = {
                     "first": first_name,
                     "last": last_name,
                     "age": age,
                     "gender": gender,
                     "password": password
                     }

def signin(username, password):
  if username in users.keys():
    if password == users[username]["password"]:
      print("Welcome to dashboard!")
  else:
    print("Wrong Username or password!")

active = True

while active:
  choice = input("Type 'si' to 'sign in', 'su' to 'sign up', and hit enter to exit: ")
  
  if choice == "si" or choice == "su":
    username= input('Enter username : ')
    password = input("Enter password: ")

    if choice == "si":
      signin(username, password)
    else:
      signup(username, password)
  else:
    print("Thank you for using 'Sasta FakeBook'!")
    active = False
