from utility.interfaces import *


class LoadingScreen(AppScreen):
    def build(self, app: App):
        label = Label(self, text=app.locale['loading'], font=app.theme.text_style('view_title'), bg=app.theme.bg_color)
        label.grid(sticky='NEWS')
