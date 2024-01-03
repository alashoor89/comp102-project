from enum import Enum
from typing import Callable

from screens.view.slide_view import SlideView
from utility.interfaces import *


class ViewMode(Enum):
    SLIDE = 0,
    LAB = 1,


def create_button(keep: bool, frame: Frame, title: str, column: int, padding: bool = True, command: Callable = None):
    if keep:
        Button(frame, text=title, bg='#D3D3D3', command=command).grid(row=0, column=column, ipadx=5,
                                                                      padx=5 if padding else 0)


class ViewScreen(AppScreen):
    __view_mode: ViewMode = ViewMode.SLIDE

    def __init__(self, app: App):
        AppScreen.__init__(self, app)
        self.current_view = None
        self.lab_view = None
        selected_topic = app.selected_topic
        self.slide_view = SlideView(selected_topic.slides, self)
        if selected_topic.lab is not None:
            self.lab_view = SlideView(selected_topic.lab, self)

    '''
        Create navigation buttons
    '''
    def build_buttons(self, app: App):
        button_frame = Frame(self)
        create_button(self.__view_mode is not ViewMode.SLIDE,
                      button_frame, 'Slides', 1, self.lab_view is None or self.__view_mode is ViewMode.LAB,
                      command=lambda: self.change_mode(app, ViewMode.SLIDE))
        create_button(self.__view_mode is not ViewMode.LAB and self.lab_view is not None,
                      button_frame, 'Lab', 2,
                      command=lambda: self.change_mode(app, ViewMode.LAB))
        create_button(True, button_frame, 'Go Back', 4,
                      command=lambda: app.switch_screen('/home'))
        button_frame.grid(row=0, column=1, sticky='E')

    def build(self, app: App):
        Label(self, text=app.selected_topic.name, font=app.theme.text_style('view_title'), height=1).grid(row=0,
                                                                                                          column=0,
                                                                                                          sticky="W",
                                                                                                          pady=15)
        self.build_buttons(app)
        if self.__view_mode == ViewMode.SLIDE:
            self.current_view = self.slide_view
        elif self.__view_mode == ViewMode.LAB:
            self.current_view = self.lab_view
        else:
            self.current_view = self.video_view
        self.current_view.build(app)

    '''
        Change the screen mode and rebuild
    '''
    def change_mode(self, app: App, view_mode: ViewMode):
        self.__view_mode = view_mode
        self.rebuild(app)
