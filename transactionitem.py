#Author: Andrew Hebert
#Assignment Number & Name: Final Project - TransactionItem Class
#Due Date: N/A
#Program Description: This file contains one of the necessary classes for the final project in MIS 380P, TransactionItem. On this class, there are 4 attributes with getter and setter methods
#for each attribute. There is also a method for calculating the cost of an item order, which takes the desired quantity and multiplies it by the item price. 


#class for transaction item
class TransactionItem:
    def __init__(self):
        self.__id = '' #string value for id and name
        self.__name = '' 
        self.__quantity = 0 #integer for whole stock
        self.__price = 0.0 #float for price

    #getter and setter for each attribute
    def get_id(self):
        return self.__id
    def set_id(self, new_id):
        self.__id = new_id
    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        self.__name = new_name
    def get_qty(self):
        return self.__quantity
    def set_qty(self,new_qty):
        self.__quantity = new_qty
    def get_price(self):
        return self.__price
    def set_price(self, new_price):
        self.__price = new_price

    #method for calculating the whole cost of a transaction
    def calc_cost(self):
        cost = self.__quantity * self.__price #cost not to be stored in the class
        return cost

    #override str method for formatting invoice
    def __str__(self):
        str_out = "{:<20}{:<20}{} \t${:>12,.2f}\t${:>10,.2f}".format(self.get_id(),self.get_name(),self.get_qty(),self.get_price(),self.calc_cost())
        return str_out
 