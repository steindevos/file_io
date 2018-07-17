lines = [
   "This is the first line",
   "This is the second line",
   "This is the third line",
   "This is the fourth line"
   ]
  
def text_file(text):
    text = '\n'.join(sentence for sentence in text)
    with open('test.txt', 'w') as f:
        f.write(text)
    
    
text_file(lines)
    




