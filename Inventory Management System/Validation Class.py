#Program Description: This file contains a validation class for user inputs to be checked and to make sure the desired ID number exists in the inventory. 
#This class has no attributes, just functions to verify and validate values. 

   
#class for validation and collection
class Validation:

    #this function will collect the product id from the user, validating it to make sure it is a number firstly
    def get_desired_id(self):
        while True:
            desired_id = input("Which product ID would you like to purchase? Enter 0 to Exit. ")
            try:
                desired_id = int(desired_id) #if it can be cast to int, we are good to go here
                if desired_id == 0:
                    #the user will receive a message through main even if they don't want to buy or return anything. This will send a -1 back indicating an end to the program.
                    return 0
                return desired_id
            except:
                return -1 #input was not a number, loop back through

    #this will make a list of all the ids in the object list containing inventory objects, which we then use to check if the desired id is in the list
    def find_id(self,inventory_list, desired_id):
        #create the list of ids by looping through the objects and using the getter method for id
        item_ids = []
        for obj in inventory_list:
            item_id = obj.get_id()
            item_ids.append(item_id)

        #if the id is in this list, return True to main, and False otherwise
        if desired_id in item_ids:
            return True
        else:
            return False
        
        
    #this method will ask the user for input on how many items they want
    def get_desired_quantity(self):
        while True:
            desired_quantity = input("How many items would you like to purchase? Enter a negative number for a return. ")
            try:
                desired_quantity = int(desired_quantity)    #if it can be cast to int, we are good to go here
                if desired_quantity == 0:
                    print("That is an invalid quantity. Please try again. ")
                else:
                    return desired_quantity
            except:
                print("That is an invalid quantity. Please try again. ") #input was not a number, loop back through



