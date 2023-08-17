

#Get data from user
name_input = input("Enter item name: ")
cost_input = input("Enter cost of item: ")
item_name = "Item name: " + name_input + "\n" # Create a new line
item_cost = "Cost of item: " + cost_input

#Store data into a text file 
objfile = open("HomeInventory.txt", "w")
objfile.write(item_name)
objfile.write(item_cost) 
objfile.close() 

print("You have saved this data:")
print(item_name, end='') #Add in to make sure to create a new line
print(item_cost)




