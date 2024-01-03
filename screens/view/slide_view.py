from utility.addons.scrollable_frame import VerticalScrolledFrame
from utility.interfaces import *


class SlideView:
    # noinspection PyMethodMayBeStatic
    def __init__(self, slides: list[Image], screen: AppScreen):
        self.slides = slides
        self.selected_slide = slides[0]
        self.sidebar_width = None
        self.container_width = None
        self.sidebar = None
        self.container = None
        self.screen = screen

    '''
        Build the left side bar container that contains the slides
    '''
    def build_container(self, app: App):
        container = Frame(self.screen, highlightbackground="#000", highlightthickness=1)
        label = Label(container, image=self.selected_slide.photo)
        label.pack(expand=True, fill=BOTH)
        container.grid(column=0, row=1, sticky="NSEW")
        container.label = label
        self.container = container

    '''
        Builds the slide navigation toolbar
    '''
    def build_sidebar(self, app: App):
        sidebar = VerticalScrolledFrame(self.screen, width=self.sidebar_width)
        # fake width to prevent frame from shrinking
        Frame(sidebar.interior, width=self.sidebar_width).pack()
        sidebar.interior.configure(highlightbackground="#000",
                                   highlightthickness=1)
        for index in range(len(self.slides)):
            self.build_slide_toolbar(app, index, sidebar, self.slides[index])
        sidebar.grid(column=1, row=1, padx=15, sticky="NSEW")
        self.sidebar = sidebar

    '''
        Builds the slide card toolbar
    '''
    def build_slide_toolbar(self, app, index, sidebar, slide):
        slide_selection = Label(sidebar.interior, width=28)
        copy_of_slide = slide.copy()
        copy_of_slide.resize(int(self.sidebar_width), 100)
        slide_selection.image = copy_of_slide
        slide_selection.photo = copy_of_slide.photo
        slide_selection.configure(image=slide_selection.photo)
        slide_selection.pack(pady=5, fill=BOTH)
        slide_selection.bind('<Button-1>', lambda event: self.select_slide(app, index))

    def build(self, app: App):
        width = app.width
        self.container_width = width * 0.7
        self.sidebar_width = width * 0.225
        self.build_container(app)
        self.build_sidebar(app)
        self.resize(app)

    '''
       Resize the widgets
    '''
    def resize(self, app: App):
        height = app.height * 0.80
        self.container.configure(width=self.container_width, height=height)
        self.sidebar.configure(width=self.sidebar_width, height=height)
        self.selected_slide.resize(int(self.container_width), int(height))
        self.container.label.configure(image=self.selected_slide.photo)

    '''
        Selects the slides and display it in the container
    '''
    def select_slide(self, app: App, index: int):
        height = app.height * 0.80
        self.selected_slide = self.slides[index]
        self.selected_slide.resize(int(self.container_width), int(height))
        self.container.label.configure(image=self.selected_slide.photo)
        pass
