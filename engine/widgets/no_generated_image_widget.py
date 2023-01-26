from flet import Container, ProgressRing

class NoGeneratedImageWidget(Container):
    def __init__(self):
        Container.__init__(
            self,
            bgcolor="primary",
            expand=1,
            content=ProgressRing(color="red")
        )

