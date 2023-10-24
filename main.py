################### Scope ####################

enemies = 1

"""Between local and global variable"""

def increase_enemies():        #local
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()              #global
print(f"enemies outside function: {enemies}")