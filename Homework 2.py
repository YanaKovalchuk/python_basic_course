credit_card=str(input("Enter credit card number"))
674512348976567788
valid_till=input("Enter date")
"11/23"
cvv=str(input("Enter cod"))
345
print(len(credit_card))
if len(credit_card)!=16:
    exit()
try:
    int(valid_till)
except ValueError:
    print("OK")
else:
    exit()
if len(cvv)<3:
    print("Mistake")
    exit()

formula=input(5*10)
poets=input([Shakespeare,Shevchenko,Poe])

try:
    print(book+5)
except NameError:
    print("Study Python further")
print("Fine")

S="distance"
V="speed"
try:
    print(S/V)
except TypeError:
    print("Try another way")
print("Good job")

planet="Mars"
if planet is not "Mars" or "Earth":
    print("Explore satellite")
else:
    print("Habitable")

scientist="Einstein"
theory="Relativity" if scientist=="EInstein" else "Others"
