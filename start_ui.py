import flet
from flet import Page, Row, TextField, Column, Slider, Text, Divider, Container, padding, MainAxisAlignment, CrossAxisAlignment, Image, ImageFit, FilledButton

import sys

from engine.generated_image import *

from engine.widgets.no_generated_image_widget import *
from engine.widgets.generated_image_widget import *
from engine.widgets.loader_widget import *

def main(page: Page):
    # generate_image()
    page.title = "Stable Diffusion Flutter"
    page.vertical_alignment = "center"

    def prompt_changed(e):
        prompt.value = e.control.value
        page.update()

    def generate_image(e):
        selected_image.set_status(Status.GENERATING)

    selected_image = GeneratedImage()
    prompt = Text()
    prompt_textbox = TextField(
        label="Prompt",
        on_change=prompt_changed,
    )

    layout = Container(
            padding=padding.only(left=100, right=100, top=50),
            expand=1,
            content=Column(
                [
                    Container(expand=5, content=Row(
                        [
                            Container(expand=1, content=Column(
                                [
                                    Text("Width"),
                                    Slider(min=512, max=2048),
                                    Text("Height"),
                                    Slider(min=512, max=2048),
                                    Divider(height=30, thickness=3),
                                    Text("Details"),
                                    Slider(min=0, max=150),
                                    Text("Realism"),
                                    Slider(min=0, max=20),
                                ]
                            )
                            ),
                            NoGeneratedImageWidget()
                        ],
                        alignment="center",
                    ),
                    ),
                    Divider(height=100, thickness=3),
                    Container(
                        expand=1,
                        content=Column(
                            [
                                prompt_textbox,
                                FilledButton(
                                    text="Generate new image", on_click=generate_image)
                            ],
                            horizontal_alignment=CrossAxisAlignment.END
                        )
                    )
                ],
                alignment=MainAxisAlignment.CENTER,
            )
        )

    selected_image.page = page
    selected_image.layout = layout

    page.add(layout)


flet.app(target=main)
