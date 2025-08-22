name = input("Enter user name;")
gender = input("Enter your gender(M/F):")
age = int(input("Enter user age:"))
product = input("Enter product:")
gram = int(input("Enter product gram:"))
current_gold_price = 5752
making_charge = 845
discount = 0
total_gold_rate = current_gold_price * gram
total_making_charge = making_charge * gram
total_amount = total_gold_rate + total_making_charge
if gender == 'M':
    if age > 65:
        if 200000 < total_amount <= 300000:
            discount = 20
        elif 300000<total_amount <= 500000:
            discount = 30
        elif total_amount > 500000:
            discount = 35

    else:
        if 200000 < total_amount <= 300000:
            discount = 10
        elif 300000 < total_amount <= 500000:
            discount = 20
        elif total_amount > 500000:
            discount = 25 
elif gender == 'F':
    if age > 65:
        if 200000 < total_amount <= 300000:
            discount = 25
        elif 300000 < total_amount <= 500000:
            discount = 35
        elif total_amount > 500000:
            discount = 40
    else:
        if 200000 < total_amount <= 300000:
            discount = 15
        elif 300000 < total_amount <= 500000:
            discount = 25
        elif total_amount > 500000:
            discount = 30
discount_amount = (total_amount * discount) / 100
final_amount = total_amount - discount_amount
print("KALYAN JEWELLERS")
print("user's name", name)
print("Gender:",gender)
print("Age:",age)
print("Product:",product)
print("Weigth in grams:",gram)
print("Gold price per gram", current_gold_price)
print("Making charge per gram:",making_charge)
print("Total Gold Rate:", total_gold_rate)
print("Total Making charge",total_making_charge)
print("Total amount:",total_amount)
print("Dicount amount",discount_amount)
print("Final Amount user need to pay:",final_amount)