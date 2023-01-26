from flet import Container, Image, ImageFit

class GeneratedImageWidget(Container):
    def __init__(self, base64_image):
        Container.__init__(
            self,
            expand=1,
            content=Image(
                fit=ImageFit.FILL,
                src_base64=base64_image
            )
        )

