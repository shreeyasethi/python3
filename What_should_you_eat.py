dayofweek = input("What day is it today? (monday, tuesday, " \
+ "wednesday, thursday, friday) :")

hunger = input("Are you hungry on a scale of 1 to 5? "
+ "(1 - not very, 5 - super) :")
hunger = int(hunger) # convert to a number

print("If it's tuesday, "\
+ "I don't care how hungry you are. " \
+ "You should eat some tacos!")

print("If it's friday, "\
+ "I don't care how hungry you are. " \
+ "You should definitely be eating pizza...")

print("Otherwise,")

print("If your hunger level is less than 3, " \
+ "you should try a salad.")

print("If your hunger level is between 3 and 5, " \
+ "you're hungry enough to eat whatever.")

print("If your hunger level is 5, " \
+ "I see a giant burrito in your future.")

print("Otherwise, why are you taking a quiz? " \
+ "GO EAT EVERYTHING.")
