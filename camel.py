

print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! Survive your")
print("desert trek and outrun the natives.")

done = False
miles_traveled = 0
yhirst = 0
camel_tiredness = 0
natives_traveled = -20
canteen = 0

while done == False:
   print("A. Drink from your canteen.")
   print("B. Ahead moderate speed.")
   print("C. Ahead full speed.")
   print("D. Stop and rest.")
   print("E. Status check.")
   print("Q. Quit.")
   
   user_choice = input("What is your choice? ")

   if user_choice.upper() == "Q":
       done = True
   elif user_choice.upper() == "E":
       print("Miles traveled: " + str(miles_traveled))
       print("Drinks: " + str(drinks))
       print("Natives distance: ")
