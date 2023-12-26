import random

def play():
  user = input("'r' for rock, 'p' for paper, 's' for scissors: ")
  computer = random.choice(['r', 'p', 's'])
  if user == computer:
    return (f"Computer's choice was: {computer} \nIt's a tie!")
  
  return winner(user, computer)
  
def winner(player, opponent):
  if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
    return (f"Computer's choice was: {opponent} \nYou won!")
  else:
    return (f"Computer's choice was: {opponent} \nYou lost!")
  
print(play())