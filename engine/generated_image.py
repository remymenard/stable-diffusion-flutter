from flet import Container
from enum import Enum
from engine.start_engine import generate_image

from engine.widgets.no_generated_image_widget import *
from engine.widgets.generated_image_widget import *
from engine.widgets.loader_widget import *

class GeneratedImage():
    def __init__(self):
        self.__url = ""
        self.__base64_image = ""
        self.__status = Status.WAITING

    def get_url(self):
        return self.__url


    def get_status(self):
        return self.__status

    def start_generating(self):
        self.__status = Status.GENERATING
        self.__base64_image = generate_image()
        self.__status = Status.GENERATED
        return self.__base64_image
                

    def get_base64_image(self):
        return self.__base64_image
                

    def get_widget(self, status):
        match status:
            case Status.WAITING:
                return NoGeneratedImageWidget()
            case Status.GENERATING:
                return LoaderWidget()
            case Status.GENERATED:
                return GeneratedImageWidget(self.__base64_image)

class Status(Enum):
    WAITING = 1
    GENERATING = 2
    GENERATED = 3