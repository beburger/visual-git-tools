# Input the item price and the percent tax to be added
# The total price will be returned
def checkout(price, taxPercent):
    total = 1+taxPercent*price
    return round(total, 2)

print(checkout(50, 0.12))
