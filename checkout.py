def checkout(price, taxPercent):
    total = (1+taxPercent)*price
    return total

print(checkout(50, 0.12))
