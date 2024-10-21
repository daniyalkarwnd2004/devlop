import json as js


# This invoice management program
class Factor(object):
    """
    It receives customer and seller information, as well as the number of products and discount percentage
    """

    def __init__(self, seller_name, seller_address, seller_number_phone, seller_number_tax, customer_name,
                 customer_number_phone, customer_address, number, tak):
        """
        Checks the condition of correctness of the phone number
        """
        if str(seller_number_phone).isnumeric() and len(seller_number_phone) == 11:
            self.seller_number_phone = seller_number_phone
        else:
            print("please your enter number phone :)")
        if str(customer_number_phone).isnumeric() and len(customer_number_phone) == 11:
            self.customer_number_phone = customer_number_phone
        else:
            print("please your enter number phone :)")
        """

               :param seller_name: 
               :param seller_address: 
               :param seller_number_phone: 
               :param seller_number_tax: 
               :param customer_name: 
               :param customer_number_phone: 
               :param customer_address: 
               :param number: 
               :param tak: 
               """
        self.customer_address = customer_address
        self.customer_name = customer_name
        self.seller_name = seller_name
        self.seller_address = seller_address
        self.seller_number_tax = seller_number_tax
        self.number = number
        self.tak = tak

    def the_show(self):
        """
        Display seller information
        :return: Displays seller information such as name and address
        """
        return f"show data the seller: {self.seller_name} {self.seller_address} {self.seller_number_phone} " \
               f"{self.seller_number_tax}"

    def show_customer(self):
        """
        Display customer information
        :return: Displays customer information such as name and address
        """
        return f"show data the customer: {self.customer_name} {self.customer_address} {self.customer_number_phone}"

    def __str__(self):
        return f"seller: {self.seller_number_tax} {self.seller_name} \n{self.customer_name} {self.customer_number_phone}"

    def __repr__(self):
        return f"seller: {self.seller_number_tax} {self.seller_name} \n{self.customer_name} {self.customer_number_phone}"

    def name_factor(self):
        """
        This function performs all the calculation processes of this application
        This function puts the products and their amount in a list, displays the total cost of purchase and the amount
         of the discount and performs the calculations and saves all of them in a file.
        :return: Total cost  List of products with name and amount  It s how's the discount amount
        """
        list_name = []
        i = 1
        while i <= self.number:
            name = input("name: ")
            price = int(input("price: "))
            list_name.append([name, price])
            i += 1
        Sum = 0
        for i in list_name:
            Sum += i[1]
        tak = Sum * self.tak / 100
        lists = [
            "products: ", list_name,
            "total_sum: ", Sum,
            "tax_amount: ", tak
        ]
        with open("file.txt", "a", encoding="utf-8") as f:
            js.dump(lists, f)
            f.write("\n")
        print(tak)
        print("sum prise: ", Sum, "\n", "sum prise + tak: ", Sum - tak)
        print("list of products", list_name)


try:
    factor = Factor("ali", "mohammdcity", "09931805649", "18", "reza", "09931805649", "mohammdcity", 2, 10)
    factor.name_factor()
except IndexError as e:
    print(e)
