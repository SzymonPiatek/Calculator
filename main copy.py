import PySimpleGUI as sg

def create_window(theme):
    sg.theme(theme)
    sg.set_options(font = 'Calibri 18', button_element_size = (3, 2))

    size1 = (6, 3)

    layout = [
        [sg.Text('', font = 'Calibri 24', justification = 'right', expand_x = True, pad = (10, 20), right_click_menu = theme_menu, key = '-TEXT2-')],
        [sg.Text('0', font = 'Calibri 32', justification = 'right', expand_x = True, pad = (10, 20), right_click_menu = theme_menu, key = '-TEXT-')],
        [sg.Button('Undo', size = size1), sg.Button('(', size = size1), sg.Button(')', size = size1), sg.Button('Clear', expand_x = True, expand_y = True)],
        [sg.Button(7, size = size1), sg.Button(8, size = size1), sg.Button(9, size = size1), sg.Button('*', size = size1), sg.Button('**', expand_x = True, expand_y = True)],
        [sg.Button(4, size = size1), sg.Button(5, size = size1), sg.Button(6, size = size1), sg.Button('/', size = size1), sg.Button('**0.5', expand_x = True, expand_y = True)],
        [sg.Button(1, size = size1), sg.Button(2, size = size1), sg.Button(3, size = size1), sg.Button('-', size = size1), sg.Button('*(-1)', expand_x = True, expand_y = True)],
        [sg.Button(0, size = size1), sg.Button('.', size = size1), sg.Button('+', size = size1), sg.Button('=', expand_x = True, expand_y = True)] 
        ]
    return sg.Window('Calculator', layout, resizable = False)

theme_menu = ['menu', ['dark', 'DarkGray5', 'LightGrey1', 'BlueMono', 'random']]
window = create_window('LightGrey1')

full_operation = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    if event in theme_menu[1]:
        window.close()
        window = create_window(event)
        
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    functions = ['+', '-', '/', '*', '**', '**0.5', '*(-1)']
    brackets = ['(', ')']
    
    if event in numbers:
        full_operation.append(''.join(event))
        output = event
        window['-TEXT-'].update(output)
        
        window['-TEXT2-'].update(full_operation)
    
    if event in functions:
        if len(full_operation) >= 2 and full_operation[0][0].isdigit():
            if full_operation[-1] in functions:
                full_operation.pop(-1)
                if full_operation[-1][0].isdigit():
                    full_operation.append(''.join(event))
            elif full_operation[-1][0].isdigit():
                full_operation.append(''.join(event))
            elif full_operation[-1] in brackets:
                if full_operation[-1] == brackets[0]:
                    pass    
                elif full_operation[-1] == brackets[1]:
                    full_operation.append(''.join(event))
        elif len(full_operation) == 1:
            if full_operation[0] in brackets:
                pass
            elif full_operation[0][0].isdigit():
                full_operation.append(''.join(event))
        elif len(full_operation) == 0:
            pass
        else:
            full_operation.append(''.join(event))        
            
        window['-TEXT2-'].update(full_operation)
        
    if event in brackets:
        if len(full_operation) == 0:
            full_operation.append(''.join(brackets[0]))
            
        elif full_operation[0][0].isdigit():
            if len(full_operation) >= 2:
                if full_operation[-1][0].isdigit():
                    if event == brackets[0]:
                        pass
                    elif event == brackets[1]:
                        full_operation.append(''.join(event))
                elif full_operation[-1] in functions:
                    if event == brackets[0]:
                        full_operation.append(''.join(event))
                    elif event == brackets[1]:
                        pass
                      
        elif full_operation[0] in brackets:
            if len(full_operation) >= 2 and (full_operation[-1][0].isdigit() or full_operation[-1] in functions):
                if full_operation[-1] in functions:
                    full_operation.append(''.join(brackets[0]))
                elif full_operation[-1][0].isdigit():
                    full_operation.append(''.join(event))
            elif full_operation[-1] in functions:
                full_operation.append(''.join(brackets[1]))
                
                
        elif full_operation[-1] in brackets:
            full_operation.append(''.join(event))
                
        window['-TEXT2-'].update(full_operation)        
        
    if event == '=':
        if len(full_operation) == 0:
            pass
        elif ((full_operation[-1] == brackets[0]) or (full_operation[-1] in functions)):
            full_operation.pop(-1)
            result = round((eval(''.join(full_operation))), 3)
            window['-TEXT-'].update(result)
            full_operation = []
            full_operation = [str(result)]
        
        window['-TEXT2-'].update(full_operation)        
        
    if event == 'Undo':
        if len(full_operation) == 0:
            pass
        elif len(full_operation) == 1:
            full_operation = []
        else:
            full_operation.pop(-1)
    
    if event == 'Clear':
        full_operation = []
        window['-TEXT-'].update(0)
        window['-TEXT2-'].update('')
    
window.close()