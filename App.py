import sqlite3
from sqlite3 import Error
import PySimpleGUI as sg
import matplotlib.pyplot as plt

def addemployeesubmit(ev2,vals2):
    conn = sqlite3.connect('C:\\Users\\hp\\Desktop\\Project\\db\\EmployeePayroll.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO empdata VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);",(vals2[0],vals2[1],vals2[2],vals2[3],vals2[4],vals2[5],vals2[6],vals2[7],vals2[8],vals2[9],vals2[10],vals2[11],vals2['bankname'],vals2['branchname'],vals2['accno'],vals2['acctype'],vals2[12],vals2[13],vals2[14],'NULL',0,0,0))
    conn.commit()
    return

def viewempfetch():
    conn = sqlite3.connect('C:\\Users\\hp\\Desktop\\Project\\db\\EmployeePayroll.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM empdata;")
    options = list()
    options = cur.fetchall()
    conn.commit()
    return options

def remempfetch(empidval):
    conn = sqlite3.connect('C:\\Users\\hp\\Desktop\\Project\\db\\EmployeePayroll.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM empdata WHERE empid =(?);',[empidval])
    empval = list()
    empval = cur.fetchall()
    conn.commit()
    return empval

def remempdelete(val):
    conn = sqlite3.connect('C:\\Users\\hp\\Desktop\\Project\\db\\EmployeePayroll.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM empdata where empid =(?);",[val])
    conn.commit()
    return

def createpayout(val):
    conn = sqlite3.connect('C:\\Users\\hp\\Desktop\\Project\\db\\EmployeePayroll.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM empdata WHERE empid =(?);",[val])
    empval = list()
    empval = cur.fetchall()
    conn.commit()
    return empval

def payoutdb(vallist,z,dval,mval,yval,x):
    d0 = vallist[0][0]
    d1 = vallist[0][1]
    d2 = vallist[0][3]
    d3 = vallist[0][8]
    d4 = dval
    d5 = mval
    d6 = yval
    conn = sqlite3.connect('C:\\Users\\hp\\Desktop\\Project\\db\\EmployeePayroll.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO payout VALUES(?,?,?,?,?,?,?);",(d0,d1,d2,z,d4,d5,d6))
    cur.execute("UPDATE empdata SET loanrem=? WHERE empid=?",[x,d0])
    conn.commit()
    return

def viewpayfetch():
    conn = sqlite3.connect('C:\\Users\\hp\\Desktop\\Project\\db\\EmployeePayroll.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM payout;")
    options = list()
    options = cur.fetchall()
    conn.commit()
    return options

def editfetch(data):
    conn = sqlite3.connect('C:\\Users\\hp\\Desktop\\Project\\db\\EmployeePayroll.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM empdata WHERE empid=(?);",[data])
    options = list()
    options = cur.fetchall()
    conn.commit()
    return options

'''
def editloan(data):
    conn = sqlite3.connect('C:\\Users\\hp\\Desktop\\Project\\db\\EmployeePayroll.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM loan WHERE empid=(?);",[data])
    options = list()
    options = cur.fetchall()
    conn.commit()
    return options    
'''

def updatemp(di,d0,d1,d2,d3,d4,d5):
    conn = sqlite3.connect('C:\\Users\\hp\\Desktop\\Project\\db\\EmployeePayroll.db')
    cur = conn.cursor()
    cur.execute("UPDATE empdata SET fname=?,mname=?,lname=?,position=?,joindt=?,salary=? WHERE empid =?;",[d0,d1,d2,d3,d4,d5,di])
    conn.commit()
    return

def createloan(x0,x1,x2,x3):
    conn = sqlite3.connect('C:\\Users\\hp\\Desktop\\Project\\db\\EmployeePayroll.db')
    cur = conn.cursor()
    cur.execute("UPDATE empdata SET loanid=?, loanval=?, loandur=?, loanrem=? WHERE empid=?;",[x1,x2,x3,x3,x0])
    conn.commit()
    return

def promosal(d0,val):
    conn = sqlite3.connect('C:\\Users\\hp\\Desktop\\Project\\db\\EmployeePayroll.db')
    cur = conn.cursor()
    cur.execute("UPDATE empdata SET salary=? WHERE empid=?;",[val,d0])
    conn.commit()
    return

    
mainlayout = [
              [sg.Button('Create Payout',size=(20,1),pad=(10,10)),sg.VerticalSeparator(pad=(10,0)),sg.Button('View Payout History',size=(20,1),pad=(10,10))],
              [sg.Button('Add Employee To Payroll',size=(20,1),pad=(10,10)),sg.VerticalSeparator(pad=(10,0)),sg.Button('View All Employees',size=(20,1),pad=(10,10))],
              [sg.Button('Update Employee Data',size=(20,1),pad=(10,10)),sg.VerticalSeparator(pad=(10,0)),sg.Button('Remove Employee',size=(20,1),pad=(10,10))],
              [sg.Button('Promotion Services',size=(20,1),pad=(10,10)),sg.VerticalSeparator(pad=(10,0)),sg.Button('Statistics',size=(20,1),pad=(10,10))],
              [sg.Button('Loan Service',size=(20,1),pad=(10,10)),sg.VerticalSeparator(pad=(10,0)),sg.Button('Exit',size=(20,1),pad=(10,10))],
              #[sg.Button('View Payout History',size=(20,1))],              
              #[sg.Button('View All Employees',size=(20,1))],
              #[sg.Button('Remove Employee',size=(20,1))],
              #[sg.Button('Exit',size=(20,1))]
             ]

mainwindow = sg.Window(title='Payroll Manager',size=(430,250)).Layout(mainlayout)  
addempwindow_active=False
viewpaywindow_active=False
promowindow_active=False
editempwindow_active=False
loanservwindow_active=False
payoutwindow_active=False
viewempwindow_active=False
remempwindow_active=False
statwindow_active=False
payhistorywindow_active=False

while True:  
    ev1, vals1 = mainwindow.Read(timeout=100)
    if ev1 == 'Exit':
        mainwindow.Close()
    if ev1 == 'Add Employee To Payroll' and not addempwindow_active:  
        addempwindow_active = True  
        mainwindow.Hide()  
        addemplayout = [
                        [sg.Text('Employee Details:')],
                        [sg.Text('Employee ID:',size=(10,1)),sg.InputText('',size=(25,1))],
                        [sg.Text('First Name:',size=(10,1)),sg.InputText('')],
                        [sg.Text('Middle Name:',size=(10,1)),sg.InputText('')],
                        [sg.Text('Last Name:',size=(10,1)),sg.InputText('')],
                        [sg.Text('Address:',size=(10,1)),sg.InputText('',size=(45,4))],
                        [sg.Text('Pincode:',size=(10,1)),sg.InputText('',size=(10,1)),sg.Text('City:',size=(4,1)),sg.InputText('',size=(20,1))],
                        [sg.Text('State:',size=(10,1)),sg.InputCombo(["Andaman and Nicobar Islands","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chandigarh","Chhattisgarh","Dadra and Nagar Haveli","Daman and Diu","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Lakshadweep","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","National Capital Territory of Delhi","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"])],
                        [sg.Text('Department:',size=(10,1)),sg.InputCombo(['IT','Sales','Cleaning','HR'])],
                        [sg.Text('Position:',size=(10,1)),sg.InputText('')],
                        [sg.Text('Worked Since:',size=(10,1)),sg.InputText('')],
                        [sg.Text('Salary:',size=(10,1)),sg.InputText('')],
                        [sg.Text('Bank:',size=(10,1)),sg.InputCombo(["Allahabad Bank","Andhra Bank","Axis Bank Limited","Bandhan Bank Limited","Bank of Baroda","Bank of India","Bank of Maharashtra","Canara Bank","Catholic Syrian Bank Limited","Central Bank of India","City Union Bank Limited","Corporation Bank","DCB Bank Limited","Dena Bank","Dhanlaxmi Bank Limited","Federal Bank Limited","HDFC Bank Limited","ICICI Bank Limited","IDFC Bank Limited","Indian Bank","Indian Overseas Bank","IndusInd Bank Limited","Jammu & Kashmir Bank Limited","Karnataka Bank Limited","Karur Vysya Bank Limited","Kotak Mahindra Bank Limited","Lakshmi Vilas Bank Limited","Nainital Bank Limited","Oriental Bank of Commerce","Punjab & Sind Bank","Punjab National Bank","RBL Bank Limited","South Indian Bank Limited","Syndicate Bank","Tamilnad Mercantile Bank Limited","UCO Bank","Union Bank of India","United Bank of India","Vijaya Bank","YES Bank Limited"],key='bankname')],
                        [sg.Text('Branch:',size=(10,1)),sg.InputText('',size=(25,1),key='branchname')],
                        [sg.Text('Account No:',size=(10,1)),sg.InputText('',size=(25,1),key='accno')],
                        [sg.Text('Account Type:',size=(10,1)),sg.InputCombo(['Savings','Current'],key='acctype')],
                        [sg.Text('Incentives:')],
                        [sg.Checkbox('Medicare')],
                        [sg.Checkbox('Life Insurance')],
                        [sg.Checkbox('Festive Bonus')],
                        [sg.Text('',size=(30,1),key='Updatekey')],
                        [sg.Button('Submit'),sg.Exit()]
                       ]

        addempwindow = sg.Window('Employee Details:',size=(600,610)).Layout(addemplayout)  
        while True:  
            ev2, vals2 = addempwindow.Read()
            if ev2 == 'Submit':
                addemployeesubmit(ev2,vals2)
                addempwindow.FindElement('Updatekey').Update('Employee Added')
            if ev2 is None or ev2 == 'Exit':  
                addempwindow.Close()  
                addempwindow_active = False  
                mainwindow.UnHide()  
                break

    if ev1 == 'Promotion Services' and not promowindow_active:  
        promowindow_active = True  
        mainwindow.Hide()  
        promolayout = [
                       [sg.Text('Employee ID:',size=(10,1)),sg.InputText('',key='empidkey'),sg.Button('Fetch')],
                       [sg.Text('First Name:',size=(15,1)),sg.Text('',key='fnamekey')],
                       [sg.Text('Last Name:',size=(15,1)),sg.Text('',key='lnamekey')],
                       [sg.Text('Department:',size=(15,1)),sg.Text('',key='deptkey')],
                       [sg.Text('Position:',size=(15,1)),sg.Text('',key='poskey')],
                       [sg.Text('Salary:',size=(15,1)),sg.Text('',size=(15,1),key='salkey')],
                       [sg.Text('Increment Percentage:',size=(18,1)),sg.InputCombo(["1","1.5","2","2.5","3","3.5","4","4.5","5","5.5","6","6.5","7","7.5","8","8.5","9","9.5","10","10.5","11","11.5","12","12.5","13","13.5","14","14.5","15","15.5","16","16.5","17","17.5","18","18.5","19","19.5","20"]),sg.Button('Increment')],
                       #[sg.Text('New Salary:',size=(15,1)),sg.Text('',key='incrsal')],
                       [sg.Text('Decrement Percentage:',size=(18,1)),sg.InputCombo(["1","1.5","2","2.5","3","3.5","4","4.5","5","5.5","6","6.5","7","7.5","8","8.5","9","9.5","10","10.5","11","11.5","12","12.5","13","13.5","14","14.5","15","15.5","16","16.5","17","17.5","18","18.5","19","19.5","20"]),sg.Button('Decrement')],
                       [sg.Text('New Salary:',size=(15,1)),sg.Text('',size=(25,1),key='crsal')],
                       [sg.Button('Finalize'),sg.Button('Exit')]
                      ]

        promowindow = sg.Window('All Employees:',size=(600,610)).Layout(promolayout) 
        c = 0
        while True:
            ev2, vals2 = promowindow.Read()
            if ev2 == 'Fetch':
                val = promowindow.FindElement('empidkey').Get()
                vallist = createpayout(val)
                promowindow.FindElement('fnamekey').Update(value=vallist[0][1])
                promowindow.FindElement('lnamekey').Update(value=vallist[0][3])
                promowindow.FindElement('poskey').Update(value=vallist[0][9])
                promowindow.FindElement('deptkey').Update(value=vallist[0][8])
                promowindow.FindElement('salkey').Update(value=vallist[0][11])
            if ev2 == 'Increment':
                val = promowindow.FindElement('empidkey').Get()
                vallist = createpayout(val)
                c = float(vals2[0])
                sal = float(vallist[0][11])/100
                inc = c * sal
                finsalary = float(vallist[0][11]) + inc
                c = finsalary
                promowindow.FindElement('crsal').Update(str(finsalary))
            if ev2 == 'Decrement':
                val = promowindow.FindElement('empidkey').Get()
                vallist = createpayout(val)                
                c = float(vals2[1])
                sal = float(vallist[0][11])/100
                inc = c * sal
                finsalary = float(vallist[0][11]) - inc
                c = finsalary
                promowindow.FindElement('crsal').Update(str(finsalary))
            if ev2 == 'Finalize':
                val = promowindow.FindElement('empidkey').Get()
                vallist = createpayout(val)
                d0 = vallist[0][0]
                promosal(d0,c)
            if ev2 is None or ev2 == 'Exit':  
                promowindow.Close()  
                promowindow_active = False  
                mainwindow.UnHide()  
                break

    if ev1 == 'View All Employees' and not viewempwindow_active:  
        viewempwindow_active = True  
        mainwindow.Hide()  
        viewemplayout = [
                         [sg.Button('Fetch')],
                         [sg.Listbox(values=[],size=(80,15),key='listbox')],
                         [sg.Button('Exit')]
                        ]

        viewempwindow = sg.Window('All Employees:',size=(600,610)).Layout(viewemplayout) 
        while True:
            ev2, vals2 = viewempwindow.Read()  
            if ev2 == 'Fetch':
                data = viewempfetch()
                viewempwindow.FindElement('listbox').Update(values=data)
            if ev2 is None or ev2 == 'Exit':  
                viewempwindow.Close()  
                viewempwindow_active = False  
                mainwindow.UnHide()  
                break

    if ev1 == 'Loan Service' and not loanservwindow_active:  
        loanservwindow_active = True  
        mainwindow.Hide()  
        loanservlayout = [
                          [sg.Text('Employee ID:',size=(10,1)),sg.InputText('',key='empidkey'),sg.Button('Fetch')],
                          [sg.Text('First Name:',size=(15,1)),sg.Text('',key='fnamekey')],
                          [sg.Text('Last Name:',size=(15,1)),sg.Text('',key='lnamekey')],
                          [sg.Text('Department:',size=(15,1)),sg.Text('',key='deptkey')],
                          [sg.Text('Position:',size=(15,1)),sg.Text('',key='poskey')],
                          [sg.Text('Salary:',size=(15,1)),sg.Text('',key='salkey')],
                          [sg.Text('',size=(18,1),key='notif')],
                          [sg.Text('Loan ID:',size=(20,1)),sg.InputText('',key='loanid')],
                          [sg.Text('Loan Amount:',size=(20,1)),sg.InputText('',key='loanval')],
                          [sg.Text('Payment Tenure(in months):',size=(20,1)),sg.InputText('',key='loandur')],
                          [sg.Text('',size=(20,1),key='createnotif')],
                          [sg.Button('Create'),sg.Button('Exit')]
                         ]


        loanservwindow = sg.Window('Loan Service',size=(600,610)).Layout(loanservlayout) 
        while True:
            ev2, vals2 = loanservwindow.Read()
            if ev2 == 'Fetch':
                val = loanservwindow.FindElement('empidkey').Get()
                listdata = editfetch(val)
                x = listdata[0][19]
                loanservwindow.FindElement('fnamekey').Update(value=listdata[0][1])
                loanservwindow.FindElement('lnamekey').Update(value=listdata[0][3])
                loanservwindow.FindElement('poskey').Update(value=listdata[0][9])
                loanservwindow.FindElement('deptkey').Update(value=listdata[0][8])
                loanservwindow.FindElement('salkey').Update(value=listdata[0][11])
                if x != 'NULL':
                    loanservwindow.FindElement('notif').Update('Loan exists')
                    loanservwindow.FindElement('loanid').Update(value=listdata[0][20])
                    loanservwindow.FindElement('loanval').Update(value=listdata[0][21])
                    loanservwindow.FindElement('loandur').Update(value=listdata[0][22])
                if x == 'NULL':
                    loanservwindow.FindElement('notif').Update('No existing loan found')

            if ev2 == 'Create':
                n0 = loanservwindow.FindElement('empidkey').Get()
                n1 = loanservwindow.FindElement('loanid').Get()
                n2 = loanservwindow.FindElement('loanval').Get()
                n3 = loanservwindow.FindElement('loandur').Get()
                createloan(n0,n1,n2,n3)
                loanservwindow.FindElement('createnotif').Update('Loan created')
            if ev2 is None or ev2 == 'Exit':  
                loanservwindow.Close()  
                loanservwindow_active = False  
                mainwindow.UnHide()  
                break    
    
    if ev1 == 'Update Employee Data' and not editempwindow_active:  
        editempwindow_active = True  
        mainwindow.Hide()  
        editemplayout = [
                         [sg.Text('Edit Employee Information')],
                         [sg.Text('Employee ID:',size=(15,1)),sg.InputText('',key='idfetch'),sg.Button('Fetch')],
                         [sg.Text('First Name:',size=(15,1)),sg.InputText('',key='fnamekey')],
                         [sg.Text('Middle Name:',size=(15,1)),sg.InputText('',key='mnamekey')],
                         [sg.Text('Last Name:',size=(15,1)),sg.InputText('',key='lnamekey')],
                         [sg.Text('Position:',size=(15,1)),sg.InputText('',key='poskey')],
                         [sg.Text('Worked Since:',size=(15,1)),sg.InputText('',key='dtkey')],
                         [sg.Text('Salary:',size=(15,1)),sg.InputText('',key='salkey')],
                         [sg.Text('Incentives:')],
                         [sg.Checkbox('Medicare')],
                         [sg.Checkbox('Life Insurance')],
                         [sg.Checkbox('Festive Bonus')],
                         [sg.Button('Update'),sg.Button('Exit')]
                        ]

        editempwindow = sg.Window('Update Employee Details',size=(600,610)).Layout(editemplayout)  
        while True:  
            ev2, vals2 = editempwindow.Read()
            if ev2 == 'Fetch':
                val = editempwindow.FindElement('idfetch').Get()
                listdata = editfetch(val)
                editempwindow.FindElement('fnamekey').Update(value=listdata[0][1])
                editempwindow.FindElement('mnamekey').Update(value=listdata[0][2])
                editempwindow.FindElement('lnamekey').Update(value=listdata[0][3])
                editempwindow.FindElement('poskey').Update(value=listdata[0][9])
                editempwindow.FindElement('dtkey').Update(value=listdata[0][10])
                editempwindow.FindElement('salkey').Update(value=listdata[0][11])
            if ev2 == 'Update':
                di=editempwindow.FindElement('idfetch').Get()
                d0=editempwindow.FindElement('fnamekey').Get()
                d1=editempwindow.FindElement('mnamekey').Get()
                d2=editempwindow.FindElement('lnamekey').Get()
                d3=editempwindow.FindElement('poskey').Get()
                d4=editempwindow.FindElement('dtkey').Get()
                d5=editempwindow.FindElement('salkey').Get()
                updatemp(di,d0,d1,d2,d3,d4,d5)
            if ev2 is None or ev2 == 'Exit':
                editempwindow.Close()  
                editempwindow_active = False  
                mainwindow.UnHide()  
                break

    if ev1 == 'Create Payout' and not payoutwindow_active:
        payoutwindow_active = True  
        mainwindow.Hide()  
        payoutlayout = [
                        [sg.Text('Employee ID:',size=(10,1)),sg.InputText('',key='empidkey'),sg.Button('Fetch')],
                        [sg.Text('First Name:',size=(15,1)),sg.Text('',size=(15,1),key='fnamekey')],
                        [sg.Text('Last Name:',size=(15,1)),sg.Text('',key='lnamekey')],
                        [sg.Text('Department:',size=(15,1)),sg.Text('',key='deptkey')],
                        [sg.Text('Position:',size=(15,1)),sg.Text('',key='poskey')],
                        [sg.Text('Payout Date:',size=(15,1)),sg.InputCombo(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'],key='ddkey'),sg.InputCombo(['January','February','March','April','May','June','July','August','September','October','November','December'],key='mmkey'),sg.InputCombo(['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022'],key='yykey')],
                        [sg.Text('Salary:',size=(15,1)),sg.Text('',key='salkey')],
                        [sg.Text('Loan amount:',size=(15,1)),sg.Text('',size=(15,1),key='loankey')],
                        [sg.Text('Tax deduction:',size=(15,1)),sg.Text('',size=(15,1),key='notif')],
                        [sg.Text('Loan payment:'),sg.Text('',size=(10,1),key='loanamt'),sg.Text('Monthly payments remaining:'),sg.Text('',size=(5,1),key='emikey')],
                        [sg.Text('Final Salary:',size=(15,1)),sg.Text('',size=(15,1),key='finsal')],
                        [sg.Button('Create'),sg.Button('Exit')]
                       ]

        payoutwindow = sg.Window('Create Payout',size=(600,400)).Layout(payoutlayout)  
        while True:  
            ev2, vals2 = payoutwindow.Read()
            if ev2 == 'Fetch':
                val = payoutwindow.FindElement('empidkey').Get()
                vallist = createpayout(val)
                payoutwindow.FindElement('fnamekey').Update(value=vallist[0][1])
                payoutwindow.FindElement('lnamekey').Update(value=vallist[0][3])
                payoutwindow.FindElement('deptkey').Update(value=vallist[0][8])
                payoutwindow.FindElement('poskey').Update(value=vallist[0][9])
                payoutwindow.FindElement('salkey').Update(value=vallist[0][11])
                payoutwindow.FindElement('loankey').Update(value=vallist[0][20])
                ddval = vals2['ddkey']
                mmval = vals2['mmkey']
                yyval = vals2['yykey']
                s = 0
                if int(vallist[0][11]) > 250000:
                    r = vallist[0][11]/100
                    s = r * 5
                    payoutwindow.FindElement('notif').Update(str(s))
                if int(vallist[0][11]) < 250000:
                    payoutwindow.FindElement('notif').Update('Not taxable')
                a = int(vallist[0][20])
                b = int(vallist[0][21])
                if b!= 0:
                    c = a/b
                    payoutwindow.FindElement('loanamt').Update(str(c))
                    d = b - 1
                    z = int(vallist[0][11]) - s - c
                    payoutwindow.FindElement('finsal').Update(str(z))
                    payoutwindow.FindElement('emikey').Update(str(d))
                    #payoutdb(vallist,str(z),ddval,mmval,yyval,str(d))
                if b == 0:
                    z = int(vallist[0][11]) - s
                    payoutwindow.FindElement('finsal').Update(str(z))
                    payoutwindow.FindElement('emikey').Update('N.A.')
                    #payoutdb(vallist,str(z),ddval,mmval,yyval,str(0))
            if ev2 == 'Create':
                val = payoutwindow.FindElement('empidkey').Get()
                vallist = createpayout(val)
                ddval = vals2['ddkey']
                mmval = vals2['mmkey']
                yyval = vals2['yykey']
                s = 0
                if int(vallist[0][11]) > 250000:
                    r = vallist[0][11]/100
                    s = r * 5
                    payoutwindow.FindElement('notif').Update(str(s))
                if int(vallist[0][11]) < 250000:
                    payoutwindow.FindElement('notif').Update('Not taxable')
                a = int(vallist[0][20])
                b = int(vallist[0][21])
                if b!= 0:
                    c = a/b
                    #payoutwindow.FindElement('loanamt').Update(str(c))
                    d = b - 1
                    z = int(vallist[0][11]) - s - c
                    #payoutwindow.FindElement('finsal').Update(str(z))
                    #payoutwindow.FindElement('emikey').Update(str(d))
                    payoutdb(vallist,str(z),ddval,mmval,yyval,str(d))
                if b == 0:
                    z = int(vallist[0][11]) - s
                    #payoutwindow.FindElement('finsal').Update(str(z))
                    #payoutwindow.FindElement('emikey').Update('N.A.')
                    payoutdb(vallist,str(z),ddval,mmval,yyval,str(0))

            if ev2 is None or ev2 == 'Exit':  
                payoutwindow.Close()  
                payoutwindow_active = False  
                mainwindow.UnHide()  
                break

    if ev1 == 'Remove Employee' and not remempwindow_active:
        remempwindow_active = True  
        mainwindow.Hide()  
        rememplayout = [
                        [sg.Text('Employee ID:',size=(10,1)),sg.InputText('',key='empidkey'),sg.Button('Fetch')],
                        [sg.Text('First Name:',size=(15,1)),sg.Text(text='',key='fnamekey')],
                        [sg.Text('Last Name:',size=(15,1)),sg.Text(text='',key='lnamekey')],
                        [sg.Text('Department:',size=(15,1)),sg.Text(text='',key='deptkey')],
                        [sg.Text('Position:',size=(15,1)),sg.Text(text='',key='poskey')],
                        [sg.Text('Worked Since:',size=(15,1)),sg.Text(text='',key='dtkey')],
                        [sg.Text('Salary:',size=(15,1)),sg.Text(text='',key='salkey')],
                        [sg.Button('Remove'),sg.Button('Exit')]
                       ]

        remempwindow = sg.Window('Remove Employee',size=(600,610)).Layout(rememplayout)  
        while True:  
            ev2, vals2 = remempwindow.Read()
            if ev2 == 'Fetch':
                empidval = remempwindow.FindElement('empidkey').Get()
                empdat = remempfetch(empidval)
                d0 = empdat[0][0]
                d1 = empdat[0][1]
                d2 = empdat[0][2]
                d3 = empdat[0][3]
                d4 = empdat[0][4]
                d5 = empdat[0][8]
                d6 = empdat[0][9]
                d7 = empdat[0][10]
                d8 = empdat[0][11]
                d9 = empdat[0][9]
                #d10 = empdat[0][10]
                #d11 = empdat[0][11]
                remempwindow.FindElement('fnamekey').Update(value=d1)
                remempwindow.FindElement('lnamekey').Update(value=d3)
                remempwindow.FindElement('deptkey').Update(value=d5)
                remempwindow.FindElement('poskey').Update(value=d6)
                remempwindow.FindElement('dtkey').Update(value=d7)
                remempwindow.FindElement('salkey').Update(value=d8)
            if ev2 == 'Remove':
                empidval = remempwindow.FindElement('empidkey').Get()
                remempdelete(empidval)                
            if ev2 is None or ev2 == 'Exit':  
                remempwindow.Close()  
                remempwindow_active = False  
                mainwindow.UnHide()  
                break

    if ev1 == 'View Payout History' and not payhistorywindow_active:  
        payhistorywindow_active = True  
        mainwindow.Hide()  
        payhistorylayout = [
                            [sg.Text('Employee ID:',size=(15,1)),sg.InputText('',size=(15,1),key='fetchempid')],
                            [sg.Text('Department:',size=(15,1)),sg.InputCombo(['IT','Sales','Cleaning','HR'],key='deptcombo')],
                            [sg.Text('From:'),sg.InputCombo(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'],key='ddkey1'),sg.InputCombo(['January','February','March','April','May','June','July','August','September','October','November','December'],key='mmkey1'),sg.InputCombo(['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022'],key='yykey1')],
                            [sg.Text('To:'),sg.InputCombo(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'],key='ddkey2'),sg.InputCombo(['January','February','March','April','May','June','July','August','September','October','November','December'],key='mmkey2'),sg.InputCombo(['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022'],key='yykey2')],                       
                            [sg.Button('Fetch')],
                            [sg.Listbox(values=[],size=(80,15),key='listbox')],
                            [sg.Button('Exit')]
                           ]

        payhistorywindow = sg.Window('Payouts:',size=(600,610)).Layout(payhistorylayout) 
        while True:
            ev2, vals2 = payhistorywindow.Read()  
            if ev2 == 'Fetch':
                data = viewpayfetch()
                payhistorywindow.FindElement('listbox').Update(values=data)
            if ev2 is None or ev2 == 'Exit':  
                payhistorywindow.Close()  
                payhistorywindow_active = False  
                mainwindow.UnHide()  
                break

    if ev1 == 'Statistics' and not statwindow_active:  
        statwindow_active = True  
        mainwindow.Hide()  
        statlayout = [
                      [sg.Text('Employee ID:',size=(15,1)),sg.InputText('',size=(15,1),key='fetchempid')],
                      [sg.Text('Department:',size=(15,1)),sg.InputCombo(['IT','Sales','Cleaning','HR'],key='deptcombo')],
                      [sg.Button('Fetch')],
                      [sg.Listbox(values=[],size=(80,15),key='listbox')],
                      [sg.Button('Exit')]
                     ]

        statwindow = sg.Window('Statistics:',size=(600,610)).Layout(statlayout) 
        while True:
            ev2, vals2 = statwindow.Read()  
            if ev2 == 'Fetch':
                data = viewpayfetch()
                payhistorywindow.FindElement('listbox').Update(values=data)
                '''
                5data1 = {'apples': 10, 'oranges': 15, 'lemons': 5, 'limes': 20}
                names = list(data1.keys())
                values = list(data1.values())

                fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
                axs[2].plot(names, values)
                '''                
                
            if ev2 is None or ev2 == 'Exit':  
                statwindow.Close()  
                statwindow_active = False
                window_active = False  
                mainwindow.UnHide()  
                break
