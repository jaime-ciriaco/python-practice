def dis(price,discount):
    discounted_price = price * (discount/100)
    return price  - discounted_price

total = dis(1500,50)
print(total)  