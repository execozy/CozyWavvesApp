
import reflex as rx


def color_mode_control() -> rx.Component:
    return rx.color_mode.button(position="top-right")