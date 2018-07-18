import json

def show_menu(): 
    print("1. Ask question")
    print("2. Add a question")
    print("3. Print highscores")
    print("4. Exit")
    
    return input("Enter choice: ")

def ask_questions():
    score = 0
    n_answers_right = 0
    total_questions = 0
    highscore = {}
    highscore["name"] = input("Enter player name: ")
    
    with open("questions.txt", "r") as f: 
        lines = f.read().split("\n")
    lines = lines[:-1]
    
    
    for line in lines:
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
    
def add_question():
    question = input("Enter a question: ")
    answer = input("Okay, then tell me:  " + question.lower() +": ")
    text = question + "|" + answer + "\n" 
    
    with open("questions.txt", "a") as f:
        f.write(text)

def show_highscores():
    with open("highscores.txt") as f: 
        scores = f.read()
        print(scores)

def main():
    while True: 
        choice = show_menu()
        
        if choice == "1": 
            ask_questions()
            
        if choice == "2":
            add_question()
        
        if choice == "3": 
            show_highscores()
        
        if choice == "4": 
            break 
main()
