"""moduli sisältää pääohjelman"""
import config
from tkinter import Tk 
from ui.ui import UI


def main():
    """pääohjelma, käynnistää käyttöliittymän"""

    window = Tk()
    window.title("MNIST numeroiden tunnistus KNN:llä")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()