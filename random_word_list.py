f = open("/Users/rohansenan/Desktop/python_stuff/wordle/five_letter_words.txt", "r")
lines = f.readlines()
results = []
for x in lines:
    results.append(x.split(' ')[5].lower())
dictionary = []
for x in results:
    dictionary.append(x.strip())
f.close()

file = open("/Users/rohansenan/Desktop/python_stuff/wordle/word_list.txt", "r")
lines = file.readlines()
full_word_list = []
for word in lines:
    full_word_list.append(word.strip())

