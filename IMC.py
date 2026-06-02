weight = float(input("Enter your weight in KG: "))
height = float(input("Enter your height in meters: "))
imc = weight / (height ** 2)
print("Your imc is:", round(imc, 2))
if imc < 18.5:
    print("your imc is low - underweight")
elif imc <= 24.9:
    print("your imc is normal - healthy weight")
elif imc <= 29.9:
    print("your imc is high - overweight")
else:
    print("your imc is very high - obesity")