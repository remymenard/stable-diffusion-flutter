from flet import Container, ProgressRing, Column, Text,CrossAxisAlignment, MainAxisAlignment

class LoaderWidget(Container):
    def __init__(self):
        Container.__init__(
            self,
            bgcolor="primary",
            expand=1,
            content=Column(
                [
                    ProgressRing(color="white"), 
                    Text("Generating your image..", color="white")
                ],
                horizontal_alignment=CrossAxisAlignment.CENTER,
                alignment=MainAxisAlignment.CENTER
            ),
        )

