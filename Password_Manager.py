#PassWord Manager ver 0.1
#Created by Johnson Zhang
#First verison
import base64
name = ""
age = ""

passl = []
userl = ["Johnson", "BDSC"]

def req (name, age):
  print("Hello", name.capitalize())
  while True:
    try: 
      if age < 13:
        print("You are below the restricted age")
        print("The program will now exit")
        exit()
  
      elif age >= 13:
        granted()

    except ValueError:
      print("Enter a valid number")
    
def granted():
  choice = int(input("Enter your choice:\n1. Add Password\n2. View Password\n3. Exit\n"))
  while True:
    try:
      if choice == 1:
        add_pass()
      elif choice == 2:
        view_pass()
      elif choice == 3:
        break

    except ValueError:
      print("Please enter a vaild number")

def add_pass():
  add = input("Whats the Password you want to add: ") 
  tname = input("Whats the website of this password: ".title())
  passl.append(add)
  passl.append(tname)
  print("Successful!!!")
  check = int(input("Would you like to check your password. Yes(1) No(2): "))
  if check == 1:
    print(passl)
    print("You will now retuen back to main menu")
    req(name,age)
  elif check == 2:
    req(name, age)

def view_pass():
  for list in passl:
    print(list)
  print("You will be send back to the main menu")
  req(name,age)

print("Welcome to the Password_manager!!")
print("You must be over 13 to access this program")

name = input("What is your name: ")
age = float(input("How old are you: "))
req(name,age)



