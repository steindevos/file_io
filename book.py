# import itertools
# import operator
import collections
import re

f = open("data/1155-0.txt")
text = f.read()

words = re.findall('\w+', text.lower())
long_words = [i for i in words if len(i) >= 4]


counter = collections.Counter(long_words)

print(counter.most_common(20))









# f.close()

# new_words = ["hello", "world", "hello", "hello", "and", "and"]

# frequency_dict = {}

# for word in words: 
#     existing = frequency_dict.get(word, 0)
#     new = existing + 1
#     frequency_dict[word] = new
        
# print(max(frequency_dict.values()))
