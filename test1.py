#Created by Johnson Zhang
#24/02/2021
#Ver. 0.1

import os.path

if os.path.exists("Saved_Password.txt"):
  pass
else:
  file = open("Saved_Password.txt", 'w')
  file.close()


print("########################################")
print("Welcome to Password_Manager_0.1")
print("You will now be direct to the Main menu")
print("########################################")


def menu():
  choice = int(input(""))  
  if choice == 1:
    add_p()
  elif choice == 2:
    file = open("Saved_Password.txt", "r")
    test = file.read()
    print(test)
    file.close()

def add_p():
  file = open("Saved_Password.txt", 'a')

  print()
  print()

  usern = input("Please enter the username to access the website: ")

  passw = input("Please enter the password here: ")

  web = input("Please enter the website address: ")

  print()
  print()

  usrnm = "UserName: " + usern + "\n"
  pwd = "Password: " + passw + "\n"
  webs = "Website: " + web + "\n"

  file.write("##############################\n")
  file.write(usrnm)
  file.write(pwd)
  file.write(webs)
  file.write("\n##############################\n")
  file.write("\n")
  file.close()
  menu()

  

menu()