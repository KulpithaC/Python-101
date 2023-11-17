old = int(input("Old price: "))

remain = old % 100
result = old - remain

adjustments = {True: 98, False: -100 + 98}

new = result + adjustments[(remain >= 50) & (old >= 100)] | (98 * (old < 100 and old > 0))

print("New Price:", new)
