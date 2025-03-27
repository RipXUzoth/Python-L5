atten = int(input("Hey user what is your attendance percentage?"))
if atten  >= 75: 
    print("you can sit in the examination")
else:
    medical = input("Do you have a medical condition")
    if medical == "yes":
        print("you can sit in the examination")
    else:
        print("sorry, you can't sit in the examination")