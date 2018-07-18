def show_menu(): 
    print("1. Ask question")
    print("2. Add a question")
    print("3. Exit")
    
    return input("Enter choice: ")

def ask_questions():
    print("You chose to ask the questions")
    
def add_question():
    print("You chose to add a question")

def main():
    while True: 
        choice = show_menu()
        
        if choice == "1": 
            ask_questions()
            
        if choice == "2":
            add_question()
        
        if choice == "3": 
            break
    
main()
