import os
import csv
#Initialize list to store employees' information
employeeList = []
ssnDict ={}
#clear IDLE shell window
def cls():
    print ('\n' * 50)

#display employee information in the required format
def employeeFortmattedInfo(name,ssn,phone,email,salary):
    print("")
    print('------------- {0:s} ------------------------------------'.format(name))
    print('       SSN: {0:s}'.format(ssn))
    print('       Phone: {0:s}'.format(phone))
    print('       Email: {0:s}'.format(email))
    print('       Salary: {0:s}'.format(salary))
    print("--------------------------------------------------------")
    print("")
    print(len(employeeList))

#view all employees in the system
def viewAllEmployeeInfo():
    cls()
    print("----------------------------------------------------------")
    print("")
    print("            View all employees in the system")
    print("")
    print("----------------------------------------------------------")
    print("")
    if(len(employeeList))==0:
        #when no employees in the system,view the "No employees in the list" message
        print("----------------------------------------------------------")
        print("             No employees in the list.")
        print("----------------------------------------------------------")
    else:
        try:
        #display all employees in the system
            for i in range(0, len(employeeList)):
                line = employeeList[i].split(',')
                employeeFortmattedInfo(line[0],line[1],line[2],line[3],line[4])
        except IndexError:
                cls()
    try:
        option=int(input('Enter 0 to exit or any key to continue: '))
        if option == 0:
            cls()
    except:
        cls()

#add employee to the system
def addEmployeeToList():
    cls()
    print("------------------------------------------------------------------------")
    print("")
    print("            Add employee Information")
    print("")
    print("------------------------------------------------------------------------")
    print("")
    try:
        #allows users to enter the employee Name,SSN,Phone,Email, and Salary
        name=input('Employee Name: ')
        while name == "":
            name=input('Please enter a name: ')
            continue
        ssn= input('Employee SSN: ')
        while ssn == "":
            ssn = input('Please enter a number: ')
            continue
        phone=input('Employee Phone No.: ')
        while phone == "":
            phone = input('Please enter a number: ')
            continue
        email=input('Employee Email: ')
        while "@" not in email:
                email=input('Please enter a valid email address: ')
                continue
        salary=input('Employee Salary: ')
        while salary == "":
            salary = input('Please enter a number: ')
            continue
        line = name+','+ssn+','+phone +',' +email +',' +salary
        index= len(employeeList)
        employeeList.insert(index, line)
        ssnDict[ssn]= index
    except:
        cls()
        addEmployeeToList()
    print("")
    print("Employee information has been successfully added to the list.")
    print("")
    print("-----------------------------------------------------------------------")
    print("")
    try:
        #allow users to add new employee or return to the main menu when they enter zero
        option=int(input('Enter 0 to return to main menu, or any other number to add new employee: '))
        if option == 0:
            cls()
        else:
            cls()
            addEmployeeToList()
    except:
          cls()
          addEmployeeToList()
#edit employee info
def editEmployeeInfo():
    cls()
    print("------------------------------------------------------------------------")
    print("")
    print("            Edit employee Information")
    print("")
    print("------------------------------------------------------------------------")
    print("")
    try:
        userSSNsearch = input ('Enter an employee SSN to edit: ')
        while userSSNsearch == "":
            userSSNsearch = input ('Enter an employee SSN: ')
            continue
        if userSSNsearch in ssnDict:
            ssnIndex = ssnDict[userSSNsearch]
            line = employeeList[ssnIndex].split(',')
            employeeFortmattedInfo(line[0],line[1],line[2],line[3],line[4])
        while userSSNsearch not in ssnDict:
            print("Employee not in system")
            userSSNsearch = input ('Enter an employee SSN: ')
            continue
        
#allows users to edit the employee Name,SSN,Phone,Email, and Salary
        name=input('Employee Name: ')
        ssn= input('Employee SSN: ')
        phone=input('Employee Phone No.: ')
        email=input('Employee Email: ')
        salary=input('Employee Salary: ')
        employeeLine = name+','+ssn+','+phone +',' +email +',' +salary
        employeeList.pop(ssnIndex)
        employeeList.insert(ssnIndex,employeeLine)
        print("\n")
        print("Updated employee information")
        line = employeeList[ssnIndex].split(',')
        employeeFortmattedInfo(line[0],line[1],line[2],line[3],line[4])
    except:
        cls()
    print("")
    print("Employee information has been successfully edited.")
    print("")
    print("-----------------------------------------------------------------------")
    print("")
    try:
        #allow users to return to the main menu when they enter zero
        option=int(input('Enter 0 or press any key to return to main menu: '))
        if option == 0:
            cls()
    except:
        cls()

#search employee by SSN
def ssnSearch():
    cls()
    print("------------------------------------------------------------------------")
    print("")
    print("            Search employee Information by SSN")
    print("")
    print("------------------------------------------------------------------------")
    print("")
    try:
        userSSNsearch = input ('Enter an employee SSN: ')
        while userSSNsearch == "":
            userSSNsearch = input ('Enter an employee SSN: ')
            continue
        if userSSNsearch in ssnDict:
            ssnIndex = ssnDict[userSSNsearch]
            line = employeeList[ssnIndex].split(',')
            employeeFortmattedInfo(line[0],line[1],line[2],line[3],line[4])
    except:
        cls()
    try:
        #allow users to return to the main menu when they enter zero
        option=int(input('Enter 0 or press any key to return to main menu: '))
        if option == 0:
            cls()
    except:
        cls()
def exportEmployeeInfo():
        from tkinter.filedialog import asksaveasfile
        file=asksaveasfile(mode='w',defaultextension=".txt")
        if file:
            for i in range(0, len(employeeList)):
                file.write(employeeList[i])
                file.write("\n")
                print("Employees' record exported to file.\n\n")
        
    
def importEmployeeInfo():
    from tkinter.filedialog import askopenfilename
    filename = askopenfilename()
    file = open(filename,"r")
    lines = file.readlines()
    index = 0
    for line in lines:
        try:
            employeeList.insert(index, line)
            index +=1
            print('File imported.')
        except IndexError:
            continue
    try:
        #allow users to return to the main menu when they enter zero
        option=int(input('Enter 0 or press any key to return to main menu: '))
        if option == 0:
            cls()
    except:
        cls()
#display the system "main menu"
def printOptions():
    print("             -----------------Employee Management System ------------------------\n")
    print('                            There are ( {0:2} ) employees in the system.'.format (len(employeeList)))
    print("\n           ----------------------------------------------------------------------")
    print("1. Add new employee \n")
    print("2. View all employees \n")
    print("3. Search employee by SSN \n")
    print("4. Edit employee information \n")
    print("5. Export emplyee information \n")
    print("6. Import employee information \n")
    print("\n           ----------------------------------------------------------------------")
    #validate the user selection
    try:
        answer=int(input('Please enter your option number: '))
        
    except ValueError:
        print("Not a number")
        return 100
    print("")
    print("--------------------------------------------------")
    print("")
    return answer
#utilize looping to run the Python script constantly
while True:
    cls()
    mode = printOptions()
    #add employee to the system
    if mode == 1:
        cls()
        addEmployeeToList()
    #view all employees in the system
    if mode == 2:
        cls()
        viewAllEmployeeInfo()
    #search employee by SSN
    if mode == 3:
        cls()
        ssnSearch()
    #edit employee
    if mode == 4:
        cls()
        editEmployeeInfo()
    #export employee information
    if mode == 5:
        cls()
        exportEmployeeInfo()
    #import employee information
    if mode == 6:
        cls()
        importEmployeeInfo()
    if mode == 7:
        printEmployeeList()
        
        
    
    
        
    
