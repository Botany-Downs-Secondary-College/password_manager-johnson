#Created by Johnson Zhang
#24/02/2021
#Ver. 0.1

import os.path

def menu():
  print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
  print("Please choose your option:")
  choice = int(input("1. Add new Password details\n2. View password list\n3. Exit the program\n"))
  if choice == 1:
    write_txt()
  elif choice == 2:
    read()
  elif choice == 3:
    exit()
  else:
    print("Please enter the right number !!")
    menu()

def checktext():
  if os.path.exists("Saved_Password.txt"):
    pass
  else:
    file = open("Saved_Password.txt", 'w')
    file.close()

def write_txt():
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
  file.close
  choice()

def choice():
  choice = int(input("1. Do you wish to add more Passwords?\n2. View the password list\n3. Head back to the main menu\n"))
  if choice == 1:
    write_txt()
  elif choice == 2:
    read()
  elif choice == 3:
    menu()
  else:
    print("Please enter a valid number")
    choice()

def read():
  file = open('Saved_Password.txt', 'r')
  cont = file.read()
  print(cont)
  file.close()
  choice()

checktext()
print("########################################")
print("Welcome to Password_Manager_0.1")
print("You will now be direct to the Main menu")
print("########################################")
menu()