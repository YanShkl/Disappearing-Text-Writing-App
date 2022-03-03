from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #

BACKGROUND = "#B1DDC6"
WHITE = 'white'
BROWN = '#503629'

# ---------------------------- VARIABLES ------------------------------- #

text = ""

# ----------------------------   UI    ------------------------------- #

class DisappearingText:

    def __init__(self):

        self.window = Tk()
        self.window.title('Disappearing Text App')
        self.window.config(highlightcolor=BROWN)
        self.canvas = Canvas(self.window, width=600, height=500, bg=BACKGROUND, highlightthickness=0,)
        self.canvas.grid(column=1, row=1)
        self.printButton = Button(self.window,
                                text="Start",
                                command=self.check_disappear
                                )
        self.printButton.place(x=50, y=15)

        # Text Widget
        self.t = Text(self.window, width=60, height=25)
        self.t.place(x=50, y=50)

        #Info Text
        self.wpm_label = Label(text="Press 'Start' button. After that if you stop typing\n "
                                    "all written text will dissapear within 11 seconds.", font=("Arial", 12), bg=BACKGROUND)
        self.wpm_label.place(x=100, y=8)
        self.window.mainloop()


    # ----------------------------   Timer Functions    ------------------------------- #

    def disappear_text(self):
        self.t.delete(1.0, END)
        self.t.insert(END, "")

    def check_disappear(self):
        global counter, text
        if text == self.t.get(1.0, END):
            if counter == 10:
                self.window.after(1000, self.disappear_text)
                counter = -1
            self.window.after(1000, self.check_disappear)
            counter += 1
        else:
            self.window.after(1000, self.check_disappear)
            text = self.t.get(1.0, END)
            counter = 0

# Run App
app = DisappearingText()