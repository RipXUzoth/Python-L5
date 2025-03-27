print("select your ride")
print("1. Car")
print("2. Bike")
choice = int(input("Enter your choice"))
if choice == 1:
    print("what car do you want to pick?")
    print("1. Mazda RX-7")
    print("2. Toyota AE86 Trueno")
    car = int(input("Enter your choice"))
    if car == 1:
        print("You have selected the Mazda")
    else:
        print("you have selected the Toyota")