from pathlib import Path
import json

path = Path('quiz_game.json')

def create_questions():
    number_of_questions = input("How many questions do you want in your quiz? ")
    if number_of_questions.isdigit():
        number_of_questions = int(number_of_questions)
    else:
        while True:
            number_of_questions = input("How many questions do you want in your quiz? ")
            if number_of_questions.isdigit():
                number_of_questions = int(number_of_questions)
                break
    while number_of_questions == 0:
        number_of_questions = input("How many questions do you want in your quiz? ")
        if number_of_questions.isdigit():
            number_of_questions = int(number_of_questions)
    list = []
    list1 = []
    for question in range(0,number_of_questions):
        a = input(f"What is your {question+1} question? ")
        a = a.lower()
        b = input("What is the answer to that question? ")
        b = b.lower()
        list.append(a)
        list1.append(b)
    dictionary = dict(zip(list,list1))
    return dictionary

def store_data():
    dictionary = create_questions()
    contents = json.dumps(dictionary)
    path.write_text(contents)
    print("The questions and answers are stored.")
    p = input("Do you which to play it now? (yes/no) ")
    if p == "yes":
        play()
    else:
        print("Run this code again if you wish to play!")

def play():
    guesses = []
    correct_answers = 0
    if path.exists():
        play = input("Are you ready to play an existing game? (yes/no) ")
        key = path.read_text()
        dictionary = eval(key)
        if play != 'no':
            for question in dictionary:
                print(question)
                guess = input("What is the answer to this question? ")
                guess = guess.lower()
                if guess == dictionary[question]:
                    print("Correct")
                    correct_answers += 1
                else:
                    print("Incorrect")
                    correct_answers +=0
                guesses.append(guess)
            print("Your score is: ",round((correct_answers/len(dictionary))*100),"%")
        else:
            next = input("Do you want to make a game? (yes/no) ")
            if next == 'yes':
                store_data()
            else:
                print("Good bye")
    else:
        store_data()

play()

