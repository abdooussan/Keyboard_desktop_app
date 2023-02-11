import time
import flet as ft
from pynput.keyboard import Key, Controller

keyboard = Controller()


def main(page: ft.Page):
    page.window_always_on_top = True
    # set the size of the window
    page.window_width = 840
    page.window_height = 350
    # show what is written on the keyboard

    def show(string):

        # turn to the file by pressing Alt+Tab and type the specific character
        keyboard.press(Key.alt)
        time.sleep(0.05)
        keyboard.press(Key.tab)
        time.sleep(0.05)
        keyboard.release(Key.alt)
        keyboard.release(Key.tab)
        if string == "space":
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        elif string == "delete":
            keyboard.press(Key.backspace)
            keyboard.release(Key.backspace)
        elif string == "return":
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
        else:
            keyboard.press(string)
            keyboard.release(string)
    # regular sized buttons 50*50

    def Button_1(string, upper=True):
        if upper:  # to type uppercase letters
            return ft.ElevatedButton(
                on_click=(lambda e: show(string)),
                style=ft.ButtonStyle(
                    bgcolor="#212b35", color="white", shape=ft.RoundedRectangleBorder(radius=5)),
                text=string,
                width=50,
                height=50,
            )
        else:  # to type lowercase letters
            return ft.ElevatedButton(
                on_click=(lambda e: show(string.lower())),
                style=ft.ButtonStyle(
                    bgcolor="#212b35", color="white", shape=ft.RoundedRectangleBorder(radius=5)),
                text=string.lower(),
                width=50,
                height=50,
            )

    # for other buttons like delete and return
    def Button_2(string, y, alignmentt):
        return ft.ElevatedButton(
            on_click=(lambda e: show(string.lower())),
            style=ft.ButtonStyle(bgcolor="#212b35", color="white",
                                 shape=ft.RoundedRectangleBorder(radius=5)),
            width=y,
            height=50,
            content=ft.Container(
                content=ft.Text(string, size=10, color=ft.colors.WHITE),
                alignment=alignmentt,
            ),)

    # change between uppercase and lowercase letters by clicking on the keyboard_capslock button
    def button_clicked(e):
        keyboard.press(Key.caps_lock)
        keyboard.release(Key.caps_lock)
        b_capslock.data = not b_capslock.data
        
        x = b_capslock.data
        Col = ft.Column(
            spacing=4,
            controls=[ft.Row(
                spacing=4,
                controls=[
                    Button_1("1", x),
                    Button_1("2", x),
                    Button_1("3", x),
                    Button_1("4", x),
                    Button_1("5", x),
                    Button_1("6", x),
                    Button_1("7", x),
                    Button_1("8", x),
                    Button_1("9", x),
                    Button_1("0", x),
                    Button_1("-", x),
                    Button_1("+", x),
                    Button_1("=", x),
                    Button_1("&", x),
                    Button_1("/", x),

                ]
            ),
                ft.Row(
                spacing=4,
                controls=[
                    Button_1("Q", x),
                    Button_1("W", x),
                    Button_1("E", x),
                    Button_1("R", x),
                    Button_1("T", x),
                    Button_1("Y", x),
                    Button_1("U", x),
                    Button_1("I", x),
                    Button_1("O", x),
                    Button_1("P", x),


                    Button_2("delete", 104, ft.alignment.center_right),

                    Button_1("@", x),
                    Button_1("#", x),
                    Button_1("_", x),

                ]
            ),
                ft.Row(
                spacing=4,
                controls=[
                    b_capslock,
                    Button_1("A", x),
                    Button_1("S", x),
                    Button_1("D", x),
                    Button_1("F", x),
                    Button_1("G", x),
                    Button_1("H", x),
                    Button_1("J", x),

                    Button_1("K", x),
                    Button_1("L", x),



                    Button_2("return", 104, ft.alignment.center_right),

                    Button_1(".", x),
                    Button_1("\"", x),
                    Button_1("\\", x),
                ]
            ),
                ft.Row(
                spacing=4,
                controls=[
                    b_change_language,

                    Button_1("Z", x),
                    Button_1("X", x),
                    Button_1("C", x),
                    Button_1("V", x),
                    Button_1("B", x),
                    Button_1("N", x),
                    Button_1("M", x),



                    Button_2("space", 212, ft.alignment.center_left),

                    Button_1(",", x),
                    Button_1("!", x),
                    Button_1("?", x),



                ]
            )])
        page.clean()
        page.add(Col)
    b_capslock = ft.ElevatedButton(
        text=" ",
        icon="keyboard_capslock",
        style=ft.ButtonStyle(bgcolor="#212b35", color="white",
                             shape=ft.RoundedRectangleBorder(radius=5)),
        width=50,
        height=50,
        on_click=button_clicked,
        data=False
    )

    # change between Arabic and English keyboard
    def button_clicked_2(e):
        b_change_language.data = not b_change_language.data
        page.clean()
        if b_change_language.data:
            page.window_width = 840
            page.add(Col)
        else:
            page.window_width = 1000
            page.add(Col_arb)

    b_change_language = ft.IconButton(
        icon="language",
        style=ft.ButtonStyle(
            bgcolor="#212b35", color="white", shape=ft.RoundedRectangleBorder(radius=5)),
        width=50,
        height=50,
        data=True,
        on_click=button_clicked_2,
    )

    # set background color
    page.bgcolor = "#000000"

    # set window title name
    page.title = "keyboard"

    # show the text in a text field
    x = b_capslock.data

    # English keyboard buttons
    Col = ft.Column(
        spacing=4,
        controls=[ft.Row(
            spacing=4,
            controls=[
                Button_1("1", x),
                Button_1("2", x),
                Button_1("3", x),
                Button_1("4", x),
                Button_1("5", x),
                Button_1("6", x),
                Button_1("7", x),
                Button_1("8", x),
                Button_1("9", x),
                Button_1("0", x),
                Button_1("-", x),
                Button_1("+", x),
                Button_1("=", x),
                Button_1("&", x),
                Button_1("/", x),

            ]
        ),
            ft.Row(
            spacing=4,
            controls=[
                Button_1("Q", x),
                Button_1("W", x),
                Button_1("E", x),
                Button_1("R", x),
                Button_1("T", x),
                Button_1("Y", x),
                Button_1("U", x),
                Button_1("I", x),
                Button_1("O", x),
                Button_1("P", x),


                Button_2("delete", 104, ft.alignment.center_right),

                Button_1("@", x),
                Button_1("#", x),
                Button_1("_", x),

            ]
        ),
            ft.Row(
            spacing=4,
            controls=[
                b_capslock,
                Button_1("A", x),
                Button_1("S", x),
                Button_1("D", x),
                Button_1("F", x),
                Button_1("G", x),
                Button_1("H", x),
                Button_1("J", x),

                Button_1("K", x),
                Button_1("L", x),



                Button_2("return", 104, ft.alignment.center_right),

                Button_1(".", x),
                Button_1("\"", x),
                Button_1("\\", x),
            ]
        ),
            ft.Row(
            spacing=4,
            controls=[
                b_change_language,
                Button_1("Z", x),
                Button_1("X", x),
                Button_1("C", x),
                Button_1("V", x),
                Button_1("B", x),
                Button_1("N", x),
                Button_1("M", x),



                Button_2("space", 212, ft.alignment.center_left),

                Button_1(",", x),
                Button_1("!", x),
                Button_1("?", x),



            ]
        )])

    # Arabic keyboard buttons
    Col_arb = ft.Column(
        spacing=4,
        controls=[ft.Row(
            spacing=4,
            controls=[
                Button_1("%"),
                Button_1("،"),
                Button_1("ذ"),
                Button_1("1"),
                Button_1("2"),
                Button_1("3"),
                Button_1("4"),
                Button_1("5"),
                Button_1("6"),
                Button_1("7"),
                Button_1("8"),
                Button_1("9"),
                Button_1("0"),
                Button_1("-"),
                Button_1("+"),
                Button_1("="),
                Button_1("&"),
                Button_1("/"),

            ]
        ),
            ft.Row(
            spacing=4,
            controls=[
                Button_1("ض"),
                Button_1("ص"),
                Button_1("ث"),
                Button_1("ق"),
                Button_1("ف"),
                Button_1("غ"),
                Button_1("ع"),
                Button_1("ه"),
                Button_1("خ"),
                Button_1("ح"),
                Button_1("ج"),
                Button_1("د"),


                Button_2("delete", 158, ft.alignment.center_right),

                Button_1("@"),
                Button_1("#"),
                Button_1("_"),

            ]
        ),
            ft.Row(
            spacing=4,
            controls=[
                ft.IconButton(
                    icon="keyboard_capslock",
                    style=ft.ButtonStyle(
                        bgcolor="#212b35", color="white", shape=ft.RoundedRectangleBorder(radius=5)),
                    width=50,
                    height=50,
                ),
                Button_1("ش"),
                Button_1("س"),
                Button_1("ي"),
                Button_1("ب"),
                Button_1("ل"),
                Button_1("ا"),
                Button_1("ت"),
                Button_1("ن"),
                Button_1("م"),

                Button_1("ك"),
                Button_1("ط"),



                Button_2("return", 158, ft.alignment.center_right),

                Button_1("."),
                Button_1("\""),
                Button_1("\\"),
            ]
        ),
            ft.Row(
            spacing=4,
            controls=[
                b_change_language,
                Button_1("ئ"),
                Button_1("ء"),
                Button_1("ؤ"),
                Button_1("ر"),
                Button_1("لا"),
                Button_1("ى"),
                Button_1("ة"),
                Button_1("و"),
                Button_1("ز"),
                Button_1("ظ"),


                Button_2("space", 212, ft.alignment.center_left),

                Button_1(","),
                Button_1("!"),
                Button_1("?"),



            ]
        )])
    page.add(
        Col
    )


ft.app(target=main)
