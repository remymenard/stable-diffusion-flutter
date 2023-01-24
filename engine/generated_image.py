from flet import Container

class GeneratedImage:
    def __init__(self):
        self.url = ""
        self.status = "loading"

    def get_url(self):
        return self.url

    def set_url(self, value):
        self.url = value

    def get_status(self):
        return self.status

    def set_status(self, value):
        self.status = value
        print(self.status)

    def get_widget(self):
        match self.status:
            case "loading":
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

