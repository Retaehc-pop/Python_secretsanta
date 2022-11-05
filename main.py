import os
import random

def random_player(player):
  original_player = player[:]
  already_play = []
  while (len(player)!=0):
    clear("Are you ready to know your secret santa?","player:"+",".join(original_player))
    print(player)
    name = input("what is your name? : ")
    if name not in original_player:
      if name in already_play:
        print("this user already play, Try again")
      else:
        print("incorrect username, Try again")
      input("press enter to clear the screen to Try again....")
      continue
    else:
      already_play.append(name)
    add_name = False
    if name in player:
      player.pop(player.index(name))
      add_name = True
    secret_santa = random.choice(player)
    player.pop(player.index(secret_santa))
    if add_name:
      player.append(name)
    print("Your secret santa is : ",secret_santa)
    input("press any key to clear the screen for the next player....")
  clear("all Secret santa has been selected!")


def input_player(player_num):
  player = []
  while player_num!=len(player):
    name = input(f"name of the player {len(player)+1}:")
    if name in player:
      print("player already exists")
    else:
      player.append(name)
    clear()
  return player

def clear(*oldmsg):
  os.system('cls')
  print("""
 _______  _______  _______  _______  _______  _________   _______  _______  _       _________ _______ 
(  ____ \(  ____ \(  ____ \(  ____ )(  ____ \ \__   __/  (  ____ \(  ___  )( (    /|\__   __/(  ___  )
| (    \/| (    \/| (    \/| (    )|| (    \/    ) (     | (    \/| (   ) ||  \  ( |   ) (   | (   ) |
| (_____ | (__    | |      | (____)|| (__        | |     | (_____ | (___) ||   \ | |   | |   | (___) |
(_____  )|  __)   | |      |     __)|  __)       | |     (_____  )|  ___  || (\ \) |   | |   |  ___  |
      ) || (      | |      | (\ (   | (          | |           ) || (   ) || | \   |   | |   | (   ) |
/\____) || (____/\| (____/\| ) \ \__| (____/\    | |     /\____) || )   ( || )  \  |   | |   | )   ( |
\_______)(_______/(_______/|/   \__/(_______/    )_(     \_______)|/     \||/    )_)   )_(   |/     \|
        """)
  for msg in oldmsg:
    print(msg)

def main():
  clear()
  player_num = int(input("input number of player : "))
  while player_num<=3:
    print("player not enough! need at least 3 player to play secret santa")
    player_num =  int(input("input number of player : "))
  players = input_player(player_num)
  random_player(players)

  

  
if __name__ == "__main__":
  main()