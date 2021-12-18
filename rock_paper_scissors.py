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

rps_inp = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
rps = [rock,paper,scissors]
print(f"\nYou have chosen\n{rps[rps_inp]}")
comp = random.randint(0,2)
print (f'\nThe computer has chosen\n{rps[comp]}')

if rps_inp == 0 and comp == 1:
  print ("Paper beats Rock, Computer wins.")
elif rps_inp == 0 and comp == 2:
  print ("Congratulations! Rock beats Scissors, You Win!")
elif rps_inp == 1 and comp == 0:
  print ("Congratulation! Paper beats Rock, You win!")
elif rps_inp == 1 and comp == 2:
  print ("Scissors beats Paper, Computer Wins.")
elif rps_inp == 2 and comp == 0:
  print ("Rock beats Scissors, Computer Wins.")
elif rps_inp == 2 and comp == 1:
  print ("Congratulations! Scissors beats Paper, You win!")
else:
  print ("It is a tie, please play again.")
