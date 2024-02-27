import PySimpleGUI as sg

sg.theme("DarkBlack")
sg.set_options(font="Georgia 20")

layout = [
    [
        sg.Input("", key="-INPUT-", pad=(10, 10), size=(7, 5), expand_x=True),
        sg.Spin(
            ["C to F", "F to C"],
            key="-UNITS-",
            size=(5, 10),
            pad=(10, 10),
            expand_x=True,
        ),
    ],
    [
        sg.Button(
            "Convert",
            button_color="#228822",
            border_width=0,
            key="-CONVERT-",
            size=(10, 1),
            pad=(10, 10),
            expand_x=True,
        ),
        sg.Text("", key="-OUTPUT-", size=(10, 1), pad=(10, 10), expand_x=True),
    ],
]

window = sg.Window(
    "Converter",
    layout,
    size=(400, 150),
    element_justification="center"
)


while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "-CONVERT-":
        input_value = values["-INPUT-"]

        try:
            float_input = float(input_value)

            match values["-UNITS-"]:

                case "C to F":
                    output_value = round((float_input * 9 / 5) + 32, 2)
                    # (0°C × 9/5) + 32 = 32°F
                    output_string = f"{output_value} °F"

                case "F to C":
                    output_value = round((float_input - 32) * 5 / 9, 2)
                    # (0°F − 32) × 5/9 = -17.78°C
                    output_string = f"{output_value} °C"

            window["-OUTPUT-"].update(output_string)

        except:
            window["-OUTPUT-"].update("")

window.close()
