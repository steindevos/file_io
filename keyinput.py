name = input("Enter name: ")
n_children = int(input("How many children do you have? "))
children = [input("What is the name of child {0}: ".format(i + 1)) for i in range(n_children)]

print("hello {0}, your children are named {1} and {2}".format(name, ', '.join(children[0:len(children)-1]), children[len(children)-1]))

