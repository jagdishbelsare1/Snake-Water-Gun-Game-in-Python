import random
#s>w w>g g>s
def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True    
print("Computer Turn: snake(s) water(w) or gun(g)")
randonNo = random.randint(1, 3)
if randonNo == 1:
    comp = 's'
elif randonNo == 2:
    comp = 'w'
elif randonNo == 3:
    comp = 'g'

you = input("Your Turn: snake(s) water(w) gun(g): ")
print(f"Computer select {comp}")
print(f"Your select {you}")

a = gameWin(comp, you)

if a == None:
    print("Game is tie")
elif a:
    print("You Win")
else:
    print("You lost the Game")
