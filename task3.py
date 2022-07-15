weight = input("Please enter your weight : ")
unit = input("(L)bs or (K)g : ")
if unit in ['L', 'l', 'Lbs', 'LBS']:
    weight_in_kg = int(weight) / 2.20462
    print("Your weight in kilograms is : " + str(weight_in_kg))
elif unit in ['K', 'k', 'Kg', 'KG']:
    weight_in_pound = int(weight) * 2.20462
    print("Your weight in pounds is : " + str(weight_in_pound))
else:
    print("Please Enter the unit carefully!!")

print("Thankyou Babye!")

