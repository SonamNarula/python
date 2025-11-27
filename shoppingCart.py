item = input("what items would you like to buy ? : ")
price = float(input("what is the price ? : "))
quantity = int(input("how many ? : "))
total = price * quantity

print(f"the price of {quantity} {item} is ${total}")
