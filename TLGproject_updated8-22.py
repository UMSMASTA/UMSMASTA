
#importing modules
import csv
import random
import time
import pandas
import crayons

#File path, goal for this is to pull from github, then we take the raw .csv file and read it via pandas
url = 'https://raw.githubusercontent.com/UMSMASTA/UMSMASTA/main/Actors.csv'
raw_csv_file = pandas.read_csv(url, encoding='latin1')



#then we convert the dataset to a dictionary
csv_dict_list = raw_csv_file.to_dict('records')

#random choice , will be in main        
random_actor = random.choice(csv_dict_list)

#Intro game startup
def game_startup():
    username = input("What is your name? ")
    print("Greetings," , username +"! Here is how the game will go.\n")
    time.sleep(1)
    print("You have five chances to guess the actor from the movie and year I provide you.\n")
    time.sleep(3)
    print("Good Luck!\n")
    time.sleep(1)
    return username




#variables assigned to 5 movies, randomized.
movie_key = ['Movie1', 'Movie 2', 'Movie3', 'Movie4', 'Movie5']

def main(username):



    random_actor = random.choice(csv_dict_list)
   
    
#for loop to take selected actor name and make a wheel of fortune-esque blank space.
    blanks = ['_' if char.isalpha() else ' ' for char in random_actor['Name']]
    print(' '.join(blanks))

    #variable to define the answer the user must type
    actor_answer = random_actor['Name'].lower()
    #Defining how many turns the user has to guess correctly
    attempt = 5
    movie_hint_counter = 0
    #keep track of correctly guessed letters
    guessed_letters = []

    #list to keep track of used movies 
    used_movies = []

    #list to show random letters 
    unrevealed_letters = []
    for i, char in enumerate(actor_answer):
        if blanks[i] == '_':
            unrevealed_letters.append(i)

#While loop for the guessing
    while attempt > 0:

        random_movie_key = random.choice([key for key in movie_key if key not in used_movies])
        used_movies.append(random_movie_key)
        random_movie = random_actor[random_movie_key]
        movie_hint_counter += 1
        print("\n------------------------------------")
        print("Movie hint #" , movie_hint_counter, random_movie)
        guess = str(input("Type your guess: ").lower())
        
        print(' '.join(blanks))
        #win condition, with a loop to play again
        if guess == actor_answer:
            print(actor_answer.title())
            print("You have guessed the correct actor! Well done", username + '!')
            time.sleep(1)
            play_again = input("\nWould you like to try again? (Y/N): ")
            if play_again.lower() == "y":
                main(username)
            else:
                break
        #oount down attempts
        else:
            attempt = attempt - 1
            print(f"\nYou have {attempt} attempts remaining..\n")
            if unrevealed_letters:
                #variable to assign a random letter to show as a hint
                random_unrevealed_index = random.choice(unrevealed_letters)
                blanks[random_unrevealed_index] = actor_answer[random_unrevealed_index]
                unrevealed_letters.remove(random_unrevealed_index)  # Remove the revealed index
                print("Here's a hint: " + ' '.join(blanks))
            else:
                print("No more letters to reveal!")
            
 



        if attempt == 0:
            print('You have run out of attempts! The correct actor was: ', actor_answer.title())
            play_again = input("\nWould you like to try again? (Y/N): ")
            if play_again.lower() == "y":
                main(username)
            else:
                break

username = game_startup()
main(username)



