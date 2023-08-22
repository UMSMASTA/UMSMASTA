
#importing modules
import csv
import random
import time

#File path, goal for this is to pull from github
csv_file_path = 'C:\\Users\\pauly\\Desktop\\CS251\\cs251-hop01-introduction-to-r-UMSMASTA\\UMSMASTA\Actors.csv'

#list that will house the dictionary/.csv being read below
csv_dict_list = []
#opening up the .csv file and converting it into a dictionary
with open(csv_file_path, 'r') as csv_file:
    csv_dict_reader = csv.DictReader(csv_file)
    csv_dict_list = list(csv_dict_reader)

#random choice , will be in main        
random_actor = random.choice(csv_dict_list)

print(random_actor)   

#Intro game startup
def game_startup():
    username = input("What is your name? ")
    print("Greetings," , username +"! Here is how the game will go.\n")
    time.sleep(1)
    print("You have five chances to guess the actor from the movie and year I provide you.\n")
    time.sleep(3)
    print("Good Luck!")

#Things to do:


#variables assigned to 5 movies, randomized.
movie_key = ['Movie1', 'Movie 2', 'Movie3', 'Movie4', 'Movie5']
random_movie_key = random.choice(movie_key)
random_movie = random_actor[random_movie_key]

def main():

    random_actor = random.choice(csv_dict_list)
   
    game_startup()
    
#for loop to take selected actor name and make a wheel of fortune-esque blank space.
    blanks = ['_' if char.isalpha() else ' ' for char in random_actor['Name']]
    print(' '.join(blanks))

    #variable to define the answer the user must type
    actor_answer = random_actor['Name'].lower()
    #Defining how many turns the user has to guess correctly
    attempt = 5
    #keep track of correctly guessed letters
    guessed_letters = []
#While loop for the guessing
    while attempt > 0:
        print('\n'+ random_movie)
        guess = str(input("Type your guess: ").lower())
        if guess == actor_answer:
            print("You have guessed the correct actor! Well done", username , '!')
            break
        else:
            attempt = attempt - 1
            print(f"You have {attempt} attempts remaining..\n")
            new_blanks = []

        #check for correct letters and positions
        for actor_char, guess_char, blank_char in zip(actor_answer, guess, blanks):
            if actor_char == guess_char:
                new_blanks.append(actor_char)
            else:
                new_blanks.append(blank_char)

        blanks = new_blanks
        print(' '.join(blanks))
        print("Guessed letters:", ' '.join(guessed_letters))  # Print guessed letters

        if attempt == 0:
            print('You have run out of attempts! The correct actor was: ', actor_answer)

main()




