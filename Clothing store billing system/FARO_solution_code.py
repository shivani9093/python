pants_price_list = []
shirts_price_list = []
shopping_cart = [
       ["Gucci", "M", 8],
       ["Armani", "XL", 1],
       ["Gucci", "S", 1],
       ["Gucci", "40", 1],
       ["Armani", "10", 1],
      ]

class Clothes(object):
    def __init__(self, brand, size, price):
        self.brand = brand
        self.size = size
        self.price = price

pgs = Clothes("Gucci", "S", 10)
pgm = Clothes("Gucci", "M", 20)
pgl = Clothes("Gucci", "L", 30)
pgxl = Clothes("Gucci", "XL", 40)
pas = Clothes("Armani", "S", 20)
pam = Clothes("Armani", "M", 30)
pal = Clothes("Armani", "L", 40)
paxl = Clothes("Armani", "XL", 50)

sg10 = Clothes("Gucci", "10", 10)
sg20 = Clothes("Gucci", "20", 20)
sg30 = Clothes("Gucci", "30", 30)
sg40 = Clothes("Gucci", "40", 40)
sa10 = Clothes("Armani", "10", 20)
sa20 = Clothes("Armani", "20", 30)
sa30 = Clothes("Armani", "30", 40)
sa40 = Clothes("Armani", "40", 50)

pants_variety = [pgs, pgm, pgl, pgxl, pas, pam, pal, paxl]
shirts_variety = [sg10, sg20, sg30, sg40, sa10, sa20, sa30, sa40]

#  Function to calculate prices
def Cashier(shopping_cart):
    ''' ========================== Pants Price Calculator ================================= '''
    S_size_counter = []
    other_size_counter = []
    j = 0
    while j in range(len(shopping_cart)):
        i = 0
        while i in range(len(pants_variety)):
            if pants_variety[i].brand == shopping_cart[j][0] and pants_variety[i].size == shopping_cart[j][1]:
                rolling_price = pants_variety[i].price*shopping_cart[j][2]
                pants_price_list.append(rolling_price)
                total_pants_price = sum(pants_price_list)
            i+=1
        if shopping_cart[j][1] == "S":
            S_size_counter.append(shopping_cart[j][2])
        elif shopping_cart[j][1] == "M" or shopping_cart[j][1] == "L" or shopping_cart[j][1] == "XL":
            other_size_counter.append(shopping_cart[j][2])
        j+=1
    
    # Discount calculation for pants
    if sum(S_size_counter) > 5 and sum(other_size_counter) > 2:
        for i in range(len(shopping_cart)):
            if shopping_cart[i][0] == "Gucci" and shopping_cart[i][1] == "S":
                total_pants_price = (total_pants_price)-(total_pants_price*0.05) - 10
                break
            elif shopping_cart[i][0] == "Armani" and shopping_cart[i][1] == "S":
                total_pants_price = (total_pants_price)-(total_pants_price*0.05) - 20
                break
    elif sum(S_size_counter) > 5:
        total_pants_price = (total_pants_price)-(total_pants_price*0.05)
    
    print(f'Total quantity of pants purchased: {sum(S_size_counter)+sum(other_size_counter)}')
    print(f'Total price of pants: {total_pants_price} € \n')

    ''' ============================ Shirts Price Calculator =============================='''
    
    qty_counter = []
    p = 0
    while p in range(len(shopping_cart)):
        q = 0
        while q in range(len(shirts_variety)):
            if shirts_variety[q].brand == shopping_cart[p][0] and shirts_variety[q].size == shopping_cart[p][1]:
                rolling_price = shirts_variety[q].price*shopping_cart[p][2]
                shirts_price_list.append(rolling_price)
                total_shirts_price = sum(shirts_price_list)
            q+=1
        
        #  Discount calculation for shirts
        if shopping_cart[p][1] == "10" or shopping_cart[p][1] == "20" or shopping_cart[p][1] == "30" or shopping_cart[p][1] == "40":
            qty_counter.append(shopping_cart[p][2])
        p+=1
    if sum(qty_counter) > 6:
        total_shirts_price = (total_shirts_price)-(total_shirts_price*0.08)

    print(f'Total quantity of shirts purchased: {sum(qty_counter)}')
    print(f'Total price of shirts: {total_shirts_price} €\n')

    # Total bill calculation
    print(f'Total quantity of clothes purchased: {sum(S_size_counter)+sum(other_size_counter)+sum(qty_counter)}')
    print("Total bill of clothes purchased: ")
    return str(total_pants_price + total_shirts_price) + " €"

print(Cashier(shopping_cart))