print("Welcome to the tip calculator!")

bill = int(input("What is your total bill?"))

tip = int(input("How much tip would you like to give? 10 , 12 or 15?"))

split_between = int(input("How many people to split the bill?"))

tip_percent = tip / 100
tip_amt = bill * tip_percent
total_bill = bill + tip_amt
bill_person = total_bill / split_between

final_amt = round(bill_person, 2)

print(f"Each person should pay {final_amt}")
