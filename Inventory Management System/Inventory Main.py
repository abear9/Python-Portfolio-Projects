#Program Description: This file contains the main function for the inventory management system. Prior to any data collection, this function sets up the necessary data structures and 
#creates a list of objects for the content of the inventory file. Then, it loops through asking the user for the product ID they would like to purchase, until they 
#enter 0 to exit the program. If a valid ID is entered, the program asks the user for the desired quantity. That quantity is added to an invoice list of transaction objects,
#which accumulates objects until the user is done. Finally, an invoice is displayed and the totals are calculated. 

#import the classes from their files
import validation
import inventory
import transactionitem

def main():
    
    #start by creating validation object
    val_obj = validation.Validation()

    #read in the inventory file to a 2d list inventory
    inventory = read_inventory("Inventory.txt")

    #use process inventory function to take 2 list and instantiate an object for each inventory item while also printing the menu
    inventory_list = process_inventory(inventory)
 
    #set up empty list for all transaction objects
    transaction_list = []

    #initialize the check variable to false, will change to true if an item is purchased. 
    item_purchased_check = False 


    #Transaction loop
    while True:
        desired_id = val_obj.get_desired_id() #goes through collection and validation method from validation class to get the desired id
        
        #find_id returns true or false, so a true means move on, we got the ID
        if val_obj.find_id(inventory_list,desired_id): 
            desired_quantity = val_obj.get_desired_quantity() #collect the desired quantity of items from the user
            purchase = purchase_quantity_by_id(inventory_list,desired_id, desired_quantity) #this variable calls the function to use the purchase method for the correct obj in the inv list
            if purchase == False: #that method will return false if quantity > stock
                print("There is not enough inventory for the purchase of this many items. Please try again. ")
            else: #there is enough stock for this purchase, so continue

                #instantiate a transaction with all of its attributes and add it to the transaction list
                transaction_obj = transactionitem.TransactionItem() #need ID (desired ID), name (get_name?), price (get_price), quantity (desired_quantity)
                transaction_obj.set_id(desired_id)
                transaction_obj.set_name(item_name(inventory_list, desired_id))
                transaction_obj.set_price(item_price(inventory_list, desired_id))
                transaction_obj.set_qty(desired_quantity)

                #append this transaction object to the master list
                transaction_list.append(transaction_obj)

                #an item has been purchased now, change to True
                item_purchased_check = True
                print_menu(inventory_list) #print an updated menu
        elif desired_id == 0 and item_purchased_check == False:   #if 0 is returned and nothing has been purchased, end the program here with the correct message
            print("No items purchased. Thanks for visiting!")
            exit()
        elif desired_id == 0 and item_purchased_check == True: #if 0 is returned, but something has been purchased, the transaction is done
            break
        else:
            print("Invalid ID. Please try again. ") #if the id is a valid number but not in the inventory, loop back through
    

    #now out of the loop, print the invoice and the total values
    print_invoice(transaction_list)

    #write the new inventory to an updated file by calling custom function
    write_to_file(inventory_list)

    
   

#Functions

#this function takes the txt file as input and reads it into a 2d list, with each inner list being the details for one item category in the inventory
def read_inventory(file):
    # Create a list where I will store the data
    data_list = []
    # Open the file in read mode
    file_obj = open(file, 'r')
    #read all of the data into lines
    lines = file_obj.readlines()
    # Iterate over the lines and group the data into sublists of four elements each
    for i in range(0, len(lines), 4): #every 4 items go together
        #go through each element of each item, convert to appropriate data type, strip extra spaces, and add to items list
        item = [int(lines[i].strip()),                
                lines[i+1].strip(),                   
                int(lines[i+2].strip()),              
                float(lines[i+3].strip())]       
        #add the individual item to the 2d list
        data_list.append(item)
    #finally, return the master list
    return data_list

#2 main purposes: prints out the menu for the first time and also creates an object list for inventory
def process_inventory(process_list):
    #initialize empty list for objects
    inventory_list = []
    print("{:<20}{:<20}{:>20}{:>20}".format("ID", "Name", "Price", "Quantity"))
    for item in process_list:
        inv_instance = inventory.Inventory(*item) #unpack the items of the list into an inventory class, instantiating an object
        inventory_list.append(inv_instance) #add objects to the obj list
        print(inv_instance) #print out this inventory item and move to the next one
    #send the inventory obj list out
    return inventory_list

#use this function to print out the updated menu in subsequent updates
def print_menu(print_list):
    print("{:<20}{:<20}{:>20}{:>20}".format("ID", "Name", "Price", "Quantity"))
    for item in print_list:
        print(item)

#this function prints the purchase invoice using the __str__ method in the transaction item class
def print_invoice(print_list):
    #print out header
    print()
    print("Order Complete. See Invoice below: ")
    print("{:<20}{:<20}{:20}{}{:>18}".format("ID", "Name", "Quantity", "Price", "Extended Price"))

    #go through each item and print out the details
    for item in print_list:
        print(item)

    #calculate the totals including sales tax by looping through each item in the list and get the cost for the item and add the quantity to the total
    total_items = 0
    subtotal = 0 
    tax_rate = 0.085
    for item in print_list:
        total_items += item.get_qty()
        subtotal += item.calc_cost()

    #now with accumulated totals, calculated tax and grand total to display to user
    sales_tax = subtotal * (tax_rate)
    grand_total = subtotal + sales_tax
    print()
    print("Total Items: {} \nSubtotal: ${:.2f} \nSales Tax: ${:.2f} \nGrand Total: ${:.2f}".format(total_items, subtotal, sales_tax, grand_total))

#This will find the appropriate item in the inventory and call the purchase method - this will return True or False. If true, it will update the stock on the inv object.
def purchase_quantity_by_id(object_list, target_id, purch_qty):
    for item in object_list:
        if item.get_id() == target_id:
            return item.purchase(purch_qty)  # Call the purchase method to update the quantity
    return False  # Return False if ID is not found in the list

#this function writes the final updated inventory to a file
def write_to_file(object_list):
    #open up a new file for updated inventory
    file = open('UpdatedInventory.txt', 'w')

    #loop through all of the objects in the list and get the necessary attributes. Format the file to be like the input file
    for obj in object_list:
        file.write(str(obj.get_id()) + '\n')
        file.write(obj.get_name()+ '\n')
        file.write(str(obj.get_stock())+ '\n')
        file.write(str(obj.get_price())+ '\n')

#this will go through the inventory list to find item name for purposes of instantiating transactionitem obj.        
def item_name(object_list, item_id):
    for obj in object_list:
        if obj.get_id() == item_id: #find the correct item based on the id passed in
            return obj.get_name()

#similar to above, this will find the item price for the id the user enters in order to instantiate a transaction item obj.
def item_price(object_list, item_id):
    for obj in object_list:
        if obj.get_id() == item_id: #find the correct item based on the id passed in
            return obj.get_price()

    


main()

