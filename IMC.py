weight = float(input("Enter your weight in KG: "))
height = float(input("Enter your height in meters: "))
imc = weight / (height ** 2)
print("Your imc is:", round(imc, 2))