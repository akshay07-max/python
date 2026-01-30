class Bank:
    bName = "Canara"
    location="Mumbai"
    pinCode= 400062
    status="open"
    atm=True


fBank = Bank()
fBank.location = "Chennai"

print(f"Bank is located in {fBank.location}")