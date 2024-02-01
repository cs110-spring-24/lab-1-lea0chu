import random

cpu = random.randint(1,3)
user = input("Enter rock, paper, or scissors: ")

if user == "rock":
  print("You chose rock.")
  if cpu == 1:  #cpu chose rock
    print("The computer chose rock.")
    print("It's a Tie!")
  elif cpu == 2: #cpu chose paper
    print("The computer chose paper.")
    print("You Lost.")
  else: #cpu chose scissors
    print("The computer chose scissors.")
    print("You won!")
if user == "paper":
   print("You chose paper.")
   if cpu == 1: #cpu chose rock
     print("The computer chose rock.")
     print("You Won!")
   elif cpu == 2: #cpu chose paper
      print("The computer chose paper.")
      print("It's a Tie!")
   else: #cpu chose scissors
      print("The computer chose scissors.")
      print("You Lost.")
if user == "scissors":
  print("You chose scissors.")
  if cpu == 1: #cpu chose rock
     print("The computer chose rock.")
     print("You Lost.")
  elif cpu == 2: #cpu chose paper
     print("The computer chose paper.")
     print("You Won!")
  else: #cpu chose scissors
     print("The computer chose scissors.")
     print("It's a Tie!")


