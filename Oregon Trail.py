#Chris Hogan

import random, colors
name = input("What is your name?")
date = [3, 1]
miles_traveled = 0
health = 5
food = 500
monthly_health = [random.randint(1,31),random.randint(1,31)]
quit = 0
last = [miles_traveled, health, food]
last_colors = [colors.blue, colors.blue, colors.blue]

def select_action():
  action = input("Enter an action: ")
  return action

def health_lose():
  global date, monthly_health, health
  if date[1] >= monthly_health[0]:
    health -= 1
    monthly_health[0] = 100
  if date[1] >= monthly_health[1]:
    health -= 1
    monthly_health[1] = 100
  
def date_change(x,y):
  global date, food, health, monthly_health, last
  days_traveled = random.randint(x,y)
  food -= 5 * days_traveled
  if date[0] == 3 or date[0] == 5 or date[0] == 7 or date[0] == 8 or date[0] == 10 or date[0] == 12:
    date[1] += days_traveled
    health_lose()
    if date[1] >= 32:
      date[1] -= 31
      date[0] += 1
      if date[0] == 8:
        monthly_health = [random.randint(1,31),random.randint(1,31)]
      else:
        monthly_health = [random.randint(1,30),random.randint(1,30)]
  elif date[0] == 4 or date[0] == 6 or date[0] == 9 or date[0] == 11:
    date[1] += days_traveled
    health_lose()
    if date[1] >= 31:
      date[1] -= 30
      date[0] += 1
      monthly_health = [random.randint(1,31),random.randint(1,31)]
  
def status():
  global date, miles_traveled, health, food, last, last_colors
  current = [miles_traveled, health, food]
  index = 0
  while index < 3:
    if last[index] > current[index]:
      last_colors[index] = colors.red
    if last[index] < current[index]:
      last_colors[index] = colors.green
    index += 1
  print (last_colors[1]('Health:' + str(health)))
  print (last_colors[0]('Miles traveled:' + str(miles_traveled)))
  print (last_colors[2]('Food left:' + str(food) + 'lbs'))
  print (colors.blue('Date:' + str(date)))

def travel():
  global miles_traveled, last
  last = [miles_traveled, health, food]
  miles_walked = random.randint(30, 60)
  miles_traveled += miles_walked
  date_change(3,7)
  
def rest():
  global health, last
  last = [miles_traveled, health, food]
  if health < 5:
    health += 1
    date_change(2,5)
  else:
    print('You are full HP')
  
def hunt():
  global food, last
  last = [miles_traveled, health, food]
  food += 100
  date_change(2,5)

while date[0] < 13 and health > 0 and food > 0 and miles_traveled < 2000 and quit == 0:
  action = select_action()
  if action == 'travel':
    travel()
  elif action == 'status':
    status()
  elif action == 'rest':
    rest()
  elif action == 'hunt':
    hunt()
  elif action == 'help':
    print('Commands: travel, rest, hunt, status, help, quit')
  elif action == 'quit':
    quit = 1
if miles_traveled >= 2000:
  print (colors.green(name + ' you won'))
elif date[0] == 13 or health <= 0 or food <= 0:
  print (colors.red(name + ' you died'))