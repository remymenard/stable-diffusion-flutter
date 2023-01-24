# from start_engine import generate_image
import flet
from flet import Page, Row, TextField, Column, Slider, Text, Divider, Container, padding, MainAxisAlignment, CrossAxisAlignment, Image, ImageFit, FilledButton

import sys
sys.path.insert(0, '../engine')


def main(page: Page):
    # generate_image()
    page.title = "Stable Diffusion Flutter"
    page.vertical_alignment = "center"

    def prompt_changed(e):
        prompt.value = e.control.value
        page.update()

    prompt = Text()
    prompt_textbox = TextField(
        label="Prompt",
        on_change=prompt_changed,
    )

    page.add(
        Container(
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
                            Container(
                                expand=1,
                                content=Container(
                                    content=Image(
                                        fit=ImageFit.FIT_HEIGHT,
                                        src=f"https://picsum.photos/1024/1024?10",
                                    )
                                )

                            )
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
                                FilledButton(text="Generate new image")
                            ],
                            horizontal_alignment=CrossAxisAlignment.END
                        )
                    )
                ],
                alignment=MainAxisAlignment.CENTER,
            )
        )
    )


flet.app(target=main)
