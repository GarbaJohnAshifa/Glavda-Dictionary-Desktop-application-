
import json
from difflib import get_close_matches
from tkinter import *
import tkinter.messagebox

# Load dictionary data
data = json.load(open("dictionary.json"))
keys = data.keys()

def meaning():
    w = e1_value.get()
    t1.config(state=NORMAL)  # Allow editing for inserting text
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
    t1.config(state=DISABLED)  # Set back to read-only

def clear_screen():
    t1.config(state=NORMAL)  # Allow editing for clearing text
    t1.delete(1.0, END)
    e1.delete(0, END)
    t1.config(state=DISABLED)  # Set back to read-only

# Create GUI
root = Tk()
root.title("DICTIONARY APP")
root.configure(bg="#f5f5f5")  # Light grey background

header = Label(root, text="DICTIONARY SOFTWARE", bg="#3498db", fg="white", pady=10, font=("Arial", 18, "bold"))
header.pack(fill=X)

frame = Frame(root, bg="#f5f5f5")
frame.pack(pady=20)

label1 = Label(frame, text="Enter your word:", bg="#f5f5f5", font=("Arial", 14))
label1.grid(row=0, column=0, padx=10, pady=10, sticky=W)

e1_value = StringVar()
e1 = Entry(frame, textvariable=e1_value, font=("Arial", 14), width=30, bd=2, relief=SOLID)
e1.grid(row=0, column=1, padx=10, pady=10)

button = Button(frame, text="Get Meaning", command=meaning, bg="#2ecc71", fg="white", font=("Arial", 14, "bold"))
button.grid(row=1, column=0, columnspan=2, pady=10)

t1 = Text(root, font=("Arial", 14), height=10, width=50, bd=2, relief=SOLID, state=DISABLED)  # Set to read-only
t1.pack(pady=10, padx=10)

label2 = Label(root, text="Press to clear screen", bg="#f5f5f5", font=("Arial", 12))
label2.pack(pady=5)

button2 = Button(root, text="Clear Screen", command=clear_screen, bg="#e74c3c", fg="white", font=("Arial", 14, "bold"))
button2.pack(pady=10)

root.mainloop()

