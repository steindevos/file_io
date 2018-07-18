#!/usr/bin/python3
import sys
import json
from random import shuffle

print("Welcom to quiz version 1.0.2")
print(sys.argv)


def ask_questions(filename):
    score = 0
    n_answers_right = 0
    total_questions = 0
    highscore = {}
    highscore["name"] = input("Enter player name: ")
    
    with open(filename, "r") as f: 
        lines = f.read().split("\n")
    lines = lines[:-1]
    shuffle(lines)
    
    for line in lines[:10]:
        total_questions += 1
        qa = line.split("|")
        answer = input(qa[0] + " ")
        if qa[1].lower() == answer.lower(): 
            print("right answer")
            score+=2
            n_answers_right += 1
            print("score: {0}".format(score))
        else: 
            print("wrong answer! The correct answer is: {0}".format(qa[1]))
            score-=1
            print("score: {0}".format(score))
    
    highscore["score"] = score
    with open('highscores.txt', 'a') as outfile: 
        j = json.dumps(highscore) + "\n"
        outfile.write(j)   
    
    print("you got {0} answer right out of {1}. Your score is {2}".format(n_answers_right, total_questions, score)) 


def add_question(filename):
    question = input("Enter a question: ")
    answer = input("Okay, then tell me:  " + question.lower() +": ")
    text = question + "|" + answer + "\n" 
    
    with open(filename, "a") as f:
            f.write(text)
  

def show_highscores():
    with open("highscores.txt") as f: 
        scores = f.read()
        print(scores)

if sys.argv[1] == "--add":
    choice = input("Choose catagory (sports, music or the Netherlands): ")
    filename = "garbage-bin.txt"
    if choice.lower() == "sports":
        filename = "sports.txt"
    if choice.lower() == "music":
        filename = "music.txt"
    if choice.lower() == "the netherlands":
        filename = "netherlands.txt"
    add_question(filename)
    
if sys.argv[1] == "--ask": 
    choice = input("Choose catagory (sports, music or the Netherlands): ")
    filename = "garbage-bin.txt"
    if choice.lower() == "sports":
        filename = "sports.txt"
    if choice.lower() == "music":
        filename = "music.txt"
    if choice.lower() == "the netherlands":
        filename = "netherlands.txt"
    ask_questions(filename)

if sys.argv[1] == "--scores":
    show_highscores()

if sys.argv[1] == "--help":
    print("--add        Add a question to the quiz. You can choose from three categories: sports, music, and the Netherlands")
    print("--ask        Start the quiz. You can choose from three categories: sports, music, and the Netherlands")
    print("--scores     Show highscores")
    