#Password Manageer v2.0
#Made by Johnson Zhang Copy-right
#Pre-Realease Simple_Password_Manager
#Creating a .txt file, Reading from .txt file, Write to .txt file
#Added No_Option_List makes the program more human like
#Added Encryption
#Added function to check if Cryptography is installed on the computer

import os.path, os, random
no_option_list = ['There is no such option avaliable, please enter again!','You have entered an invalid option, please try again!','Your option is invalid, please enter again!','There is no option for what you have entered, try again!']

def install():
    import sys
    import subprocess
    import pkg_resources
    
    required = {'Cryptography'}
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed
    
    if missing:
        python = sys.executable
        subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
        print("Cryptography is installed!!!")
    else:
        print("Cryptography is already installed, no need for futher installation!")

def create(cap_user, st_password):
    if os.path.exists("{}_Password.txt".format(cap_user)):
        from cryptography.fernet import Fernet
        # using the key
        with open('filekey.key', 'rb') as filekey:
            key = filekey.read()
        fernet = Fernet(key)
          
        # opening the encrypted file
        with open('{}_Password.txt'.format(cap_user), 'rb') as enc_file:
            encrypted = enc_file.read()
          
        # decrypting the file
        decrypted = fernet.decrypt(encrypted)
          
        # opening the file in write mode and
        # writing the decrypted data
        with open('{}_Password.txt'.format(cap_user), 'wb') as dec_file:
            dec_file.write(decrypted)   

        if passcheck('{}_Password.txt'.format(cap_user), 'MASTERKEY: {}'.format(st_password)):
            print("Please do add Password after you signed in !!!!")
            global rise 
            rise = 1
            menu(cap_user)
            
        else:
            main()            
    else:
        print("\nWelcome {} ! Enjoy you experience by using our app!!!\n".format(cap_user))
        mp = "################## MASTERKEY: {} ##############################\nPlease Don't Change the MASTERKEY, as this is you personal login password!!!!\n############################################################\n".format(st_password)
        file = open("{}_Password.txt".format(cap_user), 'w')
        file.write(mp)
        file.close()   
        print("Your login detail has been created!!!!")
        menu(cap_user)

def passcheck(file_name, string_to_search):    
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            if string_to_search in line:
                return True
    return False


def write(cap_user, username, password, website):   
    file = open("{}_Password.txt".format(cap_user), 'a')
    file.write('UserName: ' + username + '\n')
    file.write('Password: ' + password + '\n')
    file.write('Website: '+ website + '\n' + '############################################################')
    file.close() 
    print("Success")
    print("$$$$$$$$$$$$$$$$$")
    print("Encrypting......")
    encryption(cap_user)
    
def encryption(cap_user):
    from cryptography.fernet import Fernet
    # key generation
    key = Fernet.generate_key()
      
    # string the key in a file
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)
       
    # opening the key
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()
      
    # using the generated key
    fernet = Fernet(key)
      
    # opening the original file to encrypt
    with open('{}_Password.txt'.format(cap_user), 'rb') as file:
        original = file.read()
          
    # encrypting the file
    encrypted = fernet.encrypt(original)
      
    # opening the file in write mode and 
    # writing the encrypted data
    with open('{}_Password.txt'.format(cap_user), 'wb') as encrypted_file:
        encrypted_file.write(encrypted) 
        
    print("Succeed!")
    print("$$$$$$$$$$$$$$$$$")
    menu(cap_user)
    
def read(cap_user):
    from cryptography.fernet import Fernet
    # using the key
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
      
    # opening the encrypted file
    with open('{}_Password.txt'.format(cap_user), 'rb') as enc_file:
        encrypted = enc_file.read()
      
    # decrypting the file
    decrypted = fernet.decrypt(encrypted)
      
    # opening the file in write mode and
    # writing the decrypted data
    with open('{}_Password.txt'.format(cap_user), 'wb') as dec_file:
        dec_file.write(decrypted)   
    
    file = open("{}_Password.txt".format(cap_user), 'r')
    print(file.read())
    file.close()
    encryption(cap_user)
    
def menu(cap_user):
    while True:
        try:
            print("\nHello {}, this is your personal password manager!".format(cap_user))
            print("Please follow the instruction and enter the details you wants to save")
            print("#####################################################################")
            print("TO ADD PASSWORD PRESS 1\nTo VIEW PASSWORD PRESS 2\nEXIT PRESS 3")
            mode = int(input("Please enter you number:\n>>> "))
            if mode == 1:
                
                username = input("Please enter the username to access the website:\n>>> ")
        
                password = input("Please enter the password here:\n>>> ")
        
                website = input("Please enter the website address:\n>>> ")  
                
                write(cap_user, username, password, website)
          
            elif mode == 2:
                read(cap_user)
            
            elif mode == 3:
                exit()
                
        except ValueError:
            print(f'{random.choice(no_option_list)}')

        
def main():
    print("############################################################")
    print("Welcome to Password_manager pre_realeas v 2.0")
    print("############################################################")
    print("""\nIf you're a new user, kindly give us your 
    name and we will register a account for you!\n""")
    print("############################################################")
    print("""If you are a exsiting user, Just enter your name, and the 
    system will direct you to your file!\n""")
    print("############################################################")
    
    user = input("Could you please tell us your name?\n>>> ")
    global cap_user
    cap_user = user.capitalize()
    
    password = input("Please enter your password!/Or to make your new password\n>>> ")
    global st_password
    st_password = password.strip()
    
    create(cap_user, st_password)
        
#Main Program
install()
print("##################################")
print("Password_Manager Pre_Release v2.0")
print("##################################")
while True:
    try:
        age = float(input("Your age Please!\n>>> "))
        if age < 13:
            print("Not old enought :(")
            exit()
        elif age >= 13:
            main()
            
    except ValueError:
        print(f'{random.choice(no_option_list)}')
        print("ENTER A NUMBER!!!!")
        
        