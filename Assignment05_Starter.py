
# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Kimberly Domingo,8/7/2023,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
import os # need to check if text file exists 
nameFile = 'ToDoList.txt'
objFile = None   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

if os.path.isfile("ToDoList.txt"):
    objFile = open(nameFile, "r")
    for row in objFile:
        lstRow = row.split(",") # Returns a list!
        dicROW = {'Task': lstRow[0],
                'Priority': lstRow[1].strip()
                }
        lstTable.append([dicRow])
    objFile.close()
else:
    print("\n" + "There are currently no items on your To Do List. Please add some tasks!")

# Function that display data
def DisplayData():
    print("Your current To Do List:")
    for row in lstTable: 
        print("Task: " + row["Task"].strip() + " | Priority: " + row["Priority"].strip())

# Function to add new item
def AddData():
    print("Please enter a task and its priority: ")
    Task = input("Enter a task: ")
    Priority = input("Enter its priority [Low, Medium, or High]: ")
    lstTable.append({"Task": Task,
                     "Priority": Priority})
    print()
    print("The task, " + Task + ", has been added to the list")

# Function to remove item
def RemoveData():
    RemoveEntry = input("What task would you like to remove from the list? ")
    found = False
    for Task in lstTable: 
        if Task["Task"].lower() == RemoveEntry.lower():
            lstTable.remove(Task)
            found = True
            break 
    if found: 
        pass
    else: 
        print("No task was found. Please enter another task to be remove or display current data.")

# Function to save tasks to file
def SaveData():
    objFile = open(nameFile, "w")
    for row in lstTable: 
        objFile.write("Task: " + str(row['Task']) + "\n"
                      "Priorioty: " + str(row["Priority"]) + "\n")

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        DisplayData()
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        AddData() 
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        RemoveData()
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        SaveData()
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        break  # and Exit the program