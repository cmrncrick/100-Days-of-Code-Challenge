print("Welcome to the tip calculator!")

bill_total = float(input("What was the total bill? $"))
tip_total = float(
    input("How much tip would you like to give? 10, 12, or 15? "))
num_ppl = int(input("How many people to split the bill? "))

bill_amount = (tip_total / 100 * bill_total + bill_total) / num_ppl

# tip_total = tip_total/100
# total_bill = ((float(bill_total) * (float(tip_total)/100)) + float(bill_total))
# bill_amount = (total_bill / float(num_ppl))

# bill_amount = (bill_total*tip_total) + bill_total
# bill_amount = bill_amount/num_ppl

print(f"Each person should pay: ${round(bill_amount, 2)}")
