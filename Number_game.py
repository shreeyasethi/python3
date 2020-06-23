import time
import random

while True:
  topic = input('''What math skill would you like to work on today?
\nAddition, Subtraction, Multiplication, or all topics?''')
  print("Type STOP when you want to exit the current topic and move on to another one.")
  time.sleep(0.8)

  if topic.lower() == "addition":
    while True:
      number1=random.randint(1,100)
      number2=random.randint(1,100)
      answer=input("What is " + str(number1) + '+' + str(number2) + '?') 
      if answer == str(number1 + number2): 
          print("\nCorrect! Great Job!")
      elif answer.upper() == "STOP":
        break
      else: 
        print("\nNope! The correct answer is " + str(number1 + number2) + '.')
        

  if topic.lower() == "subtraction":
    while True:
      number1=random.randint(1,100)
      number2=random.randint(1,100)
      answer=input("What is " + str(number1) + '-' + str(number2) + '?') 
      if answer == str(number1 - number2): 
        print("\nCorrect! Great Job!")
      elif answer.upper() == "STOP":
        break
      else: 
        print("\nNope! The correct answer is " + str(number1 - number2) + '.')


'''
if topic == "Multiplication" or "multiplication":
  number1=random.randint(1,100)
  number2=random.randint(1,100)
  answer=input("What is " + str(number1) + 'X' + str(number2) + '?') 
  if answer == str(number1 * number2): 
    print("\nCorrect! Great Job!")
  
  else: 
    print("\nNope! The correct answer is " + str(number1 * number2) + '.')
    


if topic == "All Topics" or "all Topics" or "all topics" or "All topics": 
  number1=random.randint(1,100)
  number2=random.randint(1,100)
  answer=input("What is " + str(number1) + '+' + str(number2) + '?') 
  if answer == str(number1 + number2): 
    print("\nCorrect! Great Job!")
  else: 
    print("\nNope! The correct answer is " + str(number1 + number2) + '.')

  number1=random.randint(1,100)
  number2=random.randint(1,100)
  answer=input("What is " + str(number1) + '-' + str(number2) + '?') 
  if answer == str(number1 - number2): 
    print("\nCorrect! Great Job!")
  
  else: 
    print("\nNope! The correct answer is " + str(number1 - number2) + '.')
    
  number1=random.randint(1,100)
  number2=random.randint(1,100)
  answer=input("What is " + str(number1) + 'X' + str(number2) + '?') 
  if answer == str(number1 * number2): 
    print("\nCorrect! Great Job!")
  
  else: 
    print("\nNope! The correct answer is " + str(number1 * number2) + '.')
    
  '''  
