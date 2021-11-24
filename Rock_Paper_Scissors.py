import random



rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

you = input("What do you choose?")

if you == "paper":
  print(paper)
elif you == "rock":
  print(rock)
else:
  print(scissors)



options = ["rock", "paper", "scissors"]

computer = random.choice(options)

if computer == "rock":
  print(rock)
elif computer == "paper":
  print(paper)
else:
  print(scissors)


print(f"Computer chose {computer}")

if you == "rock" and computer == "paper":
  print("You lose")
elif you == "rock" and computer == "scissors":
  print("You win")
elif you == "paper" and computer == "scissors":
  print("You lose")  
elif you == "paper" and computer == "rock":
  print("You win")
elif you == "scissors" and computer == "rock":
  print("You lose")
elif you == "scissors" and computer == "paper":
  print("You win")
else:
  print("It is draw")  











