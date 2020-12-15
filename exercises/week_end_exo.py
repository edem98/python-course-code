def clearance_solde(price,days):
    promo_price = price
    for x in range(days):
        promo = promo_price * 0.02
        promo_price -= promo

    return int(promo_price)

print(clearance_solde(25000,7))