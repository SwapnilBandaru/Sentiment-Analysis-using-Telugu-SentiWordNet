from tkinter import *
import tkinter
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter import simpledialog
import numpy as np
import matplotlib.pyplot as plt


main = tkinter.Tk()
main.title("Telugu Sentiment Detection Using SentiWordNet") #designing main screen
main.geometry("1300x1200")

global filename
positive_list = []
negative_list = []
neutral_list = []

global pos
global neg
global neu
global fscore
global pos_count
global neg_count
global count

def uploadSentiwordnet():
    text.delete('1.0', END)
    text1.delete('1.0', END)
    text2.delete('1.0', END)
    text.insert(END,"Sentiment Negative Words List\n\n");
    text1.insert(END,"Sentiment Neutral Words List\n\n");
    text2.insert(END,"Sentiment Positive Words List\n\n");
    with open("Telugu_SentiWordNet/TE_NEG.txt", "r",encoding="utf-8") as file:  #reading LIWC dictinary
      for line in file:
        line = line.strip('\n')
        line = line.strip()
        arr = line.split("\t")
        negative_list.append(arr[1])
        text.insert(END,arr[1]+"\n")

    with open("Telugu_SentiWordNet/TE_NEU.txt", "r",encoding="utf-8") as file:  #reading LIWC dictinary
      for line in file:
        line = line.strip('\n')
        line = line.strip()
        arr = line.split("\t")
        neutral_list.append(arr[1])
        text1.insert(END,arr[1]+"\n")

    with open("Telugu_SentiWordNet/TE_POS.txt", "r",encoding="utf-8") as file:  #reading LIWC dictinary
      for line in file:
        line = line.strip('\n')
        line = line.strip()
        arr = line.split("\t")
        positive_list.append(arr[1])
        text2.insert(END,arr[1]+"\n")
    

def uploadSentences(): #function to upload tweeter profile
    global filename
    filename = filedialog.askopenfilename(initialdir="Book_Reviews_Sentences")
    pathlabel.config(text=filename)
   
    

def sentimentAnalysis():
    global pos
    global neg
    global neu
    global fscore
    global pos_count
    global neg_count
    global count
    neg_count = 0
    pos_count = 0
    fscore = 0
    text3.delete('1.0', END)
    count = 0;
    with open(filename, "r",encoding="utf-8") as file:  #reading LIWC dictinary
      for line in file:
        line = line.strip('\n')
        line = line.strip()
        arr = line.split()
        pos = 0
        neg = 0
        neu = 0
        print(str(len(arr))+" "+str(len(neutral_list)))
        if len(arr) > 0 and (line.startswith('__________________________') == False):
            count = count + 1
            for word in arr:
                if word in neutral_list:
                    neu = neu + 1
                if word in negative_list:
                    neg = neg + 1
                if word in positive_list:
                    pos = pos + 1

            pos = pos + neu
            if pos == 0 and neg == 0:
                text3.insert(END,line+"\n")
                text3.insert(END,"Sentence Sentiment : Neutral\n\n")
            elif pos > 0 and neg > 0:
                pos = pos/len(arr)
                neg = neg/len(arr)
                if pos > neg :
                    fscore = fscore + pos
                    pos_count = pos_count
                    text3.insert(END,line+"\n")
                    text3.insert(END,"Sentence Sentiment : Positive, Sentiment Score = "+str(pos)+"\n\n")
                else:
                    #fscore = fscore + neg
                    neg_count = neg_count + 1
                    text3.insert(END,line+"\n")
                    text3.insert(END,"Sentence Sentiment : Negative, Sentiment Score = "+str(neg)+"\n\n")
            elif pos > 0 and neg == 0:
                pos = pos/len(arr)
                fscore = fscore + pos
                pos_count = pos_count + 1
                text3.insert(END,line+"\n")
                text3.insert(END,"Sentence Sentiment : Positive, Sentiment Score = "+str(pos)+"\n\n")
            elif pos == 0 and neg > 0:
                neg = neg/len(arr)
                #fscore = fscore + neg
                neg_count = neg_count + 1
                text3.insert(END,line+"\n")
                text3.insert(END,"Sentence Sentiment : Negative, Sentiment Score = "+str(neg)+"\n\n")
                
            count = count + 1
    text3.insert(END,"\n\nAccuracy : "+str(((fscore*100)/count)*20)+"\n\n\n\n\n\n")                


def graph():
    height = [count,pos_count,neg_count]
    bars = ('Total Sentences', 'Positive Sentences','Negative Sentences')
    y_pos = np.arange(len(bars))
    plt.bar(y_pos, height)
    plt.xticks(y_pos, bars)
    plt.show()
    
font = ('times', 16, 'bold')
title = Label(main, text='Sentiment Analysis Using Telugu SentiWordNet', justify=LEFT)
title.config(bg='lavender blush', fg='DarkOrchid1')  
title.config(font=font)           
title.config(height=3, width=120)       
title.place(x=100,y=5)
title.pack()

font1 = ('times', 14, 'bold')
uploadButton = Button(main, text="Upload Telugu Sentiwordnet", command=uploadSentiwordnet)
uploadButton.place(x=50,y=100)
uploadButton.config(font=font1)  

pathlabel = Label(main)
pathlabel.config(bg='brown', fg='white')  
pathlabel.config(font=font1)           
pathlabel.place(x=360,y=100)

sentenceButton = Button(main, text="Upload Telugu Sentences", command=uploadSentences)
sentenceButton.place(x=50,y=150)
sentenceButton.config(font=font1) 

sentimentButton = Button(main, text="Sentiment Analysis From Sentences", command=sentimentAnalysis)
sentimentButton.place(x=300,y=150)
sentimentButton.config(font=font1)

graphbutton = Button(main, text="Sentiment Graph", command=graph)
graphbutton.place(x=630,y=150)
graphbutton.config(font=font1) 


font1 = ('times', 12, 'bold')
text=Text(main,height=20,width=20)
scroll=Scrollbar(text)
text.configure(yscrollcommand=scroll.set)
text.place(x=10,y=200)
text.config(font=font1)

text1=Text(main,height=20,width=20)
scroll1=Scrollbar(text1)
text1.configure(yscrollcommand=scroll1.set)
text1.place(x=220,y=200)
text1.config(font=font1)

text2=Text(main,height=20,width=20)
scroll2=Scrollbar(text2)
text2.configure(yscrollcommand=scroll2.set)
text2.place(x=430,y=200)
text2.config(font=font1)

text3=Text(main,height=20,width=80)
scroll3=Scrollbar(text3)
text3.configure(yscrollcommand=scroll.set)
text3.place(x=650,y=200)
text3.config(font=font1)


main.config(bg='brown')
main.mainloop()

