def calculate_imc(weight, height):
    return weight / (height ** 2)

def diagnose(imc):
    if imc < 18.5:
        return "low - underweight"
    elif imc <=24.9:
        return "normal- healthy weight"
    elif imc <=29.9:
        return "high - overweight"
    else:
        return "very high - obesity"
    
def show_results(imc, diagnosis):
    print("your imc is:", round(imc, 2))
    print("diagnosis:", diagnosis)

weight = float(input("enter weight in kg: "))
height = float(input("enter your height in meters: "))

imc= calculate_imc(weight, height)
diagnosis = diagnose(imc)
show_results(imc, diagnosis)