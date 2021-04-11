"""Case-study 
Developers:   Ignatovich D. (%),
              Miller A. (30%),
              Poylova E. (40%)
""" 
s = 'Это утро, радость эта, Эта мощь и дня и света, Этот синий свод, Этот крик и вереницы, Эти стаи, эти птицы, Этот говор вод, Эти ивы и березы, Эти капли - эти слезы, Этот пух - не лист, Эти горы, эти долы, Эти мошки, эти пчелы, Этот зык и свист, Эти зори без затменья, Этот вздох ночной селенья, Эта ночь без сна, Эта мгла и жар постели, Эта дробь и эти трели,Это всё - весна.'
import re
s = re.sub(r'\s+(?=(?:[,.?!:;… -;:]))', r'', s)
marks = '''()-[]{};@#$%:'"\/^&amp;*_'''
for i in s:
    if i in marks:
         t = s.replace(i, "")
         continue
    else:
        continue

def open_initial_text(filename):
    with open('input.txt', "r") as f_in:
        initial_text = f_in.read()
    return initial_text

def clean_initial(initial):
    initial = initial.replace("\n", " ")
        
text = t.split(' ')

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
number_sentence = int(input('Введите количество предложений для генирации текста: '))
for i in range(0, number_sentence):
    x = random.randint(0, len(start_list)-1)
    sentence = start_list[x]
    x = words.index(sentence)
    for e in range (19):
        if len(word_connections[x])>0:
            b = random.randint(0, len(word_connections[x])-1)
        else:
            b = 0
        sentence += ' ' + str(word_connections[x][b])
        if '.' in word_connections[b]:
            break
        if e == 18:
            sentence += '.'
        x = words.index(word_connections[x][b])
    print(sentence)

