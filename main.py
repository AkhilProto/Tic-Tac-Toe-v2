import math
name= input("Enter your Name: ")
option= input("MaximaxAI: Woah... So " + name + ", You wanna beat me in this game of Tic-Tac-Toe? Y/N: ")

if option == 'y' or 'Y':
  
  with open("actualgame.py") as f:
    exec(f.read())

elif option == 'n' or 'N':
    print("Ok then Loser, Go on and do your boring stuff in your boring life.")

else:
    print("What did you say? Run this thing again.")








