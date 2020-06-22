import random

characters = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*+="

print("Welcome! Today we will create a password for you to keep your accounts safe.")
print("\n")
pickcharacters=int(input("How many characters long do you want you password to be?"))
print ("Here is your new password:")
print("\n")

password = ""
for x in range(pickcharacters): 
  password = password + random.choice(characters)

  print(password)


  
