from tkinter import *
import os, random

root = Tk()
root.title("Jumble Game")
root.minsize(600, 400)
root.maxsize(600, 400)
x_Left = int(root.winfo_screenwidth() / 2 - 600 / 2)
y_Top = int(root.winfo_screenheight() / 2 - 400 / 2)
root.geometry(f"600x400+{x_Left}+{y_Top}")  # "widthxheight+Left+Top"
root.configure(bg="beige")


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.environ.get("_MEIPASS2", os.path.abspath("."))

    return os.path.join(base_path, relative_path)


wordLabel = Label(root, text="", font=("Helvetica", 48), bg="beige")
wordLabel.pack(pady=20)

answerField = Entry(root, font=("Helvetica", 24), justify="center")
answerField.pack(pady=20)


words = []
def load_words():
    with open(resource_path("words.txt"), "r") as f:
        data = f.readlines()

    [words.append(i.strip().lower()) for i in data]
    return words


def shuffle():
    # clear screen and reset
    answerLabel.config(text="")
    hintLabel.config(text="")
    answerField.delete(0, END)
    global counter
    counter = 0

    # load words
    words = load_words()
    global chosenWord
    chosenWord = random.choice(words)

    # break the word and shuffle
    brokenWord = list(chosenWord)
    random.shuffle(brokenWord)

    # turn shuffled list to word
    global currentWord
    currentWord = ""
    for letter in brokenWord:
        currentWord += letter

    wordLabel.config(text=currentWord)


def answer():
    answer = answerField.get().strip()
    check = False
    if len(answer) > 0:
        if chosenWord == answer.lower():
            answerLabel.config(text="Correct!!", fg="green")
        else:
            answerLabel.config(text="Incorrect!!", fg="maroon")
    else:
        answerLabel.config(text="Please type answer!!", fg="maroon")


global counter
counter = 0
def hint(count):
    global counter
    counter = count

    if counter < len(chosenWord):
        hintLabel.config(text=f"{hintLabel['text']} {chosenWord[count]}")
        counter += 1


# frame for buttons
frame = LabelFrame(root, padx=10, pady=10)
frame.pack(pady=10)

answerBtn = Button(
    frame,
    text="Answer",
    bg="green",
    fg="white",
    activebackground="green",
    activeforeground="white",
    width=7,
    command=answer,
)
answerBtn.grid(row=0, column=0, padx=10)

nextWordBtn = Button(frame, text="Pick Another Word", bg="silver", command=shuffle)
nextWordBtn.grid(row=0, column=1, padx=10)

hintBtn = Button(
    frame,
    text="Hint",
    bg="maroon",
    fg="white",
    activebackground="maroon",
    activeforeground="white",
    width=8,
    command=lambda: hint(counter),
)
hintBtn.grid(row=0, column=2, padx=10)
# end of frame


answerLabel = Label(root, text="", font=("Helvetica", 18), bg="beige")
answerLabel.pack(pady=15)

hintLabel = Label(root, text="", font=("Helvetica", 15), bg="beige")
hintLabel.pack(pady=10)


shuffle()
root.iconbitmap(resource_path("jg.ico"))
root.mainloop()
