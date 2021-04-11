"""Case-study 
Developers:   Ignatovich D. (60%),
              Miller A. (30%),
              Poylova E. (40%)
""" 
import re
import random

def open_initial_text():
    with open('input.txt', "r") as f_in:
        initial_text = ''
        for lines in f_in:
            lines.replace("\n", ' ')
            initial_text += lines
    return initial_text
  
text = open_initial_text()
text = re.sub(r'\s+(?=(?:[,.?!:;… -;:]))', r'', text)
marks = '''()-[]{};@#$%:'"\/^&amp;*_'''
for i in text:
    if i in marks:
        text = text.replace(i, "")
        continue
    else:
        continue

text = text.split(' ')

#Create a list of unique words.
words = []
for i in text:
    if i not in words:
        words.append(i)

#Creating a list of starting words.
start_list=[]
for i in range(len(text)):
    if str(text[i]).istitle()==True:
        start_list.append(text[i])

#Creating a list of links.
word_connections = []
for i in range(len(words)):
    next_word = []
    for e in range(len(text)):
        if (words[i] == text[e]) and (e+1 != len(text)):
            next_word.append(text[e+1])
    word_connections.append(next_word)

#Generating a delusional text.
with open('output.txt', 'w') as f_out:
    number_sentence = int(input('Введите количество предложений для генирации текста: '))
    for i in range(0, number_sentence):
        x = random.randint(0, len(start_list)-1)
        sentence = start_list[x]
        x = words.index(sentence)
        for e in range (19):
            if len(word_connections[x]) > 1:
                b = random.randint(1, len(word_connections[x])-1)
            else:
                b = 1
            sentence += ' ' + str(word_connections[x][b-1])
            if '.' in word_connections[b-1]:
                break
            elif e == 18:
                sentence += '.'
            x = words.index(word_connections[x][b-1])
        print(sentence, end = ' ', file = f_out)

