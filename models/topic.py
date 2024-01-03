import io
import os.path

import PIL.Image
import fitz

from models.image import Image


def convert_pdf(path: str):
    pages: list[Image] = []
    document = fitz.open(path)
    for page in document:
        bytes_io = io.BytesIO(page.get_pixmap().tobytes('ppm'))
        image = PIL.Image.open(bytes_io)
        pages.append(Image(image=image))
    return pages


class Topic:
    def __init__(self, name: str, folder: str, video: str = None):
        self.lab = None
        self.name = name
        self.video = video
        self.image = Image(rf'{folder}\thumbnail.jpg')
        self.slides = convert_pdf(rf'{folder}\slides.pdf')
        lab_file = rf'{folder}\lab.pdf'
        if os.path.isfile(lab_file):
            self.lab = convert_pdf(lab_file)
