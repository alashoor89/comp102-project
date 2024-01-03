from tkinter import *

from models.topic import Topic
from utility.locale import EnglishLocale
from utility.theme import Theme


class App(Tk):
    selected_topic: Topic = None
    topics: [Topic] = []

    """
        self.

        Initiate the default variables
        Theme contains the program colors and attributes
        Locale contains the program messages
        Icon is a photo of the program
        Selected Topic contain the chosen topic and by default it is none until user choose it
        Screens contains all the screens that program uses and switch between them
        Selected topic saves the current selected topic

    """

    def __init__(self):
        Tk.__init__(self)
        self.width = 1000
        self.height = 600
        self.theme = Theme()
        self.locale = EnglishLocale()
        self.icon = PhotoImage(file='assets/icons/icon.png')

    def switch_screen(self, screen: str):
        pass

    def navigate(self, topic: Topic):
        pass


class AppScreen(Frame):

    def build(self, app: App):
        label = Label(self, text=app.locale['welcome'], bg=app.theme.bg_color)
        label.pack()

    def rebuild(self, app: App):
        for child in self.winfo_children():
            child.destroy()
        self.build(app)
        self.pack(expand=True)
        print(f'DEBUG: Screen rebuilt.')
