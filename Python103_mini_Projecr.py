class create_bike:
    def __init__(self,description, cost,sold, sale_price, condition):
        self.description=description
        self.cost=cost
        self.sale_price=sale_price
        self.condition=condition
        self.sold=sold
  
def update_sale_price(sold, sale_price):
        if sold == True:
            print('Action not allowed, Bike has already been sold')
        else:
            sale_price = sale_price
            print("The bick's new price is:",sale_price)
        
def sell(sold):
         sold == True
         print("Bike has been sold")





bike1 = create_bike('Univega Alpina, orange', cost=100,sold=True, sale_price=500, condition=0.5)
update_sale_price(bike1.sold, 350)
sell(bike1)



##////////////////Convert the code below from Procedure Oriented Programming to Object Oriented Programming (OOP)//////////////////

#  def update_sale_price(bike, sale_price):
#         if bike['sold'] == True:
#             print('Action not allowed, Bike has already been sold')
#         else:
#             bike['sale_price'] = sale_price
    
    
#     def sell(bike):
#         bike['sold'] = True
    
    
#     def create_bike(description, cost, sale_price, condition):
#         return {
#             'description': description,
#             'cost': cost,
#             'sale_price': sale_price,
#             'condition': condition,
#             'sold': False
#         }
    
    
#     bike1 = create_bike('Univega Alpina, orange', cost=100, sale_price=500, condition=0.5)
#     update_sale_price(bike1, 350)
#     sell(bike1)