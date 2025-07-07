# test.py
name = item = str(input("What is your name?: "))
item = str(input("What are you gonna add?: "))
price = float(input ("The price is: "))
quantity = int(input("How many?: "))

total_amount = quantity * price

print(f"Welcome {name}!")
print(f"You added {item} which cost {total_amount}.")
