import random
rock= """
    _________  
---'     ____)___
        (________)_
        (__________)
        (________)
----.____(_____)
"""
paper="""
    _________
---'    _____)_________
             __________)_____
            _________________)
          _________________)
 ---.________________)           
"""
scissors=""""
    _________
---'    _____)_________
              _________)_____
        _____________________)
        (_________)
---.__(_______)
"""
game_images = [rock,paper,scissors]
while True:
    user_choice=int(input("\n0 for rock \n1 for paper \n2 for Scissors \n3 for exit \n\n\nEnter your choice:"))
    if user_choice ==3:
        print("Game closed")
        break
    elif user_choice > 3 or user_choice <0:
        print("Invalid number")
    else:
        print(game_images[user_choice])
        computer_choice=random.randint(0,2)
        print("Computer Chose:", computer_choice)
        print(game_images[computer_choice])
        if computer_choice == user_choice:
            print("It's a draw.")
        elif computer_choice == 0 and user_choice == 2:
            print("You lose")
        elif user_choice == 0 and computer_choice == 2:
            print("You Win!")
        elif computer_choice > user_choice:
            print("You lose")
        elif user_choice>computer_choice:
            print("You Win!")