class Theme(object):
    def __init__(self):
        #  TODO IN THIS PLACE, YOU CAN DEFINE TEXT STYLE
        self.texts = {
            'view_title': ('Arial', 16),
            'home_title': ('Arial', 16),

        }
        self.bg_color = "#f0f3f9"

    def text_style(self, style: str):
        return self.texts[style]
