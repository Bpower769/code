import sys
import random

def attack_likes():
  enemy_health = 40
# the menu
print('                   ')
print('PYTHION v0.1')
print('                   ')
print('------------------------------')
print('PLAY[1]')
print('INFO[2]')
print('TUTORIAL[3]')
print('QUIT[4]')


while True:
  t = input('>>>')
  # input buttons
  if t == "4": sys.exit(0)
  if t == "2": print('This is a indie text based video game coded by Braden Maclemale!')
  if t == "3": print('The Tutorial is not Yet Ready')
  if t == "1": break

# character name stuff
while True:
  print('------------------------------')
  print('                   ')
  e = input('Enter a Character Name Here:')
  print('                   ')
  print('------------------------------')
  print('                   ')
  print('Is This Correct?, ' + e)
  print('                   ')
  print('------------------------------')
  print('                   ')
  x = input('Answer YES[1] or N0[2] :')
  print('                   ')
  if x == "1": break

print('                   ')
print('Ok Lets Start Playing!')
print('                   ')
print('------------------------------')



while True:
  t = input('>>>')
  if t == "i": print('              INVENTORY            ')
  print('              | Sword |    ') 
  print('              |  Bow  |   ') 
  print('              --------- ')
  print('------------------------------')
  print('                   ')
  


