import json

employee = {}

employee["f_name"] = input("Enter first name: ")
employee["l_name"] = input("Enter last name: ")
employee["age"] = int(input("Enter age: "))
n_coding_languages = int(input("How many coding languages can you 'speak': "))
employee["coding_languages"] = [input("language {0}: ".format(i + 1)) for i in range(n_coding_languages)]


with open('data.txt', 'a') as outfile: 
    j = json.dumps(employee) + "\n"
    outfile.write(j)    
    