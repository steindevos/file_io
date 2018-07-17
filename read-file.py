
# f = open("data/data.txt")
# text = f.read()
# f.close()

# lines = text.split('\n')

# print(text)
# print(lines)

with open("data/data.txt") as f: #like so you don't have to use the close() function
    text = f.read() 

print(text)