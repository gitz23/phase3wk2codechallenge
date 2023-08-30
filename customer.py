class Customer:
    all = []

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Customer.all.append(self)

    def given_name(self):
        return self.first_name

    def family_name(self):
        return self.last_name

    def full_name(self):
        full_name = self.first_name + " " + self.last_name
        return full_name

cus1 = Customer("Gitau", "Njung'e")
print(Customer.all)

class Restaurant:
    def __init__(self, res_name):
        self.res_name = res_name

    def name(self):
        return self.res_name 


class Review:
    def __init__(self, rating):
        super().__init__()
        self.rating = rating
        

rev1= Review(3)