class Bank:
    bName = "Canara"
    location="Mumbai"
    pinCode= 400062
    status="open"
    atm=True


    


fBank = Bank()
fBank.location = "Chennai"

gBank = Bank()


del fBank  # deletes the fBank instance of class Bank



print(f"Bank is located in {fBank.location}")
print(f"Bank is located in {gBank.location}")