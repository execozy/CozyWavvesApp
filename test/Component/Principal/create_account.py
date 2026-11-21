import reflex as rx



def CreateAccount() -> rx.Component:
    return rx.vstack(
        rx.button("Create Account", color_scheme="blue", size="3"),
        spacing="4",
        align="center",
    )
