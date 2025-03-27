unit = int(input("Enter number of units consumed by user."))
if unit  < 50:
    bill = unit * 0.50 - 20
elif unit < 100:
    bill = unit * 0.75 - 40
elif unit < 200:
    bill = unit * 1.20 - 50
else:
    bill = unit * 1.5 - 100
print("Electicity Bill = ", bill)