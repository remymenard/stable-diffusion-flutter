from flet import Container
from enum import Enum
from engine.start_engine import generate_image

class GeneratedImage:
    def __init__(self):
        self.__url = ""
        self.__status = Status.WAITING

    def get_url(self):
        return self.__url


    def get_status(self):
        return self.__status

    def set_status(self, value):
        self.__status = value
        match self.__status:
            case Status.GENERATING:
                print("start generating")
                generate_image()
                print("stop generating")
                

    def get_widget(self):
        match self.__status:
            case Status.WAITING:
                return Container(
                    bgcolor="red",
                    border_radius=20,
                    expand=1
                )
            case _:
                print("green")
                return Container(
                    bgcolor="green",
                    border_radius=20,
                    expand=1
                )


class Status(Enum):
    WAITING = 1
    GENERATING = 2
    GENERATED = 3