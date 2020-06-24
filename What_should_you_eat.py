dayofweek = input("What day is it today? (monday, tuesday, " \
+ "wednesday, thursday, friday) :")

hunger = input("Are you hungry on a scale of 1 to 5? "
+ "(1 - not very, 5 - super) :")
hunger = int(hunger) # convert to a number

if dayofweek.lower() == "tuesday":
  print("I don't care how hungry you are. " \
  + "You should eat some tacos!")
elif dayofweek.lower() =="friday":
  print("I don't care how hungry you are. " \
  + "You should definitely be eating pizza...")

elif hunger < 3:
  print("you should try a salad.")
elif hunger == 3:
  print("you're hungry enough to eat whatever.")
elif hunger < 5:
  print("I see a giant burrito in your future.")
else: 
  print("Why are you taking a quiz? " \
  + "GO EAT EVERYTHING.")
