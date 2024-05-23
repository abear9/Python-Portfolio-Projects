#Author: Andrew Hebert
#Assignment Number & Name: Final Project - Inventory Class
#Due Date: N/A
#Program Description: This file contains one of the necessary classes for the final project in MIS 380P, Inventory. On this class, there are 4 attributes and getter methods
#for each attribute. There are also methods for restock and purchase, which validate a quantity and update stock accordingly. 

#class for inventory
class Inventory:
    #initialize with the following attributes, the class will receive these upon instantiation
    def __init__(self,new_id,new_name,new_stock,new_price):
        self.__id = new_id
        self.__name = new_name 
        self.__stock = new_stock #integer for whole stock
        self.__price = new_price #float for price

    #getter methods for the attributes - 
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_stock(self):
        return self.__stock
    def get_price(self):
        return self.__price
    
    #method to determine if restock or not
    def restock(self, new_stock):
        if new_stock > 0:
            self.__stock += new_stock
            return True
        else:
            return False

    #method to deduct quantity from stock if there is sufficient sotck on hand, otherwise return false and do not change 
    def purchase(self, purch_qty):
        if purch_qty > self.__stock:
            return False
        else:
            self.__stock -= purch_qty
            return True
    
    #override str method to display menu of items
    def __str__(self):
        str_out = "{:<20}{:<20}   ${:>20.2f}{:>20}".format(self.get_id(),self.get_name(),self.get_price(),self.get_stock()) #this uses the getters to retrieve all attributes
        return str_out

