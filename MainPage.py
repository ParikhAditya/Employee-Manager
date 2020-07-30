import PySimpleGUI as sg
layout = [
          [sg.Button('Add Employee',)],
          [sg.Button('View Payouts')],
          [sg.Button('Edit Employee Data')],
          [sg.Button('View All Employees')],
          [sg.Button('Exit')]
         ]

addemplayout = [
                [sg.Text('Employee Details:')],
                [sg.Text('First Name:',size(15,1),sg.InputText(''))],
                [sg.Text('Middle Name:',size(15,1),sg.InputText(''))],
                [sg.Text('Last Name:',size(15,1),sg.InputText(''))],
                [sg.Text('Position:',size(15,1),sg.InputText(''))],
                [sg.Text('Worked Since:',size(15,1),sg.CalendarButton())],
                [sg.Text('Salary:',size(15,1),sg.InputText(''))],
                [sg.Text('Incentives:'],
                [sg.Checkbox('Medicare')],
                [sg.Checkbox('Life Insurance')],
                [sg.Checkbox('Festive Bonus')],
                [sg.Submit(),sg.Exit()]
               ]

viewpaylayout = [
                 [sg.Text('Payout History')],
                 [sg.Listbox()],
                 [sg.Button('Exit')]
                ]

editemplayout = [
                 [sg.Text('Edit Employee Information')],
                 [sg.Text('Employee ID:',size=(15,1)),sg.InputText(''),sg.Button('Fetch')],
                 [sg.Text('First Name:',size(15,1),sg.InputText(''))],
                 [sg.Text('Middle Name:',size(15,1),sg.InputText(''))],
                 [sg.Text('Last Name:',size(15,1),sg.InputText(''))],
                 [sg.Text('Position:',size(15,1),sg.InputText(''))],
                 [sg.Text('Worked Since:',size(15,1),sg.CalendarButton())],
                 [sg.Text('Salary:',size(15,1),sg.InputText(''))],
                 [sg.Text('Incentives:'],
                 [sg.Checkbox('Medicare')],
                 [sg.Checkbox('Life Insurance')],
                 [sg.Checkbox('Festive Bonus')],
                 [sg.Button('Confirm'),sg.Text('Information Updated')],
                 [sg.Button('Exit')]
                ]
window = sg.Window('Payroll Manager').Layout(layout)
button, values = window.Read()

addempwindow = sg.Window('Add Employee').Layout(addemplayout)
button, values = addempwindow.Read()
