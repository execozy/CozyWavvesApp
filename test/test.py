"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from test.Component.labelWelhome import welcome_content
from test.Component.Principal.create_account import CreateAccount
# from test.View.globalColour import color_mode_control


def index() -> rx.Component:
    return rx.container(
        welcome_content(),
        CreateAccount()
    )

app = rx.App(
    theme=rx.theme( appearance='dark')
)

# app.extra_app_wraps[(100, "ColorModeControl")] = lambda _: rx.fragment(
#     color_mode_control()
# )
app.add_page(index)
