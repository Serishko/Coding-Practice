#Solution to the problem described in https://www.youtube.com/watch?v=PIeiiceWe_w&t=280s

import re

phonenumber = input("Enter the phone number:")
words_length = input("Enter the length of the words:")
words = []
for i in range(int(words_length)):
    words.append(input("Enter the word:"))

labels = {2:['a','b','c'], 3:['d','e','f'], 4:['g','h','i'], 5:['j','k','l'], 6:['m','n','o'], 7:['p','q','r','s'], 8:['t','u','v'], 9:['w','x','y','z']}

new_words_to_numeric = []
for i in words:
    words_to_numeric = []
    for j in i:
        for k in range(2,10):
            if j in labels[k]:
                words_to_numeric.append(str(k))
    new_words_to_numeric.append(''.join(words_to_numeric))
new_list = []
for i in range(len(new_words_to_numeric)):
    try:
        a = re.search(f".*{new_words_to_numeric[i]}.*", phonenumber).group()
        if a == phonenumber:
            new_list.append(words[i])
    except:
        pass

print(sorted(new_list))
