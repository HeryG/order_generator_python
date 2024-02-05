#OBLICZANIE PODATKU

class TaxCalculator:
    @staticmethod
    def calculate(element):

        if element.product.category_name == "Owoce i warzywa":
            tax_value = element.calculate_price() * 0.05

        elif element.product.category_name == "Jedzenie":
            tax_value = element.calculate_price() * 0.08
        else:
            tax_value = element.calculate_price() * 0.2

        return tax_value