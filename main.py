import os
import threading

from screens.home_screen import HomeScreen
from screens.loading_screen import LoadingScreen
from screens.view_screen import ViewScreen
from utility.interfaces import *


class AppImpl(App):
    current_screen: AppScreen = None
    """
        self.

        Current_Screen_Name saves the current screen
        Current_Screen saves the frame screen
        Loaded saves the loading application state
        Screens saves all the screens and navigate throw them 
    """

    def __init__(self):
        App.__init__(self)
        self.loaded = False
        self.current_screen_name = None
        self.screens = {'/loading': LoadingScreen, '/home': HomeScreen, '/view': ViewScreen}

    '''
        Setup method load up the default attributes of the program
        before showing the window.
    '''

    def setup(self):
        self.configure(bg=self.theme.bg_color)
        self.title(self.locale['title'])
        self.iconphoto(False, self.icon)
        self.geometry(f'{self.width}x{self.height}')
        self.resizable(False, False)
        self.switch_screen('/loading')
        threading.Thread(target=self.load_topics).start()

    '''
        Loads the topics then navigate to home screen
    '''
    def load_topics(self):
        self.read_topics()
        self.loaded = True
        self.switch_screen('/home')
        print('DEBUG: Topics Loaded')

    '''
        Load topics
    '''
    def read_topics(self):
        directory = rf'{os.getcwd()}\assets\topics'
        for filename in os.listdir(directory):
            topic_directory = os.path.join(directory, filename)
            if os.path.isdir(topic_directory):
                file_directory = os.path.join(topic_directory, 'info.topic')
                with open(file_directory, 'r') as file_reader:
                    lines = list(map(lambda value: value.replace('\n', ''), file_reader.readlines()))
                    self.topics.append(Topic(lines[0], topic_directory, video=lines[0] if len(lines) >= 0 else None))
                    file_reader.close()

    '''
        Selects a topic and navigate to other screen
    '''
    def navigate(self, topic: Topic):
        self.selected_topic = topic
        self.switch_screen('/view')

    '''
        Switch between other screens
    '''

    def switch_screen(self, screen: str):
        screen = screen.lower()
        if screen != '/loading' and not self.loaded:
            return

        if screen == self.current_screen_name:
            return

        if self.current_screen is not None:
            self.current_screen.destroy()

        print(f'DEBUG: Switched screen from {self.current_screen_name} to {screen}.')
        self.current_screen_name = screen
        self.current_screen = self.screens[screen](self)
        self.current_screen.build(self)
        self.current_screen.pack(expand=True)


if __name__ == "__main__":
    app = AppImpl()
    app.setup()
    print('-----------------------------------------------------')
    print('COMP102 Subject Materials')
    print('Description: ')
    print(' COMP102 Subject Materials let students to navigate throw materials easily instead of using ppt. \n'
          ' Application provides slides and lab view in one screen.')
    print('-----------------------------------------------------')
    app.mainloop()


"""
-----------------------------------------------------
COMP102 Subject Materials
Description: 
 COMP102 Subject Materials let students to navigate throw materials easily instead of using ppt. 
 Application provides slides and lab view in one screen.
-----------------------------------------------------
"""
