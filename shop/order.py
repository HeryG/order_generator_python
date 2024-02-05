import random
from shop.product import Product
from shop.order_element import OrderElement
from shop.tax_calculator import TaxCalculator

#TWORZENIE LISTY ZAMÓWIEŃ 

class Order():
    
    MAX_ORDER_ELEMENTS = 10
    FAVOURITE_CLIENTS = ["Aleksander Dziobkowski"]

    def __init__(self, first_name, last_name, order_elements = None,):
        self.first_name = first_name
        self.last_name = last_name
        if order_elements is None:
            order_elements = []
        self.order_elements = order_elements
        self.total_price = self.rabat_policy()
           
        if len(self.order_elements) >= Order.MAX_ORDER_ELEMENTS:
            self.order_elements = self.order_elements[0:Order.MAX_ORDER_ELEMENTS]

    def calculate_total_price(self):
        total_price = 0
        for element in self.order_elements:
            total_price += element.calculate_price()
        return total_price

    def __str__(self):
        mark_line = ("="*100)
        order_details = (f"{self.first_name} {self.last_name}")
        value_details = (f"O łącznej wartości {round(self.total_price,2)} PLN")
        product_details = "Zamówione produkty:\n"
        for element in self.order_elements:
            product_details += f"\t{element} Tax:{round(TaxCalculator.calculate(element),2)} PLN \n"    
        result = "\n".join([order_details, value_details, product_details, mark_line])
        return result
    
    def __len__(self):
        return len(self.order_elements)
    
    def __eq__(self,other):
        if self.__class__ != other.__class__:
            NotImplemented
        for order_element in self.order_elements:
            if order_element not in other.order_elements:
                return False
            return self.first_name == other.first_name and self.last_name == other.last_name and len(self.order_elements) == len(other.order_elements)
        
    def add_order(self,product,quantity):
        if len(self.order_elements) < Order.MAX_ORDER_ELEMENTS:  
            element = OrderElement(product,quantity)
            self.order_elements.append(element)
            self.total_price = self.calculate_total_price()
        else:
            print("="*25)
            print("nie ma juz miejsca")

    @classmethod
    def order_generator(cls):
        number_of_products = random.randint(1,cls.MAX_ORDER_ELEMENTS)
        order_elements = []
        for number in range(number_of_products):
            name = f"Produkt-{number+1}"
            categories = ["Inne","Owoce i warzywa","Jedzenie"]
            category_name = categories[random.randint(0,2)]
            unit_price = random.randint(1,30)
            product = Product(name,category_name,unit_price)
            quantity = random.randint(1,10)
            element = OrderElement(product,quantity)
            order_elements.append(element)
            names = ["Aleksander","Oliwier","Andrzej","Krzysztof","Daniel","Mariusz"]
            second_names = ["Dziobkowski", "Kowalski", "Duda", "Malanowicz", "Solarczyk", "Nitka"]
            name_of_user = names[random.randint(0,5)]
            second_name_of_user = second_names[random.randint(0,5)]
        order = Order(name_of_user,second_name_of_user,order_elements)
        return order

    def rabat_policy(self):

        if f"{self.first_name} {self.last_name}" in Order.FAVOURITE_CLIENTS and self.calculate_total_price() < 100:
            total_price = self.total_price = 0.95 * self.calculate_total_price()

        elif f"{self.first_name} {self.last_name}" not in Order.FAVOURITE_CLIENTS and self.calculate_total_price() >= 100:
            total_price = self.total_price = self.calculate_total_price() - 20

        elif f"{self.first_name} {self.last_name}" in Order.FAVOURITE_CLIENTS and self.calculate_total_price() >= 100:
            total_price = self.total_price = 0.95 * self.calculate_total_price() - 20

        else:
            total_price = self.total_price = self.calculate_total_price()

        return total_price

    