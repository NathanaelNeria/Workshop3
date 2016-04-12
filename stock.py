import random
MAX_INCREASE = 0.175
MAX_DECREASE = 0.05
MIN_PRICE = 1.0
MAX_PRICE= 100.0
INITIAL_PRICE = 10.0
day = 0
price = INITIAL_PRICE
print("${:,.2f}".format (price))

while price >= MIN_PRICE and price <= MAX_PRICE:
    priceChange = 0
    day=day+1
    if random.randint(1, 2) == 1:
        priceChange = random.uniform(0, MAX_INCREASE)
    else:
        priceChange = random.uniform(-MAX_DECREASE, 0)
    price *= (1 + priceChange)
    print("${:,.2f}".format(price),"day",day)
