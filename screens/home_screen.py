from utility.interfaces import *


class HomeScreen(AppScreen):
    def build(self, app: App):
        Label(self, text=app.locale['home_header'], font=app.theme.text_style('home_title')).pack(pady=10)
        self.create_topics(app)

    '''
        Displays the topics in terms of 3x3
    '''
    def create_topics(self, app):
        container = Frame(self)
        row = 0
        column = 0
        for topic in app.topics:
            self.build_slide_toolbar(app, container, topic, column, row)
            column += 1
            if column == 3:
                column = 0
                row += 1
        container.pack()

    '''
        Creates topic card
    '''
    def build_slide_toolbar(self, app, frame, topic: Topic, column: int, row: int):
        topic_card = Label(frame)
        copy_of_slide = topic.image.copy()
        copy_of_slide.resize(200, 150)
        topic_card.image = copy_of_slide
        topic_card.photo = copy_of_slide.photo
        topic_card.configure(image=topic_card.photo)
        topic_card.grid(column=column, row=row, padx=15, pady=5, )
        topic_card.bind('<Button-1>', lambda event: app.navigate(topic))
