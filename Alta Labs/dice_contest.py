from cheatdice import *

def main():

    swapper = Cheat_Swapper()

    loaded_dice = Cheat_Loaded_Dice()

    #track scores
    swapper_score = 0
    loaded_dice_score = 0

    #how many games
    number_of_games = 10000000
    game_number = 0

    #begin 
    print("Simulation Running")
    print("===================")
    while game_number < number_of_games:
        swapper.roll()
        loaded_dice.roll()

        swapper.cheat()
        loaded_dice.cheat()

        if sum(swapper.get_dice()) == sum(loaded_dice.get_dice()):
            #print("Draw")
            pass
        elif sum(swapper.get_dice()) > sum(loaded_dice.get_dice()):
            #print("Dice swapper wins")
            swapper_score += 1
        else:
            #print("loaded dice wins")
            loaded_dice_score += 1
        game_number += 1

    print("Simulation Complete")
    print("Swapper won", swapper_score, "times. With a percentage of", swapper_score/number_of_games)
    print("Loaded dice won", loaded_dice_score, "times. With a percentage of", loaded_dice_score/number_of_games)
    

    if swapper_score == loaded_dice_score:
        print("Game was drawn")
    elif swapper_score > loaded_dice_score:
        print("Swapper won most games")
    else:
        print("Loaded dice won most games")

main()