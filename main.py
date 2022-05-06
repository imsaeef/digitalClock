from tkinter import *
from time import strftime


class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital clock by SAEEF")

        def time():
            string = strftime("%I:%M:%S %p")
            clockLabel.config(text=string)
            clockLabel.after(1000, time)

        clockLabel = Label(
            self.root,
            font="DS-Digital 50 italic",
            background="black",
            foreground="cyan"
        )
        clockLabel.pack(anchor=CENTER)
        time()


if __name__ == "__main__":
    root = Tk()
    app = DigitalClock(root)
    root.mainloop()
