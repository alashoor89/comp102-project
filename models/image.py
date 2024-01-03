import PIL.Image
from PIL import ImageTk


class Image:
    def __init__(self, path: str = None, image: PIL.Image = None):
        if image is None:
            self.image = PIL.Image.open(path).copy()
        else:
            self.image = image
        self.photo = ImageTk.PhotoImage(self.image)
    '''
        Resize the ImageTk
    '''
    def resize(self, width: int, height: int):
        self.image = self.image.resize((width, height))
        self.photo = ImageTk.PhotoImage(self.image)

    '''
        Copy the image to a new Image instance
    '''
    def copy(self):
        return Image(image=self.image)
