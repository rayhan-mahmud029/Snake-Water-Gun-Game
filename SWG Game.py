import random


user_point = 0
pc_point = 0
l = 1

while True:
  daan = ["Snake", "Water", "Gun"] 
  choosing = random.choice(daan)
  print("Choose Your Weapen..")
  user_input = input("Snake, Water or Gun: \n")


  if l == 11:
    print('{0:*^100}'.format("GAME OVER"))
    break
  elif user_input == choosing:
    print("Result: draw!")
    print('{0: >100}'.format(f"Virtual user point = {pc_point}"))
    print('{0: >100}'.format(f"Your point = {user_point}"))
    print('{0: >100}'.format(f"Chances remaining = {10 - l}"))
    l += 1
    continue
    
     

  elif user_input == "Snake" and choosing == "Water":
    print("Your Snake drunk all the water...")
    print("Result: Hurra! You won.")
    user_point += 1
    print('{0: >100}'.format(f"Virtual user point = {pc_point}"))
    print('{0: >100}'.format(f"Your point = {user_point}"))
    print('{0: >100}'.format(f"Chances remaining = {10 - l}"))
    l += 1
    continue   
   


  elif user_input == "Water" and choosing == "Snake":
    print("Snake drunk all of your water...")
    print("Result: Alas! You lose.")
    pc_point += 1
    print('{0: >100}'.format(f"Virtual user point = {pc_point}"))
    print('{0: >100}'.format(f"Your point = {user_point}"))
    print('{0: >100}'.format(f"Chances remaining = {10 - l}"))
    l += 1
    continue

  elif user_input == "Gun" and choosing == "Snake":
    print("WoW! you shoot the Snake...")
    print("Result: Hurra! You won.")
    user_point += 1
    print('{0: >100}'.format(f"Virtual user point = {pc_point}"))
    print('{0: >100}'.format(f"Your point = {user_point}"))
    print('{0: >100}'.format(f"Chances remaining = {10 - l}"))
    l += 1
    continue
    

  elif user_input == "Snake" and choosing == "Gun":
    print("sHHit! your Snake died by Gun Shoot...")
    print("Result: Alas! You lose.")
    pc_point += 1
    print('{0: >100}'.format(f"Virtual user point = {pc_point}"))
    print('{0: >100}'.format(f"Your point = {user_point}"))
    print('{0: >100}'.format(f"Chances remaining = {10 - l}"))
    l += 1
    continue
    

  elif user_input == "Gun" and choosing == "Water":
    print("Oh noU! Water has drowned out you...")
    print("Result: Alas! You lose.")
    pc_point += 1
    print('{0: >100}'.format(f"Virtual user point = {pc_point}"))
    print('{0: >100}'.format(f"Your point = {user_point}"))
    print('{0: >100}'.format(f"Chances remaining = {10 - l}"))
    l += 1
    continue
    

  elif user_input == "Water" and choosing == "Gun":
    print("Oh yes! Your water flaw has drowned the Gun Man...")
    print("Result: Hurra! You won.")
    user_point += 1
    print('{0: >100}'.format(f"Virtual user point = {pc_point}"))
    print('{0: >100}'.format(f"Your point = {user_point}"))
    print('{0: >100}'.format(f"Chances remaining = {10 - l}"))
    l += 1
    continue
    
  
  else:
    print("Wrong input! Please, try again.")
    continue

print('{0:/^30}'.format("Results"))
print(f"*/Your Total Point = {user_point}")
print(f"*/Virtual Players Total Point = {pc_point}")
if user_point > pc_point:
  print('{0:*>30}'.format("Congratulations You Won!"))
else:
  print('{0:*>30}'.format("ShiTT man, You Lose!"))

  