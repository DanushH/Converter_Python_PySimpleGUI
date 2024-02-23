import PySimpleGUI as sg

sg.theme("DarkBlack")
sg.set_options(font="Georgia 20")

layout = [
    [
        sg.Input("0", key="-INPUT-", pad=(10,10), size=(7,5), expand_x=True),
        sg.Spin(["C to F", "F to C"], key="-UNITS-", size=(5,10), pad=(10,10), expand_x=True),
    ],
    [    
        sg.Button("Convert", key="-CONVERT-", size=(10,1), pad=(10,10), expand_x=True),
        sg.Text("32.0 F", key="-OUTPUT-", size=(10,1), pad=(10,10), expand_x=True)
    ]    
]

window = sg.Window("Converter", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "-CONVERT-":
        input_value = values["-INPUT-"]

        if input_value.isnumeric():
        
            match values["-UNITS-"]:
        
                case "C to F":
                    output_value = round((float(input_value) * 9/5) + 32, 2)
                    # (0°C × 9/5) + 32 = 32°F
                    output_string = f"{output_value} F"
        
                case "F to C":
                    output_value = round((float(input_value) - 32) * 5/9, 2)
                    # (0°F − 32) × 5/9 = -17.78°C
                    output_string = f"{output_value} C"

            window["-OUTPUT-"].update(output_string)
                

window.close()







