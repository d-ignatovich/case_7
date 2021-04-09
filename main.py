"""Case-study 
Developers:   Ignatovich D. (%),
              Miller A. (%),
              Poylova E. (%)
""" 

s = 'Сегодня статья и посвящена Одному из глобальных явлений из человеческой культуры и базовому понятию для всех пишущих Людей. k'
text = s.split(' ')

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

