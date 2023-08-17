
# Add colors to my print statements
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#empty list
list = []

#function for the first menu option
def AddData():
    global list #global variable that can be used anywhere in the program
    item_name = str(input("Enter an item: "))
    item_cost = str(input("Enter the estimated value: "))
    item = [item_name, item_cost]
    print(item)
    list.append(item) #built-in function for lists
    print(list)

#function for the second menu option
def DisplayData(): 
    for x in list: 
        print("Furniture: " + str(x[0]) + "| " "Cost: $" + str(x[1])) #For formatting, added extra strings

#function for the third menu option
def SaveData():
    objfile = open("Home Inventory.txt", "w")
    for x in list: #same as DisplayData function for formatting
        objfile.write("Furniture: " + str(x[0]) + "| " "Cost: $" + str(x[1]) + '\n')
    objfile.close()


#While loop. Need to make break at the end
while(True):

   print(color.BOLD  + color.DARKCYAN + """
         Kim's Furniture Shopping List """ + color.END)
   print(
       """      
                Menu Options
            1. Add data to list
            2. Display current list
            3. Exit and save to file
         """)
#input function. Beggining of the loop 
   user_choice = str(input("Please select an option [1 to 3]: "))
   if user_choice == "1":
       AddData()
       continue #loops back to the top
   
   elif user_choice == "2":
       DisplayData()
       continue #loops back to the top

   elif user_choice == "3":
       SaveData()
       print(color.BOLD + color.GREEN + "You have saved this data" + color.END)
       DisplayData()
       break #stop the loop
   
   else: # added for extra feature 
       print(color.BOLD + color.RED + "Please only choose from option [1, 2, or 3]" + color.END)


