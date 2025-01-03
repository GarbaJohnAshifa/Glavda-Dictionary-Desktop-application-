import json
from difflib import get_close_matches
from tkinter import *
import tkinter.messagebox

# Load dictionary data
data = json.load(open("dictionary.json"))
keys = data.keys()

def meaning():
    w = e1_value.get()
    t1.delete(1.0, END)  # Clear previous results
    
    if w in data:
        for i, j in enumerate(data[w]):
            t1.insert(END, str(i) + ' ' + j + '\n')
    elif w.upper() in data:
        for i, j in enumerate(data[w.upper()]):
            t1.insert(END, str(i) + ' ' + j + '\n')
    elif w.title() in data:
        for i, j in enumerate(data[w.title()]):
            t1.insert(END, str(i) + ' ' + j + '\n')
    else:
        suggestions = get_close_matches(w, keys, n=1, cutoff=0.8)
        if len(suggestions) == 0:
            t1.insert(END, "Sorry, no word found!")
        else:
            real_word = suggestions[0]
            answer = tkinter.messagebox.askquestion("Word Suggestion", "Is your word " + real_word + "?")
            if answer == "yes":
                for i, j in enumerate(data[real_word]):
                    t1.insert(END, str(i) + ' ' + j + '\n')
            else:
                t1.insert(END, "No word found. Please check your input again.")

def clear_screen():
    t1.delete(1.0, END)
    e1.delete(0, END)

# Create GUI
root = Tk()
root.title("GLAVDA DICTIONARY APP")

header = Label(root, text="GLAVDA DICTIONARY SOFTWARE", bg="tomato", fg="white")
header.pack(fill=X)

label1 = Label(root, text="Enter your word:")
label1.pack()

e1_value = StringVar()
e1 = Entry(root, textvariable=e1_value)
e1.pack()

button = Button(root, text="Get Meaning", command=meaning, bg="dark orchid")
button.pack()

t1 = Text(root)
t1.pack(fill=X)

label2 = Label(root, text="Press to clear screen")
label2.pack()

button2 = Button(root, text="Clear Screen", command=clear_screen, bg="dark orchid")
button2.pack()

root.mainloop()
