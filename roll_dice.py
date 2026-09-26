import random
while True:
    number = random.randint(1,6)
    roll = input("Do u want to roll dice > y/n <").strip().lower()       # 'y' determines yes
    if roll == 'y':                                                      # 'n' determines no
        print("Number rolled from dice is", number)
    elif roll == 'n':
        print("U quit the game")
        break
    else:
        print("invalid command")
