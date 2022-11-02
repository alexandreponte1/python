# BMI = (peso em KG / altura em metro quadrado)
# Versão imperial : BMI * 703

def gather_info():
    altura = float(input ("Qual a sua altura? (metros ou polegadas)"))
    peso = float (input("Qual o seu peso? (KG ou Libras)"))
    system = input("Qual o seu sistema métrico ou imperial?").lower().strip()
    return (altura, peso, system)

def calcular_bmi(peso, altura, system='metrico'):
    """
    Return the body Mass Index (BMI) for the given weight, height, and measurement system.
    """
    if system == 'metric':
        bmi = (peso / (altura ** 2))
    else:
        bmi = 703 * (peso / (altura ** 2))
    return bmi

while True:
    altura, peso, system = gather_info()
    if system.startswith('i'):
        bmi = calcular_bmi(peso, system=system, altura=altura)
        print(f"o seu BMI é {bmi} ")
        break
    elif system.startswith('m'):
        bmi = calcular_bmi(peso, altura)
        print(f"O seu BMI é {bmi}")
        break
    else:
        print("Error:Systema métrico desconhecido, por favor use metrico ou imperial.")


